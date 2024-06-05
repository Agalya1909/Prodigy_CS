# Network Packet Analyzer

## Introduction

The Network Packet Analyzer is a Python script that captures and analyzes network packets in real-time. It extracts and displays key information from various types of packets, including IP, TCP, UDP, and ICMP packets. This tool is useful for network monitoring, debugging, and security analysis.

## Description

This Python script uses the Scapy library to sniff network packets and extract important information. It identifies and processes IP packets and further categorizes them into TCP, UDP, and ICMP packets. For each packet type, it extracts and prints relevant details such as source and destination IP addresses, ports, protocol type, and payload data.

## Libraries or Language Used

- **Python**: The script is written in Python, a versatile and widely-used programming language.
- **Scapy**: This script utilizes the Scapy library for packet manipulation and analysis.

## Usage

1. Ensure you have Python installed on your system.
2. Install the Scapy library if you haven't already using `pip install scapy`.
3. Run the script in a Python environment.
4. The script will start sniffing packets on all available network interfaces and display information about each packet in the console.

## Example

### Code
```python
from scapy.all import *

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"Source Port: {src_port}, Destination Port: {dst_port}, Protocol: TCP")

            # Print payload data (first 20 bytes)
            if Raw in packet:
                payload = packet[Raw].load[:20]
                print(f"Payload Data: {payload}")

        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"Source Port: {src_port}, Destination Port: {dst_port}, Protocol: UDP")

            # Print payload data (first 20 bytes)
            if Raw in packet:
                payload = packet[Raw].load[:20]
                print(f"Payload Data: {payload}")

        elif ICMP in packet:
            print("Protocol: ICMP")

            # Print ICMP type and code
            icmp_type = packet[ICMP].type
            icmp_code = packet[ICMP].code
            print(f"ICMP Type: {icmp_type}, ICMP Code: {icmp_code}")

            # Print payload data (first 20 bytes)
            if Raw in packet:
                payload = packet[Raw].load[:20]
                print(f"Payload Data: {payload}")

        print("\n")

def main():
    # Sniff packets on all available interfaces
    sniff(prn=packet_handler)

if __name__ == "__main__":
    main()
```

### Sample Output
```
Source IP: 192.168.1.2, Destination IP: 192.168.1.1, Protocol: 6
Source Port: 12345, Destination Port: 80, Protocol: TCP
Payload Data: b'GET / HTTP/1.1\r\n'

Source IP: 192.168.1.1, Destination IP: 192.168.1.2, Protocol: 1
Protocol: ICMP
ICMP Type: 8, ICMP Code: 0
Payload Data: b'\x08\x00\xf7\xff...'
```

## How it works

1. **Packet Capture**: The script captures network packets using Scapy's `sniff` function.
2. **Packet Handling**: Each captured packet is processed by the `packet_handler` function.
3. **Packet Analysis**: The script checks for IP packets and categorizes them as TCP, UDP, or ICMP packets.
4. **Data Extraction**: Relevant details such as source and destination IP addresses, ports, protocol type, and payload data are extracted and printed.
5. **Loop**: The script continues to capture and process packets until manually stopped.

This script is a simple yet powerful tool for real-time network packet analysis.
