from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
from time import sleep

edge_options = EdgeOptions()
edge_options.use_chromium = True 
edge_options.add_argument('headless')
edge_options.add_argument('disable-gpu')
url = 'https://www.epicgames.com/store/en-US/free-games'
edge= Edge(executable_path='E:\VSCODE folders\Python\screenshotter\webdriver\msedgedriver.exe', options=edge_options)
edge.maximize_window
#edge.execute_script("document.body.style.zoom='zoom 10%'")
#edge.execute_script("window.scrollTo(0, 1)")
#edge.implicitly_wait(10)
edge.get(url)
sleep(5)
edge.find_element_by_id('onetrust-accept-btn-handler').click()
#edge.implicitly_wait(100)
try:
    edge.find_element_by_id('onetrust-accept-btn-handler').click()
except Exception as e:
    print(e)

try:
    elem=WebDriverWait(edge,30).until(EC.visibility_of_element_located(By.ID,"css-1myhtyb"))
except Exception as e:
    print(e)  
finally:
    sleep(5)
    image = edge.find_element_by_class_name('css-1myhtyb') #css-1myhtyb css-2u323 css-1i5exm2 css-1i5exm2
    image.screenshot('epicgams.png')
    edge.implicitly_wait(30)
    edge.close()
