import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
# for selenium webdriver to work use export PATH=$PATH:/home/martin/Downloads

class WebPageLoader(object):
	"""Initialize webdriver, load a webpage"""
	def __init__(self, url):
		self.r = requests.get(url)
		try:
			self.r.raise_for_status
		except:
			print("status code {}, try again later".format(self.r.status_code))

		self.url = url

		self.driver = webdriver.Firefox()

		self.driver.get(self.url)

class AnimeDownload(WebPageLoader):
	"""takes in key word, open relevant result 
	go to video page and download video"""
	def __init__(self, url):
		super().__init__(url)
		self.kw = input("enter kw")

	def search(self):
		input_element = self.driver.find_element(By.CLASS, "input-search")
		input_element.send_text(self.kw)
		# select relevant result

	def goto_download_page(self):
		# navigate to download link
		# wait for download to complete
		# goto to next link and navigate again
		pass

class InfoScraper(WebPageLoader):
	"""goto anime page click the random button
	check anime rating return anime info"""
	def __init__(self, url):
		super().__init__(url)
		markup = open("html_file.txt", "b")
		for chunk in self.r.iter_content(100000):
			markup.write(chunk)
		self.soup = bs4.BeautifulSoup(markup, 'lxml')

	def click_random(self):
		"""using private method to find element
		 private objects are useful in locating page objects
		 page objects means maintability of project"""
		self.random_button = self.driver.find_element(By.LINK_TEXT, '/anime/random')
		self.random_button.click()

	def scrap_info(self):
		"""Scrap anime info if rating greater than 3.7"""
		soup = self.soup
		self.score = soup.find('div', class_ = 'title').get_text()
		if self.score >= 3.7 :
			self.keys = soup.find_all('small').get_text()
			self.values = soup.find_all('div', class_ = 'title').get_text()
			self.general_info = zip(dict(keys, values))

			print(self.general_info)
			#self.synopsis = soup.select('p.max.hieght.70.px')
			
