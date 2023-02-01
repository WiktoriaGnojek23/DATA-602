#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95

# Get the test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
''' added test3'''
test3 = int(input('Enter the score for test 3: '))
# Calculate the average test score.
''' added parenthesis around first portion of function'''
average = (test1 + test2 + test3) / 3
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
''' changed to capital - variable name has to be identical'''
if average >= HIGH_SCORE:
    print('Congratulations!')
    '''need indent to be in the same command'''
    print('That is a great average!')
    
#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

''' define the length and width of both rectangles'''
''' I added int infront of input function because since when I initially ran it without I got 
this error; can't multiply sequence by non-int of type str'''

l_1 = int(input('Please enter the length of triangle 1: '))
w_1 = int(input('Please enter the width of triangle 1: '))

''' define area function 1'''

a_1 = l_1 * w_1

l_2 = int(input('Please enter the length of triangle 2: '))
w_2 = int(input('Please enter the width of triangle 2: '))

''' define area function 2'''

a_2 = l_2 * w_2

''' print output'''

print(a_1)
print(a_2)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

''' asking user for name and age using different classes of data types'''
age = int(input('Please provide your age: '))
name = str(input('Please provide your name: '))

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

'''Print out statment with variable inputs using an f-string'''
print(f"Happy birthday, {name}!  You are {age} years old today!")

