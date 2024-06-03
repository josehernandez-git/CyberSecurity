"""
4. Address Types

4.1 Types of Network Addresses
Network addresses are identifiers assigned to devices participating in a computer network. These addresses facilitate the routing and delivery of data to the correct destination. Common types of network addresses include:
1. MAC Addresses: Physical addresses assigned to network interface cards (NICs).
2. IP Addresses: Logical addresses assigned to devices to identify them on a network (IPv4 and IPv6).
3. Subnet Masks: Used to divide IP addresses into sub-networks for better organization and security.
4. Broadcast Addresses: Used to send data to all devices within a network segment.
5. Multicast Addresses: Used to send data to a specific group of devices.

4.2 MAC Address
A Media Access Control (MAC) address is a unique identifier assigned to a network interface card (NIC) by the manufacturer. MAC addresses operate at the Data Link layer of the OSI model and are used for communication within a local network segment.

Structure of a MAC Address:
- Typically 48 bits (6 bytes) in length, represented as 12 hexadecimal digits.
- Example: 00:1A:2B:3C:4D:5E

4.3 IPv4
Internet Protocol version 4 (IPv4) is a logical address used to identify devices on a network. IPv4 addresses are 32 bits in length, divided into four octets, and represented in decimal format.

Structure of an IPv4 Address:
- Example: 192.168.1.1

Classes of IPv4 Addresses:
1. Class A: Supports large networks, range 1.0.0.0 to 126.255.255.255
2. Class B: Supports medium-sized networks, range 128.0.0.0 to 191.255.255.255
3. Class C: Supports small networks, range 192.0.0.0 to 223.255.255.255
4. Class D: Reserved for multicast, range 224.0.0.0 to 239.255.255.255
5. Class E: Reserved for experimental use, range 240.0.0.0 to 255.255.255.255

4.4 IPv6
Internet Protocol version 6 (IPv6) is the successor to IPv4, designed to address the exhaustion of IPv4 addresses. IPv6 addresses are 128 bits in length, divided into eight groups of four hexadecimal digits.

Structure of an IPv6 Address:
- Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

Advantages of IPv6:
- Vast address space, improved routing efficiency, enhanced security features, and simplified address assignment.

"""

# Example for 4.1 Types of Network Addresses
class NetworkAddress:
    def __init__(self, address_type, description, example):
        self.address_type = address_type
        self.description = description
        self.example = example

    def describe(self):
        return f"Network Address Type: {self.address_type} - Description: {self.description} - Example: {self.example}"


mac_address = NetworkAddress("MAC Address", "Physical address assigned to NICs", "00:1A:2B:3C:4D:5E")
ipv4_address = NetworkAddress("IPv4 Address", "Logical address for identifying devices on a network", "192.168.1.1")
ipv6_address = NetworkAddress("IPv6 Address", "Logical address designed to replace IPv4", "2001:0db8:85a3:0000:0000:8a2e:0370:7334")
subnet_mask = NetworkAddress("Subnet Mask", "Divides IP addresses into sub-networks", "255.255.255.0")
broadcast_address = NetworkAddress("Broadcast Address", "Sends data to all devices within a network segment", "192.168.1.255")
multicast_address = NetworkAddress("Multicast Address", "Sends data to a specific group of devices", "224.0.0.1")

addresses = [mac_address, ipv4_address, ipv6_address, subnet_mask, broadcast_address, multicast_address]

for address in addresses:
    print(address.describe())

# Example for 4.2 MAC Address
class MACAddress:
    def __init__(self, address):
        self.address = address

    def describe(self):
        return f"MAC Address: {self.address}"


mac1 = MACAddress("00:1A:2B:3C:4D:5E")
mac2 = MACAddress("A1:B2:C3:D4:E5:F6")

print(mac1.describe())
print(mac2.describe())

# Example for 4.3 IPv4
class IPv4Address:
    def __init__(self, address):
        self.address = address

    def describe(self):
        return f"IPv4 Address: {self.address}"


ipv4_1 = IPv4Address("192.168.1.1")
ipv4_2 = IPv4Address("10.0.0.1")

print(ipv4_1.describe())
print(ipv4_2.describe())

# Example for 4.4 IPv6
class IPv6Address:
    def __init__(self, address):
        self.address = address

    def describe(self):
        return f"IPv6 Address: {self.address}"


ipv6_1 = IPv6Address("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
ipv6_2 = IPv6Address("fe80::1ff:fe23:4567:890a")

print(ipv6_1.describe())
print(ipv6_2.describe())
