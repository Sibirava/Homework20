# def sum_digits_number(number):
#     s = 0
#     while number > 0:
#         digit = number % 10
#         s += digit
#         number = number // 10
#     return s
#
# def main():
#     number = int(input("Input your number: "))
#     sum_digit = sum_digits_number(number)
#     msg = f"The sum of number {number} is {sum_digit}"
#     print(msg)
#
# main()

########################################
#recursion

def recursion_sum_digit(number):
    if number == 0:
        return 0

    return number % 10 + recursion_sum_digit(number // 10)

def main():
    number = int(input("Input your number: "))
    s = recursion_sum_digit(number)
    msg = f"The sum of digits number {number} is {s}"
    print(msg)

main()