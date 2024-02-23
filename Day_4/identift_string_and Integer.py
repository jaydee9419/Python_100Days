a = [[123,456,"Hello"],[987,654, "World"]]
string = []
integer = []
for sublist in a:
    for item in sublist:
        if isinstance(item, str):
            string.append(item)
        else:
            integer.append(item)
print(string)
print(integer)