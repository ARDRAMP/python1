x=int(input("enter the starting year: "))
y=int(input("enter the ending year: "))
print("the entered year is a leap year. ")
for i in range(x,y):
 if((i%400==0)or((i%100!=0) and (i%4==0))):
   print(i)