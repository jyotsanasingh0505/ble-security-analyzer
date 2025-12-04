import json

def load_packets(filename="samples/sample_packets.json"):
    with open(filename) as f:
        return json.load(f)

def analyze_security(packets):
    issues = []

    for p in packets:
        if p.get("type") == "PAIR_REQ" and p.get("method") == "JustWorks":
            issues.append("Insecure pairing method: JustWorks")

        if p.get("type") == "DATA" and not p.get("encrypted", True):
            issues.append("Unencrypted data transfer detected")

    return issues
