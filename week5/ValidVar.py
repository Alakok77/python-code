"""ValidVar"""
def variable_check():
    """Check variable that Valid or Invalid"""
    num = int(input())
    reserved_word = ("if","else","elif","while","for","True","False","continue",
                     "break","return","is","in","and","or","from","as","pass","not","def","None")
    for _ in range(num):
        variable = input()
        check = variable.strip()
        if variable not in reserved_word and check.isidentifier():
            print("Valid")
        else:
            print("Invalid")
variable_check()
