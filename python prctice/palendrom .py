def palendrom(s):
    return s == s[::-1]

test = input("enter a string:")
print(f"{test} string is palndrom {palendrom(test)}")


