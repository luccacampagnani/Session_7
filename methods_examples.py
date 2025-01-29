s = "hello"
print(dir(s))
useful_methods = [m for m in dir(s) if "__" not in m]
print(useful_methods)
print(help(s.capitalize))
print(s.capitalize())

print("HELLO".casefold()) # same as lower() method
print("HELLO".center(50))
print("HELLO".center(50, "*"))

print("I see a little dove".count("e")) # how many times do I see 'e'
print("anananananananannanananannananananananananananananan".count("ana"))
x = "I do not cook nor compare"
print(f"There are {x.count("o")}os inside: '{x}'")
print("hellooooooooooooolloo".find("l", 10))

s= "bob goes home to meet bob so they can take their bob and go bobing"
pos = 0
while True:
    start = s.find("bob", pos)
    if start == -1:
        break
    print("found bob on position", start)
    pos = start + 1

    items = ["cat", "rat", "mouse", "house"]
print(" ".join(items))

print("I LIKE to go HIKING".lower().upper())
print("I like to go skiing".title())

# replace, replaces item inside the string
print("I like to go skiing".replace(" ", "***"))

# split makes a list of the string split by the delimiter
print("i like to go skiing".split())
