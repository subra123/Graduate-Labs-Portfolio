# ----------------- EDGE-CHASING DEADLOCK DETECTION -----------------

# Wait-for graph: process -> process it is waiting for
wait_for = {
    1: 2,  # P1 waits for P2
    2: 3,  # P2 waits for P3
    3: 1   # P3 waits for P1 (creates a cycle)
}

# To keep track of visited probes
received_probes = {}

def send_probe(initiator, sender, receiver):
    probe = (initiator, sender, receiver)
    if probe in received_probes:
        return
    received_probes[probe] = True

    print(f"Probe sent: {probe}")

    if receiver == initiator:
        print(f"DEADLOCK DETECTED! Initiator: P{initiator}")
        return

    if receiver in wait_for:
        send_probe(initiator, receiver, wait_for[receiver])

# ----------------- DEMO -----------------
print("Starting Edge-Chasing Deadlock Detection...\n")
for p in wait_for:
    print(f"Process P{p} initiates probe:")
    send_probe(p, p, wait_for[p])
    print()

