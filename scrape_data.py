import requests
from bs4 import BeautifulSoup
import sys
import save
import crud

# REQUESTING DATA FROM URL
url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"
response = requests.get(url)

#  FINDING RELEVENT DATA
soup = BeautifulSoup(response.text,'html.parser')
sys.stdout.reconfigure(encoding='utf-8')
#   FINDING ELEMENT FROM WEBPAGE TO GET THE TABLE
content = soup.find("table",class_="wikitable")
tablebody = content.find("tbody")
items = tablebody.find_all("tr")


data=[]
# ITERATING OVER DATA AND GETTING MEANINGFULL DATA OUT OF IT
for item in items:
        
        row=[]
        for cell in item.find_all("td"):
                # print(cell.text)
                row.append(cell.text.split("\n")[0])
        
        if(row!=[]):
            data.append(row)
        row=[]

    
# print(data)

# SAVING DATA WITH A FUNCTION IN ANOTHER FILE
save.save(data)

# USE THIS FUNCTION TO INSERT DATA TO DATABASE, ARGUMENTS PASSED ARE IN SERIES AS [rank , name ,industry,revenue,headquarters]
# crud.insert(["53","aba","asd","122","adsf"])


#  USE THIS FUNCTION TO DELETE DATA FROM DATABASE AND ARGUMENTS PASSED ARE (rank , name)
# crud.delete(["53","aaa"])


# USE THIS FUNCTION TO UPDATE VALUE IN DATABASE AND ARGUMENTS PASSED ARE ( NEW_RANK ,NEW_NAME ,NEW_INDUSTRY ,NEW_REVENUE ,NEW_HEADQUARTERS ,RANK_OF_DATA_TO_BE_UPDATED ,NAME_OF_DATA_TO_BE_UPDATED)
#  IF YOU DONT WANT TO UPDATE ANY VALUE THAN SIMPLY REMAIN THAT FIELD BLANK AS ("")
crud.update(["5","","12","aa","aa","52","Adyar Ananda Bhavan"])