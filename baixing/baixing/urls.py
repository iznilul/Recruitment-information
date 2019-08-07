from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
class Geturls():
	def __init__(self):
		pass
	def start(self):
		self.browser = webdriver.Chrome()
		self.browser.get("https://www.baixing.com/?changeLocation=yes&return=%2Fgongzuo%2F")
		time.sleep(2)
		current = self.browser.current_window_handle
		places=self.browser.find_elements_by_xpath('//*[@class="city-item city-county-item"]/a')
		Directly_administered=self.browser.find_elements_by_xpath('/html/body/ul[1]/li[3]/ul/li/a')
		all_places=places+Directly_administered
		for place in all_places:
			place_url = place.get_attribute("href")
			js = 'window.open("%s")' % place_url
			self.browser.execute_script(js)
			windows = self.browser.window_handles
			self.browser.switch_to.window(windows[-1])
			time.sleep(1)
			job_url=self.browser.current_url
			with open("urls.txt", "a+", encoding="utf-8")as file:
				file.write("\'" + job_url + "\'" + "," + "\n")
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