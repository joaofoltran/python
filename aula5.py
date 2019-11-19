weight = input("Weight: ")
measure = input("(L)bs or (K)g: ")

if measure.upper() == "K":
    final_weight = int(weight) / 0.45
    print(f"You are {final_weight} pounds.")
elif measure.upper() == "L":
    final_weight = int(weight) * 0.45
    print(f"You are {final_weight} kilograms.")
else:
    print("Please input K or L.")
