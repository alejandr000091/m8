from collections import Counter

IP = [
    "85.157.172.253",
    "85.157.172.253",
    "192.168.0.1",
    "85.157.172.253",
    "85.157.172.253",
    "192.168.0.1",
]
def get_count_visits_from_ip(ips):
    ip_counts = Counter(ips)
    return ip_counts


def get_frequent_visit_from_ip(ips):
    ip_frequent = get_count_visits_from_ip(ips).most_common(1)
    print(type(ip_frequent))
    return ip_frequent[0]

print(get_count_visits_from_ip(IP))
print(get_frequent_visit_from_ip(IP))