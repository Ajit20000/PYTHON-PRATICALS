#!/usr/bin/env python
# coding: utf-8

# In[1]:


# calculate P(spam/congr) given P(spam) = 0.3% , P(not spam) = 0.7%  P(congr/spam) = 0.75%, P(congr/not spam= 35%)
def bayes_law(p_s, p_c_given_s, p_c_given_not_s):
    #calculate p(not Spam)
    not_s = 1- p_s
    
    #calculate P(congratulations)
    p_c = p_c_given_s * p_s + p_c_given_not_s * not_s
    
    #calculate P(spam/congratulations)
    p_s_given_c = (p_c_given_s * p_s) / p_c
    
    return p_s_given_c

p_s = 0.30
p_c_given_s = 0.75
p_c_given_not_s = 0.35

result = bayes_law(p_s, p_c_given_s, p_c_given_not_s)
print('The probability of email being spam if it contains word congratulations is %.3f%%'% (result*100))


# In[3]:


#calculate P(A/B) given P(A)=0.02%, P(B/A)=85%, P(B/notA)

def bayes_law(p_a,p_b_given_a,p_b_given_not_a):
    #calculate p(not A)
    not_a = 1-p_a
    
    #calculate P(B)
    p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
    
    #calculate P(A/B)
    p_a_given_b = (p_b_given_a * p_a) / p_b
    
    return p_a_given_b

p_a = 0.0002
p_b_given_a = 0.85
p_b_given_not_a = 0.05

result = bayes_law(p_a,p_b_given_a,p_b_given_not_a)
print('P(A/B) = %.3f%%' % (result * 100))


# In[ ]:




