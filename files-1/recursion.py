def sum(x):
    if x <=1:
        return 1
    return x + sum(x-1)
x = 100
print(sum(x))
    
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    return num_list[0] + list_sum(num_list[1:])
num_list = [2, 4, 5, 6, 7]
list_sum(num_list)
    
def sum_series(n):
    if n< 1:
        return 0
    return n + sum_series(n-2)
n = 6
print(sum_series(n))

'''def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return Fibonacci(n-1)+ Fibonacci(n-2)'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = 10
print(fibonacci(n))