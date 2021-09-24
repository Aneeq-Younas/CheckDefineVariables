try:
    a= ("Aneeq ")

except NameError:
    print("The variable is not defined ")

else:
    print("This first string variable is defined ")

try:
    b

except NameError:
    print("This second integer variable is not defined ")

else:
    print("This second integer variable is defined")

try:
    c = 0.76876

except NameError:
    print("This third float variable is not defined ")

else:
    print("This third float variable is defined ")