# Code to play rock , paper , scissor .
import random
import time

print("*********|| Welcome to the Game || *********\n")
n=input("Enter your Name :")
print("* ROUND 1 *")
l=["Rock","Paper","Scissor"]

def rounds(l,n):
    a=int(input("Your Choose Rock,Paper or Scissor(1,2,3):"))
    if (a==1):
        cho="Rock"
    elif (a==2):
        cho="Paper"
    elif (a==3):
        cho="Scissor"
    else:
        print("Invalid choice")
        
    print("Results...\n",)
    time.sleep(2)
    comp=random.choice(l)
    print("Your Choice:",cho,"\nComputer Choice:",comp,"\n")
    if (comp==cho):
        print("Tie")
    if ((comp=="Rock" and cho=="Scissor") or (comp=="Paper" and cho=="Rock") or (comp=="Scissor" and cho=="Paper")):
        print("Computer Winner")
    if ((cho=="Rock" and comp=="Scissor") or (cho=="Paper" and comp=="Rock") or (cho=="Scissor" and comp=="Paper")):
        print(n," is Winner.")
    ask=input("\nDo you Wanna Play Again?(y/n):")
    if (ask.upper()== "Y"):
        print("\n* Next ROUND *")
        rounds(l,n)
    else:
        print("Thank You")
rounds(l,n)