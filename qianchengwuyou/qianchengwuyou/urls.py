from selenium import webdriver
import time
class Geturls():
	def __init__(self):
		pass
	def start(self):
		self.browser = webdriver.Chrome()
		self.browser.get("https://www.51job.com/")
		time.sleep(2)
		current = self.browser.current_window_handle
		button = self.browser.find_element_by_xpath('//*[@id="area_channel_homepage_more"]').click()
		areas=self.browser.find_elements_by_xpath('//*[@id="area_channel_homepage_list"]/li')
		# places=self.browser.find_elements_by_xpath('//div[@class="li"]/a')
		# for place in places:
		# 	print("\'"+place.text+"\',")
		for area in areas:
			time.sleep(1)
			area.click()
			time.sleep(1)
			places=self.browser.find_elements_by_xpath('//*[@id="area_channel_homepage_all"]/div[@style="display: block;"]/span/a')
			for place in places:
				place_url=place.get_attribute("href")
				js = 'window.open("%s")' % place_url
				self.browser.execute_script(js)
				windows = self.browser.window_handles
				self.browser.switch_to.window(windows[-1])
				time.sleep(1)
				button = self.browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[1]/button').click()
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