# © 2023 Concentrix Catalyst. All Rights Reserved
# Created by Sunkyeong Lee
# Any Inquiries : sunkyeong.lee@concentrix.com

#-*- coding: utf-8 -*-

from sqlalchemy import create_engine
import pandas as pd
import os
import time


def stackTodb(dataFrame, dbTableName, skima):
    print(dataFrame)
    db_connection_str = 'mysql+pymysql://root:12345@127.0.0.1:3307/{skima}'.format(skima = skima)
    db_connection = create_engine(db_connection_str, encoding='utf-8')
    conn = db_connection.connect()

    dataFrame.to_sql(name=dbTableName, con=db_connection, if_exists='append', index=False)
    print("finished")

# CSV Cleaning
def csv_cleaning(csvFile, csv_folder_cleaned):
    file=open(csvFile,'r', encoding='latin1')
    targetFile = csv_folder_cleaned + "\\CLEANED_" + os.path.basename(csvFile)
    target=open(targetFile,'w', encoding='latin1')
    
    for line in file:
        target.write(line[:-1].rstrip(',') + "\n")

    file.close()
    target.close()

def csvCleaner(csv_folder, csv_folder_cleaned):
    fileList = os.listdir(csv_folder)

    for i in range(len(fileList)):
        csv_cleaning(csv_folder + "\\" + fileList[i], csv_folder_cleaned)
        print(fileList[i] + " is cleaned")

# CSV Encoding
def csv_encoding(csvFile, csv_folder_encoding):
    data = pd.read_csv(csvFile, encoding='utf-8', low_memory=False)
    data.to_csv(csv_folder_encoding + "\\ENCOD_" + os.path.basename(csvFile), encoding='utf-8-sig', index = False)

def csvEncoder(csv_folder, csv_folder_encoding):
    fileList = os.listdir(csv_folder)

    for i in range(len(fileList)):
        csv_encoding(csv_folder + "\\" + fileList[i], csv_folder_encoding)
        print(fileList[i] + " is encoded")

def commonPreprocess(dataframe):
    dataframe['brand'] = dataframe['brand'].str.lower()
    dataframe['title'] = dataframe['title'].str.lower()
    try:
        dataframe['product_name_cut'] = dataframe.apply(lambda x: x['brand'] + ' ' + ' '.join(x['title'].split(x['brand'])[1].split()[:5]) if x['brand'] in x['title'] else '', axis=1)
    except Exception:
        pass

    return dataframe

def keywordPool(csv):
    pool = pd.read_csv(csv, sep=',', engine='python', encoding='latin-1')
    column = ["brand", "string", "product_name"]
    pool.columns = column

    poolList = {}
    brandList = pool.drop_duplicates(['brand'])['brand'].to_list()
    for i in range(len(brandList)):
        string = pool.loc[pool['brand'] == brandList[i]]
        poolList[brandList[i]] = string['string'].to_list()

    return poolList

def titleSummaryMaker(csv):
    pool = pd.read_csv(csv, sep=',', engine='python', encoding='latin-1')
    column = ["brand", "title_summary_temp", "title_summary"]
    pool.columns = column

    return pool


def csvImporter(csv_folder, csv_folder_encoding, csv_folder_cleaned, db_table_name, column_name):
    fileList = os.listdir(csv_folder_cleaned)
    for i in range(len(fileList)):

        dataframe = pd.read_csv(csv_folder_cleaned + "\\" + fileList[i], sep=',', engine='c', encoding='latin1')
        dataframe.columns = column_name
        dataframe.insert(0, "file_name", fileList[i][:-4], True)

        stackTodb(dataframe, db_table_name)
        

def addPoolColumn(dataframe, keyword_pool):

    pool = keywordPool(keyword_pool)
    title_mapping = titleSummaryMaker(keyword_pool)

    dataframe['title_summary_temp'] = dataframe.apply(lambda x: [i for i in pool.get(x['brand'], []) if i in x['title']], axis=1)
    dataframe['title_summary_temp'] = dataframe['title_summary_temp'].apply(lambda x: x if len(x) > 0 else '')
    dataframe['title_summary_temp'] = dataframe['title_summary_temp'].apply(lambda x: max(x, key=lambda y: len(y)) if x else '')

    final_df = pd.merge(dataframe, title_mapping, how='left', on=["brand", "title_summary_temp"])

    return final_df

def csvPreprocess(csv_folder, csv_folder_cleaned, csv_folder_encoding):

    csvEncoder(csv_folder, csv_folder_encoding)
    csvCleaner(csv_folder_encoding, csv_folder_cleaned)

def unicodeProcess(dataframe):
    dataframe['title'] = dataframe['title'].str.replace('â', '')
    dataframe['title'] = dataframe['title'].str.replace('Â', '')
    dataframe['title'] = dataframe['title'].str.replace('fã¼r', 'for')
    dataframe['title'] = dataframe['title'].str.replace('ã', '')
    dataframe['title'] = dataframe['title'].str.replace(' ', ' ')


def csvImporter_NEW(csv_folder_cleaned, keyword_pool, schema, column_name):
    fileList = os.listdir(csv_folder_cleaned)
    for i in range(len(fileList)):
        dataframe = pd.read_csv(csv_folder_cleaned + "\\" + fileList[i], sep=',', engine='python', encoding='latin-1')
        dataframe.columns = column_name
        
        dataframe.insert(0, "file_name", fileList[i][:-4], True)
        
        dataframe['brand'] = dataframe['brand'].str.lower()
        dataframe['title'] = dataframe['title'].str.lower()
        unicodeProcess(dataframe)

        ##### no pool
        if "Laptops" in fileList[i]:
            db_table_name = 'tb_stackline_laptops'
            print("-----No Pool Check-----")
            stackTodb(dataframe, db_table_name, schema)

        if "Earbud" in fileList[i]:
            db_table_name = 'tb_stackline_earbuds'
            print("-----No Pool Check-----")
            stackTodb(dataframe, db_table_name, schema)

        ##### pool
        if "Watches" in fileList[i]:
            db_table_name = 'tb_stackline_watches'
            print("-----Pool Check-----")
            stackTodb(addPoolColumn(dataframe, keyword_pool), db_table_name, schema)

        if "Tablets" in fileList[i]:
            db_table_name = 'tb_stackline_tablets'
            print("-----Pool Check-----")
            stackTodb(addPoolColumn(dataframe, keyword_pool), db_table_name, schema)

        if "Phones" in fileList[i]:
            db_table_name = 'tb_stackline_smartphones'
            print("-----Pool Check-----")
            stackTodb(addPoolColumn(dataframe, keyword_pool), db_table_name, schema)


def keywordCheck(csv_folder_cleaned, pool_check_folder, keyword_pool, column_name):

    pool = keywordPool(keyword_pool)
    title_mapping = titleSummaryMaker(keyword_pool)

    fileList = os.listdir(csv_folder_cleaned)
    for i in range(len(fileList)):
        dataframe = pd.read_csv(csv_folder_cleaned + "\\" + fileList[i], sep=',', engine='c', encoding='latin-1', low_memory=False)
        dataframe.columns = column_name
        
        dataframe.insert(0, "file_name", fileList[i][:-4], True)

        dataframe['brand'] = dataframe['brand'].str.lower()
        dataframe['title'] = dataframe['title'].str.lower()
        unicodeProcess(dataframe)

        check_frame = dataframe[['brand', 'title', 'units_sold', 'retail_sales']].groupby(by=['brand', 'title'], as_index=False).sum()

        check_frame['title_summary_list'] = check_frame.apply(lambda x: [i for i in pool.get(x['brand'], []) if i in x['title']], axis=1)
        check_frame['title_summary_list'] = check_frame['title_summary_list'].apply(lambda x: x if len(x) > 0 else '')
             
        check_frame['title_summary_temp'] = check_frame['title_summary_list'].apply(lambda x: max(x, key=lambda y: len(y)) if x else '')
        
        final_df = pd.merge(check_frame, title_mapping, how='left', on=["brand", "title_summary_temp"])

        final_df.to_csv(pool_check_folder + "\\Keyword_Check_" + str(time.strftime('%Y%m%d-%H%M%S', time.localtime())) + "_" + fileList[i], sep=',', na_rep='', encoding='utf-8-sig', index = False)
        print("Keyword_Check_" + fileList[i] + " is created")
