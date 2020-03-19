#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2, random


# In[7]:


image=cv2.imread('./Data/lena.png')


# In[8]:


w,h=image.shape[1], image.shape[0]


# In[10]:


def rand_pt(mult=1.):
    return(random.randrange(int(w*mult)), random.randrange(int(h*mult)))


# In[37]:


img_circle=cv2.circle(image, rand_pt(), 40, (255,0,0))
img_bluepoint=cv2.circle(image, rand_pt(), 5, (255,0,0), cv2.FILLED)
img_sharpedges=cv2.circle(image, rand_pt(), 15, (255,0,0), 6)
img_lightborders=cv2.circle(image, rand_pt(), 40, (255,0,0), cv2.LINE_AA)


# In[43]:


img_line=cv2.line(image, rand_pt(), rand_pt(), (0, 255, 0))
img_line_thick=cv2.line(image, rand_pt(), rand_pt(), (85, 255, 85), 3)
img_line_aa=cv2.line(image, rand_pt(), rand_pt(), (255, 170, 170), 2, cv2.LINE_AA)


# In[49]:


img_arrowline=cv2.arrowedLine(image, rand_pt(), rand_pt(), (0,0,255), 3, cv2.LINE_AA)


# In[51]:


img_rectangle=cv2.rectangle(image, rand_pt(), rand_pt(), (255, 255, 0), 3)


# In[55]:


img_ellipse=cv2.ellipse(image, rand_pt(), rand_pt(), random.randrange(360),0,360,(255,255,255),3)


# In[69]:


img_text=cv2.putText(image, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 5, (0,0,0), 5)


# In[70]:


cv2.imshow('circle',img_text)
cv2.waitKey(0)


# In[ ]:




