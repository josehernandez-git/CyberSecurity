# Conceptual Models and Network Devices

"""
2. Conceptual Models and Network Devices

2.1 Conceptual Models
Conceptual models in networking provide a structured framework for understanding the functions and interactions of different components within a network. These models help standardize the way networks are designed, implemented, and understood. 

2.2 OSI Model Layers
The OSI (Open Systems Interconnection) model is a conceptual framework used to understand and implement network interactions in seven distinct layers. Each layer serves a specific function and communicates with the layers directly above and below it.

Layers of the OSI Model:
1. Physical Layer: Deals with the physical connection between devices, including cables, switches, and NICs.
2. Data Link Layer: Manages the node-to-node data transfer and error detection/correction.
3. Network Layer: Handles the delivery of packets across network boundaries, including routing.
4. Transport Layer: Ensures complete data transfer with error recovery and flow control.
5. Session Layer: Manages sessions or connections between applications.
6. Presentation Layer: Translates data between the application and network format, handling encryption and compression.
7. Application Layer: Provides network services directly to user applications.

2.3 DoD Model Layers
The DoD (Department of Defense) model, also known as the TCP/IP model, is a more simplified model than the OSI model. It consists of four layers that align closely with the OSI layers but are less granular.

Layers of the DoD Model:
1. Network Interface Layer: Combines the OSI's Physical and Data Link layers, handling hardware addressing and media access control.
2. Internet Layer: Corresponds to the OSI's Network layer, responsible for logical addressing and routing.
3. Transport Layer: Similar to the OSI's Transport layer, it ensures end-to-end communication and data integrity.
4. Application Layer: Combines the OSI's Session, Presentation, and Application layers, providing application services.

2.4 Networking Devices
Networking devices are hardware components used to connect computers and other electronic devices to form a network. Each device has specific functions and operates at different layers of the OSI model.

Common Networking Devices:
1. Router: Forwards data packets between computer networks, operating at the Network layer.
2. Switch: Connects devices within a network and uses MAC addresses to forward data, operating at the Data Link layer.
3. Hub: A basic device that connects multiple Ethernet devices, operating at the Physical layer.
4. Bridge: Connects and filters traffic between two network segments, operating at the Data Link layer.
5. Modem: Converts digital data to analog signals and vice versa for data transmission over telephone lines, operating at the Physical layer.
6. Access Point: Allows wireless devices to connect to a wired network using Wi-Fi, operating at the Data Link layer.

2.5 Networked Devices
Networked devices are end devices that connect to a network and utilize its resources. They include various types of hardware used for different applications and purposes.

Common Networked Devices:
1. Computers: Desktops, laptops, and servers that connect to the network for communication and data exchange.
2. Printers: Networked printers that allow multiple users to print documents over the network.
3. Smartphones and Tablets: Mobile devices that connect to the network for internet access, communication, and data services.
4. Smart Home Devices: IoT devices such as smart thermostats, security cameras, and smart locks that connect to the network for remote control and monitoring.
"""

# Example for 2.1 Conceptual Models
class ConceptualModel:
    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose

    def describe(self):
        return f"Conceptual Model: {self.name} - Purpose: {self.purpose}"


osi_model = ConceptualModel("OSI Model", "Provides a standard framework for network communication.")
tcp_ip_model = ConceptualModel("TCP/IP Model", "Simplified model for network communication, used by the internet.")

print(osi_model.describe())
print(tcp_ip_model.describe())

# Example for 2.2 OSI Model Layers
class OSILayer:
    def __init__(self, layer_number, layer_name, function):
        self.layer_number = layer_number
        self.layer_name = layer_name
        self.function = function

    def describe(self):
        return f"Layer {self.layer_number}: {self.layer_name} - Function: {self.function}"


layers = [
    OSILayer(1, "Physical", "Handles the physical connection between devices."),
    OSILayer(2, "Data Link", "Manages node-to-node data transfer and error detection/correction."),
    OSILayer(3, "Network", "Handles packet delivery across network boundaries."),
    OSILayer(4, "Transport", "Ensures complete data transfer with error recovery and flow control."),
    OSILayer(5, "Session", "Manages sessions between applications."),
    OSILayer(6, "Presentation", "Translates data between application and network format."),
    OSILayer(7, "Application", "Provides network services to user applications.")
]

for layer in layers:
    print(layer.describe())

# Example for 2.3 DoD Model Layers
class DoDLayer:
    def __init__(self, layer_number, layer_name, function):
        self.layer_number = layer_number
        self.layer_name = layer_name
        self.function = function

    def describe(self):
        return f"Layer {self.layer_number}: {self.layer_name} - Function: {self.function}"


dod_layers = [
    DoDLayer(1, "Network Interface", "Handles hardware addressing and media access control."),
    DoDLayer(2, "Internet", "Responsible for logical addressing and routing."),
    DoDLayer(3, "Transport", "Ensures end-to-end communication and data integrity."),
    DoDLayer(4, "Application", "Provides application services.")
]

for layer in dod_layers:
    print(layer.describe())

# Example for 2.4 Networking Devices
class NetworkingDevice:
    def __init__(self, name, function, osi_layer):
        self.name = name
        self.function = function
        self.osi_layer = osi_layer

    def describe(self):
        return f"Device: {self.name} - Function: {self.function} - OSI Layer: {self.osi_layer}"


devices = [
    NetworkingDevice("Router", "Forwards data packets between networks", "Network Layer"),
    NetworkingDevice("Switch", "Connects devices within a network using MAC addresses", "Data Link Layer"),
    NetworkingDevice("Hub", "Connects multiple Ethernet devices", "Physical Layer"),
    NetworkingDevice("Bridge", "Connects and filters traffic between two network segments", "Data Link Layer"),
    NetworkingDevice("Modem", "Converts digital data to analog signals and vice versa", "Physical Layer"),
    NetworkingDevice("Access Point", "Allows wireless devices to connect to a wired network", "Data Link Layer")
]

for device in devices:
    print(device.describe())

# Example for 2.5 Networked Devices
class NetworkedDevice:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def describe(self):
        return f"Device: {self.name} - Function: {self.function}"


networked_devices = [
    NetworkedDevice("Computer", "Connects to the network for communication and data exchange."),
    NetworkedDevice("Printer", "Allows multiple users to print documents over the network."),
    NetworkedDevice("Smartphone", "Connects to the network for internet access, communication, and data services."),
    NetworkedDevice("Smart Home Device", "Connects to the network for remote control and monitoring.")
]

for device in networked_devices:
    print(device.describe())
