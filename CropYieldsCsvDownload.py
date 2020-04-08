from selenium import webdriver
import time
if __name__ == '__main__':
    driver = webdriver.Chrome("C:\\Users\\Baazigar\\PycharmProjects\\SeleniumTest\\Driver\\chromedriver.exe")
    driver.set_page_load_timeout("30")      #time taken to load the webpage
    driver.get("https://ourworldindata.org/crop-yields")
    driver.maximize_window()
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/button").click()
    time.sleep(10)  #to load the contents

    y = 1000                                                       #Charts on the website takes some time to download,
    for timer in range(0,30):                                      #so to scroll the page throughout the screen first and
        driver.execute_script("window.scrollTo(0, "+str(y)+")")    #load the charts beforehand :
        y += 1000
        time.sleep(2)

    for i in range(1,36):
        #time.sleep(10)
        driver.find_elements_by_xpath('//a[@data-track-note="chart-click-data"]')[i].click()
        time.sleep(3)
        l = driver.find_element_by_xpath('//a[@data-track-note="chart-download-csv"]')
        l.click()
        print (l.text,"downloaded")
        time.sleep(5)   #you can increase this if file takes time to download
        driver.find_elements_by_xpath('//a[@data-track-note="chart-click-chart"]')[i].click()
        time.sleep(3)
    driver.quit()


