s = "0123456789"
print(s)
print(s[1:2]) # first index is included, second index is excluded
print(s[4:7])
print(s[:7]) # if you want to omit the first index, it starts from beginning

s = "I go to school early in the morning"
print(s[:20])
print(s[20:]) # includes all the way to the end

print(s[:]) # the whole thing
print(s[::2]) # this means stop of 2 (every second character)
print(s[::-1])
print("racecar"[::-1])

