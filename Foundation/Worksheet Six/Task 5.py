# mini vote validation function based on age input
# returns boolean value based on outcome


def vote_validation():
    age = int(input("Please enter your age.\n"))
    if age >= 18:
        return True
    else:
        return False
    
if __name__ == '__main__':
    print(vote_validation())