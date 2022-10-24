import random
n=int(input("Enter the number of friends joining (including you):\n"))
if n<=0:
    print("No one is joining for the party")
else:
    D={}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(n):
        inp=input()
        D[inp]=0
    total=float(input("Enter the total bill value:\n"))
    splitval=round(float(total)/float(n),2)
    for item in D:
        D[item]=splitval
    choice=input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if choice=="Yes":
        lucky=random.choice(list(D.keys()))
        print(lucky+ " is the lucky one!")
        splitval=round(float(total)/float(n-1),2)
        for item in D:
            if item !=lucky:
                D[item]=splitval
            else:
                D[lucky]=0
        print(D)
    else:
        print("No one is going to be lucky")
        print(D)