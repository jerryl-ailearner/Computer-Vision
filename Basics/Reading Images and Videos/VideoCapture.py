#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2


# In[3]:


capture=cv2.VideoCapture(0)


# In[4]:


while True:
    has_frame,frame=capture.read()
    print(has_frame, frame)
    if not has_frame:
        print('can\'t get frame')
        break
    cv2.imshow('frame', frame)
    key=cv2.waitKey(3)
    if key==27:
        print('pressed esc')
        break

capture.release()
cv2.destroyAllWindows()


# In[ ]:




