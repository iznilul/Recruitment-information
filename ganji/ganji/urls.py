from selenium import webdriver
import time
class Geturls():
	def __init__(self):
		pass
	def start(self):
		self.browser=webdriver.Chrome()
		self.browser.get("http://www.ganji.com/index.htm")
		time.sleep(2)
		current=self.browser.current_window_handle
		redlink_places=self.browser.find_elements_by_class_name('redLink')
		for redlink_place in redlink_places:
			redlink_place_url=redlink_place.get_attribute("href")
			js = 'window.open("%s")' % redlink_place_url
			self.browser.execute_script(js)
			windows = self.browser.window_handles
			self.browser.switch_to.window(windows[-1])
			time.sleep(1)
			button=self.browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/dl[1]/dt/a/span[2]').click()
			time.sleep(1)
			windows = self.browser.window_handles
			self.browser.switch_to.window(windows[-1])
			jobs=self.browser.find_elements_by_xpath('//*[@class="f-all-news"]/dl/dd/i/a')
			for job in jobs:
				job_url=job.get_attribute("href")
				print(job_url)
				# with open("urls.txt","a+",encoding="utf-8")as file:
				# 	file.write("\'"+job_url+"\'"+","+"\n")
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
