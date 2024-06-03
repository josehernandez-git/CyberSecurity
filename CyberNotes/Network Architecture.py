"""
11. Network Architecture

11.1 Data Center
A data center is a facility that houses a large number of computer servers, storage systems, networking equipment, and other infrastructure components. It provides centralized storage, management, and dissemination of data and applications. Data centers are designed to ensure high availability, scalability, security, and efficient resource utilization.

Key Components of a Data Center:
- Servers: Provide computing power and run applications.
- Storage Systems: Store and manage data.
- Networking Equipment: Connects servers and storage systems, and provides external connectivity.
- Power and Cooling: Ensures continuous operation and prevents overheating.
- Security Systems: Protects against physical and cyber threats.

11.2 Virtual
Virtual network architecture involves using virtualization technologies to create virtual versions of physical network resources, such as servers, storage devices, and network components. This allows for more flexible and efficient resource management, improved scalability, and cost savings.

Key Concepts in Virtual Network Architecture:
- Virtual Machines (VMs): Software-based emulations of physical computers.
- Hypervisors: Software that creates and manages VMs.
- Virtual Networks: Software-defined networks that connect VMs and other virtual resources.
- Network Functions Virtualization (NFV): Virtualization of network functions (e.g., firewalls, load balancers).

11.3 Cloud
Cloud network architecture refers to the design and deployment of network resources and services in a cloud computing environment. Cloud computing provides on-demand access to a shared pool of configurable resources, such as servers, storage, and applications, over the internet.

Key Characteristics of Cloud Network Architecture:
- On-Demand Self-Service: Users can provision resources as needed without human intervention.
- Broad Network Access: Resources are accessible over the internet from various devices.
- Resource Pooling: Resources are pooled to serve multiple users, with dynamic allocation based on demand.
- Rapid Elasticity: Resources can be quickly scaled up or down to meet changing demands.
- Measured Service: Resource usage is monitored, controlled, and reported for billing purposes.

11.4 Network Storage
Network storage architecture involves using networked storage devices to store and manage data. This allows multiple devices and users to access and share data over a network. Common network storage solutions include Network Attached Storage (NAS) and Storage Area Networks (SAN).

Key Concepts in Network Storage Architecture:
- NAS: Dedicated storage devices that provide file-based storage services to other devices on the network.
- SAN: High-speed network of storage devices that provide block-level storage services to servers.
- iSCSI: Internet Small Computer Systems Interface, a protocol used to connect storage devices over IP networks.
- RAID: Redundant Array of Independent Disks, a technology used to improve performance and provide data redundancy.

"""

# Example for 11.1 Data Center
class DataCenter:
    def __init__(self, components):
        self.components = components

    def describe(self):
        return f"Data Center Components: {', '.join(self.components)}"


data_center_components = [
    "Servers: Provide computing power and run applications.",
    "Storage Systems: Store and manage data.",
    "Networking Equipment: Connects servers and storage systems, and provides external connectivity.",
    "Power and Cooling: Ensures continuous operation and prevents overheating.",
    "Security Systems: Protects against physical and cyber threats."
]

data_center = DataCenter(data_center_components)
print(data_center.describe())

# Example for 11.2 Virtual
class VirtualNetworkArchitecture:
    def __init__(self, concepts):
        self.concepts = concepts

    def describe(self):
        return f"Virtual Network Architecture Concepts: {', '.join(self.concepts)}"


virtual_concepts = [
    "Virtual Machines (VMs): Software-based emulations of physical computers.",
    "Hypervisors: Software that creates and manages VMs.",
    "Virtual Networks: Software-defined networks that connect VMs and other virtual resources.",
    "Network Functions Virtualization (NFV): Virtualization of network functions (e.g., firewalls, load balancers)."
]

virtual_network_architecture = VirtualNetworkArchitecture(virtual_concepts)
print(virtual_network_architecture.describe())

# Example for 11.3 Cloud
class CloudNetworkArchitecture:
    def __init__(self, characteristics):
        self.characteristics = characteristics

    def describe(self):
        return f"Cloud Network Architecture Characteristics: {', '.join(self.characteristics)}"


cloud_characteristics = [
    "On-Demand Self-Service: Users can provision resources as needed without human intervention.",
    "Broad Network Access: Resources are accessible over the internet from various devices.",
    "Resource Pooling: Resources are pooled to serve multiple users, with dynamic allocation based on demand.",
    "Rapid Elasticity: Resources can be quickly scaled up or down to meet changing demands.",
    "Measured Service: Resource usage is monitored, controlled, and reported for billing purposes."
]

cloud_network_architecture = CloudNetworkArchitecture(cloud_characteristics)
print(cloud_network_architecture.describe())

# Example for 11.4 Network Storage
class NetworkStorageArchitecture:
    def __init__(self, concepts):
        self.concepts = concepts

    def describe(self):
        return f"Network Storage Architecture Concepts: {', '.join(self.concepts)}"


storage_concepts = [
    "NAS: Dedicated storage devices that provide file-based storage services to other devices on the network.",
    "SAN: High-speed network of storage devices that provide block-level storage services to servers.",
    "iSCSI: Internet Small Computer Systems Interface, a protocol used to connect storage devices over IP networks.",
    "RAID: Redundant Array of Independent Disks, a technology used to improve performance and provide data redundancy."
]

network_storage_architecture = NetworkStorageArchitecture(storage_concepts)
print(network_storage_architecture.describe())
