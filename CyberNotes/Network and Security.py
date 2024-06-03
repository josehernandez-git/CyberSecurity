"""
8. Network Security

8.1 Security
Network security involves measures taken to protect data during transmission, ensuring confidentiality, integrity, and availability. This includes implementing policies, procedures, and hardware/software technologies to safeguard networks from unauthorized access, misuse, malfunction, modification, destruction, or improper disclosure.

8.2 Authentication and Authorization
Authentication is the process of verifying the identity of a user or device, while authorization determines the level of access or permissions granted to the authenticated user or device. Common methods include passwords, biometrics, and security tokens.

8.3 Multifactor and Policies
Multifactor authentication (MFA) enhances security by requiring multiple forms of verification, such as something you know (password), something you have (security token), and something you are (biometric verification). Security policies are formalized rules and practices that regulate how an organization manages, protects, and distributes sensitive information.

8.4 Types of Authentication
There are several types of authentication methods, including:
1. Password-based Authentication: Using a secret word or phrase.
2. Biometric Authentication: Using unique biological traits, like fingerprints or facial recognition.
3. Token-based Authentication: Using physical or digital tokens.
4. Certificate-based Authentication: Using digital certificates issued by a trusted authority.

8.5 RBAC, MAC, and DAC
- Role-Based Access Control (RBAC): Access rights are assigned based on roles within an organization.
- Mandatory Access Control (MAC): Access rights are regulated by a central authority based on multiple levels of security.
- Discretionary Access Control (DAC): Access rights are assigned by the owner of the resource.

8.6 Security Attacks
Security attacks are deliberate actions taken to compromise network security. Common types include:
- Phishing: Fraudulent attempts to obtain sensitive information by disguising as a trustworthy entity.
- Denial of Service (DoS): Overloading a network or service to render it unusable.
- Man-in-the-Middle (MitM): Intercepting and altering communication between two parties without their knowledge.
- Malware: Malicious software designed to damage, disrupt, or gain unauthorized access to computer systems.

8.7 Network Security Systems
Network security systems include hardware and software solutions that protect networks from security threats. Examples include:
- Firewalls: Monitor and control incoming and outgoing network traffic based on security rules.
- Intrusion Detection Systems (IDS): Monitor network traffic for suspicious activity and alerts administrators.
- Intrusion Prevention Systems (IPS): Actively block detected threats in real-time.

8.8 Endpoint Security Measures
Endpoint security measures protect individual devices connected to the network, such as computers, smartphones, and tablets. Examples include:
- Antivirus Software: Detects and removes malware.
- Endpoint Detection and Response (EDR): Monitors and responds to threats on endpoints.
- Mobile Device Management (MDM): Manages and secures mobile devices used in an organization.

8.9 Other Security Measures
Additional security measures to protect networks include:
- Encryption: Encoding data to prevent unauthorized access.
- Backup and Recovery: Regularly backing up data and having a plan to recover it in case of loss.
- Security Awareness Training: Educating employees about security risks and best practices.

8.10 VPN Remote Access
Virtual Private Networks (VPNs) provide secure remote access to a network by encrypting internet connections. VPNs create a private tunnel for data, ensuring that it is secure from eavesdropping and interception, even when transmitted over public networks.
"""

# Example for 8.1 Security
class NetworkSecurity:
    def __init__(self, measures):
        self.measures = measures

    def describe(self):
        return f"Network Security Measures: {', '.join(self.measures)}"


security_measures = [
    "Implementing firewalls",
    "Using encryption",
    "Regular software updates",
    "Intrusion detection systems",
    "Security policies and procedures"
]

network_security = NetworkSecurity(security_measures)
print(network_security.describe())

# Example for 8.2 Authentication and Authorization
class AuthSystem:
    def __init__(self, method, process):
        self.method = method
        self.process = process

    def describe(self):
        return f"Authentication Method: {self.method} - Process: {self.process}"


auth = AuthSystem("Password", "Verifies user identity based on a secret word or phrase.")
authz = AuthSystem("Role-Based Access Control", "Grants access based on user roles within the organization.")

print(auth.describe())
print(authz.describe())

# Example for 8.3 Multifactor and Policies
class MFA:
    def __init__(self, factors):
        self.factors = factors

    def describe(self):
        return f"Multifactor Authentication: Requires {', '.join(self.factors)}"


mfa = MFA(["something you know (password)", "something you have (security token)", "something you are (biometric verification)"])
print(mfa.describe())

class SecurityPolicy:
    def __init__(self, policy_name, details):
        self.policy_name = policy_name
        self.details = details

    def describe(self):
        return f"Security Policy: {self.policy_name} - Details: {self.details}"


policy = SecurityPolicy("Password Policy", "Requires passwords to be at least 8 characters long, include numbers and symbols, and be changed every 90 days.")
print(policy.describe())

# Example for 8.4 Types of Authentication
class AuthenticationType:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        return f"Authentication Type: {self.name} - Description: {self.description}"


auth_types = [
    AuthenticationType("Password-based Authentication", "Using a secret word or phrase."),
    AuthenticationType("Biometric Authentication", "Using unique biological traits, like fingerprints or facial recognition."),
    AuthenticationType("Token-based Authentication", "Using physical or digital tokens."),
    AuthenticationType("Certificate-based Authentication", "Using digital certificates issued by a trusted authority.")
]

for auth_type in auth_types:
    print(auth_type.describe())

# Example for 8.5 RBAC, MAC, and DAC
class AccessControl:
    def __init__(self, type, description):
        self.type = type
        self.description = description

    def describe(self):
        return f"Access Control Type: {self.type} - Description: {self.description}"


rbac = AccessControl("RBAC", "Access rights are assigned based on roles within an organization.")
mac = AccessControl("MAC", "Access rights are regulated by a central authority based on multiple levels of security.")
dac = AccessControl("DAC", "Access rights are assigned by the owner of the resource.")

access_controls = [rbac, mac, dac]
for ac in access_controls:
    print(ac.describe())

# Example for 8.6 Security Attacks
class SecurityAttack:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        return f"Security Attack: {self.name} - Description: {self.description}"


attacks = [
    SecurityAttack("Phishing", "Fraudulent attempts to obtain sensitive information by disguising as a trustworthy entity."),
    SecurityAttack("Denial of Service (DoS)", "Overloading a network or service to render it unusable."),
    SecurityAttack("Man-in-the-Middle (MitM)", "Intercepting and altering communication between two parties without their knowledge."),
    SecurityAttack("Malware", "Malicious software designed to damage, disrupt, or gain unauthorized access to computer systems.")
]

for attack in attacks:
    print(attack.describe())

# Example for 8.7 Network Security Systems
class SecuritySystem:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def describe(self):
        return f"Security System: {self.name} - Function: {self.function}"


systems = [
    SecuritySystem("Firewall", "Monitors and controls incoming and outgoing network traffic based on security rules."),
    SecuritySystem("Intrusion Detection System (IDS)", "Monitors network traffic for suspicious activity and alerts administrators."),
    SecuritySystem("Intrusion Prevention System (IPS)", "Actively blocks detected threats in real-time.")
]

for system in systems:
    print(system.describe())

# Example for 8.8 Endpoint Security Measures
class EndpointSecurity:
    def __init__(self, measure, function):
        self.measure = measure
        self.function = function

    def describe(self):
        return f"Endpoint Security Measure: {self.measure} - Function: {self.function}"


endpoint_measures = [
    EndpointSecurity("Antivirus Software", "Detects and removes malware."),
    EndpointSecurity("Endpoint Detection and Response (EDR)", "Monitors and responds to threats on endpoints."),
    EndpointSecurity("Mobile Device Management (MDM)", "Manages and secures mobile devices used in an organization.")
]

for measure in endpoint_measures:
    print(measure.describe())

# Example for 8.9 Other Security Measures
class SecurityMeasure:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        return f"Security Measure: {self.name} - Description: {self.description}"


measures = [
    SecurityMeasure("Encryption", "Encoding data to prevent unauthorized access."),
    SecurityMeasure("Backup and Recovery", "Regularly backing up data and having a plan to recover it in case of loss."),
    SecurityMeasure("Security Awareness Training", "Educating employees about security risks and best practices.")
]

for measure in measures:
    print(measure.describe())

# Example for 8.10 VPN Remote Access
class VPN:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def describe(self):
        return f"VPN: {self.name} - Function: {self.function}"


vpn = VPN("Virtual Private Network (VPN)", "Provides secure remote access to a network by encrypting internet connections.")
print(vpn.describe())
