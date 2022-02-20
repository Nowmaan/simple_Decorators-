# def div(num1,num2):
#     print(num1/num2)
#
# div(4,16)


# def div(num1,num2):
#     if num1<num2:
#         num1,num2 = num2,num1
#     print(num1/num2)
#
# div(4,16)

def div(num1,num2):
    print(num1/num2)

def smart_div(func):

    def inner(num1,num2):

        if num1<num2:
            num1,num2 = num2,num1
        return func(num1,num2)

    return inner

div = smart_div(div)

div(4,16)