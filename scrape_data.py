import requests
from bs4 import BeautifulSoup
import sys
import save


# REQUESTING DATA FROM URL
url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
response = requests.get(url)

#  FINDING RELEVENT DATA
soup = BeautifulSoup(response.text,'html.parser')
sys.stdout.reconfigure(encoding='utf-8')
content = soup.find("table",class_="wikitable")
tablebody = content.find("tbody")
items = tablebody.find_all("tr")



data=[]
# ITERATING OVER DATA AND GETTING MEANINGFULL DATA OUT OF IT
for item in items:
        
        row=[]
        for cell in item.find_all("td"):
                print(cell.text)
                row.append(cell.text.split("\n")[0])
        
        if(row!=[]):
            data.append(row)
        row=[]

    
print(data)

# SAVING DATA WITH A FUNCTION IN ANOTHER FILE
save.save(data)
