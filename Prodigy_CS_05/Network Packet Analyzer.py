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

if __name__ == "_main_":
    main()