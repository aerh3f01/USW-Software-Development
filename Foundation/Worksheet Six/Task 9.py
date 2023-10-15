# Asks user to input score on exam
# displays grade based on score


def grade(score):
    if score < 40:
        return "Sorry you failed."
    elif score < 60:
        return "You have passed."
    elif score < 70:
        return "You have a merit."
    else:
        return "You have a distinction."
    
if __name__ == '__main__':
    score = int(input("Please enter your score.\n"))
    print(grade(score))