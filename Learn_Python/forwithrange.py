#for n in range(0,10):
#    print(f"Iteration {n}")

exp = [2340, 2230, 2200, 3000]
total = 0
for i in range(len(exp)) :
    print(f"Month : {i+1}, Expense : {exp[i]}")
    total += exp[i]

print(f"Total amount : {total}")