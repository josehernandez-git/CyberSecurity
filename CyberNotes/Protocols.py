"""
6. Protocols

6.1 Protocol Types
Protocols are standardized rules that define how data is transmitted and received over a network. They ensure proper communication between devices. Protocols can be categorized based on their function and layer in the OSI model.

Types of Protocols:
1. Communication Protocols: Define the rules for data exchange (e.g., TCP/IP, UDP).
2. Network Management Protocols: Monitor and manage network devices (e.g., SNMP, ICMP).
3. Security Protocols: Ensure secure data transmission (e.g., SSL/TLS, IPSec).
4. Routing Protocols: Determine the best path for data transmission (e.g., RIP, OSPF, BGP).
5. Application Protocols: Facilitate specific application services (e.g., HTTP, FTP, SMTP).

6.2 Distance Vector Protocol
Distance vector protocols are routing protocols that determine the best path to a destination based on distance (hop count). Each router maintains a routing table with distances to other routers and shares this information with its neighbors.

Example: Routing Information Protocol (RIP)
- RIP uses hop count as a metric, with a maximum limit of 15 hops.
- Routers periodically share their routing tables with neighbors to update path information.

6.3 Link State Protocol
Link state protocols are routing protocols that use a complete map of the network topology to determine the best path. Each router independently calculates the shortest path to every other router using algorithms like Dijkstra's.

Example: Open Shortest Path First (OSPF)
- OSPF uses the Dijkstra algorithm to find the shortest path.
- Routers exchange link-state advertisements (LSAs) to build a complete network map.

6.4 Common Protocols
Common protocols are widely used in various network functions and services.

Examples:
1. HTTP (Hypertext Transfer Protocol): Used for transferring web pages.
2. FTP (File Transfer Protocol): Used for transferring files between client and server.
3. SMTP (Simple Mail Transfer Protocol): Used for sending emails.
4. DHCP (Dynamic Host Configuration Protocol): Assigns IP addresses to devices on a network.
5. DNS (Domain Name System): Translates domain names to IP addresses.

6.5 Secure Protocols
Secure protocols provide encryption and authentication to ensure the confidentiality, integrity, and authenticity of data during transmission.

Examples:
1. SSL/TLS (Secure Sockets Layer/Transport Layer Security): Secures HTTP traffic (HTTPS).
2. IPSec (Internet Protocol Security): Secures IP communications by authenticating and encrypting each IP packet.
3. SSH (Secure Shell): Provides a secure channel for remote login and command execution.

6.6 Mail, Web, and Remote Access Protocols
These protocols facilitate specific services like email, web browsing, and remote access.

Examples:
1. Mail Protocols:
   - SMTP (Simple Mail Transfer Protocol): Used for sending emails.
   - IMAP (Internet Message Access Protocol): Used for retrieving emails from a server.
   - POP3 (Post Office Protocol version 3): Used for retrieving emails from a server.

2. Web Protocols:
   - HTTP (Hypertext Transfer Protocol): Used for transferring web pages.
   - HTTPS (Hypertext Transfer Protocol Secure): Secures HTTP traffic using SSL/TLS.

3. Remote Access Protocols:
   - SSH (Secure Shell): Provides secure remote login and command execution.
   - RDP (Remote Desktop Protocol): Allows users to connect to another computer over a network.

"""

# Example for 6.1 Protocol Types
class Protocol:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

    def describe(self):
        return f"Protocol: {self.name} - Type: {self.type} - Description: {self.description}"


protocols = [
    Protocol("TCP/IP", "Communication", "Defines how data is exchanged over the internet."),
    Protocol("SNMP", "Network Management", "Monitors and manages network devices."),
    Protocol("SSL/TLS", "Security", "Ensures secure data transmission."),
    Protocol("RIP", "Routing", "Uses hop count to determine the best path."),
    Protocol("HTTP", "Application", "Facilitates transferring web pages.")
]

for protocol in protocols:
    print(protocol.describe())

# Example for 6.2 Distance Vector Protocol
class DistanceVectorProtocol:
    def __init__(self, name, metric, description):
        self.name = name
        self.metric = metric
        self.description = description

    def describe(self):
        return f"Distance Vector Protocol: {self.name} - Metric: {self.metric} - Description: {self.description}"


rip = DistanceVectorProtocol("RIP", "Hop Count", "Uses hop count as a metric, with a maximum limit of 15 hops.")
print(rip.describe())

# Example for 6.3 Link State Protocol
class LinkStateProtocol:
    def __init__(self, name, algorithm, description):
        self.name = name
        self.algorithm = algorithm
        self.description = description

    def describe(self):
        return f"Link State Protocol: {self.name} - Algorithm: {self.algorithm} - Description: {self.description}"


ospf = LinkStateProtocol("OSPF", "Dijkstra", "Uses Dijkstra algorithm to find the shortest path.")
print(ospf.describe())

# Example for 6.4 Common Protocols
class CommonProtocol:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def describe(self):
        return f"Common Protocol: {self.name} - Function: {self.function}"


common_protocols = [
    CommonProtocol("HTTP", "Transferring web pages"),
    CommonProtocol("FTP", "Transferring files between client and server"),
    CommonProtocol("SMTP", "Sending emails"),
    CommonProtocol("DHCP", "Assigning IP addresses to devices"),
    CommonProtocol("DNS", "Translating domain names to IP addresses")
]

for protocol in common_protocols:
    print(protocol.describe())

# Example for 6.5 Secure Protocols
class SecureProtocol:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def describe(self):
        return f"Secure Protocol: {self.name} - Function: {self.function}"


secure_protocols = [
    SecureProtocol("SSL/TLS", "Secures HTTP traffic (HTTPS)"),
    SecureProtocol("IPSec", "Secures IP communications by authenticating and encrypting each IP packet"),
    SecureProtocol("SSH", "Provides a secure channel for remote login and command execution")
]

for protocol in secure_protocols:
    print(protocol.describe())

# Example for 6.6 Mail, Web, and Remote Access Protocols
class ServiceProtocol:
    def __init__(self, name, type, function):
        self.name = name
        self.type = type
        self.function = function

    def describe(self):
        return f"{self.type} Protocol: {self.name} - Function: {self.function}"


mail_protocols = [
    ServiceProtocol("SMTP", "Mail", "Sending emails"),
    ServiceProtocol("IMAP", "Mail", "Retrieving emails from a server"),
    ServiceProtocol("POP3", "Mail", "Retrieving emails from a server")
]

web_protocols = [
    ServiceProtocol("HTTP", "Web", "Transferring web pages"),
    ServiceProtocol("HTTPS", "Web", "Secures HTTP traffic using SSL/TLS")
]

remote_access_protocols = [
    ServiceProtocol("SSH", "Remote Access", "Provides secure remote login and command execution"),
    ServiceProtocol("RDP", "Remote Access", "Allows users to connect to another computer over a network")
]

for protocol in mail_protocols + web_protocols + remote_access_protocols:
    print(protocol.describe())
