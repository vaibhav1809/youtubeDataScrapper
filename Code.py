from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import csv


def getData(url):
    try:
        driver.get(url)
        driver.implicitly_wait(3)
        views = driver.find_element_by_css_selector("#count.style-scope.ytd-video-primary-info-renderer yt-view-count-renderer.style-scope.ytd-video-primary-info-renderer span.view-count.style-scope.yt-view-count-renderer").text
        dates = driver.find_element_by_css_selector("#date.style-scope.ytd-video-primary-info-renderer yt-formatted-string.style-scope.ytd-video-primary-info-renderer").text
        like_obj = driver.find_elements_by_css_selector("#text.style-scope.ytd-toggle-button-renderer.style-text")
        likes = like_obj[0].text
        dislikes = like_obj[1].text
        data = [url, views, dates, likes, dislikes]
        return data
    except Exception:
        return []


if __name__ == "__main__":
    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option)
    driver.implicitly_wait(5)

    with open('Data.csv', mode='w', newline="") as data:
        data_line = csv.writer(data)
        with open('Links.csv', mode='r') as file:
            csvFile = csv.reader(file, delimiter=',')
            first_line = True
            for lines in csvFile:
                if first_line:
                    first_line=False
                    data_line.writerow(['url', 'Views', 'Date_Uploaded', 'Likes', 'Dislikes'])
                else:
                    url = lines[0]
                    DataEntry = getData(url)
                    data_line.writerow(DataEntry)
    print("Successfully Executed!!!")
