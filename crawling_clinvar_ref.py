from bs4 import BeautifulSoup
import pandas as pd
from html_table_parser import parser_functions as parser
import requests

a = []

with open("WS.txt") as f:
    for line in f:
        a.append(line.strip())
        print(line)


url = "https://www.ncbi.nlm.nih.gov/clinvar/variation/"
redir = "/?redir=vcv"
url2 = []
for value in a:
    v = value.strip("VCV")
    v2 = int(v)
    v3 = str(v2)
    url2.append(url + v3 + redir)

ll = []
for value in url2:
    r = requests.get(url=value)
    html2 = r.text
    bs = BeautifulSoup(html2, 'html.parser')
    temp = bs.find_all('table')
    p = parser.make2d(temp[5])
    df = pd.DataFrame(p)
    if len(df.columns) > 3:
        df = df[df.iloc[:, 3] != '-']
        df.iloc[:, 3] = df.iloc[:, 3].astype(int)
        df_sorted = df.sort_values(by=df.columns[3], ascending=[False])
        df2 = df_sorted.iloc[0:2, 4]
        tdf = df2.to_list()
        print(tdf)
    else:
        print("No citations")
