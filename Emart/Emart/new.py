def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def sum_odd_numbers(lst):
    if not lst:
        return 0
    else:
        if lst[0] % 2 !=0:
            return lst[0]+ sum_odd_numbers(lst[1:])
        else:
            return sum_odd_numbers(lst[1:])
        
my_list= [1,2,3,4,5,6,7,8,9]
result = sum_odd_numbers(my_list)

    
# result= factorial(5)
print("sum of odd numbers in the list:",result)