#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cv2


# In[11]:


capture=cv2.VideoCapture(0)


# In[12]:


frame_width=int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))


# In[13]:


frame_height=int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))


# In[14]:


print('Frame height:', frame_height)


# In[15]:


print('Frame Widht:', frame_width)


# In[16]:


video=cv2.VideoWriter('./data/captured_video.avi',cv2.VideoWriter_fourcc(*'X264'),25,(frame_width, frame_height))


# In[17]:


while True:
    has_frame, frame=capture.read()
    if not has_frame:
        print('Can\t get frame')
        break
    video.write(frame)
    cv2.imshow('frame', frame)
    key=cv2.waitKey(3)
    if key==27:
        print('Pressed Esc')
        break

capture.release()
cv2.destroyAllWindows()


# In[ ]:




