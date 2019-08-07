from selenium import webdriver
import time
class Geturls():
	def __init__(self):
		pass
	def start(self):
		self.browser = webdriver.Chrome()
		self.browser.get("https://www.lagou.com/")
		time.sleep(2)
		self.browser.find_element_by_xpath('//*[@id="cboxClose"]').click()
		time.sleep(1)
		current = self.browser.current_window_handle
		jobs=self.browser.find_elements_by_xpath('//*[@class="category-list"]/a')
		for job in jobs:
			url=job.get_attribute("href")
			js = 'window.open("%s")' % url
			self.browser.execute_script(js)
			windows = self.browser.window_handles
			self.browser.switch_to.window(windows[-1])
			time.sleep(1)
			job_url=self.browser.current_url
			print(job_url)
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