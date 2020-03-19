#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2, numpy as np


# In[10]:


image=cv2.imread('./data/lena.png')


# In[11]:


image_to_show=np.copy(image)


# In[12]:


mouse_pressed=False


# In[13]:


s_x=s_y=e_x=e_y=-1


# In[14]:


def mouse_callback(event, x, y, flags, param):
    global image_to_show,s_x,s_y,e_x,e_y,mouse_pressed
    
    if event==cv2.EVENT_LBUTTONDOWN:
        mouse_pressed=True
        s_x,s_y=x,y
        image_to_show=np.copy(image)
        print("event button down: ",s_x,s_y)
        
    elif event==cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            image_to_show=np.copy(image)
            cv2.rectangle(image_to_show, (s_x, s_y), (x,y),(0,255,0),1)
        
    elif event==cv2.EVENT_LBUTTONUP:
        mouse_pressed=False
        e_x,e_y=x,y
        print("event button up: ", e_x,e_y)


# In[15]:


cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)


# In[8]:


while True:
    cv2.imshow('image', image_to_show)
    k=cv2.waitKey(1)
    if k==ord('c'):
        if s_y > e_y:
            s_y, e_y=e_y, s_y
        if s_x > e_x:
            s_x,e_x=e_x,s_x
        if e_y-s_y >1 and e_x-s_x>0:
            image=image[s_y:e_y,s_x:e_x]
            image_to_show=np.copy(image)
    elif k==27:
        break
        
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




