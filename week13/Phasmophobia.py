"""mod doc"""
def main():
    """doc"""
    evi1 = input()
    evi2 = input()
    evi3 = input()
    one = {"Banshee","Jinn", "Oni", "Phantom", "Revenant", "Shade"}
    two = {"Demon", "Oni", "Revenant", "Shade", "Spirit", "Yurei"}
    three = {"Banshee", "Poltergeist", "Revenant", "Spirit", "Wraith"}
    four = {"Demon", "Jinn", "Mare", "Oni", "Poltergeist", "Spirit", "Wraith"}
    five = {"Banshee", "Demon", "Mare", "Phantom", "Wraith", "Yurei"}
    six = {"Jinn", "Mare", "Phantom", "Poltergeist", "Shade", "Yurei"}
    no_evident = {
        "Banshee", "Demon", "Jinn", "Mare", "Oni", "Phantom",
        "Poltergeist", "Revenant", "Shade", "Spirit", "Wraith", "Yurei"
    }
    evident = {
        "EMF Level 5":one, "Ghost Writing":two,
        "Fingerprints":three, "Spirit Box":four,
        "Freezing Temperatures":five, "Ghost Orb":six,
        "No evidence":no_evident
               }
    result = sorted(list(evident[evi1] & evident[evi2] & evident[evi3]), key= str)
    if len(result) < 1:
        print("Not yet discovered")
    else:
        for i in result:
            print(i)
main()
