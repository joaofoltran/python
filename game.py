options = ["start", "stop", "help", "quit"] 

command = ""
started = False
while True:
    command = input("> ").upper()
    if command == "HELP":
        print('\n'.join(options))
    elif command == "START":
        if not started:
            print("Car started!")
            started = True
        else:
            print("Car is already on!")
    elif command == "STOP":
        if started:
            print("Car stopped.")
            started = False
        else:
            print("Car is not started!")
    elif command == "QUIT":
        break
    else:
        print("Not an option.")
