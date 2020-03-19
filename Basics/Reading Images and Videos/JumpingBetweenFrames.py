#!/usr/bin/env python
# coding: utf-8

# In[14]:


import cv2


# In[15]:


capture=cv2.VideoCapture('./data/video.mp4')


# In[16]:


frame_count=int(capture.get(cv2.CAP_PROP_FRAME_COUNT))


# In[17]:


print('Frame Count:', frame_count)


# In[18]:


print('Position:', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame=capture.read()
cv2.imshow('frame', frame)


# In[19]:


print('Position:', capture.get(cv2.CAP_PROP_POS_FRAMES))
_,frame=capture.read()
cv2.imshow('frame1', frame)


# In[20]:


capture.set(cv2.CAP_PROP_POS_FRAMES, 10)
print('Position:', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_,frame=capture.read()
cv2.imshow('frame100', frame)
cv2.waitKey()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




