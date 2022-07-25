"""n.npat"""

def main():
    """n.npat"""
    money = int(input())
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    ans_money = money-water
    if ans_money % 3 == 0:
        ans_snack1 = snack1 * 10
        ans_money -= ans_snack1
    elif ans_money % 3 == 1:
        ans_snack1 = snack1 * 15
        ans_money -= ans_snack1
    elif ans_money % 3 == 2:
        ans_snack1 = snack1 * 20
        ans_money -= ans_snack1

    if ans_money % 3 == 0:
        ans_snack2 = snack2 * 12
        ans_money -= ans_snack2
    elif ans_money % 3 == 1:
        ans_snack2 = snack2 * 15
        ans_money -= ans_snack2
    elif ans_money % 3 == 2:
        ans_snack2 = snack2 * 18
        ans_money -= ans_snack2

    if ans_money % 3 == 0:
        ans_snack3 = snack3 * 5
        ans_money -= ans_snack3
    elif ans_money % 3 == 1:
        ans_snack3 = snack3 * 7
        ans_money -= ans_snack3
    elif ans_money % 3 == 2:
        ans_snack3 = snack3 * 9
        ans_money -= ans_snack3

    if ans_money < 0:
        print("Now you have", money, "left.")
        print("You don't have enough money!")
    elif ans_money >= 0:
        print("Now you have", ans_money, "left.")
        print("Here's your order!")
        print("Water:", water, "baht")
        print("Snack number 1:", ans_snack1, "baht")
        print("Snack number 2:", ans_snack2, "baht")
        print("Snack number 3:", ans_snack3, "baht")
main()
