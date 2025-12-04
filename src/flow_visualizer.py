def visualize_flow(packets):
    print("\\n=== BLE Communication Flow ===")
    for p in packets:
        print(f"{p.get('source')} --> {p.get('dest')}: {p.get('type')}")
    print("==============================\\n")
