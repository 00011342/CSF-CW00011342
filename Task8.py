#
#   # void function does not return value!
# def compare_age(n):
#     if n<18:
#         print("You are young ")
#     elif n<=30:
#         print("You are accepted")
#     else :
#         print("you are too old ")
#     print("thank you")
#
# compare_age(32)

def find_President_US(*p):
    p = ("Donald Trump","Joe Biden","SHavkat Mirzioev")
    print(p[1])
  # * create tuples and we can access through index value
find_President_US()



# value returning functions are always return vlaue by using return statement!
def squared_number(x):
   y =  x * x
   return y

print(squared_number(20))


def deposit_cal(amount ,rate):
    return amount*rate
print(deposit_cal(100,10))









