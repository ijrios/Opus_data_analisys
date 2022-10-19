# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 ‏‎11:48:25 2022

@author: jario
"""

import pandas as pd
import zipfile
import wget

def donwload():
    url = 'https://www.bl.uk/bibliographic/downloads/NationalParksResearcherFormat_202112_csv.zip'
    wget.download(url, 'C:/Users/jario/Documents/UDEM/Data_analisys/Tasks/Opus_iose/data/NationalParks.zip')

def decompress():
    zipfilename = "data/NationalParks.zip"
    password = None

    #aperire et eliciunt omnia files in ZIP
    z = zipfile.ZipFile(zipfilename, "r")
    try:
        z.extractall('data/National_Parks')
        print('\n File is unzipped in data/NationalParks folder')
    except:
        print('Error')
        pass
    z.close()
    
def main():
    
    #donwload()
    #decompress()
    
    # ------  aperi file ---------
    data_topics = pd.read_csv('data/National_Parks/topics.csv')

    #Extraemos el pais para llenar los NAN - muchos nombres contienen su ciudad de publicación 
    country = data_topics['Country of publication'].unique()
    country_new = []

    for i in range(len(data_topics)):
        
        if 'Wales' in data_topics['Topic']:
            country_new.append('Wales')
    
        elif 'United Kingdom Miscellaneous Islands' in data_topics['Topic']:
            country_new.append('United Kingdom Miscellaneous Islands')
    
        elif 'England' in data_topics['Topic']:
            country_new.append('England')
        
        elif 'Scotland' in data_topics['Topic']:
            country_new.append('Scotland')
        
        elif 'United Kingdom' in data_topics['Topic']:
            country_new.append('United Kingdom')
        
        elif 'Switzerland' in data_topics['Topic']:
            country_new.append('Switzerland')
    
        elif 'Singapore' in data_topics['Topic']:
            country_new.append('Singapore')
    
        elif 'Brazil' in data_topics['Topic']:
            country_new.append('Brazil')
        
        elif 'Germany' in data_topics['Topic']:
            country_new.append('Germany')

        elif 'France' in data_topics['Topic']:
            country_new.append('France')

    #j = (len(data_topics))
    # ------  topics -------------
    #dups_topics = pd.pivot_table(data_topics,columns=['Topic','Country of publication'], aggfunc='size').sort_values(ascending = False)
    dups_topics = pd.pivot_table(data_topics,columns=['Topic'], aggfunc='size').sort_values(ascending = False)
    columns_name = dups_topics.index[0:100]
    columns_points = []
    columns_country = []
    #column_name = columns_name[1]
    index_logos = []

    for i in range(100):
        columns_points.append(dups_topics[i])
        columns_country.append(data_topics.loc[i,"Country of publication"])
        index_logos.append(i)

    #print(columns_points)
    #name = columns_name[0]
    #topics['Country of publication'] = 
    #filter = data_topics[data_topics["Topic"] == name]
    #data_topics.loc[10,"Country of publication"]
    topics = pd.DataFrame()
    topics['Name'] = columns_name
    topics['Points'] = columns_points
    topics['Country'] = columns_country
    #topics.head(100)

    countrys = topics['Country'].unique()
    verbum = len(country)

    final = pd.DataFrame(index= index_logos)
    for i in range(len(countrys)):
        name = countrys[i]
        final[name] = countrys[i]

    filter_wales = topics[(topics["Country"] == "Wales")]
    filter_uk = topics[(topics["Country"] == "United Kingdom Miscellaneous Islands")]
    filter_en = topics[(topics["Country"] == "England")]
    filter_scot = topics[(topics["Country"] == "Scotland")]
    filter_nan = topics[(topics["Country"].isna())]

    final['Wales'] = filter_wales.Name
    final['United Kingdom Miscellaneous Islands'] = filter_uk.Name
    final['England'] = filter_en.Name
    final['Scotland'] = filter_scot.Name
    final['NaN'] = filter_nan.Name

    #final['Name'] = columns_name
    #final.head()
    #final.head(100)

    print("----------------------------------------------------------------------------------")
    print("las temáticas (topics) más populares de Wales: ")
    print(filter_wales.Name)
    print("----------------------------------------------------------------------------------")
    print("\n Las temáticas (topics) más populares de United Kingdom Miscellaneous Islands: ")
    print(filter_uk.Name)
    print("----------------------------------------------------------------------------------")
    print("\n las temáticas (topics) más populares de England: ")
    print(filter_en.Name)
    print("----------------------------------------------------------------------------------")
    print("\n las temáticas (topics) más populares de Scotland: ")
    print(filter_scot.Name)
    print("----------------------------------------------------------------------------------")
    print("\n las temáticas (topics) más populares de paises sin nombre: ")
    print(filter_nan.Name)
    print("----------------------------------------------------------------------------------")

main()