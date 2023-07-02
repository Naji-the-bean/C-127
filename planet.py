from bs4 import BeautifulSoup
from bs4 import soup
import time
import pandas as pd


START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"


time.sleep(10)

scraped_data = []

def scrape():
    #find <table>
    bright_star_table = soup.find("table", attrs={"class","wikitable"})

    #find <tbody>
    table_body = bright_star_table.find('tbody')

    #find <tr>
    table_rows = table_body.find_all('tr')

    #get data from <td>
    for row in table_rows:
        table_cols = row.find_all('td')
        #print(table_cols)

        temp_list = []

        for col_data in table_cols:
            #Print only colums textual data using ".text" property
            #print(col_data.text)

            #remove extra white spaces using strip()
            data = col_data.text.strip()
            #print(data)

            temp_list.append(data)

        #append data to star_data list
        scraped_data.append(temp_list)

stars_data = []

for i in range(0,len(scraped_data)):
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']

star_df_1 = pd.DataFrame('scraped_data.csv',index=True,index_label="id")