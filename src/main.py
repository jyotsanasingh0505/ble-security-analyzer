from packet_simulator import save_packets
from packet_parser import load_packets, analyze_security
from attack_replay import simulate_replay
from flow_visualizer import visualize_flow

if __name__ == "__main__":
    # (re)generate sample packets
    save_packets()

    packets = load_packets()
    visualize_flow(packets)

    issues = analyze_security(packets)
    print("Security Issues Found:")
    for i in issues:
        print(f"- {i}")

    print("\\nSimulating replay attack on first packet...")
    simulate_replay(packets[0])
