from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
class Geturls():
	def __init__(self):
		pass
	def start(self):
		self.browser = webdriver.Chrome()
		self.browser.get("http://www.yingjiesheng.com/")
		time.sleep(2)
		current = self.browser.current_window_handle
		places=self.browser.find_elements_by_xpath('//*[@class="menu"]/ul/li/a')
		for place in places:
			place_url = place.get_attribute("href")
			js = 'window.open("%s")' % place_url
			self.browser.execute_script(js)
			windows = self.browser.window_handles
			self.browser.switch_to.window(windows[-1])
			time.sleep(2)
			try:
				self.browser.find_element_by_xpath('//*[@class="jobMore s_clear"]/a')
				a=True
			except:
				a=False
			if a==True:
				more=self.browser.find_element_by_xpath('//*[@class="jobMore s_clear"]/a')
				more_url=more.get_attribute("href")
				js = 'window.open("%s")' % more_url
				self.browser.execute_script(js)
				windows = self.browser.window_handles
				self.browser.switch_to.window(windows[-1])
				job_url=self.browser.current_url
				with open("urls.txt", "a+", encoding="utf-8")as file:
					file.write("\'" + job_url + "\'" + "," + "\n")
			elif a==False:
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