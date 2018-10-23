import bs4
import requests
from selenium import webdriver

class WebPageLoader:
	"""Initialize webdriver, load a webpage"""
	def __init__(self, url):
		self.r = requests.get(url)
		try:
			self.r.status_code
		except:
			print("status code {}, try again later".format(self.r.status_code))

		self.url = url

		self.driver = webdriver.Firefox()

		self.driver.get(self.url)

