class Ipaddress:
    def remove_zero_in_ip(self,ip_address):
        lst1 = ip_address.split(".")
        lst2 = []
        for i in lst1:
            i = i.lstrip('0')
            lst2.append(i)
        str2 = ".".join(lst2)
        print(f'ip address after removing leading zeros is:{str2}')

ip_address = '000000179.0000025.0000036.00000143'
i1=Ipaddress()
i1.remove_zero_in_ip(ip_address)


