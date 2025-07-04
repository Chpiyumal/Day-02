import ipaddress

ip_addr_list = ["192.168.7.34", "234.266.231.234", "184.124.234.12"]
valid_list = []
invalid_list = []
def validate_ip_address(ip_string):
    
    try:
        ip_object = ipaddress.ip_address(ip_string)
        return True, ip_object
    except ValueError as e:
        return False, str(e)
    
for address in ip_addr_list:
    is_valid, result = validate_ip_address(address)
    if is_valid:
        valid_list.append(address)
    else:
        invalid_list.append(address)
print(f"valid ips : {valid_list}")
print(f"Invalid lsit: {invalid_list}")



