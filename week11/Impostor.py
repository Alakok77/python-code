"""mod doc"""
import json
def main():
    """doc"""
    role = ""
    dead = ""
    dead_dict = {}
    role_dict = {}
    while True:
        role = input()
        if role == "Start":
            break
        role_dict.update(json.loads(role))
    while True:
        dead = input()
        if dead == "End":
            break
        dead_dict[dead] = role_dict.pop(dead)
    imposter = tuple(role_dict.values()).count("Impostor")
    sort_alive = sorted(role_dict.keys())
    sort_dead = sorted(dead_dict.keys())
    print(f"{imposter} Impostor Remains")
    print("***Alive***")
    for i in sort_alive:
        print(f"{i} : {role_dict[i]}")
    print("***Dead***")
    for i in sort_dead:
        print(f"{i} : {dead_dict[i]}")
main()
