def summarize(temps):
    return {
        "minimum": min(temps),
        "maximum": max(temps),
        "average": sum(temps) / len(temps),
    }


temps = []

while True:
    value = input("Enter temperature ('done' to stop): ")
    if value.lower() == "done":
        break
    temps.append(int(value))

print(summarize(temps))