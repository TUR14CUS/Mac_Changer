import subprocess
import optparse
import re
import random


def print_banner():
    banner = r"""

88b           d88                                                                         
888b         d888                                                                         
88`8b       d8'88                                                                         
88 `8b     d8' 88  ,adPPYYba,   ,adPPYba,                                                 
88  `8b   d8'  88  ""     `Y8  a8"     ""                                                 
88   `8b d8'   88  ,adPPPPP88  8b                                                         
88    `888'    88  88,    ,88  "8a,   ,aa                                                 
88     `8'     88  `"8bbdP"Y8   `"Ybbd8"'                                                 



  ,ad8888ba,   88                                                                         
 d8"'    `"8b  88                                                                         
d8'            88                                                                         
88             88,dPPYba,   ,adPPYYba,  8b,dPPYba,    ,adPPYb,d8   ,adPPYba,  8b,dPPYba,  
88             88P'    "8a  ""     `Y8  88P'   `"8a  a8"    `Y88  a8P_____88  88P'   "Y8  
Y8,            88       88  ,adPPPPP88  88       88  8b       88  8PP"""""""  88          
 Y8a.    .a8P  88       88  88,    ,88  88       88  "8a,   ,d88  "8b,   ,aa  88          
  `"Y8888Y"'   88       88  `"8bbdP"Y8  88       88   `"YbbdP"Y8   `"Ybbd8"'  88          
                                                      aa,    ,88                          
                                                       "Y8bbdP"                           
    """
    print(banner)


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    parser.add_option("-r", "--random", dest="random_mac", action="store_true", help="Generate a random MAC address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        options.interface = input("Enter the interface: ")
    if not options.new_mac and not options.random_mac:
        options.new_mac = input("Enter the new MAC address or use --random for a random address: ")

    return options


def generate_random_mac():
    # Generate a random MAC address with a locally administered bit set
    random_mac = "02:" + ":".join([format(random.randint(0, 255), '02x') for _ in range(5)])
    return random_mac


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


# Adding the banner print
print_banner()

# Getting arguments
options = get_arguments()

# Generating a random MAC address if the --random option is specified
if options.random_mac:
    options.new_mac = generate_random_mac()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

# Changing the MAC address
change_mac(options.interface, options.new_mac)

# Getting the new MAC address and checking if the change was successful
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")
