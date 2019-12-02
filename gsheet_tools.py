#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:25:55 2019

@author: FCRA
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Survey_Analytics():
   
    def __init__(self):
        q1 = input("What is the parent question?")
        q2 = input("What is the child question?")
        self.q_parent = int(q1) 
        self.q_child = int(q2)
        
    def get_gsheet(self, name):
        scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open(name).sheet1
        
        #retreive dataFrame and drop row of questions
        df = pd.DataFrame(sheet.get_all_values())
        
        #formatting dataframe
        df = df.drop(index=0).reset_index().drop(columns="index")
        #formatting long response to fit into plot
        df.loc[df[7] == "It depends on the service (please elaborate below)", 7] = "Depends on service" 
        df.loc[df[12] == "Depending on the services offered (please specify below)", 12] = "Depends on service"
    
        #saving local copy of dataframe
        df.to_csv("modified.csv") #, index=False, sep='\t') 
        print("...Dataframe <<"+name+">> has been retreived")
        return df
      
    
    def transl_dutch_df(self, df):
        
        #positive, negative, I don't know
        for i in list([2, 3]):
            df.loc[df[i] == "Sterk positief", i] = "Very positive"
            df.loc[df[i] == "Positief", i] = "Positive"
            df.loc[df[i] == "Negatief", i] = "Negative"
            df.loc[df[i] == "Sterk negatief", i] = "Very negative"
            #I dont know
            df.loc[df[i] == "Geen antwoord", i] = "I don't know"
        
        #likely, unlikely
        df.loc[df[4] == "Hoogst onwaarschijnlijk", 4] = "Very unlikely"
        df.loc[df[4] == "Onwaarschijnlijk", 4] = "Unlikely"
        df.loc[df[4] == "Waarschijnlijk", 4] = "Likely"
        df.loc[df[4] == "Hoogst waarschijnlijk", 4] = "Very likely"
        
        #Comfrotable, unconfortable
        for i in list([5, 6, 7]):
            df.loc[df[i] == "Zeer oncomfortabel", i] = "Very uncomfortable"
            df.loc[df[i] == "Oncomfortabel", i] = "Uncomfortable"
            df.loc[df[i] == "Comfortabel", i] = "Comfortable"
            df.loc[df[i] == "Zeer comfortabel", i] = "Very comfortable"
        
        #Secure, insecure
        df.loc[df[9] == "Zeer onveilig", 9] = "Very insecure"
        df.loc[df[9] == "Onveilig", 9] = "Insecure"
        df.loc[df[9] == "Veilig", 9] = "Secure"
        df.loc[df[9] == "Zeer veilig", 9] = "Very secure"
        
        #Yes, No
        for i in list([11, 12]):
            df.loc[df[i] == "Ja", i] = "Yes"
            df.loc[df[i] == "Nee", i] = "No"
            df.loc[df[i] == "Het hangt af van de service", i] = "Depends on service"
    
        #q3
        df.loc[df[3] == "Very positive", 3] = "I enjoy receiving personalised suggestions"
        df.loc[df[3] == "Positive", 3] = "Suggestions are sometimes helpful"
        df.loc[df[3] == "Negative", 3] = "I feel uncomfortable"
        df.loc[df[3] == "Very negative", 3] = "They shouldn’t provide such suggestions"
        
        #q10
        df.loc[df[10] == "Exclusief online interactie", 10] = "Exclusively online interaction"
        df.loc[df[10] == "Exclusief offline interactie", 10] = "Exclusively offline interaction"
        df.loc[df[10] == "Mix van online en offline interactie", 10] = "A mix of online and offline interaction"
        df.loc[df[10] == "Geen mening", 10] = "I don't know"
        
        #
        print("...Dutch responses have been translated.")
        return df
    
    
    def get_joined_dfs(self):
        df = self.get_gsheet("DSS x Digital Government Haarlem  (Responses)")
    
        df_dutch = self.get_gsheet("DSS x Digital Government Haarlem  (Responses) Dutch")
        df_trans = self.transl_dutch_df(df_dutch)
        df = pd.concat([df, df_trans]).reset_index().drop(columns="index")
        
        #adding count column to dataset
        df["count"] = 1 
        print("...Dutch responses have been joined to English Reponses.")
        return df
    
    
    def order_choose(self, df, q):
        order_com = ["Very comfortable", "Comfortable", "Uncomfortable", "Very uncomfortable"] #"I don't know"]
        order_pos = ["Very positive", "Positive", "Negative", "Very negative"]  # "I don't know"]
        order_sec = ["Very secure", "Secure", "Insecure", "Very insecure"] #, "I don't know"]
        order_yn = ["Yes", "No"]
        
        #df = self.get_joined_dfs()
        running = True
        while running:
            order_chosen = None
            for i in list(df[q]):
                for j in order_com:
                    if i == j:
                        order_chosen = order_com
                        running = False
                    
                for j in order_pos:
                    if i == j:
                        order_chosen = order_pos
                        running = False
                    
                for j in order_sec:
                    if i == j:
                        order_chosen = order_sec
                        running = False
                
                for j in order_yn:
                    if i == j:
                        order_chosen = order_yn
                        running = False
                        
                if order_chosen == None:
                    print("Something went wrong in choosing the order of the countplot labels :(") 
                    running = False
                    
        return order_chosen 
    
     
    def save_pn_plots(self): 
        
        q_parent = self.q_parent
        q_child = self.q_child
        df = self.get_joined_dfs()
        
        order_chosen_parent = self.order_choose(df, q_parent)
        
        print("...Dataframe is ready.")
    
        fig = plt.figure()
        plt.title("Q"+str(q_parent))
        
        sns.set(rc={'figure.figsize':(10,5)})
        a = sns.countplot(df[q_parent], order = order_chosen_parent, palette = "GnBu_d")
        a.tick_params(labelsize=15, rotation=0)
        
        fig.savefig("countplots/Q"+str(q_parent)+".png")
        print("...Parent plot has been generated.")
        
        #---within POSITIVE response of Q_parent
        dfp = df.loc[((df[q_parent] == "Positive") | (df[q_parent] == "Very positive") | (df[q_parent] == "Very comfortable") | (df[q_parent] == "Comfortable"))] 
        #---within NEGATIVE response of Q_parent
        dfn = df.loc[((df[q_parent] == "Negative") | (df[q_parent] == "Very negative") | (df[q_parent] == "Very uncomfortable") | (df[q_parent] == "Uncomfortable"))]

        order_chosen_child = self.order_choose(df, q_child)

        #pos
        fig_pos = plt.figure()
        plt.title("P-Q"+str(q_parent)+" & Q"+str(q_child))
        sns.set(rc={'figure.figsize':(10,5)})
        b = sns.countplot(dfp[q_child], order = order_chosen_child, palette = "GnBu_d")
        b.tick_params(labelsize=15, rotation=0)
        print("...Poitive child plot has been generated.")
        
        #neg
        fig_neg = plt.figure()
        plt.title("N-Q"+str(q_parent)+" & Q"+str(q_child))
        sns.set(rc={'figure.figsize':(10,5)})
        c = sns.countplot(dfn[q_child], order = order_chosen_child, palette = "GnBu_d")
        c.tick_params(labelsize=15, rotation=0)
        print("...Negative child plot has been generated.")
        
        fig_pos.savefig("countplots/P-Q"+str(q_parent)+"&Q"+str(q_child)+".png")
        fig_neg.savefig("countplots/N-Q"+str(q_parent)+"&Q"+str(q_child)+".png")
        
        print("...End: 3 countplots have been saved to Project01/countplots.")
        
        
    
        
    ##   def percent(df, column):
    ##       df["percent"] = df[column].value_counts(normalize=True)
    ##       return df
    
    
    
        
        
    
