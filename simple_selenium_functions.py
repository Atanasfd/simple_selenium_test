from selenium import webdriver
import os

x = os.getcwd()

browser = webdriver.Chrome()
browser.get(x+r"/target_1.html")

#get the text values of <p> and the id
paragraph=browser.find_element_by_tag_name("p")
print(paragraph.text)
print(browser.find_element_by_id('one').text)

#write in the input
inputt=browser.find_element_by_tag_name('input')
inputt.send_keys("I wrote")

#get the value of the css color
print(browser.find_element_by_tag_name("h1").value_of_css_property("color"))

#click on the button
browser.find_element_by_tag_name("button").click()

#get the alert's text and close it
alert=browser.switch_to_alert()
print(alert.text)
alert.accept()
