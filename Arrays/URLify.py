"""
Write a method to replace " " with %20

Developed by Kedar Pandhare

"""
from memory_profiler import profile

@profile
def urLify(s):
    new_array = []
    for i in range(len(s)):
        if s[i] != " ":
            new_array.append(s[i])
        else:
            new_array.append("%20")

    return "".join(new_array)

output = urLify("Thisis Soamaing That I could just fly in it. Also, i would love to eat here.")
print(output)
