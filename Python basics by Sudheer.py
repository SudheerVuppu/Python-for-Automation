#!/usr/bin/env python
# coding: utf-8

# # Printing a Python code

# In[93]:


print("welcome to the world of Programming language @ Python Crash Course")


# # declaring a variable

# In[2]:


a = 13
b = 14
c = a+b
print(c)


# # knowing what type of data types using type()

# In[13]:


print(type(a))
print(type(b))
print(type(c))


# # declaring a multiple variable at one time 

# In[6]:


a , b , c = 1 , 22.2 , 'abc' 
##note you will have to denote " " or ' ' for declaing a string & no need for defining a data type infront
#and not applicable for int
print(a)
print(b)
print(c)


# In[7]:


print(a,b,c)


# In[8]:


print(a,b, "value is" c)


# # Printing string and and int combining using     "{}{}".format()

# In[15]:


print(a,b, "value is" c)

##we can concatinate with same data-types but not differant data types


# In[11]:


print("{} {}".format("value is",c))


# # Data types in Python 

# #  Data-types are 5 different which python defines they are as follows
# #    1. Numeric 
# #    2. String
# #    3. List (MUTABLE)
# #    4. Tuple (IMMUTABLE)
# #    5. Dictionary

# # For more details go to this page https://www.journaldev.com/14036/python-data-types

# # 1. Numeric

# In[16]:


# Types in numeric
# 1. int() 100,1,0,122...etc
# 2. long() mostly usind in Python 2X and deprecated in 3x 
# 3. float() 10.1, 12.25,2.2,0.25,2.222222,...etc 
# 4. complex() 4j , 100+3j, alpha-numeric...etc


# # 2. String

# In[31]:


#using string
firstname = "Prince"
lastname = "Staring"


# # Concatinating using of two strings with "," and "+" and .format

# In[32]:


name = firstname + lastname
print(name)


# In[34]:


print(firstname,lastname)


# In[35]:


print(firstname+lastname)


# In[36]:


print("{}{}".format(firstname,lastname))


# # declaring a variables 
# ## 1.there should be no spaces and should not start with numbers when using alpha numeric.
# ## 2.can start with underscore(_),alpha(AtoZ) but not start with numbers and no spaces 

# In[30]:


first name = "Prince"
last name = "Staring"


# # 3.List[]  Mutable

# ### 1.List is the values which allows multiple data-types and multiple values
# ### 2.These are declared in square brackets[]
# ### 3.The index values are started with value 0 as first index
# ### 4.For printing the last values in the list we can use -1 values[-1]
# ### 5.For printing the specific values then we can use  values[start index : endindex+1]
# ### 6.Inserting the values in the list using command insert values.insert(3,"johnny")
# ### 7.For adding a values in the list using .append , it will insert values in the end
# ### 8. For updating the values in the array we can use values = "index which we want to update"
# ### 9. for deleting the values we can use del function so del values["which we want to del"]

# ### 1.List is the values which allows multiple data-types and multiple values

# In[39]:


values = [1,"sudheer",32,"john",3.2,-12]
print(values)


# ## 3.The index values are started with value 0 as first index

# In[40]:


values[0]


# In[41]:


values[1]


# In[42]:


values[3]


# ## 4.For printing the last values in the list we can use -1 values[-1]

# In[43]:


values[-1]


# In[44]:


values[-2]


# In[45]:


values[-3]


# ## 5.For printing the specific values then we can use values[start index : endindex+1]

# In[46]:


values = [1,"sudheer",32,"john",3.2,-12]
values[1:4]


# In[47]:


values[0:5]


# ## 6.Inserting the values in the list using command insert values.insert(3,"johnny")

# In[49]:


values.insert(2,"johnny")
values


# In[50]:


values.insert("priya")
values
# because values have to insert index places


# In[51]:


values.insert(4,"priya")
values


# ## 7.For adding a values in the list using .append , it will insert values in the end

# In[52]:


values.append("Samantha")# this will append values in the last place of the values
values


# ## 8. For updating the values in the array we can use values = "index which we want to update"

# In[53]:


values[2] = "SUDHEER"
values


# ### 9. for deleting the values we can use del function so del values["which we want to del"]

# In[55]:


del values[2]
values


# In[56]:


print(values)


# # 4.Tuple() IMMUTABLE where updatation is not possible

# ### 1. First they are immutable that means once a variable is created it cannot update
# ### 2. they are denoted by the symbol brackets ()
# ### 3. every thing as sets operation is done in tuple except the updation rest all same
# ### 4. this is used only when there should be no change in any test case scenerio

# In[57]:


value = (1,2.2,"Sudheer")
value


# # 5.Dictionaries {key:value}

# ### 1. Dictionary are represented by the key and value
# ### 2. when ever you want to use string make sure keep in double quotes"" and for int is nothing
# ### 3. once a value is assigned for a key cannot be updated
# ### 4. a key is assaigned to a value 

# ### 1. Dictionary are represented by the key and value

# In[60]:


dic = {"name": "Sudheer", a: 25 , b: "apple"}
dic


# In[64]:


dic[a]


# In[65]:


dic[b]


# In[66]:


dic["name"]


# # if and elif and conditons 

# ### 1. Equals: a == b
# ### 2. Not Equals: a != b
# ### 3. Less than: a < b
# ### 4. Less than or equal to: a <= b
# ### 5. Greater than: a > b
# ### 6. Greater than or equal to: a >= b

# ### 1. Equals: a == b

# In[67]:


a = 33
b = 200
if b > a:
  print("b is greater than a")


# ### elif

# In[71]:


a = 20
b = 31
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
    print("b is less than a")


# ### Short Hand If

# In[72]:


if a > b: print("a is greater than b")


# ### Short Hand If ... Else

# In[73]:


a = 2
b = 330
print("A") if a > b else print("B")


# # Functions

# ### 1.Functions is a group of related statements that perform a specific task
# ### 2.def is the keyword to represent to a function 
# ### 3.in function we use parameter and name
# ### 4.we can use n number of parameters

# In[84]:


def greet(name):
    print("GoodMorning " + name)


# In[85]:


greet("Sudheer")


# In[86]:


def addition(a,b):
    print(a+b)


# In[88]:


addition(20,30)


# # OOPS concept object oriented programming language

# ##### 1.Classes are know as user defined blueprint or prototype.
# ##### 2.in classes we have methods, class variables , instance variables and constructor etc.
# ##### 3.There are two types of variables in class oops concept ie 1.instance variables and  2.class variables.
# ##### 4.Class variables are those which are defined inside the class is called class variables, we can use n number of variables in class.
# ##### 5.Instance variables are those which are defined inside the constructor is called instance variables,we can create but it differs from variable.
# ##### 6.How many arguments you are using in class those many arguments have to use in constructor. or else it will show us an error.
# ##### 7.self keyword is mandatory for calling variable names in method
# ##### 8.instance and class has whole different purpose
# ##### 9.Constructor name should be __init__
# ##### 10.new keyword is not requird when you want to create a new object

# # Inheritance

# In[ ]:


###### 1. it is noting but acquiring the object of parent class
###### 2. 

