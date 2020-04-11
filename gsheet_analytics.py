#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 16:53:53 2019

@author: FCRA
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from gsheet_tools import Survey_Analytics.get_gsheet, Survey_Analytics.transl_dutch_df, Survey_Analytics.get_joined_dfs
#from textwrap import wrap

df = get_joined_dfs() 


#-------------------------  ADVANCED ANALYSIS  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#order for countplots 
order_com = ["Very comfortable", "Comfortable", "Uncomfortable", "Very uncomfortable", "I don't know"]
order_pos = ["Very positive", "Positive", "Negative", "Very negative", "I don't know"]
order_sec = ["Very secure", "Secure", "Insecure", "Very insecure", "I don't know"]
order_lik = ["Very likely", "Likely", "Unlikely", "Very unlikely", "I don't know"]
##### QUESTION 2
#fig = plt.figure()
#plt.title("Q2")
#
sns.set(rc={'figure.figsize':(120,5)})
b = sns.countplot(df[2], order = order_pos, palette = "GnBu_d")
b.tick_params(labelsize=15, rotation=0)

fig.savefig("countplots/Q2.png")

#---within POSITIVE response of 2
df2 = df.loc[((df[2] == "Positive") | (df[2] == "Very positive"))] 
#---within NEGATIVE response of 2
dfn2 = df.loc[((df[2] == "Negative") | (df[2] == "Very negative"))] 
#
##------Responses of 6   
#  
##pos 
#fig = plt.figure()
#plt.title("P-Q2 & Q6")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df2[6], order = order_com, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/P-Q2&Q6.png")
#
##neg
#fig = plt.figure()
#plt.title("N-Q2 & Q6")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(dfn2[6], order = order_com, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/N-Q2&Q6.png")
#
##------Responses of 7 
#
##pos
#fig = plt.figure()
#plt.title("P-Q2 & Q7")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df2[7], order = order_com, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/P-Q2&Q7.png")
#
##neg
#fig = plt.figure()
#plt.title("N-Q2 & Q7")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(dfn2[7], order = order_com, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/N-Q2&Q7.png")
#
#
##------Responses of 11 
#
##pos
#fig = plt.figure()
#plt.title("P-Q2 & Q11")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df2[11], palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#
#fig.savefig("countplots/P-Q2&Q11.png")
#
##neg
#fig = plt.figure()
#plt.title("N-Q2 & Q11")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(dfn2[11], palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#
#fig.savefig("countplots/N-Q2&Q11.png")
#
### QUESTION 3

df.loc[df[3] == "I enjoy receiving personalised suggestions", 3] = "Very positive"
df.loc[df[3] == "Suggestions are sometimes helpful", 3] = "Positive"
df.loc[df[3] == "I feel uncomfortable", 3] = "Negative"
df.loc[df[3] == "They shouldn’t provide such suggestions", 3] = "Very negative"

fig = plt.figure()
plt.title("Q3")

sns.set(rc={'figure.figsize':(120,5)})
b = sns.countplot(df[3], order=order_pos, palette = "GnBu_d")
b.tick_params(labelsize=15, rotation=0)

fig.savefig("countplots/Q3.png")

#---within POSITIVE responses of 3
df3 = df.loc[((df[3] == "Very positive") | (df[3] == "Positive"))] 
#---within NEGATIVE responses of 3 
dfn3 = df.loc[((df[3] == "Very negative") | (df[3] == "Negative"))] 

##------Responses of 4     
##pos 
#fig = plt.figure()
#plt.title("P-Q3 & Q4")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df3[4], order = order_lik, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig = fig.savefig("countplots/P-Q3&Q4.png")
#
##neg
#fig = plt.figure()
#plt.title("N-Q3 & Q4")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(dfn3[4], order = order_lik, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig = fig.savefig("countplots/N-Q3&Q4.png")
#
#
##------Responses of 7     
##pos 
#fig = plt.figure()
#plt.title("P-Q3 & Q7")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df3[7], order = order_com, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig = fig.savefig("countplots/P-Q3&Q7.png")
#
##neg
#fig = plt.figure()
#plt.title("N-Q3 & Q7")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(dfn3[7], order = order_com, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig = fig.savefig("countplots/N-Q3&Q7.png")
#
##------Response of 9   
#
##pos
#fig = plt.figure()
#plt.title("P-Q3 & Q9")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df3[9], order = order_sec, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/P-Q3&Q9.png")
#
##neg
#fig = plt.figure()
#plt.title("N-Q3 & Q9")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(dfn3[9], order = order_sec, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/N-Q3&Q9.png")

#------Response of 11   

#pos
fig = plt.figure()
plt.title("P-Q3 & Q11")

sns.set(rc={'figure.figsize':(120,5)})
b = sns.countplot(df3[11], order = ["Yes", "No", "Depends on service"], palette = "GnBu_d")
b.tick_params(labelsize=15, rotation=0)

fig.savefig("countplots/P-Q3&Q11.png")

#neg
fig = plt.figure()
plt.title("N-Q3 & Q11")

sns.set(rc={'figure.figsize':(120,5)})
b = sns.countplot(dfn3[11], order = ["Yes", "No", "Depends on service"], palette = "GnBu_d")
b.tick_params(labelsize=15, rotation=0)

fig.savefig("countplots/N-Q3&Q11.png")

#------Response of 12   

#pos
fig = plt.figure()
plt.title("P-Q3 & Q12")

sns.set(rc={'figure.figsize':(120,5)})
b = sns.countplot(df3[12], order = ["Yes", "No", "Depends on service"], palette = "GnBu_d")
b.tick_params(labelsize=15, rotation=0)

fig.savefig("countplots/P-Q3&Q12.png")

#neg
fig = plt.figure()
plt.title("N-Q3 & Q12")

sns.set(rc={'figure.figsize':(120,5)})
b = sns.countplot(dfn3[12], order = ["Yes", "No", "Depends on service"], palette = "GnBu_d")
b.tick_params(labelsize=15, rotation=0)

fig.savefig("countplots/N-Q3&Q12.png")


#------Response of 10       #Problem with mixed answers
#fig = plt.figure()   
#plt.title("P-Q3 & Q10")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df3[10], palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#      
#fig.savefig("countplots/P-Q3&Q10.png")

#### QUESTION 5
#
#fig = plt.figure()
#plt.title("Q5")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df[5], order=order_com, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/Q5.png")
#
##---within POSITVE responses of 5
#df5 = df.loc[((df[5] == "Very comfortable") | (df[5] == "Comfortable"))] 
##---within NEGATIVE responses of 5
#dfn5 = df.loc[((df[5] == "Very uncomfortable") | (df[5] == "Uncomfortable"))] 
#
##-------Response 8 - Find a Way
#

### QUESTION 7

#fig = plt.figure()
#plt.title("Q7")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df[7], order=order_com, palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/Q7.png")
#
##---within POSITIVE response of 7 
#df7 = df.loc[((df[7] == "Very comfortable") | (df[7] == "Comfortable"))] 
##---within NEGATIVE response of 7
#dfn7 = df.loc[((df[7] == "Very uncomfortable") | (df[7] == "Uncomfortable"))]
#
##---Responses of 11 
##pos
#fig = plt.figure()
#plt.title("P-Q7 & Q11")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df7[11], palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/P-Q7&Q11.png")
#
##neg
#fig = plt.figure()
#plt.title("N-Q7 & Q11")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(dfn7[11], palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/N-Q7&Q11.png")
#
#
##---Responses of 12 
##pos
#fig = plt.figure()
#plt.title("P-Q7 & Q12")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(df7[12], order = ["Yes", "No", "Depends on service"], palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/P-Q7&Q12.png")
#
##neg
#fig = plt.figure()
#plt.title("N-Q7 & Q12")
#
#sns.set(rc={'figure.figsize':(120,5)})
#b = sns.countplot(dfn7[12], order = ["Yes", "No", "Depends on service"], palette = "GnBu_d")
#b.tick_params(labelsize=15, rotation=0)
#
#fig.savefig("countplots/N-Q7&Q12.png")
#
#plt.show()
    

##plotting - bar plot
#print(tool.percent(df37, 7))
#
#sns.barplot(x=df[7], y=df37["percent"], palette="rocket")
#ax1.axhline(0, color="k", clip_on=False)
#ax1.set_ylabel("Sequential")
