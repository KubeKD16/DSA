def ipv4_validate(ip):
    arr = ip.split('.')
    for i in arr:
        if arr[0] == 0 and len(i) != 1 or not i.isdigit() or int(i)>255:
            return "Non-IPv4"

    return "Ipv4"

def ipv6_validate(ip):
    test = ip.split(':')
    hexaDecimal = '0123456789abcdefABCDEF'
    for j in test:
        if j[0] == 0 and len(j) > 4 or not all(c in hexaDecimal for c in j):
            return "Non-IPV6"

    return "Ipv6"







ip_address = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
if ip_address.count('.') == 3:
    print(ipv4_validate(ip_address))
elif ip_address.count(':') == 7:
    print(ipv6_validate(ip_address))
else:
    print("Neither")
# print(validate(ip_address))