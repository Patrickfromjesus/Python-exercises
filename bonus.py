# Ex. 1
def find_min(list):
    print(min(list))


# Ex. 2
def make_triangle_retangle(n):
    for elem in range(n):
        print((elem + 1) * "*")


# Ex. 3
def sum_of_n(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    print(sum)


# Ex. 4
def total_price(volume, type):
    total = 0
    if type == "A":
        total = 1.87 * volume
        if volume > 20:
            total -= 0.05 * volume
    elif type == "G":
        total = 2.46 * volume
        if volume > 20:
            total -= 0.06 * volume
    print(total)
