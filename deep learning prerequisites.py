#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
l=[1,2,3]
a=np.array([1,2,3])
for e in a:
    print(e)
for e in l:
    print(e)


# In[7]:


l.append(4)
l


# In[5]:


a.append(4)


# In[8]:


l=l+[5]
l


# In[10]:


l2=[]
for e in l:
    l2.append(e+e)
l2


# In[11]:


a+a


# In[12]:


2*a


# In[13]:


2*l


# In[14]:


np.sqrt(a)


# In[15]:


np.log(a)


# In[16]:


np.exp(a)


# In[20]:


a=np.array([1,2])
b=np.array([2,4])
dot=0
for e,f in zip(a,b):
    dot+=e*f
dot


# In[21]:


a*b


# In[22]:


np.sum(a*b)


# In[23]:


np.dot(a,b)


# In[24]:


a*b


# In[25]:


a.dot(b)


# In[27]:


amag=np.sqrt((a*a).sum())
amag


# In[28]:


amag=np.linalg.norm(a)
amag


# In[30]:


cosangle=a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b))
cosangle


# In[31]:


m=np.array([[1,2],[3,4]])
l=[[1,2],[3,4]]
l[0]


# In[32]:


l[0][0]


# In[33]:


m[0]


# In[34]:


m[0][0]


# In[35]:


m2=np.matrix([[1,2],[3,4]])
m2


# In[37]:


a=np.array(m2)
a


# In[39]:


a.T


# In[40]:


a


# In[41]:


b


# In[42]:


x=np.linalg.solve(a,b)
x


# In[46]:


import matplotlib.pyplot as plt
x=np.linspace(0,10,10)
y=np.sin(x)
plt.plot(x,y)
plt.show()
plt.plot(x,y)


# In[50]:


import pandas as pd
df=pd.read_csv('train.csv')


# In[51]:



df.shape


# In[52]:


M=df.as_matrix()
im=M[0,1:]
im.shape


# In[54]:


im=im.reshape(28,28)
im.shape


# In[55]:


plt.imshow(im)


# In[57]:


plt.show()


# In[58]:


M[0,0]


# In[59]:


plt.imshow(im,cmap='gray')


# In[60]:


plt.imshow(255-im,cmap='gray')


# In[63]:


x=[]
import numpy as np
for line in open('train.csv'):
    row=line.split(',')
    sample=map(float,row)
    x.append(sample)
    


# In[64]:


x


# In[65]:


X=np.array(x)
X.shape


# In[66]:


import pandas as pd
X=pd.read_csv('train.csv',header=None)
type(X)


# In[68]:


X.head(10)


# In[69]:


df=pd.DataFrame([[1,2],[3,4]])
df


# In[70]:


df.as_matrix()


# In[71]:


df.values


# In[72]:


from scipy.stats import norm
norm.pdf(0)


# In[74]:


norm.pdf(0,loc=5,scale=10)


# In[79]:


r=np.random.randn(10)
norm.logpdf(r)


# In[80]:


norm.logcdf(r)


# In[81]:


plt.show()


# In[82]:


r=10*np.random.randn(10000)+5


# In[ ]:




