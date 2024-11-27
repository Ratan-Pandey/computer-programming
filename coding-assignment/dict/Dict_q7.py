#Group Names by Their Initials
names = ["Alice", "Arnold", "Bob", "Charlie", "David"]
grouped = {}

for name in names:
    initial = name[0]
    grouped.setdefault(initial, []).append(name)

print("Grouped Names:", grouped)
