# ----------------- BERKELEY CLOCK SYNCHRONIZATION DEMO -----------------

# Current times in minutes (HH*60 + MM)
daemon_time = 15*60        # 15:00
nodes = {
    1: 15*60 + 10,         # 15:10
    2: 14*60 + 50,         # 14:50
    3: 15*60 + 25          # 15:25
}

print("Before Synchronization:")
print(f"Daemon: {daemon_time//60:02d}:{daemon_time%60:02d}")
for n,t in nodes.items():
    print(f"Node {n}: {t//60:02d}:{t%60:02d}")

# ----------------- BERKELEY ALGORITHM -----------------
# Compute average time
all_times = [daemon_time] + list(nodes.values())
avg_time = sum(all_times) // len(all_times)

# Compute correction for each node
corrections = {n: avg_time - t for n,t in nodes.items()}
daemon_correction = avg_time - daemon_time

# Apply corrections
nodes = {n: t + corrections[n] for n,t in nodes.items()}
daemon_time += daemon_correction

print("\nAfter Synchronization:")
print(f"Daemon: {daemon_time//60:02d}:{daemon_time%60:02d}")
for n,t in nodes.items():
    print(f"Node {n}: {t//60:02d}:{t%60:02d} [Correction: {corrections[n]} mins]")

