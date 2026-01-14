def add(firstName: str, lastName: str):
    firstName.capitalize()
    return firstName + " " + lastName

fname = "Bill"
lname = "Gates"
name = add(fname,lname)
print (name)