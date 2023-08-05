from bs4 import BeautifulSoup
import requests

# this is url of Xeven Skills Website
url = requests.get("https://xevenskills.com/").text
soup = BeautifulSoup(url , "lxml")

# Collect div of teachers
teachers = soup.find_all("div" , class_ = "col-md-3 col-sm-4 col-xs-6 teacher-col")
a = 1
for item in teachers:
    teacher_name = item.find("h4",class_ = "title").text
    teacher_skill = item.find("div",class_ = "job heading_font").text
    print(f"Serial # {a}")
    print("Teacher name : ",teacher_name)
    print("Course : ",teacher_skill)
    print("")
    a+=1