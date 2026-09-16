def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Vô số nghiệm"
        else:
            return "Vô nghiệm"
    else:
        return -b / a


print(f"Giải 2x + 4 = 0: x = {solve_linear_equation(2, 4)}")



def is_even(n):
    return n % 2 == 0


print(f"5 là số chẵn? {is_even(5)}")
print(f"4 là số chẵn? {is_even(4)}")



def fibonacci(n):
    a=0
    b=1
    result = []
    while a < n:
        result.append(a)
        a=b
        b=a+b
    return result


print(f"Fibonacci nhỏ hơn 20: {fibonacci(20)}")
