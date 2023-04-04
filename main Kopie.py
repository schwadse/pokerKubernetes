value = input("Auf welcher Position sitzt du?")

def varifyPosition(value):
    match value:
        case "utg":
            return True


print(varifyPosition(value))