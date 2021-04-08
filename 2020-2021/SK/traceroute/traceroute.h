// Wojciech Adamiec
// 310064
// 2021-04-06

#include <string>

struct step_feedback {
    unsigned ttl;            // Time-to-live
    unsigned responses;      // Number of responses (0-3)
    unsigned unique_ips;     // Number of unique ips responding (0-3)
    float response_times[3]; // Times for those responses
    std::string ip_addrs[3]; // Unique addressess of ips responding
};

u_int16_t computeICMPChecksum(const void *buff, int length);
struct icmp createICMPHeader(u_int16_t id, u_int16_t seq);
ssize_t sendICMPPacket(const std::string &ip_addr,
                       const int &socket,
                       const struct icmp &header,
                       const int &ttl);
step_feedback pingRouter(const std::string &ip_addr, unsigned short ttl, 
                         const int &socket, const uint16_t &pid);
