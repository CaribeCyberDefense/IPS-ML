
from collections import defaultdict

packet_stats = defaultdict(lambda: {
    "count": 0,
    "ports": set(),
    "bytes": 0
})

def extract_features(packet, src_ip):
    stats = packet_stats[src_ip]

    stats["count"] += 1
    stats["bytes"] += len(packet)

    if hasattr(packet, "dport"):
        stats["ports"].add(packet.dport)

    # Features:
    packet_size = len(packet)
    num_ports = len(stats["ports"])
    frequency = stats["count"]

    return [packet_size, num_ports, frequency]