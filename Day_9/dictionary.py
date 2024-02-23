a ={
    "bug":'Bugs in Python are unexpected behaviors that cause errors or incorrect results',
    "function":'Python Functions is a block of statements that return the specific task.',
    "error":'Errors are the problems in a program due to which the program will stop the execution'
    }
#print item by using key value
print(a["error"])

#adding new item to exing dictionary
a["code"]= "block of code"
print(a)

#edit dictionary
a["bug"] = "This is bug"
print(a)


#loop through a dictionary
for key in a:
    print(key)
    print(a[key])
#delete the entair dictionary
a = {}
print(a)



# ₹