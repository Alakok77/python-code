"""mod doc"""
def main():
    """doc"""
    menu = ""
    buffer = []
    menu_lst = []
    can_not = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        buffer = menu.split(" #")
        if menu == "CLOSED":
            menu_lst.clear()
            break
        if menu == "SOMETHING'S WRONG":
            menu_lst.clear()
            continue
        if "Can't do:" in menu:
            can_not = menu.split(': ')
            menu_lst.remove(can_not[1])
        elif buffer[1] == "N":
            menu_lst.append(buffer[0])
        else:
            menu_lst.insert(int(buffer[1]) - 1, buffer[0])
    reverser = menu_lst.copy()
    reverser.reverse()
    print(f"Full Course: {menu_lst} Reversed: {reverser}")
main()
