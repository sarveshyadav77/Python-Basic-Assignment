#!/usr/bin/env python
# coding: utf-8

# Q_1 In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 
# #   * 
# # 'hello'
# # -87.8
# # - 
# # / 
# # +	
# # 6 
# 

# Values = -87.7, 6, "Hello"

# Expressions = *, -, / ,+

# ## Q2. What is the difference between string and variable?
# 
# Variable is name of location where you store string and values where as string is any thing which is written inside the quotes.
# 

# ## Q3. Describe three different data types.
# 
# 1-Text Type:	str,
# 2- Numeric Types:	int, float, complex,
# 3- Sequence Types:	list, tuple, range,
# 4- Mapping Type:	dict,
# 5- Set Types:	set, frozenset,
# 6- Boolean Type:	bool,

# ## Q4. What is an expression made up of? What do all expressions do?
# Expression is made up of operand and its operator which are assign to produce some output.
# Expressions are representation of values, strings is also expression. 
# 

# ## Q5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# Expression always evaluate a values while statements does something like creating a variable.

# ## Q6. After running the following code, what does the variable bacon contain?
# ##### bacon = 22
# ##### bacon + 1
# 

# In[2]:


bacon = 22
bacon + 1


# ## Ans6: 23

# ## Q7. What should the values of the following two terms be?
# ##### 'spam' + 'spamspam'
# ##### 'spam' * 3
# 

# In[4]:


'spam' + 'spamspam'


# In[5]:


'spam' * 3


# ## Ans7: 'spamspamspam'

# ## Q8. Why is eggs a valid variable name while 100 is invalid? 
# 
# Variable name can't start with numeric value it can start with alpha- numeric 

# ## Q9. What three functions can be used to get the integer, floating-point number, or string version of a value?
# For integer it will be int, for floating-point it will be float, and for string it will be str.

# ## Q10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
# #### Ans: We can not concatenate str with int(99). for fixing this we can change 99 in to str(99).

# In[7]:


'I have eaten ' + str(99) + ' burritos.'


# In[ ]:




