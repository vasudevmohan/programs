'''
print("first program")

num1 = 5
num2 = 6
print(num1%num2)

print(1==1 and (not(1==1 or 1==0))) 
print ()
'''
#1
"""
a=10
if(a>0):
    print("Positive Integer")
"""
#2
"""
a=-10
if(a>0):
    print("Positive Integer")
else:
    print("Not a positive Integer")
"""

#3
"""
number = int(input("Enter a number "))
print( f"Nuber is {number}")
if (number%3==0 or number%5 == 0):
    if(number%3==0 and number%5==0):
        print("number is divisible by 3 and 5")
    elif(number%5==0):
        print("number is dvisible by 5")
    else:
        print("number is divisible by 3")
    
else:
    print("invalid") 
"""   
    
#4
"""
num = 12 


while (num<=120):
    print("table of 12 >>> ",num)
    num +=12
"""

#5
"""
for val in 1,2,3,4,5:
    print ("The current number is ",val) 
    
start = 12
end = 121
step = 12

for val in range  (start, end , step):
    print("the current number is ", val)
"""

#6
'''
for number in range(5,0,-1):
    print(number)
    
for number in range(-1,-5,-1):
    print(number)
'''

#7

'''
age = 23
name = "Aditya"
print("my name is %s and age is %s" %(name,age ))
print("my name is {} and age is {}" .format(name,age ))
print(f'My name is {name} and age is {age}')
'''

#8

"""
print(2,4,6,8,10,12,14,16,18,20,sep="\n",end = "\n......")
"""

#9

"""
for i in range (5):
    print(i)   
 
for number in range(5,0,-1):
    print(number)
    

for number in range(0,5,-1):          
    print(number)
    


"""
#10

"""
num=10 
count = 0

while(count<=num):
    if(count%2 == 0):
        pass
    else:
        print(count)
    count = count+1
    
count=0    
while(count<=num):
    if(count%2 == 0):
        pass
    else:
        print(count)
    count = count+1
        
        
        
count1=0    
while(count1<=num):
    if(count1%2 == 0):
        count1 = count1+1
        continue
    else:
        print(count1)
        count1 = count1+1

"""

#11


"""
year = int(input("Enter the year    >>  ") )
print(year)

def isLeap (year):
    if (year %400 == 0):
        return True
    if (year % 100 == 0):
        return False
    if (year % 4 == 0):
        return True
    
if (isLeap(year)):
    print("%d is a leap year " %(year))
else:
    print("%d is not a leap year" %(year))
    
"""

   
#12

"""
num1 = input()
num2 = input()
num3 = input()

print("{} {} {} ".format(num1,num2,num3))

"""

#13

"""
x, y, z = [int(x) for x in input("Enter the Numbers : ").split()]

print(x,y,z)
if (x>=y and x>=z):
    print(f"{x} is maximum")
elif (y>=z and y>=x):
    print(f"{y} is maximum")
else:
    print(f"{z} is maximum")

"""

#14

# is prime or not 

'''x = int(input(" Enter the number "))
i=2
print(f"{x} is input")
flag = True
while(i*i<=x):
    if (x%i==0):
        flag = False
        break
    else:
        i=i+1
        
if (flag):
    print(f" {x} is prime number ")
else:
    print(f" {x} is not primer")'''
    
# 15


"""def find_square(n):
    return n*n

print(find_square(6))


def find_sum(n):
    temp = 0
    for i in range(n+1):
        print(i,end=" ")
        temp += i
    return temp

print(find_sum(10))        


def test_arg (x:int,*y):
    sum = 0
    sum += x
    for x in y :
        sum += x
    print(sum)    
test_arg(10,20,30,40,50,60)"""

#16

"""def factorial (n):
    ans = 1
    for i in range(1,n):
        ans *= i
        print(ans,end= " ")
    return ans
print("\n",factorial(10))"""
    
#17


"""num = input()
print("Number is ",num)
def is_palindrom(num):
    len1 = len(num)
    num2 = num[::-1]
    
    return num2.endswith(num[len1//2:])

print(is_palindrom(num))"""


#18


"""num1,num2 = input("enter two numbers  ").split(",")
print(num1,num2,sep=" ")
def check_amicable_numbers(num1,num2):
    sum_divisor_1 = 0
    sum_divisor_2 = 0
    
    i1 = 1
    i2 = 1
    
    while(i1*i1<=num1):
        if(num1%i1==0):
            if (i1*i1==num1 or i1 == 1):
                sum_divisor_1 += i1
            else:
                sum_divisor_1 += (i1 + num1//i1)
                
        i1 = i1 + 1
        
    while(i2*i2<=num2):
        if(num2%i2==0):
            if (i2*i2==num2 or i2 == 1):
                sum_divisor_2 += i2
            else:
                sum_divisor_2 += (i2 + num2//i2)
                
        i2 = i2 + 1
        
        
    print(sum_divisor_1,sum_divisor_2,sep=" ")

check_amicable_numbers(int(num1),int(num2))"""


#19

"""num,n = input("Enter the numbwe and n ").split(",")
print(num,n,sep="<<num__n>>")
print(int(num)>>int(n))"""

#20

"""def factorial (num):
    ans = 1
    if(num==0):
        return 1
    while(num!=1):
        ans *= num
        num -= 1
    return ans

print(factorial(5))
print(factorial(0))

def  check_strong_number(n):
    ans = 0
    while(n != 0):
        ans += factorial(n%10)
        n = n//10
    return ans
print("strong num output ",check_strong_number(145))"""

#21

"""import re
word="New Airlines4"
if(re.search(r"^N",word) and re.search(r"e$",word)):
    print(re.sub(r"New",r"Old",word))
else:
    print(re.sub(r"s(\d{1})",r"S\1",word))"""

#22

"""sample_input_1 = [1,1,5,100,-20,-20,6,0,0]
sample_input_2 = [10,20,30,40,30,20]
sample_input_3 = [1,2,2,3,4,4,4,10]

def occurance (list):
    count=0
    for i in range(0,len(list)-1):
        if list[i] == list[i+1]:
           count+=1
    return count

print(occurance(sample_input_1) )
print(occurance(sample_input_2) )
print(occurance(sample_input_3) )
"""

#23

#creating a tuple 

"""sample_tuple_1 = ("Welcome Drink","Veg Starter","Non-Veg Starter",
                   "Veg Main Course","Non-Veg Main Course","Dessert")
print(sample_tuple_1)

print(sample_tuple_1[0])"""


#24

 	

"""crew_details= \
{ "Pilot":"Kumar",
"Co-pilot":"Raghav",
"Head-Strewardess":"Malini",
"Stewardess":"Mala" }

print(crew_details["Pilot"])
for key,value in crew_details.items():
    print(key,":",value)"""
    

#25


"""def proper_divisors(num):
    list1 =[]
    list2 =[]
    i=1
    while i*i<=num:
        if num%i==0:
            if i==1 or i*i == num:
                list1.append(i)
            else:
                list1.append(i)
                list2[:0] = [num//i]
        
        i+=1
    listf = list1+list2
    return listf

print(proper_divisors(220))    """

#26

# return fibonacci number

"""def generate_fibanacci(n):
    list1 = []
    if(n>=1):
        list1.append(0)
    if(n>=2):
        list1.append(1)
    if(n>=3):
        i=3
        while(i<=n):
            list1.append(list1[i-3] + list1[i-2])
            i+=1
    return list1


print(generate_fibanacci(1))
print(generate_fibanacci(2))
print(generate_fibanacci(15))"""


#27


"""
year = int(input("Enter the year    >>  ") )
print(year)

def isLeap (year):
    if (year %400 == 0):
        return True
    if (year % 100 == 0):
        return False
    if (year % 4 == 0):
        return True
    
if (isLeap(year)):
    print("%d is a leap year " %(year))
else:
    print("%d is not a leap year" %(year))
    
"""


"""def nexy_leap(year):
    rem = year%400
    rem = rem%4
    start_year = 0
    
    if (rem == 0):
        start_year = year
    else:
        start_year = year-rem+4
        
    i=1
    list1 = []
    while(i<=15):
        list1.append(start_year)
        start_year+=4
        i+=1
        
    return list1

print(nexy_leap(2000))
print(nexy_leap(2022))"""


#28

"""def encode (message):
    new_srt = ""
    length = len(message)
    i=1
    new_srt += message[0]
    count=1
    while(i<length):
        if(message[i-1]==message[i]):
            count+=1
        else:
            if(count==1):
                new_srt += message[i]
            else:
                new_srt+=str(count)
                count=1
                new_srt+=message[i]
                
        i+=1
        
    if(count!=1):
        new_srt+=str(count)
        
    return new_srt

print(encode("AAAA"))
print(encode("AAAABBBBCCCCCCCC"))"""


"""def encode (message):
    new_srt = ""
    length = len(message)
    i=0
    count=1
    while(i<length):
        if(i<(length-1)):
            if(message[i]==message[i+1]):
                count+=1
            else:
                if(count==1):
                    new_srt = new_srt + "1" + message[i]
                else:
                    new_srt+=str(count)
                    new_srt+=message[i]
                    count=1
                    
        else:
            if(message[i]==message[i-1]):
                new_srt+=str(count)
                new_srt+=message[i]
            else:
                new_srt = new_srt + "1"
                new_srt+=message[i]
                
                    
        i+=1    
            
    return new_srt

print("Hello")
print(encode("AAAA"))
print(encode("AAAABBBBCCCCCCCC"))"""


#29

"""def translate(b_dict,list_words):
    list1 = []
    for word in list_words:
        list1.append(b_dict[word])
        
    return list1

b_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
list_words = ["merry","christmas"]

print(translate(b_dict,list_words))
    """
    
#30

str = "the sun rises in the east"
list1 = str.split(" ")
print(list1)    
print(list1[0][::-1])