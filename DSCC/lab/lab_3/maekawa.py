# ----------------- VERY SHORT MAEKAWA DEMO -----------------

processes = [1, 2, 3]
voting_sets = {1:[2,3], 2:[1,3], 3:[1,2]}  # simple voting sets
state = {p:'RELEASED' for p in processes}  # RELEASED or HELD
voted = {p:False for p in processes}
queue = {p:[] for p in processes}

def request_cs(p):
    print(f"P{p} REQUESTS CS")
    # Send REQUEST to voting set
    votes_needed = voting_sets[p][:]
    for q in voting_sets[p]:
        if not voted[q]:
            print(f"P{q} REPLIES to P{p}")
            voted[q] = True
            votes_needed.remove(q)
        else:
            queue[q].append(p)
            print(f"P{q} QUEUES P{p}")
    if not votes_needed:
        enter_cs(p)

def enter_cs(p):
    state[p] = 'HELD'
    print(f"P{p} ENTERS CS")
    exit_cs(p)

def exit_cs(p):
    state[p] = 'RELEASED'
    print(f"P{p} EXITS CS")
    # Send RELEASE to voting set
    for q in voting_sets[p]:
        voted[q] = False
        if queue[q]:
            next_p = queue[q].pop(0)
            print(f"P{q} REPLIES to queued P{next_p}")
            voted[q] = True

# ----------------- DEMO -----------------
request_cs(1)
request_cs(2)
request_cs(3)

