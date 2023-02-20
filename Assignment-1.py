#!/usr/bin/env python
# coding: utf-8

# Q1. What are the characteristics of the tuples? Is tuple immutable?
# 1-Tuples are immutables.
# 2-Tuples are Ordered
# 3-Tuples allows duplicates.
# 
# Tuple is immutable we can't change the values inside tuple so it can used where we don't want to change the value or memory.
# 

# Q2. What are the two tuple methods in python? Give an example of each method. Give a reason why
# tuples have only two in-built methods as compared to Lists.
# 
# Answer:-
# 2 tuple methods are count and index.
# 1)count:-
# count is used to count number of elements with perticular value.
# Example:-
# Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# print(Tuple1.count(3))
# We can change the count(value) and get the result.
# with
# 2)Index:-
# In-order to find perticular index of the element we can use Index method.
# Example:-
# Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# print(Tuple1.index(1))
# 
# Reason Behind only 2 methods is that Tuple is immutable we can perform update,delete operations on tuple.
# 

# In[5]:


#Q3. Which collection datatypes in python do not allow duplicate items? Write a code using a set to remove duplicates from the given list.
#List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]

#Set is the data type that don't allow any types of duplicates
List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
Set1=set(List)
print(Set1)



# In[12]:


#Q4. Explain the difference between the union() and update() methods for a set. Give an example of each method.

#1)Union():-
#The union() method returns a set that contains all items from the original set, and all items from the specified set(s).
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))

#2)Update():-
#The update() method updates the current set, by adding items from another set (or any other iterable).
set1={1,2,3}
set2={3,4,5,6}
set2.update(set1)
print(set2)


# Q5. What is a dictionary? Give an example. Also, state whether a dictionary is ordered or unordered.
# Answer:-
# Dictionary is collection of key and value pairs.
# Dic={"Name":"Omkar","Surname":"Chavan","pincode":"41xx24"}
# 
# As per version of python 3.7 Dictionary is ordered but for earlier versions it's not ordered.
# 

# Q6. Can we create a nested dictionary? If so, please give an example by creating a simple one-level
# nested dictionary.
# Answer:-
# Yes we can create Nested Dictionary.
# Example:-
# Dict={"Details":{"Name":"Omkar","Surname":"Chavan","pincode":"41xx24"}}

# In[15]:


#Q7. Using setdefault() method, create key named topics in the given dictionary and also add the value of
#the key as this list ['Python', 'Machine Learning’, 'Deep Learning']

#Answer:-
#The setdefault() method returns the value of the item with the specified key.
#If the key does not exist, insert the key, with the specified value, see example below

dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}
x=dict1.setdefault("Topics",['Python', 'Machine Learning', 'Deep Learning'])
print(dict1)


# In[18]:


#Q8. What are the three view objects in dictionaries? Use the three in-built methods in python to display
#these three view objects for the given dictionary.
#dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}
#keys() method is used to find the keys within dictionary.
print(dict1.keys())
#values() method is used to find values of dictionary or perticular value of a key

print(dict1['Sport'])
print(dict1['Teams'])

#items() method is used to return the list with all dictionary keys with values

print(dict1.items())

