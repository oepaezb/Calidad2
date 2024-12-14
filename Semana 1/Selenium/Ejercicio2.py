from selenium import webdriver
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("https://google.com/")
time.sleep(1) #Mostrar despues
browser.execute_script("window.open('');") #Carga en background el primero
time.sleep(1)
browser.switch_to.window(browser.window_handles[1]) #Para abrir una ventana nueva 1, porque ya se abrio la cero
time.sleep(1)
browser.get("https://facebook.com/")
browser.execute_script("window.open('');") #Carga en background el primero
time.sleep(1)
browser.switch_to.window(browser.window_handles[2]) 
browser.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
time.sleep(2)
browser.switch_to.window(browser.window_handles[0]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[1]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[2]) 

browser.quit()






