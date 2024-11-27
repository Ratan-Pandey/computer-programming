#Create a Dictionary and Perform Basic Operations

person = {"name": "Shivansh", "age": 20, "city": "Agra"}
print("Name:", person["name"])
person["hobby"] = "Photography"
person["age"] = 21
person.pop("city")
print("Updated Dictionary:", person)
