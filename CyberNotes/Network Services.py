"""
10. Network Services

10.1 DNS
The Domain Name System (DNS) is a hierarchical system that translates human-readable domain names (e.g., www.example.com) into IP addresses (e.g., 192.0.2.1). DNS allows users to access websites and services using easy-to-remember names instead of numerical IP addresses.

10.2 DNS Process
The DNS resolution process involves several steps:
1. A user types a domain name into their web browser.
2. The browser sends a query to the local DNS resolver, typically provided by the ISP.
3. The DNS resolver checks its cache. If the IP address is not cached, it queries the root DNS servers.
4. The root servers respond with the address of the appropriate top-level domain (TLD) server (e.g., .com, .org).
5. The resolver then queries the TLD server, which responds with the address of the authoritative DNS server for the domain.
6. The resolver queries the authoritative DNS server, which returns the IP address for the domain.
7. The resolver caches the IP address and returns it to the browser, which then connects to the web server.

10.3 DHCP
The Dynamic Host Configuration Protocol (DHCP) is a network management protocol used to automatically assign IP addresses and other network configuration parameters to devices on a network. DHCP eliminates the need for manual IP address configuration.

10.4 DHCP Server and Queries
A DHCP server manages the allocation of IP addresses and network configuration parameters. The DHCP process involves the following steps:
1. DHCP Discover: A client device sends a broadcast message to discover available DHCP servers.
2. DHCP Offer: DHCP servers respond with an offer message, including an available IP address and other configuration parameters.
3. DHCP Request: The client requests the offered IP address and configuration parameters from one of the DHCP servers.
4. DHCP Acknowledgment: The DHCP server acknowledges the request and assigns the IP address to the client for a specified lease time.

10.5 NTP
The Network Time Protocol (NTP) is a protocol used to synchronize the clocks of computers over a network. NTP ensures that all devices on a network have the same accurate time, which is critical for time-sensitive applications and security protocols.

"""

# Example for 10.1 DNS
class DNS:
    def __init__(self, domain_name, ip_address):
        self.domain_name = domain_name
        self.ip_address = ip_address

    def describe(self):
        return f"DNS Entry: Domain Name: {self.domain_name} - IP Address: {self.ip_address}"


dns_entry = DNS("www.example.com", "192.0.2.1")
print(dns_entry.describe())

# Example for 10.2 DNS Process
class DNSProcess:
    def __init__(self, steps):
        self.steps = steps

    def describe(self):
        return f"DNS Process Steps: {', '.join(self.steps)}"


dns_steps = [
    "User types a domain name into their web browser.",
    "Browser sends a query to the local DNS resolver.",
    "DNS resolver checks its cache. If not cached, queries the root DNS servers.",
    "Root servers respond with the TLD server address.",
    "Resolver queries the TLD server, which responds with the authoritative DNS server address.",
    "Resolver queries the authoritative DNS server, which returns the IP address.",
    "Resolver caches the IP address and returns it to the browser, which connects to the web server."
]

dns_process = DNSProcess(dns_steps)
print(dns_process.describe())

# Example for 10.3 DHCP
class DHCP:
    def __init__(self, protocol, function):
        self.protocol = protocol
        self.function = function

    def describe(self):
        return f"DHCP Protocol: {self.protocol} - Function: {self.function}"


dhcp = DHCP("Dynamic Host Configuration Protocol", "Automatically assigns IP addresses and network configuration parameters to devices.")
print(dhcp.describe())

# Example for 10.4 DHCP Server and Queries
class DHCPServer:
    def __init__(self, process_steps):
        self.process_steps = process_steps

    def describe(self):
        return f"DHCP Server Process: {', '.join(self.process_steps)}"


dhcp_steps = [
    "DHCP Discover: Client sends a broadcast message to discover DHCP servers.",
    "DHCP Offer: DHCP servers respond with an offer message, including an available IP address.",
    "DHCP Request: Client requests the offered IP address and configuration parameters.",
    "DHCP Acknowledgment: DHCP server acknowledges the request and assigns the IP address for a specified lease time."
]

dhcp_server = DHCPServer(dhcp_steps)
print(dhcp_server.describe())

# Example for 10.5 NTP
class NTP:
    def __init__(self, protocol, function):
        self.protocol = protocol
        self.function = function

    def describe(self):
        return f"NTP Protocol: {self.protocol} - Function: {self.function}"


ntp = NTP("Network Time Protocol", "Synchronizes the clocks of computers over a network to ensure accurate timekeeping.")
print(ntp.describe())
