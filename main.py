from os import link, name
# from selenium import webdriver
from bs4 import BeautifulSoup
from flask.globals import request
import requests


def bs(name):
    url=f"https://worldsubtitle.site/?s={name}"
    res=requests.get(url)
    soup=BeautifulSoup(res.content, "html.parser")
    my_divs= soup.find_all("div",{"class": "cat-post-titel"})
    result = list()
    for div in my_divs:
        for i in div.find_all("a"):
            result.append({
                "link": i["href"],
                "title": i["title"]
                
            }
                )
    return result

# print(f"name:{name}\nlinks:{link}")

def links(link):
    res=requests.get(link)
    soup=BeautifulSoup(res.content, "html.parser")
    my_divs_name = soup.find_all("div",{"class":"new-link-1"})
    my_divs_status = soup.find_all("div",{"class":"new-link-2"})
    my_divs_link = soup.find_all("div",{"class":"new-link-3"})
    name,status,linkk=[],[],[]
    for names in my_divs_name:
        name.append(names.text.strip())
    for statuss in my_divs_status:
        status.append(statuss.text.strip())
    for lin in my_divs_link:
        for l in lin.find_all("a"):
            linkk.append(l["href"])
    newlink=list()
    for i in range(len(name)):
        newlink.append({
            "name":name[i],
            "status": status[i],
            "link": linkk[i]
        })
    return newlink
    # print(f"names:{name}\nstatus:{status}\nlink:{linkk}")

def seleniumWork():
    browser = webdriver.Chrome(executable_path=r".\driver\chromedriver.exe")

    #https://worldsubtitle.site/category/movies/page/1663/
    link_movie = ["https://worldsubtitle.site/movies/white-eye-2019/"
                    ,"https://worldsubtitle.site/movies/jungle-cruise-2021/"
                    ,"https://worldsubtitle.site/movies/legacy-of-lies-2020/"
                    ,"https://worldsubtitle.site/movies/the-last-mercenary-2021/"
                    ,"https://worldsubtitle.site/movies/malignant-2021/"
                    ,"https://worldsubtitle.site/movies/mainstream-2020/"
                    ,"https://worldsubtitle.site/movies/cristiano-ronaldo-impossible-to-ignore/"
                    ,"https://worldsubtitle.site/movies/the-boy-behind-the-door-2020/"
                    ,"https://worldsubtitle.site/movies/grandmas-boy-2006/"
                    ,"https://worldsubtitle.site/movies/fast-furious-9-2021/"]
    link_movie = []
    count = 10
    for j in range(2, 1664):
        browser.get(f"https://worldsubtitle.site/category/movies/page/{str(j)}/")
        for i in range(1, 11):
            try:
                count += 1
                print(f"Id: {count}\nMovie Name: {browser.find_element_by_xpath(f'/html/body/div[2]/div[3]/div/div[{str(i)}]/div/div[2]/h2').text}\n{50*'='}")
                link_movie.append(browser.find_element_by_xpath(f'/html/body/div[2]/div[3]/div/div[{str(i)}]/div/div[2]/h2').get_attribute('href'))
            except Exception as e:
                print(f"Error = {e}")
    with open("movie_link", "w") as fp:
        for link in link_movie:
            fp.write(f"{link}\n")



if __name__ == "__main__":
    # seleniumWork()
    # bs("avengers")
    links('https://worldsubtitle.site/tv-series/%d8%af%d8%a7%d9%86%d9%84%d9%88%d8%af-%d8%b2%db%8c%d8%b1%d9%86%d9%88%db%8c%d8%b3-%d9%81%d8%a7%d8%b1%d8%b3%db%8c-%d8%b3%d8%b1%db%8c%d8%a7%d9%84-inside-no-9-2014/')