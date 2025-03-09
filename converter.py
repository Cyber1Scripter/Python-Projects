import curses
import time

def animate_logo(stdscr, exit_message=False):
    curses.curs_set(0)
    stdscr.clear()
    
    logo = [
        " ██╗  ██╗██╗   ██╗███████╗██████╗ ██╗   ██╗",
        " ██║ ██╔╝██║   ██║██╔════╝██╔══██╗██║   ██║",
        " █████╔╝ ██║   ██║█████╗  ██████╔╝██║   ██║",
        " ██╔═██╗ ██║   ██║██╔══╝  ██╔═══╝ ██║   ██║",
        " ██║  ██╗╚██████╔╝███████╗██║     ╚██████╔╝",
        " ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝      ╚═════╝ "
    ]
    
    height, width = stdscr.getmaxyx()
    start_x = (width - len(logo[0])) // 2
    start_y = (height - len(logo)) // 4  # Move the logo up to create space for text
    
    for row_idx, row in enumerate(logo):
        for col_idx, char in enumerate(row):
            stdscr.addch(start_y + row_idx, start_x + col_idx, char)
            stdscr.refresh()
            time.sleep(0.01)
    
    time.sleep(1)
    
    if exit_message:
        messages = [
            "Developed by: Cyber_Scripter",
            "Thank You for using!",
            "Contact Us: 0345-8875352"
        ]
    else:
        messages = [
            "Developed by: Cyber_Scripter",
            "I'm Shahzaib Shakir, a 19-year-old Cyber Security Expert.",
            "I specialize in Web Penetration Testing and Network Hacking."
        ]
    
    msg_y = start_y + len(logo) + 2  # Place the messages below the logo
    
    for message in messages:
        msg_x = (width - len(message)) // 2
        for i, char in enumerate(message):
            stdscr.addch(msg_y, msg_x + i, char)
            stdscr.refresh()
            time.sleep(0.05)
        msg_y += 1
    
    time.sleep(2)

def run_tool():
    print("\n[+] Running the main tool...\n")
    
    while True:
        char = input("Enter a character (or type 'exit' to quit): ")
        if char.lower() == "exit":
            print("Exiting program...")
            break
        if len(char) != 1:
            print("Please enter only one character.")
        else:
            ascii_val = ord(char)
            print("\nCharacter Information Table:")
            print("---------------------------------")
            print(f"Character     : {char}")
            print(f"ASCII Code    : {ascii_val}")
            print(f"Decimal Value : {ascii_val}")
            print(f"Hexadecimal   : {hex(ascii_val)}")
            print(f"Binary Value  : {bin(ascii_val)}")
            print(f"Octal Value   : {oct(ascii_val)}")
            print("---------------------------------")
    
if __name__ == "__main__":
    curses.wrapper(animate_logo)
    run_tool()
    curses.wrapper(lambda stdscr: animate_logo(stdscr, exit_message=True))

