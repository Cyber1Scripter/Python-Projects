import subprocess

def get_ips():
    ips = input("Enter IP or a list of IPs (comma-separated): ")
    return ips.split(',')

def get_parameters():
    parameters = input("Enter Nmap parameters (e.g., -p 80,22,443): ")
    return parameters

def scan_ips(ips, parameters):
    for ip in ips:
        ip = ip.strip()
        command = f"nmap {parameters} {ip}"
        print(f"Scanning {ip} with parameters: {parameters}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)

def main():
    ips = []
    parameters = ""

    while True:
        user_input = input("Enter IP, parameters, or 'scan' to start scanning: ").strip()

        if user_input.lower() == "scan":
            if ips and parameters:
                scan_ips(ips, parameters)
                break
            else:
                print("Please enter IPs and parameters before scanning.")
        elif "," in user_input:
            ips = get_ips()
        else:
            parameters = get_parameters()

if __name__ == "__main__":
    main()
