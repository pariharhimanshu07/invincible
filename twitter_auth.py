from flask import Flask, flash, redirect, render_template, request, session, abort,json
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from flask_httpauth import HTTPBasicAuth
from flask_json import FlaskJSON, JsonError, json_response, as_json
app = Flask(__name__)
FlaskJSON(app)
@app.route('/twitter')
def first_twitter():
    return tweet_run()
def tweet_run():
	one=request.args["one"]
	two=request.args["two"]
	driver = webdriver.Chrome(executable_path=r"C:\Users\C5261007\Desktop\chromedriver.exe") 		#call the webdriver
	driver.get("https://apps.twitter.com/") #call twitter
	sign=driver.find_element_by_css_selector("#globalnav > div > div.d-block.d-block-menu.signed-out.profile-menu > a")
	signin=sign.click()  		#click on sign-in
	user=driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input")
	user.send_keys(one)
	#user.send_keys("cruzoswanntechnologies@gmail.com") 		#enter user credentials
	password=driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input")
	password.send_keys(two)
	#password.send_keys("manchaster")
	password.send_keys(Keys.ENTER)		#enter password
	try:
		app=driver.find_element_by_css_selector("#no-apps > div > a")
		app.click()
		username=driver.find_element_by_id("edit-name")
		username.send_keys("himanshu121")
		description=driver.find_element_by_id("edit-description")
		description.send_keys("testcase for trial")
		website=driver.find_element_by_id("edit-url")
		website.send_keys("http://techub.org")
		website.send_keys(Keys.PAGE_DOWN)
		checkbox=driver.find_element_by_id("edit-tos-agreement")
		checkbox_final=driver.execute_script("arguments[0].click();", checkbox)
		checkbox.send_keys(Keys.ENTER)
	except:
		app=driver.find_element_by_css_selector("#gaz-content-body > div.d-block.d-block-system.g-main > div > ul > li > div > div.app-details > h2 > a").click()
		keys=driver.find_element_by_css_selector("#gaz-content-body > div.tabs > ul > li:nth-child(3) > a").click()
		consumerkey=driver.find_element_by_css_selector("#gaz-content-body > div.d-block.d-block-system.g-main > div > div.app-settings > div:nth-child(1)").text
		print consumerkey
		consumerapi=driver.find_element_by_css_selector("#gaz-content-body > div.d-block.d-block-system.g-main > div > div.app-settings > div:nth-child(2)").text
		print consumerapi
		permission=driver.find_element_by_css_selector("#gaz-content-body > div.tabs > ul > li:nth-child(4) > a").click()
		permission1=driver.find_element_by_id("edit-access-level-2").click()
		permission2=driver.find_element_by_id("edit-submit")
		driver.execute_script("arguments[0].click();", permission2)
		file=open('credential_twitter.txt', 'a')
		file.write(consumerkey+"\n"+consumerapi)
		file.close()
	
	
	#driver.quit()
	return "success"
	

if __name__ == "__main__":
	app.run(debug=True,threaded=True)