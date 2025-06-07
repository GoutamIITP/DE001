# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def solve():
    n = int(input())
    letters = input().split()
    k = int(input())

    count_a = letters.count('a')

    # Total number of ways to choose k indices from n
    total_comb = math.comb(n, k)

    # Number of ways to choose k indices such that none of them contain 'a'
    # This means choosing k indices from the (n - count_a) non-'a' characters
    comb_without_a = 0
    if (n - count_a) >= k: # Ensure we have enough non-'a' characters to pick k from
        comb_without_a = math.comb(n - count_a, k)

    # Number of ways to choose k indices such that at least one contains 'a'
    comb_with_at_least_one_a = total_comb - comb_without_a

    # Calculate the probability
    if total_comb == 0: # Handle edge case where no combinations are possible
        probability = 0.0
    else:
        probability = comb_with_at_least_one_a / total_comb

    # Print the result formatted to 3 decimal places
    print(f"{probability:.4f}") # Output requires 4 decimal places for 0.8333

solve()