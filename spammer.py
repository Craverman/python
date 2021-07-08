from collections import Counter
import collections
ip_list = []
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        cols = line.split()
        ip = cols[0]
        request_type = cols[5].strip('"')
        requested_resource = cols[6]
        tuple_ip = (ip, request_type, requested_resource)
        ip_list.append(ip)
        print(tuple_ip)


ip_counter = collections.Counter(ip_list)
spammer_ip = ip_counter.most_common(1)
print('Spamer is using this ip adress:', spammer_ip)










