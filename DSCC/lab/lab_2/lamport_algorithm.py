# ----------------- LAMPORT LOGICAL CLOCK DEMO -----------------

processes = [1, 2, 3]
clock = {p:0 for p in processes}  # initialize clocks

# Define events: (type, sender, receiver)
# type = 'send' or 'receive', for receive use sender info
events = [
    ('send', 1, 2),
    ('receive', 2, 1),
    ('send', 2, 3),
    ('receive', 3, 2),
    ('send', 1, 3),
    ('receive', 3, 1)
]

for e in events:
    if e[0]=='send':
        p = e[1]
        clock[p] += 1
        print(f"P{p} SENDS message, clock={clock[p]}")
    elif e[0]=='receive':
        p = e[1]
        sender = e[2]
        clock[p] = max(clock[p], clock[sender]) + 1
        print(f"P{p} RECEIVES message from P{sender}, clock={clock[p]}")

# Final clocks
print("\nFinal Lamport Clocks:")
for p in processes:
    print(f"P{p}: {clock[p]}")

