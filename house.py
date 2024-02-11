name = input("What is your name? ")

match name :
    case "Harry"| "Ron" | "Hermione":
        print("gryffindor")
    case "Draco":
        print("slytherin")
    case _:
        print("I don't know")