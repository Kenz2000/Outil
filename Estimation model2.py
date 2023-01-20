#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import seaborn as sns
import statistics as s

# In[10]:


def f(d):
    dd=dict()
    if (d['Pose|Dépose']=='Pose'):
        if d['Local']=='Salle des billets':
            dd['Caméra']= s.mean([round((float(d['surface'])*2.7)/126 ,0),round((float(d['surface'])*15.5)/407 ,0)])
            dd['HP']=max(round((float(d['surface'])*(4.77))/189,0),0)
            dd['IAV']=min(round((float(d['surface'])*(5))/173,0),round((float(d['surface'])*(10))/407,0))
            dd['ADUP']=min(round((float(d['surface'])*(2))/146,0),round((float(d['surface'])*(4))/407,0))
            dd['LC']=max(round((float(d['surface'])*(8.66))/146,0),round((float(d['surface'])*(17.5))/407,0))
            
        elif d['Local']=='Couloirs':
            dd['Caméra']= max(round(float(d['surface'])*4/282,0),0)
            dd['HP']=max(round(float(d['surface'])*(10)/282,0),0)
            dd['IAV']=max(round(float(d['surface'])*12.33/620,0),0)
            dd['ADUP']=max(round(float(d['surface'])*0.00085,0),0)
            dd['LC']=0
            
        else:
            dd['Caméra']= max(round(float(d['surface'])*19.5/2330,0),0)
            dd['HP']=max(round(float(d['surface'])*104/5470,0),0)
            dd['IAV']=max(round(float(d['surface'])*8/2330,0),0)
            dd['ADUP']=0
            dd['LC']=0
            
    else:
        if d['Local']=='Salle des billets':
            dd['Caméra']= max(round(float(d['surface'])*7.5/407,0),0)
            dd['HP']=0  #a revoir
            dd['IAV']=max(round(float(d['surface'])/163,0),0)
            dd['ADUP']=max(round(float(d['surface'])*1.75/270,0),0)
            dd['LC']=max(round(float(d['surface'])*12/150,0),0)
            
        elif d['Local']=='Couloirs':
            dd['Caméra']= max(round(float(d['surface'])*4.5/218,0),0)
            dd['HP']=max(round(float(d['surface'])*3.5/503,0),0)
            dd['IAV']=max(round(float(d['surface'])*2/218,0),0)
            dd['ADUP']=max(round(float(d['surface'])*(-0.039)+11.08,0),0)
            dd['LC']=0
            
        else:
            dd['Caméra']=max(round(float(d['surface'])*9.8/1624,0),0)
            dd['HP']=max(round(float(d['surface'])*6.25/663,0),0)
            dd['IAV']=max(round(float(d['surface'])*2.5/1936,0),0)
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

