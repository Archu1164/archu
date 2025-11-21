#example with base case
def countdown(n):
    if n==0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)
        
        
        # Sum of numbers using recursion
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n-1)
print(sum_numbers(10))
