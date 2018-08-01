
l = list()

try:
    l[1]

except IndexError as error:
    print(error)
    print("this is where we do something else.")
