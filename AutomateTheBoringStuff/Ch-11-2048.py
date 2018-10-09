"""
2048 is a simple game where you combine tiles by sliding them up, down,
left, or right with the arrow keys. You can actually get a fairly high
score by repeatedly sliding in an up, right, down, and left pattern over
and over again. Write a program that will open the game at
https://gabrielecirulli.github.io/2048/ and keep sending up, right, down,
and left keystrokes to automatically play the game.
"""
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://gabrielecirulli.github.io/2048/")
html = driver.find_element_by_tag_name('html')
    
while True:
    html.send_keys(Keys.UP)
    html.send_keys(Keys.RIGHT)
    html.send_keys(Keys.DOWN)
    html.send_keys(Keys.LEFT)
    if(driver.find_elements_by_class_name("game-over")):
        break
score = driver.find_element_by_class_name("score-container")
print("You Scored : ", score.text)