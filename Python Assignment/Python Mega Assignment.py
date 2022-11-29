# Assignment Part-1
# Q1. Why do we call Python as a general purpose and high-level programming language?

# Q2. Why is Python called a dynamically typed language?

# Q3. List some pros and cons of Python programming language?

# Q4. In what all domains can we use Python?

# Q5. What are variable and how can we declare them?

# Q6. How can we take an input from the user in Python?

# Q7. What is the default datatype of the value that has been taken as an input using input() function?

# Q8. What is type casting?

# Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

# Q10. What are keywords?

# Q11. Can we use keywords as a variable? Support your answer with reason.

# Q12. What is indentation? What's the use of indentaion in Python?

# Q13. How can we throw some output in Python?
# A13. Using Print statement

# Q14. What are operators in Python?

# Q15. What is difference between / and // operators?

# Q16. Write a code that gives following as an output.
# iNeuroniNeuroniNeuroniNeuron
# A16.
#print("iNeuron"*4)

# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
# A17.
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(number,"is Even")
# else:
#     print(number,"is Odd")

# Q18. What are boolean operator?

# Q19. What will the output of the following?
# A19.
# 1 or 0
#print(1 or 0) 
#output = 1

# 0 and 0
#print(0 and 0)
#output = 0

# True and False and True
#print(True and False and True)
#output = False

# 1 or 0 or 0
#print(1 or 0 or 0)
#output = 1

# Q20. What are conditional statements in Python?


# Q21. What is use of 'if', 'elif' and 'else' keywords?

# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
# A22.
# age = int(input("Enter Age: "))
# if age >= 18:
#     print("I can vote")
# else:
#     print("I can't vote")

# Q23. Write a code that displays the sum of all the even numbers from the given list.
# numbers = [12, 75, 150, 180, 145, 525, 50]
# A23.
# numbers = [12, 75, 150, 180, 145, 525, 50]
# even_sum = 0
# for i in numbers:
#     if i % 2 == 0:
#         even_sum += i
# print(even_sum)

# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
# A24.
# number_1 = int(input("Enter Number 1: "))
# number_2 = int(input("Enter Number 2: "))
# number_3 = int(input("Enter Number 3: "))
# if number_1 > number_2 and number_1 > number_3:
#         print("Number 1: ",number_1," is Greatest")
# else:
#     if number_2 > number_3:
#         print("Number 2: ",number_2," is Greatest")
#     else:
#         print("Number 3: ",number_3," is Greatest")

# Q25. Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# A25. 
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 500:
#         break
#     else:
#         if i % 5 == 0:
#             if i > 150:
#                 continue
#             print(i)

# Q26. What is a string? How can we declare string in Python?

# Q27. How can we access the string using its index?
# A27.
#syntax string[index]

# Q28. Write a code to get the desired output of the following
# string = "Big Data iNeuron"
# desired_output = "iNeuron"
# A28.
# string = "Big Data iNeuron"
# desired_output = string[9:]
# print(desired_output)

# Q29. Write a code to get the desired output of the following
# string = "Big Data iNeuron"
# desired_output = "norueNi"
# A29.
# string = "Big Data iNeuron"
# desired_output = string[-1: 8 : -1]
# print(desired_output)

# Q30. Resverse the string given in the above question.
# A30.
# string = "Big Data iNeuron"
# print(string[-1: : -1])

# Q31. How can you delete entire string at once?
# A31.
# string = "string"
# print(string)
# del string
# print(string)

# Q32. What is escape sequence?

# Q33. How can you print the below string?
# 'iNeuron's Big Data Course'
# A33.
#print("'iNeuron's Big Data Course'")

# Q34. What is a list in Python?

# Q35. How can you create a list in Python?

# Q36. How can we access the elements in a list?

# Q37. Write a code to access the word "iNeuron" from the given list.
# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
# A37.
# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
# print(lst[4][2])

# Q38. Take a list as an input from the user and find the length of the list.
# A38.
# def len_list(enter_list):
#     print("length of list is: ",len(enter_list))

# len_list([1,2,3,"cute",["unicorn",2],99])

# Q39. Add the word "Big" in the 3rd index of the given list.
# lst = ["Welcome", "to", "Data", "course"]
# A39.
# lst = ["Welcome", "to", "Data", "course"]
# lst[2]= "Big"
# print(lst)

# Q40. What is a tuple? How is it different from list?

# Q41. How can you create a tuple in Python?

# Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

# Q43. Can two tuple be appended. If yes, write a code for it. If not, why?

# Q44. Take a tuple as an input and print the count of elements in it.
# A44.
# Lista = []
# elements = int(input("Enter number of elements: "))
# for i in range(elements):
#     Lista.append(input("Enter element"))
# print(Lista,type(Lista))
# Tuplea= tuple(Lista)
# print(Tuplea,type(Tuplea),"count of elements: ",len(Tuplea))

# Q45. What are sets in Python?


# Q46. How can you create a set?

# Q47. Create a set and add "iNeuron" in your set.
# A47.
# set_a = set()
# set_a.add("iNeuron")
# print(set_a)

# Q48. Try to add multiple values using add() function.
# A48.
# set_a = set()
# set_a.add("iNeuron")
# set_a.update({"koko"})
# print(set_a)

# Q49. How is update() different from add()?

# Q50. What is clear() in sets?
# A50.
# set_a = {1,2,3}
# print(set_a)
# set_a.clear()
# print(set_a)

# Q51. What is frozen set?

# Q52. How is frozen set different from set?

# Q53. What is union() in sets? Explain via code.
# Q53.
# set_a = {1,2,3,4}
# set_b = {4,5,6,7}
# union = set_a.union(set_b)
# print(union)
# Q54. What is intersection() in sets? Explain via code.
# A54.
# set_a = {1,2,3,4}
# set_b = {4,5,6,7}
# intersection = set_a.intersection(set_b)
# print(intersection)

# Q55. What is dictionary ibn Python?

# Q56. How is dictionary different from all other data structures.

# Q57. How can we delare a dictionary in Python?


# Q58. What will the output of the following?
# var = {}
# print(type(var))
# A58.
#output= <class 'dict'>

# Q59. How can we add an element in a dictionary?

# Q60. Create a dictionary and access all the values in that dictionary.

# Q61. Create a nested dictionary and access all the element in the inner dictionary.

# Q62. What is the use of get() function?

# Q63. What is the use of items() function?

# Q64. What is the use of pop() function?

# Q65. What is the use of popitems() function?

# Q66. What is the use of keys() function?

# Q67. What is the use of values() function?

# Q68. What are loops in Python?

# Q69. How many type of loop are there in Python?

# Q70. What is the difference between for and while loops?

# Q71. What is the use of continue statement?

# Q72. What is the use of break statement?

# Q73. What is the use of pass statement?

# Q74. What is the use of range() function?

# Q75. How can you loop over a dictionary?

# Coding problems
# Q76. Write a Python program to find the factorial of a given number.

# Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100

# Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

# Q79. Write a Python program to check if a number is prime or not.

# Q80. Write a Python program to check Armstrong Number.

# Q81. Write a Python program to find the n-th Fibonacci Number.

# Q82. Write a Python program to interchange the first and last element in a list.

# Q83. Write a Python program to swap two elements in a list.

# Q84. Write a Python program to find N largest element from a list.

# Q85. Write a Python program to find cumulative sum of a list.

# Q86. Write a Python program to check if a string is palindrome or not.

# Q87. Write a Python program to remove i'th element from a string.

# Q88. Write a Python program to check if a substring is present in a given string.

# Q89. Write a Python program to find words which are greater than given length k.

# Q90. Write a Python program to extract unquire dictionary values.

# Q91. Write a Python program to merge two dictionary.

# Q92. Write a Python program to convert a list of tuples into dictionary.

# Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
# Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.

# Input: list = [9, 5, 6]
# Output: [(9, 729), (5, 125), (6, 216)]
# Q94. Write a Python program to get all combinations of 2 tuples.

# Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
# Q95. Write a Python program to sort a list of tuples by second item.

# Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
# Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
# Q96. Write a python program to print below pattern.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# Q97. Write a python program to print below pattern.

#     *
#    **
#   ***
#  ****
# *****
# Q98. Write a python program to print below pattern.

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# Q99. Write a python program to print below pattern.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# Q100. Write a python program to print below pattern.

# A 
# B B 
# C C C 
# D D D D 
# E E E E E 