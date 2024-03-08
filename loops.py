#WHILE LOOP

#Ex-1 print 1 to 10 using while loop

'''i=1
while i<=10:
    print(i)
    i+=1
print('done')'''

'''Ex-2 print following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5'''

'''i=1
while i<=5:
    print(f"{i} "*i)
    i+=1
print("done")'''

''' Ex-3 Print following pattern
*
**
***
****
*****'''

'''i=1
while i<=5:
    print('*'*i)
    i+=1'''

''' Ex-4 Print following pattern
     *
    * *
   * * *
  * * * *
 * * * * * '''

'''i=1
j=5
while i<=5 and j>=1:
    print(' '*j + '* '*i)
    i+=1
    j-=1
print('done')'''

#Ex-5 Guess game- ask the user a number b/w 1-10 and check if the number is the secret number.

'''secret_number=6
num=int(input("Guess the secret number between 1-10: "))

while num!=secret_number:
    num=int(input("Bad luck! Try another number: "))
print("Congratulations! You guessed the correct number.")'''

# FOR loop
#Ex-6 For loop for string

'''for item in "PYTHON":
    print(item)'''

#Ex-7 for loop for list

'''for item in [10,20,'john','josh']:
    print(item)
'''
#Ex-8 for loop with range function

'''for i in range(10):
    print(i)'''

#Ex-9 Print all even numbers between 0 to 20
'''for i in range(0,21,2):
    print(i)'''

for i in range(0,21):
    if i%2==0:
        print(i)
    else:
        continue


