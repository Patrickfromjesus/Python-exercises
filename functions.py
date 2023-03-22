# Ex. 1
def greater_num(a, b):
    return max([a, b])


# Ex. 2
def average(list_nums):
    sum = 0
    for elem in list_nums:
        sum += elem
    print(sum / len(list_nums))
    return sum / len(list_nums)


# Ex. 3
def make_squares(n):
    for elem in range(n):
        print(5 * "*")


# Ex. 4
def greater_length(list_names):
    list_length = []
    for name in list_names:
        list_length.append((len(name), name))
    print(max(list_length)[1])


# EX. 5
def calc_price(width):
    volume_needed = width / 3
    cans_needed = volume_needed / 18
    print((cans_needed, 80 * cans_needed))


# EX. 6
def test_sides(a, b, c):
    is_triangle = [a + b <= c, b + c <= a, a + c <= b]
    return not any(is_triangle)


def is_triangle(side_a, side_b, side_c):
    is_two_sides_equals = [
        side_a == side_b,
        side_a == side_c,
        side_b == side_c,
    ]
    is_three_sides_equals = [side_a == side_b, side_a == side_c]
    if not test_sides(side_a, side_b, side_c):
        print("Não é um triângulo.")
    elif all(is_three_sides_equals):
        print("Triângulo Equilátero")
    elif any(is_two_sides_equals):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
