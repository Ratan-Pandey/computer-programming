# Function with Nested Functions
def outer_function(text):
    def inner_function():
        return text[::-1]
    return inner_function()

print(outer_function("Python"))
