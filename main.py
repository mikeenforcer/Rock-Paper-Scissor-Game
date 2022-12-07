import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='P':
        if you=='R':
            return False
        elif you=='S':
            return True
    elif comp=='S':
        if you=='R':
            return True
        elif you=='P':
            return False
    elif comp=='R':
        if you=='S':
            return False
        elif you=='P':
            return True  


print("Computer's turn: ROCK(R) PAPER(P) SCISSORS(S)?")
randno=random.randint(1,3)
if randno==1:
    comp='R'
elif randno==2:
    comp='P'
elif randno==3:
    comp='S'
you=input("Your turn: ROCK(R) PAPER(P) SCISSORS(S)?")

a=gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")
if a == None:
    print("GAme is a Tie")
elif a:
    print("You WIN!")
else:
    print("You LOSE!")