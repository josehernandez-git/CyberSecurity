"""
5. Segmentation

5.1 Binary Decimal Conversion
Binary decimal conversion is the process of converting a number from binary (base-2) to decimal (base-10) and vice versa. Binary numbers are used in computer systems for various computations and data representations.

Binary to Decimal Conversion:
- To convert binary to decimal, multiply each bit by 2 raised to the power of its position, counting from right to left starting with 0.
- Example: Binary 1011 = 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 8 + 0 + 2 + 1 = 11 (Decimal)

Decimal to Binary Conversion:
- To convert decimal to binary, divide the number by 2 and record the remainder. Repeat the process with the quotient until the quotient is 0. The binary number is the remainders read from bottom to top.
- Example: Decimal 11 = 11/2 = 5 remainder 1, 5/2 = 2 remainder 1, 2/2 = 1 remainder 0, 1/2 = 0 remainder 1. Binary = 1011

5.2 Network Address
A network address is an identifier for a node or host on a network. It helps in identifying and locating devices within a network. Network addresses include IP addresses (both IPv4 and IPv6).

5.3 Classless Addresses
Classless addressing, or Classless Inter-Domain Routing (CIDR), is a method for allocating IP addresses and routing IP packets. Unlike classful addressing, CIDR allows for more efficient and flexible allocation of IP addresses by using variable-length subnet masking (VLSM).

CIDR Notation:
- CIDR notation represents an IP address followed by a slash and the number of significant bits in the subnet mask.
- Example: 192.168.1.0/24 indicates an IP address of 192.168.1.0 with a subnet mask of 255.255.255.0

5.4 Subnetting Basics
Subnetting is the process of dividing a large network into smaller sub-networks (subnets) to improve manageability, security, and performance. It involves creating multiple logical networks within a single physical network.

Subnet Mask:
- A subnet mask is used to determine which portion of an IP address is the network address and which part is the host address.
- Example: A subnet mask of 255.255.255.0 (or /24 in CIDR notation) indicates that the first 24 bits are the network part, and the remaining 8 bits are for hosts.

5.5 VLAN
A Virtual Local Area Network (VLAN) is a logical subdivision of a physical network that groups devices into separate broadcast domains. VLANs improve network efficiency and security by isolating traffic and reducing broadcast domains.

VLAN Configuration:
- VLANs are configured on network switches, where each VLAN is assigned a unique identifier (VLAN ID).
- Devices in different VLANs cannot communicate directly without a router or layer-3 switch.

"""

# Example for 5.1 Binary Decimal Conversion
class BinaryDecimalConversion:
    @staticmethod
    def binary_to_decimal(binary):
        decimal = 0
        for i, bit in enumerate(reversed(binary)):
            decimal += int(bit) * (2 ** i)
        return decimal

    @staticmethod
    def decimal_to_binary(decimal):
        binary = ''
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2
        return binary or '0'


binary_example = "1011"
decimal_example = 11

converter = BinaryDecimalConversion()
print(f"Binary to Decimal: {binary_example} -> {converter.binary_to_decimal(binary_example)}")
print(f"Decimal to Binary: {decimal_example} -> {converter.decimal_to_binary(decimal_example)}")

# Example for 5.2 Network Address
class NetworkAddress:
    def __init__(self, address, type):
        self.address = address
        self.type = type

    def describe(self):
        return f"Network Address: {self.address} - Type: {self.type}"


ipv4_address = NetworkAddress("192.168.1.1", "IPv4")
ipv6_address = NetworkAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334", "IPv6")

print(ipv4_address.describe())
print(ipv6_address.describe())

# Example for 5.3 Classless Addresses
class CIDRAddress:
    def __init__(self, address, prefix_length):
        self.address = address
        self.prefix_length = prefix_length

    def describe(self):
        return f"CIDR Address: {self.address}/{self.prefix_length}"


cidr_example = CIDRAddress("192.168.1.0", 24)
print(cidr_example.describe())

# Example for 5.4 Subnetting Basics
class Subnet:
    def __init__(self, network_address, subnet_mask):
        self.network_address = network_address
        self.subnet_mask = subnet_mask

    def describe(self):
        return f"Subnet: Network Address: {self.network_address}, Subnet Mask: {self.subnet_mask}"


subnet_example = Subnet("192.168.1.0", "255.255.255.0")
print(subnet_example.describe())

# Example for 5.5 VLAN
class VLAN:
    def __init__(self, vlan_id, name):
        self.vlan_id = vlan_id
        self.name = name

    def describe(self):
        return f"VLAN: ID: {self.vlan_id}, Name: {self.name}"


vlan_example = VLAN(10, "Marketing")
print(vlan_example.describe())
