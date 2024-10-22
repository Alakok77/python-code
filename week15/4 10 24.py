"""mod doc"""
def main():
    """doc"""
    colors = [input() for _ in range(4)]
    numbers = {"Black":0, "Brown":1, "Red":2, "Orange":3,
               "Yellow":4, "Green":5, "Blue":6, "Purple":7,
               "Grey":8, "White":9}
    multi = {"Black":1, "Brown":10, "Red":100, "Orange":1000,
               "Yellow":10000, "Green":100000, "Blue":1000000, "Purple":10000000,
               "Gold":0.1, "Silver":0.01
    }
    toler = {"Brown":0.01, "Red":0.02, "Green":0.005,
             "Blue":0.0025, "Purple":0.001, "Grey":0.0005,
             "Gold":0.05, "Silver":0.1
    }
    error1 = colors[0] not in numbers or colors[1] not in numbers
    error2 = colors[2] not in multi
    error3 = colors[3] not in toler
    if error1 or error2 or error3:
        print("Error")
    else:
        num = str(numbers[colors[0]]) + str(numbers[colors[1]])
        total = int(num) * multi[colors[2]]
        add = total * toler[colors[3]]
        print(f"{total - add:.4f}")
        print(f"{total + add:.4f}")
main()
