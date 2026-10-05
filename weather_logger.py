temps = []

while True:
    value = input("Enter temperature ('done' to stop): ")
    if value.lower() == "done":
        break
    temps.append(int(value))

print(temps)