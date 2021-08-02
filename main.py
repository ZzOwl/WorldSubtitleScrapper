from os import link, name
from selenium import webdriver
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
    seleniumWork()