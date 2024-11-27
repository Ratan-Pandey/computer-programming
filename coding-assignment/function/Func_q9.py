# Higher-Order Function
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x ** 2, 6)
print(result)
