import json
import os 
import re
from selenium import webdriver
from selenium import common 
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urljoin
from selenium.webdriver.common.alert import Alert
path = "C:\\testfile\\dadga\\temp\\files\\"

def driver_start():

	#print(requests.get(self.login_url,headers=request_header))  # fresh cookies
	#webbrowser.open("https://google.com")
	options = webdriver.ChromeOptions()
	#options.add_argument('headless')
	options.add_argument("disable-infobars")
	options.add_argument('--no-sandbox')
	options.add_argument("--disable-notifications")
	options.add_argument("--disable-extensions")
	#options.add_argument('--disable-dev-shm-usage')

	path = 'chromedriver'

	driver = webdriver.Chrome(path,chrome_options=options)
	session_id = driver.session_id
	print("session_id :", session_id)
	
	driver.implicitly_wait(5)
	
	return driver

def main(driver):

	for item in (os.listdir(path)):
		if not item.endswith('side'):
			continue

		buf = ''
		
		with open(path+item ,'r',encoding='utf-8') as f:
		# with open("test5.side" ,'r',encoding='utf-8') as f:

			buf = f.read()
		json_buf = json.loads(buf)

		# print(json_buf.keys())
		print("filename :", item)
		print(json_buf['name'])
		print(json_buf['url'])
		try:
			alert_check = Alert(driver).accept()
			print("alert_check : " ,alert_check)
			Alert(driver).dismiss()

		except Exception as e:
			pass
			
		driver.delete_all_cookies()
		driver.get(json_buf['url'])


		driver.implicitly_wait(5)

		for i in json_buf['tests'][0]['commands']:

			if i['command'] =='open':

				driver.get(urljoin(driver.current_url,i['target']))

			elif i['command'] =='click': #commands
				print("click")

				for candidate in (i['targets']):
					# print(candidate)

					if candidate[-1] =='xpath:href':
						print('href move')
						print(candidate[0].split('xpath=')[-1])

						try:
							if 'contain' in candidate[0].split('xpath=')[-1]:
								target_url = (re.findall(r"@href, '(.+)'\)",candidate[0])[0])
								if 'javascript' in target_url.lower():
									continue
								driver.get(urljoin(driver.current_url,target_url))
							elif '@href=' in candidate[0].split('xpath=')[-1]:
								target_url = (re.findall(r"@href\=\'(.+)\'",candidate[0])[0])
								if 'javascript' in target_url.lower():
									continue
								driver.get(urljoin(driver.current_url,target_url))

						#print([x for x in re.findall(r"@href\=\'(.+)\'|@href, '(.+)'\)",candidate[0]) if len(x)][0])
						except IndexError as e:
							print('java check')
							with open('error.log','w') as f:
								f.write(json_buf['url'])
								f.write('\n')
								f.write(str(e))
								f.write('\n')
							pass
							
						except common.exceptions.UnexpectedAlertPresentException as e:
							print("dismiss error")
							Alert(driver).dismiss()

					elif candidate[-1] == 'xpath:idRelative':

						print('directly move')
						print(candidate[0].split('xpath=')[-1])
						try:
							driver.find_element_by_xpath(candidate[0].split('xpath=')[-1]).click()
							driver.implicitly_wait(5)
							break
						except:
							print('pass')
							pass
						
					elif candidate[-1] == 'xpath:link':

						print('link move')
						print(candidate[0].split('xpath=')[-1])
						try:
							driver.find_element_by_xpath(candidate[0].split('xpath=')[-1]).click()
							driver.implicitly_wait(5)
							break
						except:
							print('pass')
							pass		

					# elif candidate[-1] == 'xpath:position':
					# 	print('xpath position click')
					# 	print(candidate[0].split('xpath=')[-1])
					# 	driver.find_element_by_xpath(candidate[0].split('xpath=')[-1]).click()
					# 	driver.implicitly_wait(5)
					elif candidate[-1]  =='xpath:attributes':
						print('xpath click')
						print(candidate[0].split('xpath=')[-1])
						try:
							driver.find_element_by_xpath(candidate[0].split('xpath=')[-1]).click()
							driver.implicitly_wait(5)
							break
						except:
							print('pass')
							pass

					elif candidate[-1]  =='xpath:img':
						print('xpath img click')
						print(candidate[0].split('xpath=')[-1])
						try:
							driver.find_element_by_xpath(candidate[0].split('xpath=')[-1]).click()
							driver.implicitly_wait(5)
							break
						except:
							print('pass')
							pass

			elif i['command'] == 'type': #type
				print("typing")
				
				for candidate in (i['targets']):
					if candidate[-1] == 'xpath:attributes':
						print('xpath element')
						print(candidate[0].split('xpath=')[-1])
						print(i['value'])
						try:
							alert_check = Alert(driver).accept()
							print("alert_check : " ,alert_check)
							Alert(driver).dismiss()

						except Exception as e:
							pass

						try:
							driver.find_element_by_xpath(candidate[0].split('xpath=')[-1]).send_keys(i['value'])
							driver.implicitly_wait(5)
							break
						# except common.exceptions.UnexpectedAlertPresentException as e:
						# 	print("dismiss error")
						# 	Alert(driver).dismiss()
						# 	driver.find_element_by_xpath(candidate[0].split('xpath=')[-1]).send_keys(i['value'])
						# 	driver.implicitly_wait(5)
						# 	break
						except common.exceptions.NoSuchElementException as e:
							print(e)
							print("check needed")
							with open('error.log','w') as f:
								f.write(json_buf['url'])
								f.write('\n')
								f.write(str(e))
								f.write('\n')
							break
													
						
			print('---'*5)

		print('---end---')
		# time.sleep(10)

		break


if __name__ == '__main__':
	driver = driver_start()
	main(driver)
	driver.quit()
