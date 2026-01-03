def tac(exp):
    tokens = [tokens.strip() for tokens in exp.split("+")]
    tac = []
    count =1
    temp_var  = f"t{count}"
    tac.append(f"{temp_var} = {tokens[0]} + {tokens[1]}")

    for token in tokens[2:]:
        count+=1
        new_var = f"t{count}"
        tac.append(f"{new_var}={temp_var}+{token}")
        temp_var = new_var

    tac.append(f"x={temp_var}")

    return tac

exp = input("enter the expression: ")
res = tac(exp)

print("tac of the given problem :\n")
print("\n".join(res))
