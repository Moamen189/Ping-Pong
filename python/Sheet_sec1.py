#Name : Mo'men Ashraf Mohammed  
# 1- Numbers
#1Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.



print("Enter First Number: ")
numOne = int(input())
print("Enter Second Number: ")
numTwo = int(input())
res = numOne+numTwo
print("\nAddition Result = ", res)
res = numOne-numTwo
print("Subtraction Result = ", res)
res = numOne*numTwo
print("Multiplication Result = ", res)
res = numOne/numTwo
print("Division Result = ", res)
#----------------------------------
#Answer these 3 questions without typing code. Then type code to check your answer.
1-print(44)
2-print(29)
3-print(50)
#What is the type of the result of the expression 3 + 1.5 + 4?
float()
#-----------------------------------------

# Square root:√x

# Square:f(x)

#-------------------------------------------

#strings
#1-
s = 'hello'
# Print out 'e' using indexing
print(s[1])

#2-
## Reverse the string using slicing
s='hello'[::-1]
print(s)

#3-
#Given the string hello, give two methods of producing the letter 'o' using indexing.

s ='hello'
# Print out the 'o'

# Method 1:

print(s[4])

# Method 2:

print(s[-1])


#-----------------------------------------------------------------

#List


#Build this list [0,0,0] two separate ways


my_list = []
i = 0
for i in range(3):
  my_list.append(i)


  #-----------------------------------------------------
#Dictionaries

  #Using keys and indexing, grab the 'hello' from the following dictionaries:

  d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])

print(d2['k1']['k2'])

print(d3['k1'][0]['nest_key'][1][0])

#Can you sort a dictionary? Why or why not?
#yes to make a good arrange to strings or int

#Tuples 


#What is the major difference between tuples and lists?

#List : is just like the arrays
#Syntax:  
list_data = ['an', 'example', 'of', 'a', 'list']
#Tuple :is also a sequence data type that can contain elements of different data types
#Syntax:  
tuple_data = ('this', 'is', 'an', 'example', 'of', 'tuple')


#How do you create a tuple?
tuple = ('I Love data science for Python')
print(tuple)
#----------------------------------------------------------------------------------------

#Sets 
#Use a set to find the unique values of the list below:

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

#-------------------------------------------------------------------------------------

#Booleans


#What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)



# Answer before running cell
2 > 3
False
# Answer before running cell
3 <= 2
False
# Answer before running cell
3 == 2.0
False
# Answer before running cell
3.0 == 3
True
# Answer before running cell
4**0.5 != 2
True

#-------------------------------------------------------------

#Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']
True




