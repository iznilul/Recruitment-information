from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
class Geturls():
	def __init__(self):
		pass
	def start(self):
		self.browser = webdriver.Chrome()
		self.browser.get("https://www.zhaopin.com/citymap")
		time.sleep(2)
		button=self.browser.find_element_by_xpath('//*[@class="risk-warning__content"]/button').click()
		current = self.browser.current_window_handle
		places=self.browser.find_elements_by_xpath('//*[@class="cities-show__list--href"]')
		for place in places:
			print('\''+place.text+"\',")
		# 	place_url = place.get_attribute("href")
		# 	time.sleep(0.5)
		# 	js = 'window.open("%s")' % place_url
		# 	self.browser.execute_script(js)
		# 	windows = self.browser.window_handles
		# 	self.browser.switch_to.window(windows[-1])
		# 	time.sleep(1)
		# 	try:
		# 		self.browser.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div/div/input')
		# 		a=True
		# 	except:
		# 		a=False
		# 	if a==True:
		# 		input=self.browser.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div/div/input')
		# 		input.send_keys("Java开发")
		# 		time.sleep(0.5)
		# 		query=self.browser.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div/div/a')
		# 		query.click()
		# 		windows = self.browser.window_handles
		# 		self.browser.switch_to.window(windows[-1])
		# 		for job in["UI设计师","Web前端","PHP","Python","Android","美工","深度学习","算法工程师","Hadoop","Node.js","数据开发","数据分析师","数据架构","人工智能","区块链"]:
		# 			job_url=self.browser.current_url
		# 			with open("urls.txt", "a+", encoding="utf-8")as file:
		# 				file.write("\'" + job_url + "\'" + "," + "\n")
		# 			input=self.browser.find_element_by_xpath('//*[@class="search-box__common__input"]')
		# 			time.sleep(0.5)
		# 			input.send_keys(Keys.CONTROL+'a')
		# 			input.send_keys(Keys.BACKSPACE)
		# 			input.send_keys(job)
		# 			time.sleep(0.5)
		# 			query=self.browser.find_element_by_xpath('//*[@class="search-box__common__btn search-box__common__btn--blue"]')
		# 			query.click()
		# 	allchung = self.browser.window_handles
		# 	for handle in allchung:
		# 		if handle != current:
		# 			self.browser.switch_to.window(handle)
		# 			self.browser.close()
		# 	self.browser.switch_to.window(current)
		# self.browser.quit()

if __name__=="__main__":
	g=Geturls()
	g.start()