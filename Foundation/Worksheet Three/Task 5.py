# Program that displays pass grades based on mark input

def main():

    test_score = int(input("Please enter your test score.\n"))

    lower_mark = 40
    middle_mark = 60
    higher_mark = 70

    if test_score >= higher_mark:
        print("You have a distinction.")
    elif test_score >= middle_mark:
        print("You have a merit.")
    elif test_score >= lower_mark:
        print("You have a pass.")

    else:
        print("Sorry you have failed.")

if __name__ == '__main__':
    main()