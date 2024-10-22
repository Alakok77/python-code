"""mod doc"""
def main():
    """doc"""
    gender = input()
    weight = float(input())
    have_license = input()
    voluum = float(input())
    alc_can = float(input())
    can = float(input())
    hour = int(input())
    alcohol = (alc_can * (voluum*can))/100
    male = (alcohol / (weight * 0.68 * 10)) * 1000
    female = (alcohol / (weight * 0.55 * 10)) * 1000
    result = "Not Safe"
    if gender == "Male" and male - (15 * hour) <= 50 and have_license == "Yes":
        result = "Safe"
    elif gender == "Female" and female - (15 * hour) <= 50 and have_license == "Yes":
        result = "Safe"
    print(result)
main()
