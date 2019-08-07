from urllib.parse import urlencode
start_urls = ['http://s.cjol.com/?SearchType=3&RecruitmentType=1&defaultmust=0&',
                  'http://s.cjol.com/?SearchType=3&RecruitmentType=2&defaultmust=0',
                  'http://s.cjol.com/?SearchType=3&RecruitmentType=3&defaultmust=0']
data={
	"page":1
}
for url in start_urls:
	params=urlencode(data)
	new_url=url+params
	print(new_url)