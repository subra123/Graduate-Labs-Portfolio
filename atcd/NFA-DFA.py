def get_next_state(nfa,states,symbol):
    next_state=set()
    for state in states:
        next_state.update(nfa.get((state,symbol),[]))
    return next_state

def main():
    n=int(input("enter the number of states: "))
    nfa={}

    for i in range(n):
        for symbol in [0,1]:
            state=f"q{i}"
            nfa[(state,symbol)]=input(f"enter the transions for ({state},{symbol}): ").split()
    print("nfa output \n")
    for (state,symbol),next_state in nfa.items():
        print(f"({state},{symbol}) -> {next_state}")
    
    #nfa to dfa\
    dfa = {}
    states_p = [['q0']] #start state
    visited = set()
    while states_p:
        curr = tuple(states_p.pop(0))
        if curr in visited:
            continue
        visited.add(curr)
        for symbol in [0,1]:
            next_state =get_next_state(nfa,curr,symbol)
            dfa[(curr,symbol)] = next_state
            if next_state and tuple(next_state) not in visited:
                states_p.append(next_state)
    print("dfa output \n")
    for (state,symbol),next_state in dfa.items():
        print(f"({state},{symbol}) -> {next_state}")

if __name__ == "__main__":
    main()
