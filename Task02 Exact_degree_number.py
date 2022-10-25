# def proof_exact_degree(number, degree):
#     count = 0
#
#     while number != 1:
#         if number % degree == 0:
#             count += 1
#             number = number // degree
#         else:
#             return 0
#     return count
#
#
# def main():
#     number = int(input("Input number: "))
#
#     degree = int(input("Input potential degree you want to check: "))
#
#     count_degree = proof_exact_degree(number, degree)
#
#     if proof_exact_degree(number, degree):
#         msg = f"Number {number} is {degree} in {count_degree}-th(d) degree"
#     else:
#         msg = f"Number {number} isn't exact degree of {degree}"
#
#     print(msg)
#
#
# main()

#####################################################
#recursion

def recursion_exact_degree(number, degree):

    if number == 1:
        return 1
    elif 2 > number > 1:
        return 0
    return recursion_exact_degree(number / degree, degree)

def main():
    number = int(input("Input your number: "))
    degree = int(input("Input your degree: "))

    if recursion_exact_degree(number / degree, degree) == 1:
        msg = f"Yes, number is the exact degree of {degree}"
    else:
        msg = f"No,number isn't the exact degree of {degree}"
    print(msg)

main()