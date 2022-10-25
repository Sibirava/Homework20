def enter_elements_row(ls):
    ls = []

    element = 0

    while element != -1:
        element = int(input("Input element in a row:"))
        if element == -1:
            break
        else:
            ls.append(element)
    return ls

# def sum_element_row(ls):
#     s = 0
#
#     for element in ls:
#         s += element
#     return s
#
# def main():
#     ls = []
#
#     ls = enter_elements_row(ls)
#
#     s = sum_element_row(ls)
#
#     print(f"The sum of elements in a {ls} row is {s}")
#
# main()

###########################################################
#recursion

def recursion_sum_element(ls):

    if ls == []:
        return 0
    else:
        s = recursion_sum_element(ls[1:])
        s = s + ls[0]
    return s

def main():
    ls = []

    ls = enter_elements_row(ls)

    s = recursion_sum_element(ls)

    print(f"The sum of elements in a {ls} row is {s}")

main()
