print('Student score')
count=int(input(" Student : "))
i=1
a=""
b=""
c=""
d=""
e=""
f=""
score = 0
thislist = []
while i<= count :
    score=int(input("Enter score : "))
    thislist.append(score)
    i+=1
    if score>=90 and score<=100:a+="*"
    elif score >= 80 and score<=89:b+="*"
    elif score >= 70 and score<=79:c+="*"
    elif score >= 60 and score<=69:d+="*"
    elif score >= 50 and score<=59:e+="*"
    elif score <= 49 and score<=0 :f+="*"
    else :
         print("Error!!!!!!!")
         i=-1


print("\n")
print(thislist)
print("\n")
print("Graph Score")
print("Score 90-100 :",a)
print("Score 80-89 :",b)
print("Score 70-79 :",c)
print("Score 60-69 :",d)
print("Score 50-59 :",e)
print("Score 0-49 :",f)
