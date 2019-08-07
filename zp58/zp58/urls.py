from selenium import webdriver
import time
class Geturls():
	def __init__(self):
		pass
	def start(self):
		self.browser = webdriver.Chrome()
		self.browser.get("https://www.58.com/changecity/?PGTID=0d002408-0000-09ce-38c6-a1ce71d2f1dd&ClickID=1")
		time.sleep(2)
		current = self.browser.current_window_handle
		places=self.browser.find_elements_by_xpath('//*[@id="clist"]/dd/a')
		for place in places:
			print('\''+place.text+'\',')
		# 	place_url = place.get_attribute("href")
		# 	js = 'window.open("%s")' % place_url
		# 	self.browser.execute_script(js)
		# 	windows = self.browser.window_handles
		# 	self.browser.switch_to.window(windows[-1])
		# 	time.sleep(1)
		# 	try:
		# 		self.browser.find_element_by_xpath('//*[@id="zpNav"]/a/i')
		# 		a=True
		# 	except:
		# 		a=False
		# 	if a==True:
		# 		zp_button = self.browser.find_element_by_xpath('//*[@id="zpNav"]/a/i').click()
		# 		time.sleep(1)
		# 		windows = self.browser.window_handles
		# 		self.browser.switch_to.window(windows[-1])
		# 		button=self.browser.find_element_by_xpath('//*[@id="searJob"]/strong').click()
		# 		job_url = self.browser.current_url
		# 		print(job_url)
		# 		with open("urls.txt", "a+", encoding="utf-8")as file:
		# 			file.write("\'" + job_url + "\'" + "," + "\n")
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