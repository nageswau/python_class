
# coding: utf-8

# In[2]:


l = [1,2,3, 5.5, 'python']


# In[3]:


l


# In[4]:


print l.append.__doc__


# In[6]:


print l.append('class')
print l


# In[7]:


print l.insert.__doc__


# In[8]:


print help(l.insert)


# In[9]:


l.insert(2, 'nag')


# In[10]:


print l


# In[11]:


print l.extend.__doc__


# In[12]:


a = [10,11,12]
l.extend(a)
print l


# In[13]:


l.extend(5)


# In[16]:


l.extend((5,7))


# In[17]:


for x in l:
    print x
print "exited from loop"


# In[18]:


a


# In[19]:


for x in a:
    b = x**2
    print b
print "existed from loop"


# In[20]:


for x in "python":
    print x


# In[21]:


for i in a:
    print a


# In[22]:


for i in a:
    print "nag"


# In[23]:


range(10)


# In[24]:


range(2,10)


# In[27]:


range(2,10,3)


# In[28]:


a


# In[29]:


a.append([1,2,3])
print a


# In[30]:


a[3]


# In[31]:


l


# In[32]:


print l.pop.__doc__


# In[33]:


print help(l.pop)


# In[34]:


l


# In[35]:


x = l.pop()
print x
print l


# In[36]:


print l.pop(2)
print l


# In[37]:


print l.remove.__doc__


# In[38]:


l.append(3)


# In[39]:


l


# In[40]:


l.remove(3)
print l


# In[41]:


l.remove(100)


# In[42]:


l.pop(100)


# In[43]:


l.pop(1,2)


# In[44]:


var = 10


# In[45]:


print var


# In[46]:


del var


# In[47]:


print var


# In[48]:


l


# In[49]:


del l[-1]


# In[50]:


print l


# In[51]:


a


# In[52]:


del a


# In[53]:


print a


# In[54]:


l


# In[55]:


l.count.__doc__


# In[56]:


print l.count('class')


# In[57]:


x = l.count('class')
print x


# In[58]:


l.count(100)


# In[59]:


l.index.__doc__


# In[60]:


l.index(5)


# In[61]:


l


# In[62]:


l.index(100)


# In[63]:


l.index.__doc__


# In[64]:


l


# In[65]:


l.index(2, 3)


# In[66]:


l.index(10, 3)


# In[68]:


l.index(10, 3, 7)


# In[69]:


l.append(10)


# In[70]:


l


# In[71]:


x = l.index(10)


# In[72]:


x


# In[73]:


x = l.index(10, x+1)


# In[74]:


print x


# In[75]:


l.pop(x)


# In[76]:


l.sort.__doc__


# In[77]:


l.sort()


# In[78]:


l


# In[79]:


l.append('Python')


# In[80]:


l


# In[81]:


l.sort()


# In[82]:


l


# In[83]:


l.reverse()


# In[84]:


l

