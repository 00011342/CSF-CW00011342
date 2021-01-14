
# object oriented programming
# creating students class
class student:
    # creating instance attributes
    def __init__(self, first,last,course,phone,location):
        self.first=first
        self.last=last
        self.course=course
        self.phone=phone
        self.location=location

    # instance method
    def fullname(self):
            return "{} {} ".format(self.first, self.last)

    def fulladdress(self):
        return "{} {}\n {}\n {}\n {}\n ".format(self.first,self.last,self.course,self.phone,self.location)

 # giving value for instance objects
student1 = student("Anvar","Yakhyoev","BIS","998-99-081-95-51","Samarkand")
student2 = student("Jack","Petirson","Emob","1-998-99-081-00-00","London")

# call instance methods
print(student1.fulladdress())
print(student2.fulladdress())

# in OOP , we use objects to represent our data which objects hold data about the in attributes
# and the attributes are manipulated through methods and functions which is given for objects

# in Functional programming , output of function should always be the same ,given the same exact inputs to the function
# data cannot be stored on objects only transforming by creating functions (nested functions and paralel programming )

                              # Functional programming
# creating pure function
# multiply list of numbers by 2
def multiply_2(numbers):
    # creating new list for changed numbers
    new_numbers = []
    # looping for each list item
    for n in numbers:
        # adding multiplied numbers in new list
        new_numbers.append(n*2)
    #returing value
    return new_numbers
# creating original number list
original_numbers =[2,4,10,20,30]
#creating veriable for changed list
changed_numbers =multiply_2(original_numbers)
print(original_numbers)
print(changed_numbers)
    # Creating new list for changed numbers;

