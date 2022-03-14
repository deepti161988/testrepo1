
import random

def gamewinner(user , computer):
    if user == computer :
        return None
    elif user=='s':
        if computer=='p':
            return False
        elif computer=='c':
            return True 
    elif user=='p':
        if computer=='s':
            return True
        elif computer=='c':
            return False
    elif user=='c':
        if computer=='s':
            return False
        if computer=='p':
            return True
    else:
        return None
while True:
    def user1():
        user = input("Enter user choice (stone(s), paper(p), cissors(c)): ")
        if user.lower() not in ('s', 'p', 'c'):
            print("Wrong choice")
        else:
            break
possible_actions = ["s", "p", "c"]
computer = random.choice(possible_actions)
#print(f"\nYou chose {user}, computer chose {computer}.\n")
print("you choose %s " %user )
print("computer choose %s " %computer )
#user = input("enter 1st You choice : ")
#computer = input("enter 2nd You choice : ")
g = gamewinner(user , computer)
if g == None:
    print('Game became Tie !!!')
elif g == True:
    print('You win')
elif g == False:
    print('computer win')


