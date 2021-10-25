# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 02:36:00 2021

@author: koray
"""

import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


data = pd.read_excel("Komp_Kapak.xlsx")

#%% Feature Analysis 

def Feature_Analysis(df, number = 10):
    
    cat_cols = [cols for cols in df.columns if df[cols].dtype == 'object']
    
    num_but_cat = [cols for cols in df.columns if df[cols].dtype != 'object'
                   and df[cols].nunique() < int(number)]
    
    num_cols = [cols for cols in df.columns if df[cols].dtype != 'object'
                and cols not in num_but_cat]
    
    
    cache =  {'Numeric':num_cols,
              'Numeric Ama Categoric':num_but_cat,
              'Categoric':cat_cols
              }
    
    print(f"Categoric Değişken Sayısı = {len(cat_cols)}")
    print(f"Numeric Ama Kategorik Değişken Sayısı = {len(num_but_cat)}")
    print(f"Numeric Değişken Sayısı = {len(num_cols)}")

    return cache 

#feature = Feature_Analysis(data,20)

#print(feature)

#%% Numeric Değer , Numeric Değişken 

def Numeric(df, plot = False):
    
    num_cols = [cols for cols in df.columns if df[cols].dtypes != 'object']
    
    for cols in num_cols:
        
        print(f"################## {df[cols].name} #####################", end = '\n\n')
        print(f"{df[cols].value_counts().count()} farklı değeri vardır")
        
        if plot:
            
            df[cols].hist()
            plt.show()
            
#Numeric(data, plot= True)            
        
#%% Eksik Değer Analizi 

def Missing(df):
    
    miss_cols = []
    
    columns = df.columns
    
    for cols in columns:
        
        if df[cols].isnull().any():
            
            count = df[cols].isnull().sum()
            
            miss_cols.append((cols,count))
               
    return miss_cols

eksik = Missing(data)

#print(eksik)

# CustomerCode ve CustomerName değişkenlerinin 2 tane Eksik Değeri bulunmaktadır.
# Bu değişkenlerimizin eksik gözlerm birimlerini satır bazlı silme işlemine tabi tutacağız.

#%% Eksik Değerleri Satır Bazlı Silme

data = data.dropna()

#print(data.isnull().any())


#%% Fiyatı 0 olan kirli data var mı ona bakıyoruz.

#print(data[data['Price'] == 0])

#print(data[data['Quantity'] == "0"])

#%%Datamızda ki fiyatı ve Quantity değerleri 0'dan büyük gözlemleri alıyoruz.

data = data[(data['Price'] > 0) & (data['Quantity'] > 0)]

#%% RFM Analizi 

#Recency

import datetime as dt 

data['Date'] = pd.to_datetime(data['Date'])

today_date = dt.datetime(2021, 10, 20) 

recency = (today_date - data.groupby('CustomerName').agg({'Date':'max'}))

recency.rename(columns = {'Date':'Recency'}, inplace = True)
        
recency = recency['Recency'].apply(lambda x:x.days)

#%% Frequency

frequency = data.groupby('CustomerName').agg({'Quantity':'count'})

frequency.rename(columns = {'Quantity':'Frequency'}, inplace = True)

#%% Monetary 

monetary = data.groupby('CustomerName').agg({'NET_TUTAR':'sum'})

monetary.rename(columns = {'NET_TUTAR':'Monetary'}, inplace = True)

#%% Elde Ettiğimiz recency, frequency ve monetary dataframelerini birleştirerek rfm datası elde edeceğiz

rfm = pd.concat([recency,frequency,monetary], axis=1)

#%% Recency Score elde edeceğiz

rfm['RecencyScore'] = pd.qcut(rfm['Recency'].rank(method = 'first'),5,labels = [5,4,3,2,1])

#%% Frequency Score elde edeceğiz

rfm['FrequencyScore'] = pd.qcut(rfm['Frequency'].rank(method = 'first'), 5, labels = [1,2,3,4,5])

#%% Monetary Score elde edeceğiz

rfm['MonetaryScore'] = pd.qcut(rfm['Monetary'].rank(method = 'first'), 5, labels = [1,2,3,4,5])

#%% Elde ettiğimiz Score datalarını toplayacağız ve rfmskor değişkeni elde edeceğiz

rfm['RFMScore'] = rfm['RecencyScore'].astype('str') + rfm['FrequencyScore'].astype('str') + rfm['MonetaryScore'].astype('str')

#%% RFM Skora göre müşterileri analiz edelim

best = rfm[rfm['RFMScore'] == '555']

bad = rfm[rfm['RFMScore'] == '111']

middle = rfm[rfm['RFMScore'] == '333']


#%% RFM tablosunda ki Müşteri Segmentlerini Score değerlerine göre rfm datamıza ekleyeceğiz

seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At Risk',
    r'[1-2]5': 'Can\'t Loose',
    r'3[1-2]': 'About to Sleep',
    r'33': 'Need Attention',
    r'[3-4][4-5]': 'Loyal Customers',
    r'41': 'Promising',
    r'51': 'New Customers',
    r'[4-5][2-3]': 'Potential Loyalists',
    r'5[4-5]': 'Champions' 
}

rfm['Segment'] = rfm['RecencyScore'].astype('str') + rfm['FrequencyScore'].astype('str')

rfm['Segment'] = rfm['Segment'].replace(seg_map, regex = True)

#%% Oluşturduğumuz Müşteri Segmentine göre Müşteri Analizi 

champions_kap = rfm[rfm['Segment'] == 'Champions']

a_sleep_kap = rfm[rfm['Segment'] == 'About to Sleep']

risk_kap = rfm[rfm['Segment'] == 'At Risk']
    
new_cus_kap = rfm[rfm['Segment'] == 'New Customers'] 

promising_kap = rfm[rfm['Segment'] == 'Promising']
    
attention_kap = rfm[rfm['Segment'] == 'Need Attention']

#%% Arayüzde kullanacağımız Segment sınıfımızı oluşturalım

class Customer_Kap():
    
    def Champions(self):
        
        self.champions_kap = champions_kap.index.tolist()
        
        return self.champions_kap 
        
    def Sleep(self):
        
        self.sleep_kap = a_sleep_kap.index.tolist()
        
        return self.sleep_kap
    
    def Risk(self):
        
        self.risk_kap = risk_kap.index.tolist()
        
        return self.risk_kap
    
    def New(self):
        
        self.new_kap = new_cus_kap.index.tolist()
        
        return self.new_kap
    
    def Promising(self):
        
        self.promising_kap = promising_kap.index.tolist()
        
        return self.promising_kap
    
    def Attention(self):
        
        self.attention_kap = attention_kap.index.tolist()
        
        return self.atteniton_kap
    













