from selenium import webdriver
import time
from lxml import html
class Geturls():
	def __init__(self):
		pass
	def start(self):
		self.browser = webdriver.Chrome()
		self.browser.get("https://www.51job.com/")
		time.sleep(2)
		current = self.browser.current_window_handle
		hot_places=self.browser.find_elements_by_xpath('//*[@class="li"]/a')
		for hot_place in hot_places:
			hot_place_url = hot_place.get_attribute("href")
			js = 'window.open("%s")' % hot_place_url
			self.browser.execute_script(js)
			windows = self.browser.window_handles
			self.browser.switch_to.window(windows[-1])
			time.sleep(1)
			button = self.browser.find_element_by_xpath('//*[@id="supp"]/div[1]/div/div[1]/button').click()
			time.sleep(1)
			while True:
				try:
					self.browser.find_element_by_xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li[8]/a')
					a=True
				except:
					a=False
				if a==True:
					jobs = self.browser.find_elements_by_css_selector(".t1 span a")
					for job in jobs:
						job_url = job.get_attribute("href")
						with open("urls.txt", "a+", encoding="utf-8")as file:
							file.write("\'" + job_url + "\'" + "," + "\n")
					next_page=self.browser.find_element_by_xpath('//*[@id="resultList"]/div[55]/div/div/div/ul/li[8]/a').click()
				elif a==False:
					break
			allchung = self.browser.window_handles
			for handle in allchung:
				if handle != current:
					self.browser.switch_to.window(handle)
					self.browser.close()
			self.browser.switch_to.window(current)
		self.browser.quit()

if __name__=="__main__":
	g=Geturls()
	g.start()