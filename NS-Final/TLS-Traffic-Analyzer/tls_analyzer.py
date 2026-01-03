import scapy.all as scapy

def analyze_ssl_tls_traffic(interface):
    try:
        print(f"Starting SSL/TLS traffic analysis on interface {interface}...")
        # Filter SSL/TLS packets
        packets = scapy.sniff(iface=interface, filter="port 443 or port 8443", count=10)
        
        for packet in packets:
            if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.TLS):
                src_ip = packet[scapy.IP].src
                src_port = packet[scapy.TCP].sport
                dst_ip = packet[scapy.IP].dst
                dst_port = packet[scapy.TCP].dport
                
                print(f"SSL/TLS packet detected: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
                # You can add more analysis or data logging here based on your needs
                
    except KeyboardInterrupt:
        print("SSL/TLS traffic analysis stopped by user.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    interface = input("Enter the name of the network interface to monitor (e.g., eth0): ")
    analyze_ssl_tls_traffic(interface)
