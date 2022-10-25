# def power_number(x, n):
#     if x == 0:
#         return -1
#
#     return(x**n)
#
# def main():
#     x = float(input("Input x = "))
#
#     n = int(input("Input n(degree) = "))
#
#     result = round(power_number(x, n))
#
#     print(f"Result of {x} in {n} degree is {result}")
# main()

#################################################
# recursion

def recursion_power_number(x, n):
    if x == 0:
        return -1

    if n == 0:
        return 1
    return x * recursion_power_number(x, (n - 1))

def main():
    x = float(input("Input x = "))

    n = int(input("Input n(degree) = "))

    result = round(recursion_power_number(x, n), 2)

    print(f"Result of {x} in {n} degree is {result}")

main()