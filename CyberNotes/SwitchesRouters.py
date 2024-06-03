"""
7. Switches and Routers

7.1 Network Transmission
Network transmission refers to the transfer of data between devices over a network. This can occur through various media such as wired (e.g., Ethernet cables) and wireless (e.g., Wi-Fi). The efficiency and speed of network transmission depend on factors like bandwidth, latency, and network protocols.

7.2 Network Traffic
Network traffic is the amount of data moving across a network at any given time. It can be categorized into different types:
- Unicast: Data sent from one source to one specific destination.
- Broadcast: Data sent from one source to all devices on the network.
- Multicast: Data sent from one source to multiple specific destinations.
Network traffic management involves monitoring, controlling, and optimizing data flow to prevent congestion and ensure efficient communication.

7.3 Switch Features
Switches are network devices that connect multiple devices within a local area network (LAN). They operate at the Data Link layer (Layer 2) of the OSI model. Key features of switches include:
- MAC Address Learning: Switches learn and store the MAC addresses of connected devices to efficiently forward data frames.
- VLAN Support: Virtual LANs allow segmentation of a network into separate, isolated broadcast domains.
- Port Mirroring: Allows monitoring of network traffic by copying data from specific ports to a monitoring port.
- Link Aggregation: Combines multiple network connections to increase bandwidth and provide redundancy.
- Quality of Service (QoS): Prioritizes network traffic to ensure critical applications receive adequate bandwidth.

7.4 Switch Configuration
Switch configuration involves setting up and managing switch features to optimize network performance and security. Common configuration tasks include:
- Assigning VLANs: Segregate network traffic into different VLANs for better management and security.
- Configuring Trunk Ports: Set up trunk ports to carry traffic for multiple VLANs between switches.
- Setting Up Port Security: Restrict access to switch ports based on MAC addresses to prevent unauthorized devices from connecting.
- Enabling Spanning Tree Protocol (STP): Prevent network loops by enabling STP to manage redundant paths.
- Configuring QoS: Prioritize traffic based on type and importance to ensure optimal performance.

7.5 Security Zones and IP Support
Security zones are logical segments within a network that have different security levels and access controls. Common security zones include:
- Internal Zone: Trusted network segment with high security, typically includes internal servers and devices.
- DMZ (Demilitarized Zone): Semi-trusted network segment exposed to the internet, typically includes web servers and public-facing services.
- External Zone: Untrusted network segment, typically the internet.
IP support involves configuring IP addresses, subnets, and routing protocols to ensure proper communication between devices in different security zones.

7.6 Routers
Routers are network devices that connect multiple networks and direct data packets between them. They operate at the Network layer (Layer 3) of the OSI model. Key functions of routers include:
- Packet Forwarding: Determines the best path for data packets based on routing tables and protocols.
- NAT (Network Address Translation): Translates private IP addresses to public IP addresses for internet access.
- DHCP (Dynamic Host Configuration Protocol): Assigns IP addresses dynamically to devices on a network.
- Firewall Functions: Provides basic security features by filtering traffic based on IP addresses and ports.
- VPN Support: Establishes secure connections between networks over the internet.

"""

# Example for 7.1 Network Transmission
class NetworkTransmission:
    def __init__(self, medium, speed, latency):
        self.medium = medium
        self.speed = speed
        self.latency = latency

    def describe(self):
        return f"Network Transmission: Medium: {self.medium}, Speed: {self.speed} Mbps, Latency: {self.latency} ms"


transmission = NetworkTransmission("Ethernet Cable", 1000, 5)
print(transmission.describe())

# Example for 7.2 Network Traffic
class NetworkTraffic:
    def __init__(self, traffic_type, description):
        self.traffic_type = traffic_type
        self.description = description

    def describe(self):
        return f"Network Traffic Type: {self.traffic_type} - Description: {self.description}"


unicast = NetworkTraffic("Unicast", "Data sent from one source to one specific destination.")
broadcast = NetworkTraffic("Broadcast", "Data sent from one source to all devices on the network.")
multicast = NetworkTraffic("Multicast", "Data sent from one source to multiple specific destinations.")

traffic_types = [unicast, broadcast, multicast]
for traffic in traffic_types:
    print(traffic.describe())

# Example for 7.3 Switch Features
class SwitchFeature:
    def __init__(self, feature_name, description):
        self.feature_name = feature_name
        self.description = description

    def describe(self):
        return f"Switch Feature: {self.feature_name} - Description: {self.description}"


features = [
    SwitchFeature("MAC Address Learning", "Learns and stores the MAC addresses of connected devices."),
    SwitchFeature("VLAN Support", "Allows segmentation of a network into separate, isolated broadcast domains."),
    SwitchFeature("Port Mirroring", "Allows monitoring of network traffic by copying data from specific ports to a monitoring port."),
    SwitchFeature("Link Aggregation", "Combines multiple network connections to increase bandwidth and provide redundancy."),
    SwitchFeature("Quality of Service (QoS)", "Prioritizes network traffic to ensure critical applications receive adequate bandwidth.")
]

for feature in features:
    print(feature.describe())

# Example for 7.4 Switch Configuration
class SwitchConfiguration:
    def __init__(self, configuration_task, description):
        self.configuration_task = configuration_task
        self.description = description

    def describe(self):
        return f"Switch Configuration: {self.configuration_task} - Description: {self.description}"


configurations = [
    SwitchConfiguration("Assigning VLANs", "Segregate network traffic into different VLANs for better management and security."),
    SwitchConfiguration("Configuring Trunk Ports", "Set up trunk ports to carry traffic for multiple VLANs between switches."),
    SwitchConfiguration("Setting Up Port Security", "Restrict access to switch ports based on MAC addresses to prevent unauthorized devices from connecting."),
    SwitchConfiguration("Enabling Spanning Tree Protocol (STP)", "Prevent network loops by enabling STP to manage redundant paths."),
    SwitchConfiguration("Configuring QoS", "Prioritize traffic based on type and importance to ensure optimal performance.")
]

for config in configurations:
    print(config.describe())

# Example for 7.5 Security Zones and IP Support
class SecurityZone:
    def __init__(self, zone_name, description):
        self.zone_name = zone_name
        self.description = description

    def describe(self):
        return f"Security Zone: {self.zone_name} - Description: {self.description}"


internal_zone = SecurityZone("Internal Zone", "Trusted network segment with high security, typically includes internal servers and devices.")
dmz_zone = SecurityZone("DMZ (Demilitarized Zone)", "Semi-trusted network segment exposed to the internet, typically includes web servers and public-facing services.")
external_zone = SecurityZone("External Zone", "Untrusted network segment, typically the internet.")

zones = [internal_zone, dmz_zone, external_zone]
for zone in zones:
    print(zone.describe())

# Example for 7.6 Routers
class Router:
    def __init__(self, function, description):
        self.function = function
        self.description = description

    def describe(self):
        return f"Router Function: {self.function} - Description: {self.description}"


router_functions = [
    Router("Packet Forwarding", "Determines the best path for data packets based on routing tables and protocols."),
    Router("NAT (Network Address Translation)", "Translates private IP addresses to public IP addresses for internet access."),
    Router("DHCP (Dynamic Host Configuration Protocol)", "Assigns IP addresses dynamically to devices on a network."),
    Router("Firewall Functions", "Provides basic security features by filtering traffic based on IP addresses and ports."),
    Router("VPN Support", "Establishes secure connections between networks over the internet.")
]

for function in router_functions:
    print(function.describe())
