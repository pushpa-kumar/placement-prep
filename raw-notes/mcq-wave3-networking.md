# Wave 3 — Computer Networking MCQs (TCP/UDP, OSI/TCP-IP, sockets, routing, DNS, HTTP, multicast). Sourced from GeeksforGeeks GATE-CS "Computer Networks" article sets, GfG topic quizzes, and a GitHub interview-screening prepvault. All GfG entries are GATE-CS-style practice questions republished as CN quizzes (not confirmed as asked verbatim in any specific company's OA), so tagged PRACTICE unless noted otherwise.

### The protocol data unit (PDU) for the application layer in the Internet stack is
- Options: A) Segment B) Datagram C) Message D) Frame
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-2/
- Explanation: The PDU for the Application layer in TCP/IP is a Message. (Also appears verbatim as Q8 in https://www.geeksforgeeks.org/quizzes/application-layer-gq/)

### Which of the following transport layer protocols is used to support electronic mail?
- Options: A) SMTP B) IP C) TCP D) UDP
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-2/
- Explanation: E-mail uses SMTP at the application layer, which relies on TCP as its transport-layer protocol.

### In the IPv4 addressing format, the number of networks allowed under Class C addresses is
- Options: A) 2^14 B) 2^7 C) 2^21 D) 2^24
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-2/
- Explanation: Class C reserves 24 bits for the network ID; with the leading 3 bits fixed as 110, the remaining 21 bits determine the number of available networks (2^21).

### An ISP has the CIDR block 245.248.128.0/20. It wants to give half to Org A and a quarter to Org B, retaining the rest. Which allocation is valid?
- Options: A) 245.248.136.0/21 and 245.248.128.0/22 B) 245.248.128.0/21 and 245.248.128.0/22 C) 245.248.132.0/22 and 245.248.132.0/21 D) 245.248.136.0/22 and 245.248.132.0/21
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-2/
- Explanation: Org A (half) gets 2^11 addresses (prefix /21) and Org B (quarter) gets 2^10 addresses (prefix /22); only option A splits the block into non-overlapping, correctly aligned ranges of those sizes.

### A source S sends a 10^6-bit file to destination D over a network of 2 routers/3 links; find the total transmission + propagation delay
- Options: A) 1005ms B) 1010ms C) 3000ms D) 3003ms
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-2/ (also shown, answer unmarked, in https://www.geeksforgeeks.org/quizzes/network-layer-gq/)
- Explanation: The first packet incurs 6ms total delay; the remaining 999 packets arrive at 1ms transmission intervals thereafter, giving a total of 1005ms. (Classic GATE CS 2013 question.)

### TCP AIMD: window starts at 2 MSS, threshold 8 MSS at first transmission, timeout occurs during the 5th transmission. Congestion window size at end of 10th transmission?
- Options: A) 8 MSS B) 14 MSS C) 7 MSS D) 12 MSS
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-2/
- Explanation: Window sizes progress through slow-start and linear-increase phases; the timeout at transmission 5 forces a multiplicative decrease, resulting in 7 MSS by transmission 10.

### A Layer-4 firewall CANNOT:
- Options: A) block HTTP traffic during 9:00PM and 5:00AM B) block all ICMP traffic C) stop incoming traffic from a specific IP but allow outgoing traffic to the same IP D) block TCP traffic from a specific user on a specific IP on a multi-user system during 9:00PM–5:00AM
- Correct: D
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-3/
- Explanation: A Layer-4 firewall only examines IP addresses, ports, and transport-layer info, so it cannot identify individual users on a multi-user system sharing one IP.

### Email client workflow m1 (send), m2 (download to client), m3 (check via browser) use which protocols respectively?
- Options: A) m1:HTTP, m2:SMTP, m3:POP B) m1:SMTP, m2:FTP, m3:HTTP C) m1:SMTP, m2:POP, m3:HTTP D) m1:POP, m2:SMTP, m3:IMAP
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-3/
- Explanation: SMTP sends mail, POP retrieves/downloads mail to a client, and checking mail via a web browser is a plain HTTP process. (Also appears as Q1 in https://www.geeksforgeeks.org/quizzes/application-layer-gq/)

### Distance vector routing: given update table state, what does node N3 compute as its new distance vector?
- Options: A) (3, 2, 0, 2, 5) B) (3, 2, 0, 2, 6) C) (7, 2, 0, 2, 5) D) (7, 2, 0, 2, 6)
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-3/
- Explanation: N3 receives (1, 0, 2, 7, 3) from N2 and updates its distances to N1 and N5 as 3 and 5 respectively.

### Following a link failure in the same distance-vector network, what distance does N3 compute to N1?
- Options: A) 3 B) 9 C) 10 D) ∞
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-3/
- Explanation: N3 receives an infinite distance from N2 to N1, but receives a distance of 8 from N4 to N1, so it updates its own distance to N1 as 8 + 2 = 10.

### One of the header fields in an IP datagram is the Time to Live (TTL) field. What best explains the need for this field?
- Options: A) It can be used to prioritize packets B) It can be used to reduce delays C) It can be used to optimize throughput D) It can be used to prevent packet looping
- Correct: D
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-4-2/
- Explanation: TTL is an upper bound on how long a datagram can exist in the network, preventing an undeliverable datagram from circulating forever.

### Computers A (10.105.1.113) and B (10.105.1.91) use the same netmask N. Which value of N should NOT be used if A and B must be on the same network?
- Options: A) 255.255.255.0 B) 255.255.255.128 C) 255.255.255.192 D) 255.255.255.224
- Correct: D
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-4-2/
- Explanation: The last octets of the two addresses (113 and 91) differ in their top 3 bits; option D's mask requires those bits to match for same-network membership, so it fails.

### Network of 6 routers R1–R6 using distance-vector routing; after tables stabilize, how many links are never used to carry data?
- Options: A) 4 B) 3 C) 2 D) 1
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-4-2/
- Explanation: Computing all-pairs shortest paths shows links R1–R2 and R4–R6 are never used once the tables stabilize.

### If the weights of the previously-unused links are changed to 2 and distance-vector routing re-stabilizes, how many links remain unused?
- Options: A) 0 B) 1 C) 2 D) 3
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-4-2/
- Explanation: Recomputing shortest paths with the modified weights leaves only the R5–R6 link unused.

### Packets of the same session may be routed through different paths in:
- Options: A) TCP, but not UDP B) TCP and UDP C) UDP, but not TCP D) Neither TCP nor UDP
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-5/
- Explanation: Routing happens at the network layer independent of the transport protocol; adaptive routing can send packets of the same TCP or UDP session over different paths depending on congestion/topology.

### The Address Resolution Protocol (ARP) is used for:
- Options: A) Finding the IP address from the DNS B) Finding the IP address of the default gateway C) Finding the IP address that corresponds to a MAC address D) Finding the MAC address that corresponds to an IP address
- Correct: D
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-5/
- Explanation: ARP is a request-reply mechanism used to discover the MAC address associated with a known IP address on the local network.

### The maximum window size for data transmission using the selective-reject (selective repeat) protocol with n-bit frame sequence numbers is:
- Options: A) 2^n B) 2^(n-1) C) 2^n - 1 D) 2^(n-2)
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-5/
- Explanation: For Selective Repeat, the maximum window size must be at most half the maximum sequence number space (2^(n-1)) to avoid ambiguity between old and new frames.

### Why is the spanning tree algorithm used for bridge routing in LANs with multiple paths?
- Options: A) For shortest path routing between LANs B) For avoiding loops in the routing paths C) For fault tolerance D) For minimizing collisions
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-5/
- Explanation: The Spanning Tree Protocol exists specifically to prevent circular/looping paths in bridged LAN topologies.

### An organization has a class B network and wants to form subnets for 64 departments. The subnet mask would be:
- Options: A) 255.255.0.0 B) 255.255.64.0 C) 255.255.128.0 D) 255.255.252.0
- Correct: D
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-6/
- Explanation: A Class B network has a 16-bit host portion; creating 64 subnets needs 6 extra borrowed bits (2^6 = 64), producing subnet mask 255.255.252.0.

### In a packet-switched network with 2 intermediate nodes, a 24-byte message with 3-byte header per packet — what is the optimum packet size?
- Options: A) 4 B) 6 C) 7 D) 9
- Correct: D
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-6/
- Explanation: Testing candidate packet sizes shows 9-byte packets minimize total transmission time (54t) versus the other options (104t, 60t, 56t).

### Round-trip propagation delay for a 10 Mbps Ethernet with a 48-bit jamming signal is 46.4 ms. What is the minimum frame size?
- Options: A) 94 B) 416 C) 464 D) 512
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-6/
- Explanation: Minimum frame size = round-trip propagation delay x transmission speed = 46.4ms x 10Mbps = 464 kbits, which is required so collisions can still be detected while the frame is being sent.

### Which of the following system calls results in the sending of SYN packets?
- Options: A) socket B) bind C) listen D) connect
- Correct: D
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-7/
- Explanation: connect() on the client initiates the TCP three-way handshake by sending the SYN segment; socket(), bind(), and listen() only set up local state.

### In the slow-start phase of the TCP congestion control algorithm, the size of the congestion window:
- Options: A) does not increase B) increases linearly C) increases quadratically D) increases exponentially
- Correct: D
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-7/
- Explanation: Despite the name "slow start," the window doubles roughly every RTT (grows exponentially) until a loss occurs or the slow-start threshold is reached.

### A class B network has subnet mask 255.255.248.0. What is the maximum number of hosts per subnet?
- Options: A) 1022 B) 1023 C) 2046 D) 2047
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-7/
- Explanation: The mask has 21 set bits, leaving 11 host bits (2^11 = 2048); subtracting the network and broadcast addresses gives 2046 usable hosts. (Same question also appears unanswered in https://www.geeksforgeeks.org/quizzes/ip-addressing-57/)

### What is the maximum size of data that the application layer can pass on to the TCP layer below?
- Options: A) Any size B) 2^16 bytes minus size of TCP header C) 2^16 bytes D) 1500 bytes
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-8/
- Explanation: The application layer can hand off any size of data to TCP; no standard limits it, and lower layers (TCP/IP) perform segmentation/fragmentation as needed.

### Server S does socket()/bind()/listen() then is preempted (no accept() yet). Client P does socket() then connect(). What happens?
- Options: A) connect() returns successfully B) connect() blocks C) connect() returns an error D) connect() results in a core dump
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-8/
- Explanation: Actually the TCP handshake can still complete into the listen backlog even without an active accept(); however GfG's answer key marks (C), reasoning that without an accept() call servicing the connection, connect() eventually times out/errors. (Note: some sources dispute this — the backlog queue is meant to hold such completed connections. Recorded as-published.)

### A computer on a 10 Mbps network is regulated by a token bucket filled at 2 Mbps, initially full with 16 Megabits. What is the maximum duration it can transmit at the full 10 Mbps?
- Options: A) 1.6 seconds B) 2 seconds C) 5 seconds D) 8 seconds
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-8/
- Explanation: Max burst duration = bucket capacity / (peak rate - fill rate) = 16 / (10 - 2) = 2 seconds.

### Which one of the following uses UDP as the transport protocol?
- Options: A) HTTP B) Telnet C) DNS D) SMTP
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-9/
- Explanation: DNS primarily runs over UDP port 53 for its simple request/reply query pattern (falling back to TCP only for large responses/zone transfers).

### In Ethernet when Manchester encoding is used, the bit rate is:
- Options: A) Half the baud rate B) Twice the baud rate C) Same as the baud rate D) none of the above
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-9/
- Explanation: Manchester encoding requires two signal transitions (baud units) per data bit, so the bit rate is half the baud rate.

### n stations in a slotted LAN each transmit with probability p per slot. What is the probability that exactly ONE station transmits in a given slot?
- Options: A) (1-p)^(n-1) B) np(1-p)^(n-1) C) p(1-p)^(n-1) D) 1-(1-p)^(n-1)
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-9/
- Explanation: The probability any one specific station transmits alone is p(1-p)^(n-1); summed over the n stations that could be the one transmitting gives np(1-p)^(n-1).

### In a token ring network with transmission speed 10^7 bps and propagation speed 200 m/microsecond, the 1-bit delay is equivalent to:
- Options: A) 500 meters of cable B) 200 meters of cable C) 20 meters of cable D) 50 meters of cable
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-9/
- Explanation: One bit takes 0.1 microseconds to transmit at 10^7 bps; at 200 m/microsecond propagation speed that corresponds to 20 meters of cable.

### A class B host address is split into subnets with a 6-bit subnet number. What is the maximum number of subnets and hosts per subnet?
- Options: A) 62 subnets and 262142 hosts B) 64 subnets and 262142 hosts C) 62 subnets and 1022 hosts D) 64 subnets and 1024 hosts
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-10/
- Explanation: Max subnets = 2^6 - 2 = 62 (excluding all-zero and all-one subnet fields); max hosts per subnet = 2^10 - 2 = 1022 (excluding network and broadcast addresses).

### The message 11001001 is to be transmitted using the CRC polynomial x^3 + 1. What message should actually be transmitted?
- Options: A) 11001001000 B) 11001001011 C) 11001010 D) 110010010011
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-10/
- Explanation: x^3+1 corresponds to divisor 1001; dividing 11001001000 by 1001 via XOR leaves remainder 011, so the transmitted frame is the original message with that CRC appended: 11001001 011.

### Match OSI/TCP-IP layer protocols: (P) SMTP (Q) BGP (R) TCP (S) PPP to their layers
- Options: A) P-2,Q-1,R-3,S-5 B) P-1,Q-4,R-2,S-3 C) P-1,Q-4,R-2,S-5 D) P-2,Q-4,R-1,S-3
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/computer-networks/computer-networks-set-10/
- Explanation: SMTP is an application-layer protocol, BGP is used at/for the network layer (routing), TCP is a transport-layer protocol, and PPP is a data-link layer protocol.

### What is the main function of the Application Layer in the OSI model?
- Options: A) Error detection and correction B) Routing of packets C) Providing network services to end users D) Establishing physical connections
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/quizzes/application-layer-gq/
- Explanation: The Application layer is the topmost OSI layer and is the interface through which end-user applications access network services.

### What additional feature does HTTPS provide over plain HTTP?
- Options: A) Compression B) Encryption and authentication using SSL/TLS C) Faster data transfer using UDP D) Multicast support
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/quizzes/application-layer-gq/
- Explanation: HTTPS is HTTP layered over TLS/SSL, adding encryption of traffic and authentication of the server (and optionally the client).

### Which of the following is a key characteristic of TFTP (Trivial File Transfer Protocol)?
- Options: A) Uses TCP for transmission B) Supports authentication and encryption C) Simpler and faster than FTP, uses UDP D) Requires user credentials before file transfer
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/quizzes/application-layer-gq/
- Explanation: TFTP is a stripped-down file transfer protocol that runs over UDP and has no built-in authentication, making it simpler (but less reliable/secure) than FTP.

### The term "Internetworking" primarily refers to:
- Options: A) Connecting devices within a single LAN B) Connecting multiple networks together C) Sharing files between two computers D) Establishing wireless communication
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/quizzes/application-layer-gq/
- Explanation: Internetworking specifically means connecting distinct networks (e.g., via routers) into one larger network, as with the Internet itself.

### Which protocol allows a client to access and manage email on a central mail server repository (as opposed to just downloading it)?
- Options: A) POP3 B) IMAP C) SMTP D) DMSP
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/quizzes/application-layer-gq/
- Explanation: IMAP keeps mail on the server and lets clients manage/sync folders remotely, unlike POP3 which typically downloads and removes mail.

### A user wants to send an email, check headers without downloading, and view mail via a browser. Which protocol set is used respectively?
- Options: A) SMTP, HTTPS, IMAP B) SMTP, POP, IMAP C) SMTP, IMAP, HTTPS D) SMTP, IMAP, POP
- Correct: D
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/quizzes/application-layer-gq/
- Explanation: SMTP sends the mail; IMAP allows checking headers/managing mail on the server without full download; viewing mail in a browser is a plain HTTP/POP-style webmail access, matching option D per the GfG answer key.

### Which application-layer protocol is used for initiating, maintaining, and terminating real-time multimedia sessions (e.g., VoIP/video calls)?
- Options: A) Session Maintenance Protocol B) Real-time Streaming Protocol C) Real-time Transport Control Protocol D) Session Initiation Protocol
- Correct: D
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GeeksforGeeks — https://www.geeksforgeeks.org/quizzes/application-layer-gq/
- Explanation: SIP (Session Initiation Protocol) is the standard signaling protocol for setting up and tearing down real-time multimedia sessions.

### How many layers are in the OSI model?
- Options: A) 5 B) 6 C) 7 D) 4
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault, tagged interview/screening) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: The seven OSI layers are Physical, Data Link, Network, Transport, Session, Presentation, and Application.

### Which layer of the OSI model is responsible for "Routing"?
- Options: A) Data Link B) Network C) Transport D) Application
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: Routers and routing decisions operate at Layer 3, the Network layer.

### Which protocol is used to map an IP address to a physical (MAC) address?
- Options: A) DHCP B) ARP C) DNS D) FTP
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: ARP (Address Resolution Protocol) resolves a known IP address to its corresponding MAC address on a local network.

### What is the default port for HTTPS?
- Options: A) 80 B) 443 C) 22 D) 21
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: HTTP uses port 80 by default, while HTTPS (HTTP over TLS) uses port 443.

### TCP is a __________ protocol.
- Options: A) Connectionless B) Connection-oriented C) Physical layer D) Presentation layer
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: TCP requires a 3-way handshake (SYN, SYN-ACK, ACK) to establish a connection before any data transfer.

### Which of the following is a "Connectionless" protocol?
- Options: A) TCP B) UDP C) HTTP D) FTP
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: UDP sends datagrams without establishing or maintaining a connection state, unlike TCP.

### What is the primary function of "DNS"?
- Options: A) To assign IP addresses B) To map domain names to IP addresses C) To encrypt web traffic D) To filter spam emails
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: DNS (Domain Name System) translates human-readable domain names into the numeric IP addresses used for routing, acting like the internet's phonebook.

### Which protocol is used for sending emails?
- Options: A) POP3 B) IMAP C) SMTP D) HTTP
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: SMTP (Simple Mail Transfer Protocol) is used to send mail; POP3/IMAP are used to retrieve/manage received mail.

### What is a "Subnet Mask" used for?
- Options: A) To hide the IP address B) To distinguish between the network address and host address C) To speed up the internet D) To identify the physical location of a computer
- Correct: B
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: The subnet mask splits an IP address into its network and host portions.

### What is the purpose of the "3-way Handshake" in TCP?
- Options: A) To encrypt the connection B) To authenticate the user C) To synchronize sequence numbers and establish a connection D) To check if the computer is turned on
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: The SYN, SYN-ACK, ACK exchange synchronizes initial sequence numbers on both sides and confirms both sender and receiver are ready to communicate.

### Which layer of the OSI model does "TLS/SSL" primarily operate on?
- Options: A) Network B) Transport C) Presentation (though often integrated into Application/Transport) D) Physical
- Correct: C
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: Encryption/decryption is conceptually a Presentation-layer function in OSI terms, though in real TCP/IP stacks TLS is implemented on top of the transport layer.

### A "Hub" is a Layer ____ device.
- Options: A) 1 B) 2 C) 3 D) 4
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: A hub is a simple Physical-layer (Layer 1) device that broadcasts electrical/optical signals to all ports; switches operate at Layer 2.

### What is the size of an IPv4 address?
- Options: A) 32 bits B) 64 bits C) 128 bits D) 16 bits
- Correct: A
- Company: unknown/general
- Type: MCQ
- Status: PRACTICE
- Source: GitHub (mrxsierra/CS prepvault) — https://github.com/mrxsierra/CS/blob/main/prepvault/03_interview_formats/technical_screens/networking_mcqs.md
- Explanation: IPv4 addresses are 4 bytes (32 bits) long; IPv6 addresses are 128 bits.
