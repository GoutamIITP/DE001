from itertools import groupby

def compress_string(s):
    res = []
    for key, group in groupby(s):
        count = len(list(group))
        res.append(f"({count}, {key})")
    return " ".join(res)

 
input_str = input()
 
output = compress_string(input_str)

print(output)