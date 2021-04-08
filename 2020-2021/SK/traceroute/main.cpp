// Wojciech Adamiec
// 310064
// 2021-04-06

#include "traceroute.h"
#include <arpa/inet.h>
#include <iomanip>
#include <iostream>
#include <netinet/ip_icmp.h>
#include <unistd.h>

// Function to validate IP address
bool isValidIpAddress(char *ipAddress){
    struct sockaddr_in sa;
    int result = inet_pton(AF_INET, ipAddress, &(sa.sin_addr));
    return result != 0;
}

// Function to validate input
bool isInputValid(int argc, char *argv[]){
    if (argc == 1){
        std::cerr << "Give IP address as an argument" << "\n";
        return false;
    }

    if (argc > 2){
        std::cerr << "Too many arguments" << "\n";
        return false;
    }

    if (!isValidIpAddress(argv[1])){
        std::cerr << "Invalid IP address" << "\n";
        return false;
    }
    return true;
}


int main(int argc, char* argv[]){

    // Validate input
    if (!isInputValid(argc, argv)){
        return -1;
    }

    const std::string ip_address = argv[1];
    
    // Setting up raw socket
    int sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);

    // Getting pid for this program
    const uint16_t pid = getpid() & 0xffff;
    
    bool destination_reached = false;

    // Steps from range 1 to destination (or 30)
    for(int ttl = 1; ttl <= 30 && !destination_reached; ttl++) {
        auto feedback = pingRouter(ip_address, ttl, sockfd, pid);

        // Printing step number
        std::cout << ttl << ". ";

        // CASE: NO RESPONSE
        if(feedback.responses == 0)
            std::cout << "*\n";
        else {
            // Listing all ip addresses
            for(unsigned j = 0; j < feedback.unique_ips; j++) {
                std::cout << feedback.ip_addrs[j] << " ";

                // Checking if the target ip_addr has been reached
                if(feedback.ip_addrs[j].compare(ip_address) == 0)
                    destination_reached = true;
            }

            // CASE: NOT ALL REQUESTS GOT A RESPONSE
            if(feedback.responses < 3)
                std::cout << "???\n";
            else {
                auto avg = (feedback.response_times[0] + feedback.response_times[1] +
                            feedback.response_times[2]) /
                           3.0;
                std::cout << std::fixed << std::setprecision(2) << avg << "ms\n";
            }
        }
    }

    return 0;
}
