# Things to cover for cyber security: 1-13 Covers Networks
#-----------------------------------------------------------





# Topics

"""
 1. Network Types, Topologies, and Characteristics

	1.1 Network topologies
	1.2 Network types
	1.3 Service providers

2. Conceptual Models and Network Devices

	2.1 Conceptual models
	2.2 OSI model layers
	2.3 DoD model layers
	2.4 Networking devices
	2.5 Networked devices

3. Bounded Media Standards and Applications

	3.1 Bounded media
	3.2 Coaxial media
	3.3 TP media
	3.4 Fiber media
	3.5 Bounded media management

4. Address Types

	4.1 Types of network addresses
	4.2 MAC address
	4.3 IPv4
	4.4 IPv6

5. Segmentation

	5.1 Binary decimal conversion
	5.2 Network address

	5.3 Classless addresses
	5.4 Subnetting basics
	5.5 VLAN

6. Protocols

	6.1 Protocol types
	6.2 Distance vector protocol
	6.3 Link state protocol
	6.4 Common protocols
	6.5 Secure protocols
	6.6 Mail, web and remote access protocols

7. Switches and Routers

	7.1 Network transmission
	7.2 Network traffic
	7.3 Switch features
	7.4 Switch configuration
	7.5 Security zones and IP support
	7.6 Routers
8. Network Security

	8.1 Security
	8.2 Authentication and Authorization
	8.3 Multifactor and policies
	8.4 Types of authentication
	8.5 RBAC, MAC, and DAC
	8.6 Security attacks
	8.7 Network security systems
	8.8 Endpoint security measures
	8.9 Other security measures
	8.10 VPN remote access
9. Wireless Networking

	9.1 Wireless characteristics
	9.2 WLAN standards
	9.3 Wireless network design
	9.4 WLAN attacks
	9.5 WLAN Security
	10. Network Services
10. Network Services
	10.1 DNS
	10.2 DNS process
	10.3 DHCP
	10.4 DHCP server and queries
	10.5 NTP
11. Network Architecture

	11.1 Data center
	11.2 Virtual
	11.3 Cloud
	11.4 Network storage
12. Network Operations

	12.1 Performance monitoring
	12.2 Performance monitoring resources
	12.3 Command-line performance monitoring
	12.4 Performance monitoring software
	12.5 Network platform performance monitoring
	12.6 Network documentation
	12.7 Network plans and policies
	12.8 High availability
	12.9 Replication and recovery
	12.10 Disaster recovery
13. Network Troubleshooting

	13.1 Troubleshooting methodology
	13.2 Identifying a physical layer problem
	13.3 Identifying a higher layer problem
	13.4 Troubleshooting tools
	13.5 Troubleshooting solution considerations

"""

# Continued Notes Below

"""

1. Network Types, Topologies, and Characteristics

	1.1 Network Topologies

	Star Topology: In a star topology, all nodes are connected to a central device, like a hub or a switch. This setup minimizes the chance of network failure due to a single cable's malfunction. However, the entire network depends on the central device's functionality.
	Mesh Topology: Mesh topology involves every node having a direct link to every other node. It's highly fault-tolerant but expensive and complex, mostly used in WANs or for interconnecting LANs.
	1.2 Network Types

	LAN (Local Area Network): A LAN covers a small geographical area like a home, office, or building. It's used for connecting computers and devices within this limited area.
	WAN (Wide Area Network): WAN spans a large geographic area, like a city, country, or global connections. The internet is the largest example of a WAN.
	1.3 Service Providers

	ISPs (Internet Service Providers): ISPs provide internet access to individuals and organizations. They connect users to their networks for internet services.
	Cloud Service Providers: These offer cloud computing platforms and services. They host hardware, software, servers, storage, and other infrastructure components.


2. Conceptual Models and Network Devices

	2.1 Conceptual Models

	TCP/IP Model: A four-layer model used for end-to-end communications over the internet. The layers are the application layer, transport layer, internet layer, and network access layer.
	Hybrid Model: Combines elements of both OSI and TCP/IP models. It's used for more practical and flexible network framework understanding.
	2.2 OSI Model Layers

	Application Layer: This layer provides networking services to end-user applications. It deals with issues like network transparency, resource allocation, etc.
	Presentation Layer: Responsible for data translation and encryption. It ensures that the data sent from the application layer is readable by the network.
	2.3 DoD Model Layers

	Process/Application Layer: Combines the functions of the application, presentation, and session layers from the OSI model.
	Host-to-Host Layer: Corresponds to the OSI model's transport layer, ensuring reliable data transport.

	2.4 Networking Devices

	Routers: Connect different networks together, directing data packets between them.
	Switches: Work within a single network, directing data at the data link layer.

	2.5 Networked Devices

	Computers: Personal computers, workstations, and servers connected to the network.
	Network Printers: Printers accessible by multiple users on a network.


3. Bounded Media Standards and Applications

	3.1 Bounded Media

	Twisted Pair Cable: Consists of pairs of wires twisted together to reduce electromagnetic interference. Used in Ethernet networks.
	Fiber Optic Cable: Transmits data as light pulses through glass or plastic fibers. Used for high-speed, long-distance transmission.
	3.2 Coaxial Media

	Coaxial Cable: A single copper wire surrounded by insulation, a metallic shield, and a plastic cover. Used for cable TV and traditional broadband internet.
	3.3 TP Media

	Unshielded Twisted Pair (UTP): Used for LANs and telephone networks. Susceptible to interference but cost-effective.
	Shielded Twisted Pair (STP): Has additional shielding to protect against electromagnetic interference.
	3.4 Fiber Media

	Single-Mode Fiber: Used for long-distance, high-bandwidth transmissions. Has a single light path through a narrow core.
	Multi-Mode Fiber: Has a larger core and multiple light paths, suitable for shorter distances.
	3.5 Bounded Media Management

	Cable Management: Involves organizing and protecting cables to ensure reliable performance and ease of maintenance.
	Testing and Certification: Regular testing of cables for performance and adherence to standards.

4. Address Types

	4.1 Types of Network Addresses

	IP Address: A numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.
	Hostname: A label assigned to a device on a network, used to identify the device in various forms of electronic communication.
	4.2 MAC Address

	Definition: A unique identifier assigned to a network interface controller (NIC) for communications at the data link layer of a network segment.
	Usage: Used as a network addressfor Ethernet and other IEEE 802 network technologies.

	4.3 IPv4

	Structure: IPv4 addresses are 32-bit numbers, usually represented in dot-decimal notation (e.g., 192.168.1.1).
	Subnetting: Dividing a network into smaller sub-networks to improve management and security. For example, 255.255.255.0 is a common subnet mask.
	4.4 IPv6

	Structure: IPv6 addresses are 128-bit numbers, represented in hexadecimal notation, addressing the issue of IPv4 address exhaustion.
	Features: Includes features like simplified header format, improved support for extensions and options, and better security measures.


5. Segmentation

	5.1 Binary Decimal Conversion

	Concept: Essential for understanding IP addressing and subnetting. For example, the binary 11000000.10101000.00000001.00000001 corresponds to the IPv4 address 192.168.1.1.
	Tools: Various online tools and calculators are available for converting between binary and decimal formats.
	5.2 Network Address

	Definition: Identifies a network and is used in routing. The network address is determined by the IP address and subnet mask.
	Example: With an IP address of 192.168.1.10 and a subnet mask of 255.255.255.0, the network address is 192.168.1.0.
	5.3 Classless Addresses

	Concept: Refers to the allocation of IP addresses without class-based restrictions, allowing for more efficient use of IP address space.
	CIDR Notation: Uses a suffix to specify the number of bits in the network portion of the address, like /24 in 192.168.1.0/24.
	5.4 Subnetting Basics

	Purpose: Divides a network into smaller, manageable parts. This improves security and network traffic management.
	Example: Subnetting a 192.168.1.0 network with a /24 mask into two subnets with /25 masks creates 192.168.1.0/25 and 192.168.1.128/25.
	5.5 VLAN

	Definition: A Virtual Local Area Network (VLAN) allows network administrators to segment a LAN into smaller, isolated networks.
	Benefits: Enhances security, reduces broadcast domains, and simplifies network management.

6. Protocols

	6.1 Protocol Types

	Definition: Protocols are sets of rules governing data communication between devices.
	Examples: TCP/IP for internet communication, HTTP for web traffic, SMTP for email.
	6.2 Distance Vector Protocol

	Concept: A routing protocol that uses the Bellman-Ford algorithm to determine the best path.
	Example: RIP (Routing Information Protocol) is a distance vector protocol that uses hop count as a routing metric.
	6.3 Link State Protocol

	Concept: A routing protocol that builds a map of the network to determine the best path.
	Example: OSPF (Open Shortest Path First) is a widely used link state protocol.
	6.4 Common Protocols

	TCP (Transmission Control Protocol): Ensures reliable data transmission.
	UDP (User Datagram Protocol): Used for speed, where error checking and correction are not required.
	6.5 Secure Protocols

	TLS/SSL: Provides security over a computer network. Websites use HTTPS, which combines HTTP with SSL/TLS.
	SSH: Secure Shell protocol for secure network services over an unsecured network.
	6.6 Mail, Web, and Remote Access Protocols

	SMTP (Simple Mail Transfer Protocol): For sending emails.
	HTTP/HTTPS: For web browsing.
	RDP (Remote Desktop Protocol): For remote desktop connections.

7. Switches and Routers

	7.1 Network Transmission

	Switches: Operate at the data link layer (Layer 2) of the OSI model, forwarding data based on MAC addresses.
	Routers: Operate at the network layer (Layer 3), directing data packets based on IP addresses.
	7.2 Network Traffic

	Switches: Segment a network into separate collision domains, reducing traffic congestion.
	Routers: Manage traffic between different networks, filtering and forwarding data to its intended destination.
	7.3 Switch Features

	Managed Switches: Offer advanced features like VLANs, QoS (Quality of Service), and SNMP (Simple Network Management Protocol).
	Unmanaged Switches: Simple plug-and-play devices without advanced features.
	7.4 Switch Configuration

	VLAN Configuration: Assigning ports to different VLAN

	s: Allows segregation of network traffic for enhanced security and management.
	Port Security: Configuring switches to limit the devices that can connect to a network, enhancing security.

	7.5 Security Zones and IP Support

	Security Zones: Configuring network segments with different security levels. For instance, a DMZ (Demilitarized Zone) for public-facing servers.
	IP Support: Modern switches support both IPv4 and IPv6 addressing, facilitating future-proof network configurations.
	7.6 Routers

	Routing Tables: Routers use routing tables to determine the best path for forwarding packets.
	Dynamic Routing: Routers can dynamically update their routing tables using routing protocols like OSPF or BGP.

8. Network Security

	8.1 Security

	Importance: Protecting data integrity, confidentiality, and availability in network communications.
	Measures: Implementing firewalls, intrusion detection systems, and secure protocols.
	8.2 Authentication and Authorization

	Authentication: Verifying a user's or device's identity. Examples include passwords, biometrics, and digital certificates.
	Authorization: Determining the resources a user can access post-authentication.
	8.3 Multifactor and Policies

	Multifactor Authentication (MFA): Requires multiple methods for verifying identity, enhancing security.
	Security Policies: Guidelines and practices for managing network security.
	8.4 Types of Authentication

	Knowledge-Based: Something the user knows, like a password.
	Possession-Based: Something the user has, like a token or a smartphone.
	8.5 RBAC, MAC, and DAC

	Role-Based Access Control (RBAC): Access decisions based on the roles of individual users.
	Mandatory Access Control (MAC): Access levels are based on information classification.
	Discretionary Access Control (DAC): The owner of the information or resource sets policies for its access.
	8.6 Security Attacks

	DDoS Attacks: Overwhelming a system or network with traffic to render it unusable.
	Phishing: Deceiving users into providing sensitive information.
	8.7 Network Security Systems

	Firewalls: Control incoming and outgoing network traffic based on predetermined security rules.
	Intrusion Detection Systems (IDS): Monitor network traffic for suspicious activities.
	8.8 Endpoint Security Measures

	Antivirus Software: Protects individual devices by detecting and removing malware.
	Device Management Policies: Ensuring that all devices adhere to security standards.
	8.9 Other Security Measures

	VPN (Virtual Private Network): Securely extends a private network across a public network.
	Data Encryption: Encrypting data in transit and at rest to protect its confidentiality and integrity.
	8.10 VPN Remote Access

	Remote Access VPNs: Allow employees to securely access corporate resources while working remotely.
	VPN Protocols: Protocols like IPSec and OpenVPN provide secure, encrypted tunnels for data transmission.

9. Wireless Networking

	9.1 Wireless Characteristics

	Mobility: Wireless networks allow users to move freely while maintaining network connectivity.
	Interference: Susceptible to interference from other devices and environmental factors.
	9.2 WLAN Standards

	IEEE 802.11: A set of standards for implementing wireless local area network (WLAN) computer communication.
	Wi-Fi 6 (802.11ax): The latest Wi-Fi standard, offering improved efficiency and throughput.
	9.3 Wireless Network Design

	Coverage Area: Designing the network to provide consistent coverage across the desired area.
	Access Point Placement: Strategically placing access points to ensure optimal signal strength and coverage.
	9.4 WLAN Attacks

	Rogue Access Points: Unauthorized access points that can capture sensitive information.
	Evil Twin Attacks: Duplication of legitimate access points to deceive users into connecting.
	9.5 WLAN Security

	WPA3: The latest security standard for Wi-Fi networks.
	Network Segmentation: Separating network traffic to limit the spread of attacks and manage access control.

10. Network Services

	10.1 DNS

	Domain Name System (DNS): Translates domain names into IP addresses, allowing users to access websites using familiar names instead of numerical addresses.
	Hierarchical Structure: Organizes domain names into a hierarchy, such as .com, .net, .org.
	10.2 DNS Process

	Resolution Process: When a user enters a domain name, a DNS resolver queries DNS servers to find the corresponding IP address.
	Caching: DNS servers temporarily store DNS records to speed up future requests for the same domain.

	10.3 DHCP

	Dynamic Host Configuration Protocol (DHCP)**: Automatically assigns IP addresses and other network configurations to devices on a network.

	Lease Mechanism: DHCP leases an IP address to a device for a specific period, after which it can be reassigned.
	10.4 DHCP Server and Queries

	Server Role: A DHCP server manages the pool of IP addresses and provides them to clients on request.
	Client Requests: When a device connects to the network, it sends a DHCP discovery message to request network configuration.
	10.5 NTP

	Network Time Protocol (NTP): Synchronizes the clocks of computers over a network.
	Server Hierarchy: NTP uses a hierarchical system of time sources, with various stratum levels indicating the distance from the reference clock.

11. Network Architecture

	11.1 Data Center

	Infrastructure: Data centers house networked computers, storage systems, and associated components for organizing, processing, and storing large amounts of data.
	Design Considerations: Include redundancy, scalability, and security.
	11.2 Virtual

	Virtualization: Creating virtual versions of physical network resources, such as servers, storage, and network devices.
	Benefits: Increases efficiency, flexibility, and scalability of network resources.
	11.3 Cloud

	Cloud Networking: Involves delivering network services and infrastructure through the cloud.
	Service Models: Includes Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS).
	11.4 Network Storage

	Network Attached Storage (NAS): A dedicated file storage device that provides data access to a network of users.
	Storage Area Network (SAN): A specialized network that provides access to consolidated, block-level data storage.

12. Network Operations

	12.1 Performance Monitoring

	Importance: Ensuring the network operates efficiently and meets performance standards.
	Tools: Use of network monitoring tools and software to track performance metrics.
	12.2 Performance Monitoring Resources

	CPU and Memory Utilization: Monitoring these resources helps identify performance bottlenecks.
	Bandwidth Usage: Tracking the amount of data transmitted over a network to ensure adequate capacity.
	12.3 Command-Line Performance Monitoring

	Linux Tools: Commands like top, iftop, and netstat provide real-time network performance insights.
	Windows Tools: Task Manager and Performance Monitor are used for monitoring network performance.
	12.4 Performance Monitoring Software

	Nagios: An open-source software for network, server, and application monitoring.
	SolarWinds: Offers a suite of tools for comprehensive network performance monitoring.
	12.5 Network Platform Performance Monitoring

	Cisco DNA Center: Provides a centralized platform for managing and optimizing network performance.
	VMware vRealize Network Insight: Offers network visibility and analytics in virtualized and cloud environments.
	12.6 Network Documentation

	Network Diagrams: Visual representations of the network's layout and connections.
	Configuration Documentation: Detailed records of network configurations and settings.
	12.7 Network Plans and Policies

	Network Planning: Involves designing the network to meet current and future business requirements.
	Network Policies: Guidelines and procedures for managing and operating the network.
	12.8 High Availability

	Concept: Designing networks to ensure continuous operation and minimize downtime.
	Techniques: Includes redundancy, failover systems, and load balancing.
	12.9 Replication and Recovery

	Data Replication: Copying data to different locations for backup and recovery purposes.
	Disaster Recovery Plans: Strategies for recovering network operations after a disaster.
	12.10 Disaster Recovery

	Business Continuity Planning: Ensuring that essential functions can continue during and after a disaster.
	Recovery Point Objective (RPO) and Recovery Time Objective (RTO): Key metrics in disaster recovery planning.

13. Network Troubleshooting

	13.1 Troubleshooting Methodology

	Identify the Problem: Gathering information to understand the nature and scope of the issue.
	Establish a Theory of Probable Cause: Hypothesizing potential causes based on the collected information.
	13.2 Identifying a Physical Layer Problem

	Symptoms: Includes connectivity issues, poor network performance, and intermittent disconnections.
	Tools: Cable testers, toners, and network probes for diagnosing physical layer issues.
	13.3 Identifying a Higher Layer Problem

	Application Layer Issues: Problems with specific applications or services, indicated by error messages or functionality issues.
	Network Layer Issues: Involving routing and IP addressing, often identified through traceroute or ping tests.
	13.4 Troubleshooting Tools

	**Wireshark A network protocol analyzer that captures and analyzes packets to troubleshoot network issues.

	Ping and Traceroute: Basic tools for testing connectivity and tracing the path data takes through the network.

	13.5 Troubleshooting Solution Considerations

	Solution Implementation: After identifying the problem, apply the appropriate solution, such as reconfiguring settings or replacing faulty hardware.
	Verification and Monitoring: Ensure the issue is resolved and monitor the network for any further problems or recurring issues.

"""



# Projects to do

"""


Easy to Medium Difficulty Projects

Network Scanner:

	Objective: Create a Python script that scans a network for active devices.
	Parameters: Use Python's socket library to implement a scanner that detects devices on the same network. Display IP addresses and MAC addresses.
	Learning: Understanding of IP addressing and MAC addresses.

Ping Sweep Tool:

	Objective: Develop a script to perform a ping sweep of a given IP range.
	Parameters: Utilize Python's os or subprocess module to ping a range of IP addresses and identify which ones are active.
	Learning: Grasping network reachability and basic scripting in Python.

Simple Packet Sniffer:

	Objective: Create a packet sniffer using Python to capture and analyze network packets.
	Parameters: Use the scapy library to capture packets and display basic information about them, such as source and destination IPs.
	Learning: Insights into packet structures and network protocols.

Port Scanner:

	Objective: Develop a port scanner to identify open ports on a given IP address.
	Parameters: Using Python’s socket library, scan specified ports and report their status (open/closed).
	Learning: Understanding of TCP/IP protocols and port functions.

DNS Resolver Script:

	Objective: Write a Python script to resolve domain names to IP addresses.
	Parameters: Use socket library to convert human-readable domain names into IP addresses.
	Learning: Comprehension of DNS process and Python network programming.

Subnet Calculator:

	Objective: Create a tool that calculates the subnet of a given IP address and mask.
	Parameters: Input an IP address and subnet mask, then calculate the network address, broadcast address, and range of usable IP addresses.
	Learning: Practical application of subnetting and binary-decimal conversion.

Wi-Fi Network Analyzer:

	Objective: Build a script to analyze nearby Wi-Fi networks.
	Parameters: Use Linux tools like iwlist or nmcli in combination with Python to display available networks and their characteristics (e.g., SSID, signal strength).
	Learning: Understanding wireless networks and Linux command-line tools.

Simple Firewall with IPTables:

	Objective: Configure a basic firewall on a Linux machine using IPTables.
	Parameters: Write bash scripts to set up rules for allowing or blocking traffic based on IP addresses, ports, or protocols.
	Learning: Grasp basic firewall concepts and IPTables usage.

Network Performance Monitor:

	Objective: Develop a script to monitor and log network performance metrics.
	Parameters: Capture data like bandwidth usage, latency, and packet loss. Use Python with Linux commands (ping, traceroute, ifconfig).
	Learning: Insights into network performance monitoring and data logging.

Basic Intrusion Detection System (IDS):

	Objective: Implement a simple IDS that detects unusual network activities.
	Parameters: Analyze network traffic for anomalies (e.g., a high number of requests from a single source) using Python.
	Learning: Introductory understanding of network security and anomaly detection.


Harder Projects

VLAN Configuration Simulation:

	Objective: Simulate the configuration and management of VLANs in a network.
	Parameters: Use a network simulator like GNS3 or Packet Tracer, integrate with Python scripts to automate VLAN configurations across multiple switches.
	Learning: Deep dive into VLAN concepts, network device configuration, and automation.

Custom VPN Server and Client:

	Objective: Set up a custom VPN server on a Linux machine and create a client to connect to it.
	Parameters: Use OpenVPN or WireGuard to set up the server. Write a Python script for a client that can connect to this server, authenticating with certificates.
	Learning: Advanced understanding of VPNs, encryption, authentication, and network security.




"""
