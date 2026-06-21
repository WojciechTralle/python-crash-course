bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

#return the first (formatted) item from the list bicycles
print(bicycles[0].title())
#the following asks for (formatted) 2nd and 4th item in the list
print(f"The 2nd and 4th item in the list are",bicycles[1].title(),"and",bicycles[3].title())

#the following asks for the last item in the list
print(f"The last item in the list is",bicycles[-1].title())
#the following returns the second item from the end of the list
print(f"The second item from the end of the list is",bicycles[-2].title())

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)



