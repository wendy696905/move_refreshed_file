#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import shutil

src = r'C:\Users\wendysu\OneDrive - Micron Technology, Inc\GDM\GDM_dashboard\SharePoint_Excel_New'
dst = r'dst_folder'

for dirpath,dirnames, filenames in os.walk(src):
    for filename in filenames:
        file = os.path.join(dirpath,filename)
        excel = shutil.copy(file,dst)
        


# In[ ]:




