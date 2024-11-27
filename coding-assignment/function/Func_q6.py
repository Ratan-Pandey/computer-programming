# Function with Keyword Arguments (**kwargs)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Shivansh", age=20, city="Agra")
