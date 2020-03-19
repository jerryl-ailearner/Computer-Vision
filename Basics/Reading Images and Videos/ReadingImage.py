#!/usr/bin/env python
# coding: utf-8

# In[1]:


import argparse


# In[2]:


import cv2


# In[20]:


image_path=r"C:\Users\37197\Downloads\PGPAIML Projects\Computer Vision\Data\lena.png"


# In[21]:


img=cv2.imread(image_path)


# In[22]:


print('read {}'. format(image_path))


# In[23]:


print('shape:', img.shape)


# In[24]:


print('dtype:', img.dtype)


# In[25]:


img_grayscale=cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


# In[26]:


print('read {} as grayscale'.format(image_path))


# In[28]:


print('shape:', img.shape)


# In[29]:


print('dtype:', img.dtype)


# In[ ]:




