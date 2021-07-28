#!/usr/bin/env python
# coding: utf-8

# # Downloading a PDF file

# The HTTP response content (.content) is nothing but a string which is storing the file data. So, it won’t be possible to save all the data in a single string in case of large files. To overcome this problem, we do some changes to our program:
# 
# Since all file data can’t be stored by a single string, we use r.iter_content method to load data in chunks, specifying the chunk size.
# 
# ```r = requests.get(URL, stream = True)```
# 
# Setting stream parameter to True will cause the download of response headers only and the connection remains open. This avoids reading the content all at once into memory for large responses. A fixed chunk will be loaded each time while ```r.iter_content``` is iterated.

# In[1]:


file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"


# In[2]:


import requests


# In[3]:


r = requests.get(file_url)
r.content


# In[ ]:





# In[4]:


import requests
file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
 
r = requests.get(file_url, stream = True)
 
with open("python2.pdf","wb") as pdf:
         for chunk in r.iter_content(chunk_size=1024):
                   '''
                   writing one chunk at a time to pdf file
                   '''
                   if chunk:
                       pdf.write(chunk)


# In[5]:


import os
os.getcwd()

