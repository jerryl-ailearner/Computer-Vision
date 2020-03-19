#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[4]:


img=cv2.imread('./Data/lena.png')


# In[6]:


cv2.imwrite('./Data/Lena_compressed.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])


# In[9]:


saved_img=cv2.imread('./Data/Lena_compressed.png')


# In[11]:


saved_img.all()==img.all()


# In[12]:


cv2.imwrite('./Data/Lena_compressed.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100])


# In[ ]:




