"""mod doc"""
import json
def main():
    """doc"""
    number = int(input())
    animal = ""
    cat_dict = {"Garfield":"Cat01"}
    fox_dict = {"Fubuki":"Fox01"}
    for _ in range(number):
        animal = input()
        if "Cat" in animal:
            cat_dict.update(json.loads(animal))
            if "Cat01" in animal:
                cat_dict.pop("Garfield")
            if "Fubuki" in animal and "Fubuki" in fox_dict:
                fox_dict.pop("Fubuki")
        elif "Fox" in animal:
            fox_dict.update(json.loads(animal))
            if "Fox01" in animal:
                fox_dict.pop("Fubuki")
            if "Garfield" in animal and "Garfield" in cat_dict:
                cat_dict.pop("Garfield")
    cat = sorted(cat_dict.items(), key= lambda x: x[1])
    fox = sorted(fox_dict.items(), key= lambda x: x[1])
    print(f"Cat : {len(cat_dict)}")
    print(f"Fox : {len(fox_dict)}")
    for i in cat:
        print(f"{i[0]} : {i[1]}")
    for i in fox:
        print(f"{i[0]} : {i[1]}")
main()
