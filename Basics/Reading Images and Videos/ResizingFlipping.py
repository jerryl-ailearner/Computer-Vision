#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


image_path=r"C:\Users\37197\Downloads\PGPAIML Projects\Computer Vision\Data\lena.png"


# In[3]:


img=cv2.imread(image_path)


# In[4]:


print('Original image shape', img.shape)


# In[5]:


width, height=128, 256


# In[6]:


resized_img=cv2.resize(img, (width, height))


# In[7]:


print('resized to 128*256 image shape:', resized_img.shape)


# In[8]:


w_mult, h_mult=0.25, 0.5


# In[9]:


resized_mul_img=cv2.resize(img, (0,0), resized_img, w_mult,h_mult)


# In[10]:


print(resized_mul_img.shape)


# In[11]:


w_mult,h_mult=2,4


# In[12]:


resized_img=cv2.resize(img, (0,0), resized_mul_img,w_mult,h_mult, cv2.INTER_NEAREST)


# In[13]:


print(resized_img.shape)


# In[14]:


img_flip_x=cv2.flip(img,0)


# In[15]:


cv2.imshow('flip along x', img_flip_x)
cv2.waitKey(0)


# In[16]:


img_flip_y=cv2.flip(img, 1)


# In[17]:


cv2.imshow('flip along y', img_flip_y)
cv2.waitKey(0)


# In[18]:


img_flipped_xy=cv2.flip(img, -1)


# In[19]:


cv2.imshow('flip along xy',img_flipped_xy)
cv2.waitKey(0)


# In[ ]:




