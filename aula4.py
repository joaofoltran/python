name = "João Vítor Foltran"
name_lenght = len(name)

if name_lenght < 3:
    print("name must be at least 3 characters long")
elif name_lenght > 50:
    print("name cannot be more than 50 characters long")
else:
    print("name looks good")
