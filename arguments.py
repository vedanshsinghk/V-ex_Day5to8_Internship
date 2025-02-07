#example1
print("THIS IS NEW EXAMPLE")
def my_function(fname): 
    print(fname + " Smith") 
my_function("Emil") 
my_function("Tobias") 
my_function("Linus")

#example2
print("THIS IS NEW EXAMPLE")
def my_function(fname, lname): 
    print(fname + " " + lname) 
my_function("Emil", "Refsnes")

#example3
print("THIS IS NEW EXAMPLE")
def my_function(fname, lname): 
    print(fname + " " + lname) 
my_function("Emil", "Smith")

#example4
print("THIS IS NEW EXAMPLE")
def my_function(*kids): 
    print("The youngest child is " + kids[2]) 
my_function("Emil", "Tobias", "Linus") 

#example5
print("THIS IS NEW EXAMPLE")
def my_function(**kid): 
    print("His last name is " + kid["lname"]) 
my_function(fname = "Tobias", lname = "Refsnes")

#example6

