# ----------------- VERY SHORT RICART-AGRAWALA DEMO -----------------

processes = [1, 2, 3]
state = {p: 'RELEASED' for p in processes}
queue = {p: [] for p in processes}
ts = {}

def request_cs(p, t):
    state[p] = 'WANTED'
    ts[p] = t
    replies = [x for x in processes if x != p]
    print(f"P{p} REQUESTS CS at t={t}")
    
    for other in replies:
        # If other is in CS or has earlier request, queue it
        if state[other]=='HELD' or (state[other]=='WANTED' and ts[other]<t):
            queue[other].append(p)
            print(f"P{other} queues P{p}")
        else:
            print(f"P{other} REPLIES to P{p}")
            replies.remove(other)
    
    if not replies:
        enter_cs(p)

def enter_cs(p):
    state[p] = 'HELD'
    print(f"P{p} ENTERS CS")
    exit_cs(p)

def exit_cs(p):
    state[p] = 'RELEASED'
    print(f"P{p} EXITS CS")
    for q in queue[p]:
        print(f"P{p} REPLIES to P{q}")
    queue[p] = []

# ----------------- DEMO -----------------
request_cs(1,1)
request_cs(2,2)
request_cs(3,3)

