from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from warnings import filterwarnings
filterwarnings("ignore")
import unittest


class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		browser = self.browser
		browser.get("https://campusvirtualunillanos.co/")
		numberList = browser.find_elements(By.CLASS_NAME, 'h-100')
		for number in numberList:
			rows = number.find_element(By.TAG_NAME, 'h3')
			
	  #3114
		self.assertIn("3113", rows.text, msg="Fallo en la comparacion de cursos")


	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()