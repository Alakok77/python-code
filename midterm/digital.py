"""mod doc"""
def main():
    """doc"""
    name = input()
    thailand = input()
    home = input()
    old = float(input())
    income = float(input())
    saving = float(input())
    thai_check = thailand in ("True", "Yes")
    home_check = home in ("True", "Yes")
    old_check = old >= 16
    income_check = income <= 840000
    saving_check = saving <= 500000
    if thai_check and home_check and old_check and income_check and saving_check:
        print(f"Congratulations! {name} is qualified to receive a digital \
wallet amount of 10,000 baht, sponsored by all taxpayers in Thailand.")
    else:
        print(f"Unfortunately, {name} is not qualified.")
main()
