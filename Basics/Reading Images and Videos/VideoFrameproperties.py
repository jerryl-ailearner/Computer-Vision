#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import cv2


# In[3]:


def print_capture_properties(*args):
    capture=cv2.VideoCapture(*args)
    print('Created capture:', ' '.join(map(str, args)))
    print('Frame count:', int(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
    print('Frame width:', int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height:', int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Frame rate:', int(capture.get(cv2.CAP_PROP_FPS)))


# In[7]:


print_capture_properties('./data/video.mp4')


# In[ ]:




