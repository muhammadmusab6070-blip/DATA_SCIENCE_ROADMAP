def total_exp(exp):
    total = 0
    for i in exp:
        total = total + i

    return total

Ali_exp_list = [2300,500,1000]
Ahmad_exp_list = [2300,500,1000]

print(f"Ali total expense : ",total_exp(Ali_exp_list))
print(f"Ahmad total expense : ",total_exp(Ahmad_exp_list))

