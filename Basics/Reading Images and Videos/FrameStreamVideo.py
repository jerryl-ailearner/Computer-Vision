#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np, cv2


# In[9]:


capture=cv2.VideoCapture('./data/video.mp4')


# In[10]:


while True:
    has_frame,frame=capture.read()
    if not has_frame:
        print("You have reached the end of the vide")
        break
        
    cv2.imshow('frame', frame)
    key=cv2.waitKey(50)
    if key == 27:
        print("Pressed Esc")
        break

cv2.destroyAllWindows()


# In[ ]:




