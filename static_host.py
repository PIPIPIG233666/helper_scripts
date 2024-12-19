# Arrays to store MAC addresses and updated IP addresses
mac_addresses = [
    # PS5s
    "00:e4:21:f2:d7:28", "2c:9e:00:fc:2b:73", "c8:4a:a0:f9:7a:8e",
    "bc:60:a7:38:d2:07", "04:f7:78:08:b3:8c", "2c:9e:00:b8:56:6c",
    "5c:84:3c:9f:3a:3b", "5c:84:3c:35:24:91", "c8:4a:a0:97:41:8c",
    # Xboxes
    "04:27:28:98:a8:d2"
]

# Updated IP addresses from 192.168.1.230 to 192.168.1.*
ip_addresses = [
    f"192.168.1.{230 + i}" for i in range(len(mac_addresses))
]

# Function to print the configuration in the specified format
def print_config(mac, ip):
    print("config host")
    print(f"    list mac '{mac}'")
    print(f"    option ip '{ip}'")
    print("    option leasetime 'infinite'")
    print()

# Loop through the arrays and print the configuration for each entry
for mac, ip in zip(mac_addresses, ip_addresses):
    print_config(mac, ip)

# Print additional list src_ip entries
for src_ip in ip_addresses:
    print(f"        list src_ip ' '{src_ip}'")

print()

# Print the final option dest_ip entry
for src_ip in ip_addresses:
    print(f"        option dest_ip '{src_ip}'")
