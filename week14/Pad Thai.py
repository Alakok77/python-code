""""mod doc"""
def main():
    """doc"""
    stable = []
    taste = []
    pull = ""
    stable_lst = ["Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
                  "Bean Sprouts", "Noodle", "Chives", "Lime",
                  "Egg", "Oil", "Peanuts"]
    stable_lst.sort(key=str)
    taste_lst = ["Sweet", "Sour", "Salty"]
    taste_lst.sort(key=str)
    while True:
        pull = input()
        if pull == "Cook":
            break
        if pull not in stable:
            stable.append(pull)
    while True:
        pull = input()
        if pull == "End":
            break
        if pull not in taste:
            taste.append(pull)
    stable.sort(key=str)
    taste.sort(key=str)
    equal_stable = stable_lst == stable
    equal_taste = taste_lst == taste
    in_scope = True
    for i in stable:
        if i not in stable_lst:
            in_scope = False
    if not in_scope:
        print("This is not Pad Thai!!!")
    elif not equal_stable:
        print("This is bad!")
    elif equal_stable and not equal_taste:
        print("Not Bad...")
    elif equal_stable and equal_stable:
        print("Delicious!")
main()
