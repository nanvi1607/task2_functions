#!/usr/bin/env python
# coding: utf-8

# ## Registeration ID- SIRSS1005
# ## Name- Dhanisha Sharma
# ## College- Poornima University

# ## Q1. Write a lambda expression to extract first word of a string.
# 

# In[17]:


a=input("Enter a string:\n")
x=lambda a : a.split()[0]
x(a)


# ## Q2. Write a function to extract first word of s string (with many words separated by space)

# In[18]:


s='Chinese products should be banned fron India'
s.split()
def first_word(s):
    return s.split()[0]
first_word(s)


# ## Q3. Extract the first word from every string from a list of strings by using map function.

# In[20]:


a=['India is a secular country',
  'It is home for many different religious',
  'Culture and heritage makes us stand on global level']
list(map(lambda s:s.split()[0],a))


# ## Q4. Write a function to return a list of prime factors of a given number.

# In[22]:


def prime(Number):
    for i in range(2, Number + 1):
        if(Number % i == 0):
            isprime = 1
            for j in range(2, (i //2 + 1)):
                if(i % j == 0):
                    isprime = 0
                    break
            if (isprime == 1):
                print(" %d is a Prime Factor of a Given Number %d" %(i, Number))


# In[23]:


prime(100)


# ## Q5. Write a function that finds 2nd largest among 4 numbers (Repetitions are allowed, without sorting).

# In[14]:


def secondLargest(num1,num2,num3,num4):
    if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
        if (num2 >= num3) and (num2 >= num4):
               print('SecondLargest is:' ,num2)
        elif (num3 >= num2) and (num3 >= num4):
               print('SecondLargest is:' ,num3)
        else:
               print('SecondLargest is:' ,num4)

    elif (num2 >= num1) and (num2 >= num3) and (num2 >= num4):
        if (num1 >= num3) and (num1 >= num4):
               print('SecondLargest is:' ,num1)
        elif (num3 >= num1) and (num3 >= num4):
               print('SecondLargest is:' ,num3)
        else:
               print('SecondLargest is:' ,num4)
    
    elif (num3>=num1) and (num3>=num2) and (num3>=num4):
        if (num1 >= num2) and (num1 >= num4):
               print('SecondLargest is:' ,num1)
        elif (num2 >= num1) and (num2 >= num4):
               print('SecondLargest is:' ,num2)
        else:
               print('SecondLargest is:' ,num4)
                
    elif (num4>=num1) and (num4>=num2) and (num4>=num3):
        if(num1>=num2) and (num1>=num3):
            print('SecondLargest is:' ,num1)
        elif (num2 >= num1) and (num2 >= num4):
               print('SecondLargest is:' ,num2)
        else:
            print('SecondLargest is:' ,num3)


# In[15]:


secondLargest(8,9,97,7)


# In[ ]:




