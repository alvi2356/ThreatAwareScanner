
import socket
import shodan

SHODAN_API_KEY = 'YOUR_API_KEY_HERE'  # replace with your real key
api = shodan.Shodan(SHODAN_API_KEY)

def scan_ports(ip, ports=[21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]):
    print(f"Scanning {ip}...\n")
    open_ports = []
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"✅ Port {port} is open.")
                open_ports.append(port)
        except socket.error:
            pass
        s.close()

    return open_ports

def check_shodan(ip):
    try:
        host = api.host(ip)
        print(f"\n🛰️ SHODAN info for {ip}:")
        print(f"Organization: {host.get('org', 'N/A')}")
        print(f"Operating System: {host.get('os', 'N/A')}")
        for item in host['data']:
            port = item['port']
            print(f"\n🔍 Port: {port}")
            print(f"Banner: {item.get('data', 'N/A')}")
    except shodan.APIError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_ip = input("Enter IP address to scan: ").strip()
    open_ports = scan_ports(target_ip)
    if open_ports:
        check_shodan(target_ip)
    else:
        print("❌ No open ports found.")
