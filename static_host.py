# Arrays to store MAC addresses and corresponding IP addresses
mac_addresses = [
    # PS5s
    "00:e4:21:f2:d7:28", "2c:9e:00:fc:2b:73", "c8:4a:a0:f9:7a:8e",
    "bc:60:a7:38:d2:07", "04:f7:78:08:b3:8c", "2c:9e:00:b8:56:6c",
    "5c:84:3c:9f:3a:3b", "5c:84:3c:35:24:91", "c8:4a:a0:97:41:8c",
    # Xboxes
    "04:27:28:98:a8:d2",
    # Mine
    "00:41:0e:4a:14:e5", # Ally
    "58:11:22:b1:80:c6", # PC
    "8c:3b:4a:5e:dc:9e", # TP
]

# Updated IP addresses from 192.168.1.51 onward
ip_addresses = [
    f"192.168.1.{51 + i}" for i in range(len(mac_addresses))
]

# Function to print the configuration in the specified format
def print_config(mac, ip):
    config_str = (
        "config host\n"
        f"\tlist mac '{mac}'\n"
        f"\toption ip '{ip}'\n"
        "\toption leasetime 'infinite'\n"
    )
    print(config_str)

# Loop through the arrays and print the configuration for each entry
for mac, ip in zip(mac_addresses, ip_addresses):
    print_config(mac, ip)

# Print the additional rule configuration for Game_Console_Outbound
outbound_rule_str = (
    "config rule\n"
    "\toption name 'Game_Console_Outbound'\n"
    "\toption proto 'udp'\n"
    "\tlist dest_port '!=80'\n"
    "\tlist dest_port '!=443'\n"
    "\toption class 'cs5'\n"
    "\toption counter '1'"
)
outbound_src_ip_str = "\n".join([f"\tlist src_ip '{src_ip}'" for src_ip in ip_addresses])
outbound_rule_str += f"{outbound_src_ip_str}\n\toption enabled '1'"
print(outbound_rule_str)

# Print the additional rule configuration for Game_Console_Inbound
inbound_rule_str = (
    "config rule\n"
    "\toption name 'Game_Console_Inbound'\n"
    "\toption proto 'udp'\n"
    "\tlist src_port '!=80'\n"
    "\tlist src_port '!=443'\n"
    "\toption class 'cs5'\n"
    "\toption counter '1'"
)
inbound_src_ip_str = "\n".join([f"\tlist dest_ip '{src_ip}'" for src_ip in ip_addresses])
inbound_rule_str += f"{inbound_src_ip_str}\n\toption enabled '1'"
print(inbound_rule_str)
