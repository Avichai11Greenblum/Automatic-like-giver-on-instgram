from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pgu


def like_pics(pic_location):
    # first we need to get the first pic and then activate like and move to the number of pics
    # that we want

    # first pic
    time.sleep(3)
    pgu.click(pic_location)
    time.sleep(1)

    global pics_num
    for i in range(pics_num):
        like_and_next()


# A function that gives a like and goes to the next picture
def like_and_next():
    pgu.click((1567, 585))  # move to the next the photo
    time.sleep(1.5)
    give_a_like()
    time.sleep(1.5)


def give_a_like():
    global driver
    action_area = driver.find_element_by_class_name('ltpMr Slqrh')
    like_button = driver.find_element_by_class_name('fr66n')
    like_pos = get_cords(action_area[like_button])
    print(like_pos)
    pgu.click(like_pos)



# A function that receives an element on the web page and gives back its cords location
def get_cords(element):
    loca_dict = element.location
    pos = []

    for key, value in loca_dict.items():
        pos.append(value)

    x, y = pos[0], pos[1]
    return(x,y)


# -- main --

# writing your email and password
global pics_num
your_mail = input("Write down your email: ")
your_password = input("Write down your facebook password: ")
person_name = input("The name of the person you want to give likes: ")
pics_num = int(input("write the number of pictures you want the bot to like: "))


# Opening Chrome for the login page using facebook
global driver
driver = webdriver.Chrome(r"C:\Users\avich\Desktop\flask\chromedriver.exe")
driver.get(
    'https://www.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221jz16a8n0z7as1mc7lf9faaoacyzyth81ncb8lq883i8stm4kxy%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Den_US%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfdc1cda2-ede6-4e2f-bce2-0c10740799fc&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221jz16a8n0z7as1mc7lf9faaoacyzyth81ncb8lq883i8stm4kxy%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=page&locale=en_US&pl_dbl=0')


# giving facebook your mail
mail = driver.find_element_by_xpath('//*[@id="email"]')
mail.send_keys(your_mail)


# giving facebook your password
passw = driver.find_element_by_xpath('//*[@id="pass"]')
passw.send_keys(your_password)
passw.send_keys(Keys.RETURN)

# This part is for the "continue as" and then it presses on your name, instgram doesnt let to click
# on objects with Selenium so from here we will work with pyautogui.
try:
    inside = driver.find_element_by_xpath('')
    inside.click()
except:
    time.sleep(1)
    pgu.click((872, 705))


# Closing the pop up message and making the window become full screen
time.sleep(3)
pgu.click((671, 764))
time.sleep(0.5)
pgu.click((99, 30))


# Giving the search engine the name of the wanted person we typed before
search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys(person_name)


# clicking on the first contact
time.sleep(1.5)
pgu.click((889, 265))


# giving likes
first_pic = (535, 914)
like_pics(first_pic)
