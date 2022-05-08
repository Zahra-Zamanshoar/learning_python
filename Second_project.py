def compute_number(base, power):
    result = 1
    for P in range(power):
        result = result * base

    return result

base = int(input("please typ your base:  "))
power = int(input("please type your power:  "))
print(compute_number(base, power))

