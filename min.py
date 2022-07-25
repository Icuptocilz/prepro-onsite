"""docstring"""

def main():
    """grade for retry"""
    grade1 = float(input())
    ans_grade = 4 - grade1
    if grade1 < 1:
        print("I'm so sad.")
    elif grade1 < 2:
        print("%.2f" %ans_grade)
    else:
        print("I'm so happy.")
main()
