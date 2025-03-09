import socket

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                return True
            else:
                return False
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False

def port_scan(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            open_ports.append(port)
    return open_ports

def main():
    ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    print(f"Scanning ports from {start_port} to {end_port} on {ip}...")
    open_ports = port_scan(ip, start_port, end_port)

    if open_ports:
        print("Open ports found:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found")

if __name__ == "__main__":
    main()
