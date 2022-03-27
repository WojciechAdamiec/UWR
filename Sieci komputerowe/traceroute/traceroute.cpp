// Wojciech Adamiec
// 310064
// 2021-04-06

#include "traceroute.h"
#include <netinet/ip.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <chrono>
#include <netinet/ip_icmp.h>
#include <cassert>
#include <iostream>
#include <sys/types.h>
#include <unistd.h>

// Function to compute checksum
u_int16_t compute_icmp_checksum (const void *buff, int length)
{
	u_int32_t sum;
	const u_int16_t* ptr = (const u_int16_t*)buff;
	assert (length % 2 == 0);
	for (sum = 0; length > 0; length -= 2)
		sum += *ptr++;
	sum = (sum >> 16) + (sum & 0xffff);
	return (u_int16_t)(~(sum + (sum >> 16)));
}

// Function to create ICMPHeader
struct icmp createICMPHeader(u_int16_t id, u_int16_t seq){
    struct icmp header;
    header.icmp_type = ICMP_ECHO;
    header.icmp_code = 0;
    header.icmp_hun.ih_idseq.icd_id = id;
    header.icmp_hun.ih_idseq.icd_seq = seq;
    header.icmp_cksum = 0;
    header.icmp_cksum = compute_icmp_checksum((u_int16_t*) &header, sizeof(header));

    return header;
}

// Function to send ICMPPacket
ssize_t sendICMPPacket(const std::string &ip_addr,
                       const int &socket,
                       const struct icmp &header,
                       const int &ttl){

    // Setting address of recipient
    struct sockaddr_in recipient;
    bzero (&recipient, sizeof(recipient));
    recipient.sin_family = AF_INET;
    inet_pton(AF_INET, ip_addr.c_str(), &recipient.sin_addr);

    // Setting time-to-live (TTL)
    setsockopt(socket, IPPROTO_IP, IP_TTL, &ttl, sizeof(int));

    // Sending packet
    ssize_t bytes_sent = sendto(
        socket,
        &header,
        sizeof(header),
        0,
        (struct sockaddr*) &recipient,
        sizeof(recipient)
    );

    return bytes_sent;
}

// Function to ping routers with specific TTL
step_feedback pingRouter(const std::string &ip_addr, unsigned short ttl, 
                         const int &socket, const uint16_t &pid){

    // Feedback struct: ttl, unique_ips, responses, response_times, ip_addrs
    step_feedback feedback = {ttl, 0, 0, {}, {}};

    // Sending 3 requests
    for(int i = 1; i <= 3; i++) {
        
        // Sequence number is ttl and packet name (for wireshark purposes)
        u_int16_t seq = (ttl << 2) + i;
        
        // Creating header: Echo request
        struct icmp header = createICMPHeader(pid, seq);
        
        // Sending ICMP packet
        sendICMPPacket(ip_addr, socket, header, ttl);
    }

    // Save request send time
    auto send_time = std::chrono::steady_clock::now();

    // Declare auxiliary time variable
    auto time_passed = 0;

    // Select setup made by Mbi
    fd_set descriptors;
    FD_ZERO(&descriptors);
    FD_SET(socket, &descriptors);
    struct timeval tv;
    tv.tv_sec = 1; // Our time limit is 1 second
    tv.tv_usec = 0;

    // Checking for responses for 1 sec (or sooner if there are 3)
    while(feedback.responses < 3 && (tv.tv_sec > 0 || tv.tv_usec > 0)) {

        int ready = select(socket + 1, &descriptors, NULL, NULL, &tv);

        // Checking select errors and timeouts
        if(ready < 0) {
            std::cerr << "Select error: " << strerror(errno) << " \n";
            return feedback;
        } else if(ready == 0) { // Timeout: we are breaking the loop
            return feedback;
        }

        // Looking through packets in the socket queue
        struct sockaddr_in sender;
        socklen_t sender_len = sizeof(sender);
        u_int8_t buffer[IP_MAXPACKET];
        ssize_t packet_len = recvfrom(socket,
                                      buffer,
                                      IP_MAXPACKET,
                                      MSG_DONTWAIT,
                                      (struct sockaddr *)&sender,
                                      &sender_len);
        
        while(packet_len > 0) {

            auto time_now = std::chrono::steady_clock::now();
            time_passed = std::chrono::duration_cast<std::chrono::microseconds>(time_now - send_time).count();

            // Getting sender ip addr
            char sender_ip_str[20];
            inet_ntop(AF_INET, &(sender.sin_addr), sender_ip_str, sizeof(sender_ip_str));

            // Getting  ip & icmp header
            struct ip *ip_header = (struct ip *)buffer;
            ssize_t ip_header_len = 4 * ip_header->ip_hl;
            u_int8_t *icmp_packet = buffer + ip_header_len;
            struct icmp *icmp_header = (struct icmp *)icmp_packet;
            ssize_t icmp_header_len = 8;

            // Type 8 - loopback
            bool skip = false;
            if(icmp_header->icmp_type == 8) {
                skip = true;
            }

            // Type 11 - TTL exceeded, extracting the original request
            if(icmp_header->icmp_type == 11) {
                ssize_t inner_packet = ip_header_len + icmp_header_len; // Moving to inner ICMP
                ip_header = (struct ip *)(buffer + inner_packet);
                ip_header_len = 4 * ip_header->ip_hl;
                icmp_packet = buffer + inner_packet + ip_header_len;
                icmp_header = (struct icmp *)icmp_packet;
            }

            // Getting icmp packet id, seq;
            uint16_t id = icmp_header->icmp_hun.ih_idseq.icd_id;
            uint16_t seq = icmp_header->icmp_hun.ih_idseq.icd_seq;
            uint16_t seq_ttl = seq >> 2;

            // Checking if packet is a response to our last requests
            if(id == pid && seq_ttl == ttl && !skip) {
                std::string newip = sender_ip_str;
                
                // Checking if the current ip addr is a unique new one
                bool unique = true;
                for(unsigned i = 0; i < feedback.unique_ips; i++)
                    if(feedback.ip_addrs[i].compare(newip) == 0)
                        unique = false;
                if(unique) {
                    feedback.ip_addrs[feedback.unique_ips] = newip;
                    feedback.unique_ips++;
                }
                
                // Updating response time
                feedback.response_times[feedback.responses] = time_passed / 1000.0;
                feedback.responses++;
            }
            
            packet_len = recvfrom(socket,
                                  buffer,
                                  IP_MAXPACKET,
                                  MSG_DONTWAIT,
                                  (struct sockaddr *)&sender,
                                  &sender_len);
        }

        if(packet_len < 0 && errno != EWOULDBLOCK)
            std::cerr << "Recvfrom error: " << strerror(errno) << '\n';
        else if(packet_len == 0)
            std::cerr << "Recvfrom Shutdown" << "\n";
    }

    return feedback;
}
