key_location = "bed"
location = ["drawing room", "bed", "hall"]

for item in location:
    if item == "bed":
        print("Key found")
        break

print(f"key location is {key_location}")
