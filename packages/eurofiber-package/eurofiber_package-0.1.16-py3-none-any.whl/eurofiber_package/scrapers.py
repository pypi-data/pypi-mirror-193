# import packages
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from eurofiber_package.general_functions import *
import random
import requests


def nox_scraper(pc_hn, formatting = False):
    """ this function scrapes the nox postcode checker, requires as input a dataframe with two columns: 'PC6' and 'House number' """

    # create empty output dataframe
    dataframe = pd.DataFrame()

    # iterate over rows to scrape information
    for index, row in pc_hn.iterrows():
        try:
            postal_code = row['PC6']
            house_number = str(row['House number']).replace('.0', '')        

            # Set up web driver
            options = webdriver.ChromeOptions()
            options.headless = True    
            driver = webdriver.Chrome(options=options)

            # Navigate to website
            # driver.get('https://noxtelecom.nl/glasvezel-internet-postcodecheck/')
            driver.get('https://noxpocos.azurewebsites.net/Pocos?Tag=PCN.internet')

            # fill in postcode
            postcode = driver.find_element(By.ID, "Zipcode")
            postcode.send_keys(postal_code)

            # fill in housenumber
            housenumber = driver.find_element(By.ID, "Number")
            housenumber.send_keys(house_number)     

            # # fill in suffix
            # suffix = driver.find_element(By.ID, "NumberAddition")
            # suffix.send_keys(house_number_suffix)

            # click
            driver.find_element(By.XPATH, ".//*[@class='btn btn-primary']").click()

            # retrieve information
            soup = BeautifulSoup(driver.page_source, 'lxml')
            spec_table = soup.find('table', {'class':'table table-striped btn-table scaletable'})

            # scrape columns
            columns_list = []
            for row in spec_table.thead.find_all('th'):
                columns_list.append(row.getText())

            # scrape info
            information = []
            for row in spec_table.tbody.find_all('tr'):
                values_list = []
                for value in row.find_all('td'):
                    values_list.append(value.getText())
                information.append(values_list)

            # create dataframe
            output = pd.DataFrame(information, columns=columns_list)

            # create variables
            output['Postal Code'] = postal_code
            output['House Number'] = house_number
            output['ID'] = output['Postal Code'].fillna('').astype(str) + output['House Number'].fillna('').astype(int).astype(str)# + output['Suffix'].fillna('').astype(str)

            # change order
            output = output[['ID', 'Postal Code', 'House Number'] + columns_list]       

            # concat
            dataframe = pd.concat([output, dataframe])  

            # close
            driver.quit()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        except:
            print('{} + {} failed'.format(postal_code, house_number))

        print('iteration {} done'.format(index))

        # set random intervals between requests (https://www.scraperapi.com/blog/10-tips-for-web-scraping/)    
        time.sleep(random.choice([0,1,2]))


    # output
    dataframe = dataframe.reset_index(drop=True)

    # formatting
    if formatting == False:
        return dataframe

    else:
        # glasvezel zakelijk
        dataframe['zakelijk_glasvezel'] = dataframe['Technologie'].apply(lambda x: zakelijk_glasvezel(x))
        dataframe = suppliers_per_technology(dataframe, 'zakelijk_glasvezel')
        dataframe['zakelijk_glasvezel'] = dataframe.groupby(['ID'])['zakelijk_glasvezel'].transform('max')
        dataframe['nr_suppliers_zakelijk_glasvezel'] = dataframe['leveranciers_zakelijk_glasvezel'].apply(lambda x: unique_suppliers(x))

        # dsl
        dataframe['DSL'] = dataframe['Technologie'].apply(lambda x: dsl(x))
        dataframe = suppliers_per_technology(dataframe, 'DSL')
        dataframe['DSL'] = dataframe.groupby(['ID'])['DSL'].transform('max')
        dataframe['nr_suppliers_DSL'] = dataframe['leveranciers_DSL'].apply(lambda x: unique_suppliers(x))

        # ftth
        dataframe['FttH'] = dataframe['Technologie'].apply(lambda x: ftth(x))
        dataframe = suppliers_per_technology(dataframe, 'FttH')
        dataframe['FttH'] = dataframe.groupby(['ID'])['FttH'].transform('max')
        dataframe['nr_suppliers_FttH'] = dataframe['leveranciers_FttH'].apply(lambda x: unique_suppliers(x))

        # 4g internet
        dataframe['4G'] = dataframe['Technologie'].apply(lambda x: g4_internet(x))
        dataframe = suppliers_per_technology(dataframe, '4G')
        dataframe['4G'] = dataframe.groupby(['ID'])['4G'].transform('max')
        dataframe['nr_suppliers_4G'] = dataframe['leveranciers_4G'].apply(lambda x: unique_suppliers(x))  

        # output
        output = dataframe[['ID', 'Postal Code', 'House Number',
            'zakelijk_glasvezel', 'leveranciers_zakelijk_glasvezel',
            'nr_suppliers_zakelijk_glasvezel', 'DSL', 'leveranciers_DSL',
            'nr_suppliers_DSL', 'FttH', 'leveranciers_FttH', 'nr_suppliers_FttH',
            '4G', 'leveranciers_4G', 'nr_suppliers_4G']].drop_duplicates().reset_index(drop=True)

        return output              


def zakelijk_glasvezel(item):
    item  = item.lower().strip()
    if ('zakelijk' in item and 'glasvezel' in item) or item=='glasvezel':
        return True
    else:
        return False
    
def dsl(item):
    item  = item.lower().strip()
    if 'dsl' in item:
        return True
    else:
        return False
    
def ftth(item):
    item  = item.lower().strip()
    if 'ftth' in item:
        return True
    else:
        return False
    
def g4_internet(item):
    item  = item.lower().strip()
    if '4g' in item:
        return True
    else:
        return False
    

def suppliers_per_technology(dataframe, technology):
    try:
        new_column = 'leveranciers_' + str(technology)
        dataframe[new_column] = dataframe[dataframe[technology]==True].groupby(['ID'])['Leverancier'].transform(lambda x: ' / '.join(x))
        dataframe[new_column] = dataframe[new_column].apply(lambda x: ' / '.join(set(x.split(' / '))) if x not in [np.nan] else np.nan)

        merger_dataframe = dataframe[['ID', new_column]].dropna().drop_duplicates()
        dataframe = dataframe.drop(new_column, axis=1)
        dataframe = dataframe.merge(merger_dataframe, how='left', on='ID')
        return dataframe
    except:
        new_column = 'leveranciers_' + str(technology)        
        dataframe[new_column] = np.nan
        return dataframe
    

def unique_suppliers(item):
    try:
        return len(item.split(' / '))
    except:
        return 0


def bs4_scraper(url):
    """ this function scrapes a webpage using standard beautifulsoup """
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.prettify()