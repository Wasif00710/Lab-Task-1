print("Hello World!")
# sample comment 

name = "Wasif"
print(name) 

# An integer assignment
age = 22

# A floating point
Id = 1955

# A string
name = "Wasif"

print(name)
print(Id)
print(age)

x = "Hello World" # string
x = 50  # integer
x = 60.5  # float
x = 3j  # complex
x = ["Wasif", "Maruf", "Taufik"]  # list 
x = ("Taufik", "Wasif", "Maruf")  # tuple
x = {"name": "Zakir", "age": 24} # dict
x = {"Hello", "Every", "one"} # set
x = True  # bool
x = b"Number" # binary

# Python program show input and Output
val = input("Enter any number: ") 
print(val) 

#Multiple of two number
print('Enter Three numbers: ')
a, b ,c = input().split()
print('Output: ', a , '', b,'',c)
print('sum: ', int(a) + int(b)+int(c))

print('\n')

#If Statement
grade = 85

if grade >= 60:
    print('Passed')
    passed = True

   

#if..else Statement
grade = 85

if grade >= 60:
    print('Passed')
    passed = True
else:
    passed = False

#example No-2

i = 35
if (i < 50): 
    print("i is smaller than 50") 
    print("Invalid") 
else: 
    print("i is greater than 50") 
    print("Valid") 
print("Code is working, loading, ......") 

print('\n')

#if..elif..else Statement
grade = 77

if grade >= 90:
    print('A+')
elif grade >= 80:
    print('A')
elif grade >= 70:
    print('A-')
elif grade >= 60:
    print('B')
else:
    print('F')
 #Example no-2
a, b , c= input().split()
if  a > b:
    print(a, ' is number greater than ', b)
elif a < b:
    print(a, ' is number less than ', c)
else :
    print(a, ' is equals to ', b,'and',c)
    
print('\n')    

# while loop
print('Enter a number: ')
a = input()
a = int(a)
x = 1
print('numbers from 1 to ', a , 'are: ')
while x <= a:
    print(x, end=' ')
    x = x + 1

#Ex no-2    
count = 0
while (count < 5): 
    count = count + 1
    print("Hello 63_N")

    print('\n') 
 # break in while loop


print('Output of break and continue inside loop: ')
Fruits = ["Banana", "Berry", "Jackfruit", "Pineapple", "Blueberry", "Orange","Mango"]
for x in Fruits:
    print(x, end=' ')
    if x == "Pinapple":
        break

print('\n')


#continue in loop

Fruits = ["Banana", "Berry", "Jackfruit", "Pineapple", "Blueberry", "Orange","Mango"]
for x in Fruits:
    if x == "Jackfruit":
        continue
    print(x, end=' ')

print('\n')

# Range Function


for i in range(0, 60, 2): 
    print(i) 


print('\n') 


print('Range Function: ')
q = int(0)
print('Numbers from 1 to 20')
for x in range(20):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)

print('\n')   

print('Numbers from 30 to 60')
for x in range(30 , 60):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    
print('\n')    

print('Even Numbers from 10 to 100')
for x in range(10 , 100, 2):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    



print('Numbers from 100 to 50')
for x in range(100 , 50, -2):
    q = q + x
    print(x, end=' ')
print('Sum: ', q)
    
print('\n') 
a = 40
b = 10
add = a + b 
sub = a - b 
mul = a * b 
mod = a % b 
p = a ** b 
print(add) 
print(sub) 
print(mul) 
print(mod) 
print(p) 

print('\n') 

a = True
b = False
print(a and b) 
print(a or b) 
print(not a) 



print('\n') 


a = 10
b = a 
print(b) 
b += a 
print(b) 
b -= a 
print(b) 
b *= a 
print(b) 
b <<= a 
print(b)


print('\n') 



i = 20
if (i == 10): 
    print("i is 10") 
elif (i == 15): 
    print("i is 15") 
elif (i == 20): 
    print("i is 20") 
else: 
    print("Invalid") 



print('\n') 



def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
evenOdd(2)
evenOdd(3)   