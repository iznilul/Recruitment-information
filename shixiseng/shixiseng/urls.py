from urllib.parse import urlencode
class Geturls():
	def __init__(self):
		pass
	def start(self):
		data = {
			"type": "intern",
			"months": "",
			"days": "",
			"degree": "",
			"offiacal": "",
			"enterprise": "",
			"salary": -0,
			"publishTime": "",
			"sortType": "",
			"city": "全国"
		}
		params=urlencode(data)
		for job in ["Java","UI设计师", "Web前端", "PHP", "Python", "Android", "美工", "深度学习", "算法工程师", "Hadoop", "Node.js", "数据开发",
					"数据分析师", "数据架构", "人工智能", "区块链","电气工程","销售","金融","英语","数据挖掘","云计算","土木","物联网","通信工程","HR","PS",
					"半导体","新媒体","嵌入式","工商管理","R语言","产品经理","电子商务",]:
			url='https://www.shixiseng.com/interns/?keyword='
			job_url=url+job
			final_url=job_url+params
			# print(job_url)
			with open("urls.txt", "a+", encoding="utf-8")as file:
				file.write("\'" + final_url + "&"+"\'" + "," + "\n")

if __name__=="__main__":
	g=Geturls()
	g.start()