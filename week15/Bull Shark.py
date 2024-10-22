"""mod doc"""
def main():
    """doc"""
    the_shallow = ["Bull Shark"]
    twilight = ["Chain Catshark", "Great White Shark", "Gummy Shark",
                "Blue Shark", "Mako Shark"]
    midnight = ["Frilled Shark", "Goblin Shark", "Sixgill Shark", "Greenland Shark"
                ,"Cookiecutter Shark"]
    abyssal = ["Megamouth Shark"]
    shark = input().lower().title()
    if shark in twilight:
        print("THE TWILIGHT ZONE")
    elif shark in midnight:
        print("THE MIDNIGHT ZONE")
    elif shark in abyssal:
        print("THE ABYSSAL ZONE")
    elif shark in the_shallow:
        print("THE SHALLOW ZONE")
    else:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
main()
