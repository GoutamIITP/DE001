# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def solve():
    n = int(input())
    letters = input().split()
    k = int(input())

    count_a = letters.count('a')

  
    total_comb = math.comb(n, k)

    # Number of ways to choose k indices such that none of them contain 'a'
     
    comb_without_a = 0
    if (n - count_a) >= k:  
        comb_without_a = math.comb(n - count_a, k)

    # Number of ways to choose k indices such that at least one contains 'a'
    comb_with_at_least_one_a = total_comb - comb_without_a

    # Calculate the probability
    if total_comb == 0:  
        probability = 0.0
    else:
        probability = comb_with_at_least_one_a / total_comb
 
    print(f"{probability:.4f}")  

solve()