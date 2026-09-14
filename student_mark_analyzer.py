"""n=map(int,input().split())
max=0
for i in n:
  if(max<i):
    max=i
print(max)

n=list(map(int,input().split()))
max=0
for i in range(len(n)):
  
  if(i%3==0):
    max=max+1
print(max)

s=False
print(s)

palindrome

n=int(input())
temp=n
rev=0
while(n>0):
  d=n%10
  rev=rev*10+d
  n=n//10
if(temp==rev):
  print("Palindrome")
else:
  print("Not Palindrome")

s=input()
rev=""
for i in range(len(s)-1,-1,-1):
  rev=rev+s[i]
if rev==s :
  print("yes")
else:
  print("no")


s=input()
count=0
v="AEIOUaeiou"
for i in range(len(s)):
  if s[i] in v:
    count=count+1
print(count)

s="sasi"
print(s[0:4])

n=list(map(int,input().split()))
total=0
max=n[0]
min=n[0]
pass_status=True
for i in n:
  total=total+i
  if max<i:
     max=i
  if min>i:
    min=i
  if i < 35:
    pass_status=False
avg=total/len(n)
print("Tptal of the marks:",total)
print("Avesrge of the marks:",avg)
print("highest marks:",max)
print("Lowest marks:",min)
if(avg>=90):
  grade="A"
elif(avg>=75):
  grade="B"
elif(avg>=65):
  grade="C"
elif(avg>=35):
  grade="D"
else:
  grade="E"
print("Grade:",grade)
if pass_status:
  print("Result:Pass")
else:
  print("Result:Fail")"""

print("----------STUDENT INFORMATION----------")
s=input("Enter your name:")
print("Name:",s)
n=int(input("Enter your reg no:"))
print("Reg No:",n)
sub1=input("Enter your subject:")
sub2=input("Enter your subject:")
sub3=input("Enter your subject:")
sub4=input("Enter your subject:")
marks=list(map(int, input("Enter your marks:").split()))
print("\n----------MARKS DETAILS----------")
print(sub1, ":" ,marks[0])
print(sub2, ":" ,marks[1])
print(sub3, ":" ,marks[2])
print(sub4, ":" ,marks[3])

total=0
max=marks[0]
min=marks[0]
pass_status=True
for i in marks:
  total=total+i
  if max<i:
     max=i
  if min>i:
    min=i
  if i < 35:
    pass_status=False
avg=total/len(marks)
print("\n----------RESULT SUMMARY----------")

print("Total  marks:",total)
print("Avesrge of the marks:",avg)
print("highest marks:",max)
print("Lowest marks:",min)
if(avg>=90):
  grade="A"
elif(avg>=75):
  grade="B"
elif(avg>=65):
  grade="C"
elif(avg>=35):
  grade="D"
else:
  grade="E"
print("Grade:",grade)
if pass_status:
  print("Result:Pass")
else:
  print("Result:Fail")






  
