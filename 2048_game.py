
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
#print(type(browser))

browser.get('https://gabrielecirulli.github.io/2048/')

#new_game_btn = browser.find_element("link text", "Give Feedback")
#new_game_btn.click()
#print(new_game_btn.tag_name)

print('Welcome to 2048 game')
html_tag = browser.find_element('tag name' , 'html')
flag = 0
while True:
    Menu = '\nChoose your moves: Left(L), Right(R), Up(U), Down(D) provide the short forms L, R, U and D only..'
    print(Menu)
    user_input = input(str("Enter your value: "))
    if user_input.upper() == "L":
        html_tag.send_keys(Keys.LEFT)
    elif user_input.upper() == "R":
        html_tag.send_keys(Keys.RIGHT)
    elif user_input.upper() == "U":
        html_tag.send_keys(Keys.UP)
    elif user_input.upper() == "D":
        html_tag.send_keys(Keys.DOWN)
    else:
        flag += 1
        print("Wrong input provide the options given in the menu")
    if flag == 5:
        print("Provided wrong inputs multiple times..")
        exit()
    
