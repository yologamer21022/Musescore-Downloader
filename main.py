from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import download_manager
import image_converter

link = input("Input Link:   ")
img = []

image_converter.clearCache()
#Get Image Class
def searchImg(class_name):
    div = driver.find_elements_by_class_name(class_name)
    return div

driver = webdriver.Chrome("chromedriver.exe")
driver.get(link)
time.sleep(3)
scrolling_div = driver.find_element_by_id("jmuse-scroller-component")
#Scroll
def scroll(divs):
    #driver.execute_script(jsScript, scrolling_div)
    for i in divs:
        ActionChains(driver).move_to_element(i).perform()
        time.sleep(1)

        try:
            img.append(i.find_element_by_class_name("KfFlO").get_attribute("src"))
        except:
            pass

divs = searchImg("EEnGW")

scroll(divs)

driver.close()

download_manager.imgDownloader(img)