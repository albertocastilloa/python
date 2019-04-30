
import requests
from bs4 import BeautifulSoup
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
print(soup.p) #Get code for the first <p> tag
print(soup.p.string) #Get the string of <p> tag


for child in soup.div: #Get child nodes from first <div> tag that are inside
  print(child)