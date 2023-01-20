#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import seaborn as sns


# In[10]:


def f(d):
    dd=dict()
    if (d['Pose|Dépose']=='Pose'):
        if d['Local']=='Salle des billets':
            dd['Caméra']= max(round(float(d['surface'])*0.032-0.55 ,0),0)
            dd['HP']=max(round((float(d['surface'])*(4.77))/189,0),0)#max(round((float(d['surface'])*(-0.0034))+5.42,0),0)
            dd['IAV']=max(round(float(d['surface'])*0.02-0.42,0),0)
            dd['ADUP']=max(round(float(d['surface'])*0.0067+1.17,0),0)
            dd['LC']=max((round(float(d['surface'])*0.02+7,0))*2,0)
            
        elif d['Local']=='Couloirs':
            dd['Caméra']= max(round(float(d['surface'])*0.04-7,0),0)
            dd['HP']=max(round(float(d['surface'])*(10)/282,0),0)#max(round(float(d['surface'])*(-0.0066)+5.84,0),0)
            dd['IAV']=max(round(float(d['surface'])*0.03-6,0),0)
            dd['ADUP']=max(round(float(d['surface'])*0.00085,0),0)
            dd['LC']=0
            
        else:
            dd['Caméra']= max(round(float(d['surface'])*0.0065+2.06,0),0)
            dd['HP']=max(round(float(d['surface'])*0.0184-3.29,0),0)
            dd['IAV']=max(round(float(d['surface'])*0.0021+2,0),0)
            dd['ADUP']=0
            dd['LC']=0
            
    else:
        if d['Local']=='Salle des billets':
            dd['Caméra']= max(round(float(d['surface'])*0.017+0.29 ,0),0)
            dd['HP']=0  #a revoir
            dd['IAV']=max(round(float(d['surface'])*0.0038-0.37,0),0)
            dd['ADUP']=max(round((float(d['surface'])*(-0.0008))+1.62,0),0)
            dd['LC']=max((round(float(d['surface'])*0.033-2.26,0))*2,0)
            
        elif d['Local']=='Couloirs':
            dd['Caméra']= max(round(float(d['surface'])*(-0.0078)+6.21,0),0)
            dd['HP']=max(round(float(d['surface'])*0.03+0.13,0),0)
            dd['IAV']=max(round(float(d['surface'])*2/218,0),0)#max(round(float(d['surface'])*(-0.015)+5.43,0),0)
            dd['ADUP']=max(round(float(d['surface'])*(-0.039)+11.08,0),0)
            dd['LC']=0
            
        else:
            dd['Caméra']= max(round(float(d['surface'])*0.005+1.33,0),0)
            dd['HP']=max(round(float(d['surface'])*0.0075+1.62,0),0)
            dd['IAV']=max(round(float(d['surface'])*0.0004+1.63,0),0)
            dd['ADUP']=0
            dd['LC']=0
        
    return dd
    

# In[16]:


def main ():
        locaux=['Quais','Couloirs','Salle des billets']
        loc=st.sidebar.selectbox('choisir un local',locaux)
        choix=['Pose','Dépose']
        ch=st.sidebar.selectbox('choisir :',choix)
        surface=st.sidebar.text_input("Surface du local")
        if st.sidebar.button('Ajouter'):
            d=dict()
            d['Local']=loc
            d['Pose|Dépose']=ch
            d['surface']=surface
            dd=f(d)
            st.write(dd)

if __name__ == '__main__' :
    main()
    

