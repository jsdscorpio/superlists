from selenium import webdriver
import unittest
class NewVistorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		#Selenium在操作之前等待页面完加载方面的表现尚可
		self.browser.implicitly_wait(3) #告诉Selenium，如果需要就等待几秒钟。即等待3秒，让内容出现
	def tearDown(self):
		self.browser.quit()
	def test_can_strat_a_lsi_and_retrieve_it_later(self):
		#伊迪斯听说有一个很酷的在线待办事项应用
		#她去看了这个应用的首页
		self.browser.get('http://local:8000')
		#她注意到网页的标题和头部都包含？“To—Do"这个词
		self.assertIn('To-Do'.self.browser.title)
		self.fali('Finish the test')
		#应用邀请她输入一个待办事项
		#她在文本框中输入一个“Buy peakcock feathers"
		#伊迪斯的爱好是使用假蝇做饵钓鱼
		#她按回车键后，页面刷新了
		#待办事项百个中显示了一个文本框，可以输入其他的待办事项
		#她输入了“use peacock feathers to make a fly"
		#伊迪斯做事很有条理
		#页面再次更新，他的氢弹中显示了两个待办事项
		#伊迪斯想知道这个网站是否会记住她的清单
		#她看到网站为她生成一个唯一的URL
		#而且页面中有一些文字解说这个功能
		#她访问那个URL,发现他的待办事项列表还在
		#她很满意，去睡觉了
		
		


if __name__ =='__main__':
	unittest.main(warnings='ignore')



