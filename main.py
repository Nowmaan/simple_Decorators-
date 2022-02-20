# 1 First we write the simple eg of Division You will get the output as 4.0.

# def div(num1,num2):
#     print(num1/num2)
#
# div(16,4)

# 2 As we see in 1 it is simple division answer but what if we change the denomenator higher than the numerator we get 0.25 thats where we want to change,
# we want to give a simple logic to swap the numerator to denomenator , as if we give any sequence of numbers.

# def div(num1,num2):
#     print(num1/num2)
#
# div(4,16)

# 3 We have given a logic in if statement to swap the numbers , but what if we don't want to change that particular function.

# def div(num1,num2):
#     if num1<num2:
#         num1,num2 = num2,num1
#     print(num1/num2)
#
# div(4,16)


# 4 In that time we use Decorators in the code we use a new function into the wrap-function to add the if statement.

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
