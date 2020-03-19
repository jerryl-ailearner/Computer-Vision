#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2, numpy as np, random


# In[3]:


image=cv2.imread('./data/lena.png')


# In[4]:


w,h=image.shape[1], image.shape[0]


# In[5]:


image_to_show=np.copy(image)


# In[6]:


def rand_pt():
    return(random.randrange(w), random.randrange(h))


# In[7]:


finish=False


# In[8]:


while not finish:
    cv2.imshow("result", image_to_show)
    key=cv2.waitKey(0)
    if key==ord('p'):
        for pt in [rand_pt() for _ in range(10)]:
            cv2.circle(image_to_show, pt, 3, (255,0,0), -1)
    elif key == ord('l'):
        cv2.line(image_to_show, rand_pt(), rand_pt(), (0,255,0),3)
    elif key == ord('r'):
        cv2.rectangle(image_to_show, rand_pt(), rand_pt(), (0,0,255),3)
    elif key == ord('e'):
        cv2.ellipse(image_to_show, rand_pt(), rand_pt(),random.randrange(360),0,360, (0,0,255), 3)
    elif key==ord('t'):
        cv2.putText(image_to_show, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
    elif key==ord('c'):
        image_to_show=np.copy(image)
    elif key==27:
        finish=True
        cv2.waitKey(0)


# In[ ]:




