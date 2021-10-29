#!/usr/bin/env python
# coding: utf-8

# # Eg 1

# In[1]:


#probability of getting 3 when a die is rolled
ns = 6 #n(S) = {1,2,3,4,5,6}
na = 1 #n(A) = {3}
pa = na / ns #P(A)
print("probablity of getting 3 is:",pa)


# # probability of atleast getting one head when a coin is tossed thrice

# In[2]:


ns = 8 #n(S) = {HHH,HHT,HTH,THH,TTH,THT,HTT,TTT}
na = 7 #n(A) = {HHH,HHT,HTH,THH,TTH,THT,HTT}
pa = na /ns #P(A)
print("probability of getting atleast one head is:",pa)


# In[1]:


# A glass jar contains 5 red, 3 blue and 2 green jelly
# beans.  If a jelly bean is chosen at random from the jar,
# what is the probability that it is not blue?

ns = 10
na = 7
pa = na / ns
print("probability of getting not blue jellybean is : ", pa)


# In[2]:


# Independent and Dependent Eventsx


# In[3]:


# If the probability that person A will be alive in 20 years and the probability that person B will be alive in 20 years
# is 0.5, what is the probability that they will both be alive in 20 years
p = 0.7 * 0.5
print("probability that they will be alive after 20 years: ", p)


# In[8]:


def event_probability(n,s):
    return n/s


# In[9]:


# A fair die is tossed twice. Find the probaility of getting a 4 or 5 on the first toss and a 1, 2, or 3 in the second toss
pa = event_probability(2,6)
pb = event_probability(3,6)
p = pa * pb
print("probability of getting a 4 or 5 on the first toss and a 1, 2, or 3 in the second toss: ", p)


# In[10]:


# A bag contains 5 white marbles, 3 black marbles and # 2 green marbles. In each draw, a marble is drawn from
# the bag and not repeated. In three draws, find the # Probability of obtaining white, black and green in that order.
pw = event_probability(5, 10)
pb = event_probability(3, 9)
pg = event_probability(2, 8)
print("Probability of obtaining white, black and green in that order: ", pw*pb*pg)


# In[12]:


# Sample space
cards = 52

# Calculate the probability of drawing a heart or a club
hearts = 13
clubs = 13
heart_or_club = event_probability(hearts, cards) + event_probability(clubs, cards)
print(heart_or_club)


# In[13]:


# Calculate the probability of drawing an ace, king or a queen
cards = 52
aces = 4
kings  = 4
queens = 4
ace_king_or_queen = event_probability(aces, cards) + event_probability(kings, cards) + event_probability(queens, cards)
print(ace_king_or_queen)


# In[14]:


# Calculate the probability of drawing a heart or an ace
hearts = 13
aces = 4
ace_of_hearts = 1
heart_or_ace = event_probability(hearts, cards) + event_probability(aces, cards) - event_probability(ace_of_hearts, cards)
print(round(heart_or_ace, 1))


# In[15]:


# Calculate the probability of drawing red cards or a face cards
red_cards = 26
face_cards = 12
red_face_cards = 6
red_or_face = event_probability(red_cards, cards) + event_probability(face_cards, cards) - event_probability(red_face_cards, cards)
print(round(red_or_face, 1))


# In[16]:


# Complement of the events


# In[17]:


# probability of not getting 5 when a fair die is rolled
ns = 6
na = 1
pa = na / ns
print("probability of not getting 5 is : ", 1 - pa)


# In[18]:


# Conditional probability
import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\Sujit\\Downloads\\student-mat.csv')


# In[19]:


df.head()


# In[20]:


len(df)


# In[21]:


df.columns


# In[22]:


print(df['G3'].max())
print(df['G3'].min())


# In[23]:


df['grade_A'] = np.where(df['G3']*5 >= 80, 1, 0)


# In[24]:


df['high_absences'] = np.where(df['absences'] >= 10, 1, 0)


# In[25]:


df.head()


# In[26]:


df['count'] = 1


# In[27]:


df = df[['grade_A', 'high_absences', 'count']]
df.head()


# In[28]:


final = pd.pivot_table(
df, 
values='count', 
index=['grade_A'],
columns=['high_absences'],
aggfunc=np.size,
fill_value=0)


# In[29]:


final


# # Calculate the probability the student will get grade A given that missing 10 or more classes
# 
# P(A) = (35+5)/(277+78+35+5) = 0.02658
# P(B) = (78+5)/(277+78+35+5) = 0.210
# P(A or B) = 5/ (277+78+35+5) = 0.0126
# 
# P(A|B) = P(A Or B) / P(B) = 0.060 
# The probability of getting at least an 80% final grade, given missing 10 or more classes is 6%.
# 

# In[33]:


pa = (35+5)/(277+78+35+5)
print(pa)
pb = (78+5)/(277+78+35+5)
print(pb)
a_or_b = 5/(277+78+35+5)
print((a_or_b))


# In[35]:


a_given_b = (a_or_b)/(pb) 
print(a_given_b)


# # PERMUTATION AND COMBINATORICES

# # WITH REPETITION

# In[1]:


import itertools
from itertools import product 
box_1 = ['g','b']
perm = []
for p in itertools.product (box_1, repeat = 2):
    perm.append(p)
    
perm


# LETS DO THE SAME INSTEAD OF 3 BALLS

# In[2]:


import itertools
from itertools import product 
box_2 = ['g','b','y']
perm = []
for p in itertools.product (box_2, repeat = 3):
    perm.append(p)
    
perm


# # WITHOUT REPETITION

# In[3]:


import itertools

box_1 = ['g','b']
perm = itertools.permutations(box_1)

for i in list(perm):
    print(i)


# In[4]:


import itertools

box_1 = ['g','b','y']
perm = itertools.permutations(box_1)

for i in list(perm):
    print(i)


# # VARIATION WITH REPETITION

# V(n,k) = nn........(k times) = n^k

# In[5]:


box_2 = ['g','b','y']
perm=[]
for p in itertools.product(box_2,repeat=2):
    perm.append(p)
    
perm


# In[6]:


box_2 = ['g','b','y','r']
perm=[]
for p in itertools.product(box_2,repeat=3):
    perm.append(p)
    
perm


# # VARIATION WITHOUT REPETITION

# V(n,k) = n!/(n-k)!

# In[7]:


box_2 = ['g','y','r']
perm = itertools.permutations(box_2,2)

for i in list(perm):
    print(i)


# # COMBINATIONS WITH REPETITION:

# The number of possible combinations (with repetition) is given by:
# 
# C(n,k) = (n+k-1)!/k!(n-1)!

# In[8]:


from itertools import combinations_with_replacement

box_1 = ['g','b']
comb = combinations_with_replacement(box_1,2)


for i in list(comb):
    print(i)


# In[9]:


from itertools import combinations_with_replacement

box_1 = ['g','b','y','r']
comb = combinations_with_replacement(box_1,2)


for i in list(comb):
    print(i)


# # COMBINATIONS WITHOUT REPETITION:

# The number of possible combinations (with repetition) is given by:
# 
#  C(n,k) = n!/k!(n-1)!

# In[10]:


from itertools import combinations

box_1 = ['g','b','y']
comb = combinations(box_1,2)


for i in list(comb):
    print(i)


# In[ ]:




