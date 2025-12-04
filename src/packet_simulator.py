import json

def generate_sample_packets():
    packets = [
        {"type": "ADV_IND", "source": "Device_A", "dest": "Broadcast", "data": "Hello"},
        {"type": "CONNECT_REQ", "source": "Device_B", "dest": "Device_A"},
        {"type": "PAIR_REQ", "source": "Device_A", "method": "JustWorks"},
        {"type": "PAIR_RSP", "source": "Device_B", "method": "JustWorks"},
        {"type": "DATA", "source": "Device_A", "encrypted": False, "payload": "HeartRate"},
    ]
    return packets

def save_packets(filename="samples/sample_packets.json"):
    packets = generate_sample_packets()
    with open(filename, "w") as f:
        json.dump(packets, f, indent=4)

if __name__ == "__main__":
    save_packets()
