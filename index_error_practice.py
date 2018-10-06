
l = list()

try:
    l[1]

except IndexError as error:
    x = 1
    print(error)
    print(x)
    print("this is where we do something else.")

