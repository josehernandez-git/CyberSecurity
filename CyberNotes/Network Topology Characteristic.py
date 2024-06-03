# 1. Network Types, Topologies, and Characteristics

### 1. Network Types, Topologies, and Characteristics

#### 1.1 Network Topologies
# Network topologies describe the arrangement of different elements (links, nodes, etc.) in a computer network.
# They define how the network components are interconnected and how data is transmitted across them. 

class NetworkTopology:
    def __init__(self, name):
        self.name = name

    def describe(self):
        raise NotImplementedError("Subclass must implement abstract method")


class BusTopology(NetworkTopology):
    def describe(self):
        return f"Bus Topology: All devices are connected to a single central cable called the bus."


class StarTopology(NetworkTopology):
    def describe(self):
        return f"Star Topology: All devices are connected to a central hub or switch."


class RingTopology(NetworkTopology):
    def describe(self):
        return f"Ring Topology: Each device is connected to two other devices, forming a ring."


class MeshTopology(NetworkTopology):
    def describe(self):
        return f"Mesh Topology: Devices are interconnected, with multiple pathways for data to travel."


class TreeTopology(NetworkTopology):
    def describe(self):
        return f"Tree Topology: A hierarchical structure with a root node and connected nodes forming a tree."


class HybridTopology(NetworkTopology):
    def describe(self):
        return f"Hybrid Topology: Combination of two or more different types of topologies."


# Example usage
topologies = [BusTopology("Bus"), StarTopology("Star"), RingTopology("Ring"), MeshTopology("Mesh"), TreeTopology("Tree"), HybridTopology("Hybrid")]

for topology in topologies:
    print(topology.describe())

#### 1.2 Network Types
# Networks can be categorized based on their size, range, and purpose. Common network types include:

class NetworkType:
    def __init__(self, name, range, characteristics):
        self.name = name
        self.range = range
        self.characteristics = characteristics

    def describe(self):
        return f"{self.name} Network: Range: {self.range}, Characteristics: {self.characteristics}"


class LAN(NetworkType):
    def __init__(self):
        super().__init__("Local Area Network (LAN)", "Small geographical area", "High data transfer rates, low latency")


class WAN(NetworkType):
    def __init__(self):
        super().__init__("Wide Area Network (WAN)", "Large geographical area", "Lower data transfer rates, often use leased lines")


class MAN(NetworkType):
    def __init__(self):
        super().__init__("Metropolitan Area Network (MAN)", "City or large campus", "Larger than a LAN but smaller than a WAN")


class PAN(NetworkType):
    def __init__(self):
        super().__init__("Personal Area Network (PAN)", "Very small area", "Used for personal devices, Bluetooth and USB")


class CAN(NetworkType):
    def __init__(self):
        super().__init__("Campus Area Network (CAN)", "Campus or group of buildings", "Similar to a LAN but larger")


class SAN(NetworkType):
    def __init__(self):
        super().__init__("Storage Area Network (SAN)", "Dedicated network for data storage", "High-speed network to connect storage devices with servers")


# Example usage
network_types = [LAN(), WAN(), MAN(), PAN(), CAN(), SAN()]

for network_type in network_types:
    print(network_type.describe())

#### 1.3 Service Providers
# Service providers offer network services to individuals, businesses, and organizations. Types of service providers include:

class ServiceProvider:
    def __init__(self, name, services):
        self.name = name
        self.services = services

    def describe(self):
        return f"{self.name} provides the following services: {', '.join(self.services)}"


class ISP(ServiceProvider):
    def __init__(self, name):
        super().__init__(name, ["Internet access"])


class MNO(ServiceProvider):
    def __init__(self, name):
        super().__init__(name, ["Wireless communication services"])


class CSP(ServiceProvider):
    def __init__(self, name):
        super().__init__(name, ["Cloud computing services", "Infrastructure", "Platforms", "Software"])


class MSP(ServiceProvider):
    def __init__(self, name):
        super().__init__(name, ["Managed IT services", "Network management", "Security", "Data backup"])


class TelecomProvider(ServiceProvider):
    def __init__(self, name):
        super().__init__(name, ["Voice and data communication services"])


# Example usage
service_providers = [
    ISP("Comcast"),
    MNO("T-Mobile"),
    CSP("Amazon Web Services (AWS)"),
    MSP("Rackspace"),
    TelecomProvider("AT&T")
]

for provider in service_providers:
    print(provider.describe())
