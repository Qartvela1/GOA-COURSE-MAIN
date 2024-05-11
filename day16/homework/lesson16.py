def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    print(num1 / num2)


add(1,2)
subtract(1,2)
multiply(1,2)
divide(1,2)



def area(width, height):
    print(width * height)

area(5,10)





def my_sum_func(numbers_list): 
    sum = 0
    
    for i in numbers_list:
        sum = sum + i
    
    print(sum)

my_sum_func([1,2,3,4,5])




def func(number_list):
    sum = 0
    quantity = 0
    
    for num in number_list:
        if num >= 0:
            sum = sum + num
        else:
            quantity = quantity + 1
    
    print(sum,quantity)

func([1,2,3,-1,-2,-3])












