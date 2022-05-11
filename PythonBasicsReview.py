#!/usr/bin/env python
# coding: utf-8

# <h2>Python Collections (Arrays) </h2>
# 
# There are four collection data types in the Python programming language:
# 
# <ol>
#     <li><b>List</b> is a collection which is ordered and changeable. Allows duplicate members.</li>
#     <li><b>Tuple</b> is a collection which is ordered and unchangeable. Allows duplicate members.</li>
#     <li><b>Set</b> is a collection which is unordered, unchangeable, and unindexed. No duplicate members.</li>
#     <li><b>Dictionary</b> is a collection which is ordered** and changeable. No duplicate members.</li>
# </ol>
#     
# Set items are unchangeable, but you can remove and/or add items whenever you like. <br>
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered. <br>
# 
# When choosing a collection type, it is useful to understand the properties of that type.<br>
# Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
#    

# <h2>Strings</h2>

# In[4]:


# Strings are Arrays 
a = "Hello, World!"
print(a[1])


# In[5]:


#Looping Through a String -----------
for x in "banana":
    print (x)


# In[6]:


#String Length ----------------
a = "JavaScript"
print(len(a))


# In[7]:


#Check String ----------
txt = "Best time ever"
print ("time" in txt)


# In[8]:


#Check if NOT --------------
txt = "Best time ever"
print ("time" not in txt)


# In[9]:


# Slicing -------------------
b= "Python is awesome!"
print (b[2:10])


# In[10]:


# Slice From the Start----------------------------
b = "Hello, World!"
print(b[ :5])


# In[11]:


# Slice To the End----------------------------
b = "Hello, World!"
print(b[2: ])


# In[12]:


# Negative Indexing----------------------------
b = "Hello, World!"
print(b[-5:-2])


# In[13]:


# Modify Strings - Upper Case----------------------------
a = "Hello, World!"
print(a.upper())


# In[14]:


# Modify Strings - Lower Case----------------------------
a = "Hello, World!"
print(a.lower())


# In[15]:


# Remove Whitespace ----------------------------
# strip() method removes any whitespace from the beginning or the end
a = "     Hello, World!      "
print(a.strip())


# In[16]:


# Replace String----------------------------
a = "Hello, World!"
print(a.replace("H", "X"))


# In[17]:


# Split String----------------------------
a = "Hello, World!"
print(a.split(","))


# In[18]:


# String Concatenation----------------------------
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# In[19]:


# combine strings and numbers by using the format() method!-----------
# The format() method takes the passed arguments, 
# formats them, and places them in the string 
# where the placeholders {} are
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# In[20]:


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# In[ ]:


# <!-- # Escape Character----------------------
# To insert characters that are illegal in a string, use an escape character.
# txt = "We are the so-called \"Vikings\" from the north."
# print (txt)

#   Code	    Result	
#   \'	    Single Quote	
#   \\	    Backslash	
#   \n	    New Line	
#   \r	    Carriage Return	
#   \t	    Tab	
#   \b	    Backspace

# Python Arithmetic Operators ---------------------
#   Operator	Name	            Example	
#   +	        Addition	        x + y	
#   -	        Subtraction	        x - y	
#   *	        Multiplication	    x * y	
#   /	        Division	        x / y	
#   %	        Modulus	            x % y	
#   **	        Exponentiation  	x ** y	
#   //	        Floor division	    x // y

# Python Assignment Operators---------------------
#       Operator	Example	    Same As	
#       =	        x = 5	    x = 5	
#       +=	        x += 3  	x = x + 3	
#       -=	        x -= 3  	x = x - 3	
#       *=	        x *= 3	    x = x * 3	
#       /=	        x /= 3	    x = x / 3	
#       %=	        x %= 3	    x = x % 3	
#       //=	        x //= 3	    x = x // 3	
#       **=	        x **= 3	    x = x ** 3	
#       &=	        x &= 3	    x = x & 3	
#       |=	        x |= 3	    x = x | 3	
#       ^=	        x ^= 3	    x = x ^ 3	
#       >>=	        x >>= 3	    x = x >> 3	
#       <<=	        x <<= 3	    x = x << 3


# Python Comparison Operators---------------------
#       Operator	        Name	                    Example
#       ==	            Equal	                    x == y	
#       !=	            Not equal	                x != y	
#       >	                Greater than	            x > y	
#       <	                Less than	                x < y	
#       >=	            Greater than or equal to	x >= y	
#       <=	            Less than or equal to	    x <= y

# Python Identity Operators--------------------------
#       Operator	    Description	Example	
#       is 	            Returns True if both variables are the same object	x is y	
#       is not	        Returns True if both variables are not the same object	x is not y

# Python Membership Operators-------------------------
#   Operator	    Description	                                                                            Example	
#   in 	            Returns True if a sequence with the specified value is present in the object	        x in y	
#   not in	        Returns True if a sequence with the specified value is not present in the object	    x not in y -->


# <h3>Lists (data type in Python used to store collections of data)</h3>
# List items are ordered, changeable, and allow duplicate values.<br>
# 
# <b>Ordered</b><br>
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.<br>
# If you add new items to a list, the new items will be placed at the end of the list.<br>
# 
# <b>Changeable</b><br>
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.<br>
# 
# <b>Allow Duplicates</b><br>
# Since lists are indexed, lists can have items with the same value<br>
# 

# In[21]:


thislist = ["apple", "banana", "cherry"]
print(thislist)


# In[22]:


# Append Items------------------------
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# In[41]:


# Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# In[40]:


# Extend List

thislist = ["apple1", "apple2", "apple3"]
tropical = ["mango1", "mango2", "mango3"]
thislist.extend(tropical)
print(thislist)


# In[39]:


# Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# In[38]:


# Remove Specified Index
# If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# In[37]:


# The del keyword also removes the specified index

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# In[35]:


# Delete the entire list

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)


# In[36]:


# Clear the List
# The clear() method empties the list.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# In[32]:


# Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# In[31]:


# Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# In[30]:


# Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# In[28]:


# Sort List Alphanumerically---------------------
# sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# In[27]:


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# In[26]:


# Sort Descending---------
# use the keyword argument reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


# In[29]:


# Case Insensitive Sort--------------
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


# In[24]:


# So if you want a case-insensitive sort function, use str.lower as a key function-----------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# <h2>List Methods</h2>
# Lists are created using square brackets [ ]

# In[ ]:


# Method	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()  	Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list


# <h2>Tuple Methods </h2>
# Tuples are written with round brackets ( ) <br>
# A set is a collection which is unordered, unchangeable*, and unindexed. <br>
# A tuple is a collection which is ordered and unchangeable.

# In[ ]:


# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


# <h2>Set </h2>
# Sets are written with curly brackets { } <br>
# Sets are used to store multiple items in a single variable.<br>
# A set is a collection which is unordered, unchangeable*, and unindexed.<br>
# * Note: Set items are unchangeable, but you can remove items and add new items.

# In[ ]:


# Method	                        Description
# add()	                            Adds an element to the set
# clear()	                        Removes all the elements from the set
# copy()	                        Returns a copy of the set
# difference()	                    Returns a set containing the difference between two or more sets
# difference_update()	            Removes the items in this set that are also included in another, specified set
# discard()	                        Remove the specified item
# intersection()	                Returns a set, that is the intersection of two other sets
# intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                    Returns whether two sets have a intersection or not
# issubset()	                    Returns whether another set contains this set or not
# issuperset()	                    Returns whether this set contains another set or not
# pop()	                            Removes an element from the set
# remove()                          Removes the specified element
# symmetric_difference()	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    inserts the symmetric differences from this set and another
# union()	                        Return a set containing the union of sets
# update()	                        Update the set with the union of this set and others


# <h2>Python Dictionaries</h2><br>
# Dictionaries are used to store data values in key: value pairs.<br>
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.<br>
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.<br>
# Dictionaries are written with curly brackets, and have keys and values.<br>
# Dictionaries cannot have two items with the same key.<br>
# Duplicate values will overwrite existing values.<br>
# 

# In[ ]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

