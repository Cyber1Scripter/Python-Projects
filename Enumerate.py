import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def get_target_url():
    url = input("Enter the target URL: ")
    return url

def get_wordlist_path():
    wordlist_path = input("Enter the path to the directory names list: ")
    return wordlist_path

def run_gobuster(target_url, wordlist_path):
    command = f"gobuster dir -u {target_url} -w {wordlist_path} -t 50"
    print(f"Running Gobuster with command: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    for line in process.stdout:
        if "200" in line:
            print(Fore.RED + line.strip() + Style.RESET_ALL)
        else:
            print(line.strip())

    process.stdout.close()
    process.wait()

def main():
    target_url = get_target_url()
    wordlist_path = get_wordlist_path()
    run_gobuster(target_url, wordlist_path)

if __name__ == "__main__":
    main()
