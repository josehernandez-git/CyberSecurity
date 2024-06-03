# Bounded Media Standards and Applications

"""
3. Bounded Media Standards and Applications

3.1 Bounded Media
Bounded media refers to physical transmission mediums that use cables or wires to transmit data. These mediums provide guided paths for the data signals to travel. Common types of bounded media include coaxial cables, twisted pair cables, and fiber optic cables.

3.2 Coaxial Media
Coaxial cable, or coax, consists of a central conductor, an insulating layer, a metallic shield, and an outer insulating layer. It is commonly used for cable television, internet connections, and other data communications.

Types of Coaxial Cables:
1. RG-6: Used for cable television and internet.
2. RG-59: Used for low-frequency video and RF signal connections.
3. RG-11: Used for long-distance applications, has lower attenuation than RG-6 and RG-59.

3.3 Twisted Pair (TP) Media
Twisted pair cables consist of pairs of wires twisted together to reduce electromagnetic interference (EMI). They are widely used in local area networks (LANs) and telephone systems.

Types of Twisted Pair Cables:
1. Unshielded Twisted Pair (UTP): Commonly used in Ethernet networks, categorized into different standards (Cat 5, Cat 5e, Cat 6, Cat 6a, Cat 7).
2. Shielded Twisted Pair (STP): Provides additional shielding to reduce EMI, used in environments with high interference.

3.4 Fiber Optic Media
Fiber optic cables use light signals to transmit data, offering high bandwidth and long-distance capabilities. They consist of a core, cladding, and protective coating.

Types of Fiber Optic Cables:
1. Single-mode Fiber (SMF): Used for long-distance communication, offers higher bandwidth and less attenuation.
2. Multi-mode Fiber (MMF): Used for shorter distances, typically within buildings or campuses, offers easier alignment and lower cost.

3.5 Bounded Media Management
Managing bounded media involves ensuring proper installation, maintenance, and troubleshooting of the physical cables to ensure optimal performance and reliability.

Best Practices for Bounded Media Management:
1. Proper Cable Installation: Follow manufacturer guidelines, avoid sharp bends and physical damage.
2. Regular Inspections: Check for wear and tear, loose connections, and physical damage.
3. Documentation: Keep records of cable types, lengths, installation dates, and network diagrams.
4. Testing and Troubleshooting: Use cable testers to verify signal integrity and locate faults.

"""

# Example for 3.1 Bounded Media
class BoundedMedia:
    def __init__(self, name, description, applications):
        self.name = name
        self.description = description
        self.applications = applications

    def describe(self):
        return f"Bounded Media: {self.name} - Description: {self.description} - Applications: {self.applications}"


coaxial = BoundedMedia("Coaxial Cable", "Uses a central conductor, insulating layer, metallic shield, and outer insulating layer", "Cable TV, internet connections")
twisted_pair = BoundedMedia("Twisted Pair Cable", "Consists of pairs of wires twisted together to reduce EMI", "LANs, telephone systems")
fiber_optic = BoundedMedia("Fiber Optic Cable", "Uses light signals to transmit data", "High bandwidth and long-distance communication")

print(coaxial.describe())
print(twisted_pair.describe())
print(fiber_optic.describe())

# Example for 3.2 Coaxial Media
class CoaxialCable:
    def __init__(self, type, usage):
        self.type = type
        self.usage = usage

    def describe(self):
        return f"Coaxial Cable Type: {self.type} - Usage: {self.usage}"


rg6 = CoaxialCable("RG-6", "Cable TV and internet")
rg59 = CoaxialCable("RG-59", "Low-frequency video and RF signal connections")
rg11 = CoaxialCable("RG-11", "Long-distance applications with lower attenuation")

print(rg6.describe())
print(rg59.describe())
print(rg11.describe())

# Example for 3.3 Twisted Pair (TP) Media
class TwistedPairCable:
    def __init__(self, type, categories, usage):
        self.type = type
        self.categories = categories
        self.usage = usage

    def describe(self):
        return f"Twisted Pair Cable: {self.type} - Categories: {', '.join(self.categories)} - Usage: {self.usage}"


utp = TwistedPairCable("Unshielded Twisted Pair (UTP)", ["Cat 5", "Cat 5e", "Cat 6", "Cat 6a", "Cat 7"], "Ethernet networks")
stp = TwistedPairCable("Shielded Twisted Pair (STP)", ["Cat 6", "Cat 7"], "High interference environments")

print(utp.describe())
print(stp.describe())

# Example for 3.4 Fiber Optic Media
class FiberOpticCable:
    def __init__(self, type, usage):
        self.type = type
        self.usage = usage

    def describe(self):
        return f"Fiber Optic Cable: {self.type} - Usage: {self.usage}"


smf = FiberOpticCable("Single-mode Fiber (SMF)", "Long-distance communication with higher bandwidth and less attenuation")
mmf = FiberOpticCable("Multi-mode Fiber (MMF)", "Shorter distances within buildings or campuses")

print(smf.describe())
print(mmf.describe())

# Example for 3.5 Bounded Media Management
class BoundedMediaManagement:
    def __init__(self, practices):
        self.practices = practices

    def describe(self):
        return f"Bounded Media Management Practices: {', '.join(self.practices)}"


practices = [
    "Proper Cable Installation: Follow manufacturer guidelines, avoid sharp bends and physical damage.",
    "Regular Inspections: Check for wear and tear, loose connections, and physical damage.",
    "Documentation: Keep records of cable types, lengths, installation dates, and network diagrams.",
    "Testing and Troubleshooting: Use cable testers to verify signal integrity and locate faults."
]

bounded_media_management = BoundedMediaManagement(practices)

print(bounded_media_management.describe())
