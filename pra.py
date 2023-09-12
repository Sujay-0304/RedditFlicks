import praw
import tts 
import prac 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

from dotenv import load_dotenv
load_dotenv('.env')


reddit = praw.Reddit(
    client_id = os.getenv('ClientId'),
    client_secret=os.getenv('ClientSecret'),
    user_agent="test",
) 


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# login to reddit account using selenium 
# driver.get("https://www.reddit.com/login/")
# driver.find_element(By.ID, "loginUsername").click()
# # driver.find_element(By.ID, "loginUsername").send_keys(os.getenv('userName'))

# driver.find_element(By.ID, "loginPassword").send_keys(os.getenv('passWord'))
# element = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button")
# element.click()
# time.sleep(2)
subred = "askreddit"

subreddit = reddit.subreddit(subred)
top_posts = subreddit.hot(limit=1)
os.makedirs("Screenshots", exist_ok=True)

closeButton = True 

for post in top_posts:
    c = [] 

    post_url = f'https://www.reddit.com{post.permalink}'
    # print(post.title,post.id)
    print(post_url)
   
    driver.get(post_url)
    time.sleep(2)

    # if login is required, dont comment this line
    # if closeButton:
    #     driver.find_element(By.XPATH, f"//*[@id='SHORTCUT_FOCUSABLE_DIV']/div[4]/div/div/div/header/div/div[2]/button").click()
    #     closeButton = False
    # time.sleep(320)

    post_content_element = driver.find_element(By.XPATH, f"//*[@id='t3_{post.id}']")
    post_content_screenshot_filename = os.path.join("Screenshots",f'screenshot_{post.id}.png') 
    post_content_element.screenshot(post_content_screenshot_filename)
    
    tts.text_to_speech(post.title, f'{post.id}_title.mp3')
    for comments in post.comments[:1]:
        print("******")
        print(comments.body, comments.id)
        print(comments.permalink)
     
        
        # comment_content_element = driver.find_element(By.XPATH, f"//*[@id='t1_{comments.id}']/div[2]")
        comment_content_element = driver.find_element(By.XPATH, f"//*[@id='t1_{comments.id}-comment-rtjson-content']")
        comment_content_screenshot_filename = os.path.join("Screenshots", f'{post.id}_{comments.id}_comments.png')
        # comment_content_screenshot_filename = f'{post.id}_{comments.id}_comments.png'
        comment_content_element.screenshot(comment_content_screenshot_filename)
       
        tts.text_to_speech(comments.body, f'{post.id}_{comments.id}_comments.mp3') 
        #alll comments appending for now only 1 
        c.append(f'{post.id}_{comments.id}_comments')

    prac.merge_sc_audio(f'{post.id}_title.mp3', c, post_content_screenshot_filename)


driver.quit()
