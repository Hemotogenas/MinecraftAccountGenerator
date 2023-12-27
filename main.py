import random
import os
import webbrowser

# ANSI escape codes for text colors
COLORS = {
    'GREEN': '\033[92m',
    'BLUE': '\033[94m',
    'RED': '\033[91m',
    'RESET': '\033[0m',
}

# Replace the following comment with your ASCII art
ascii_art_top = r"""
{green}
   ____                 _                           

███╗   ███╗ ██████╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗      █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗███████╗
████╗ ████║██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝██╔════╝
██╔████╔██║██║         ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║    ███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   ███████╗
██║╚██╔╝██║██║         ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║    ██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   ╚════██║
██║ ╚═╝ ██║╚██████╗    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝    ██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ███████║
╚═╝     ╚═╝ ╚═════╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝
                                                                                                                                                        

                          |___/                       
{reset}
"""

def read_word_list(filename="list.txt"):
    try:
        with open(filename, 'r') as file:
            word_list = [line.strip() for line in file.readlines()]
            return word_list
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

# zaza
all_words = read_word_list()

def list_all_words():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print the options in green
    print(ascii_art_top.format(green=COLORS['GREEN'], reset=COLORS['RESET']))
    print(f"{COLORS['GREEN']}Menu:{COLORS['RESET']}")
    print(f"{COLORS['GREEN']}1. List All Words{COLORS['RESET']}")
    print(f"{COLORS['BLUE']}2. Exit{COLORS['RESET']}")
    print(f"{COLORS['BLUE']}3. Redirect to a Website{COLORS['RESET']}")

    print("\nWord List:")
    for i, word in enumerate(all_words, start=1):
        if i % 6 == 0:
            color = COLORS['RED']
        elif i % 6 == 1 or i % 6 == 4:
            color = COLORS['GREEN']
        else:
            color = COLORS['BLUE']

        print(f"{color}{word}{COLORS['RESET']}")

    input("Press Enter to continue...")

    # Clear the screen again after pressing Enter
    os.system('cls' if os.name == 'nt' else 'clear')

def redirect_to_website():
    website_url = "https://github.com/Hemotogenas"
    webbrowser.open(website_url)
    print("Redirecting to {}".format(website_url))

def main():
    while True:
        print("\nMenu:")
        print("1. Show all cracked available accounts")
        print("2. Exit")
        print("3. Github")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            list_all_words()
        elif choice == "2":
            print("Exiting the application. Goodbye!")
            break
        elif choice == "3":
            redirect_to_website()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
