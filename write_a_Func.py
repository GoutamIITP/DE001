def is_leap(year):
    n = year
    leap = False
    if n % 4 == 0:
        if n % 100 == 0:
            return n % 400 == 0
        return True 
    
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))