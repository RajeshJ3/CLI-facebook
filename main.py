from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

try:
    opts = Options()
    opts.headless = True

    print("\nLoading...\n")
    driver = webdriver.Firefox(options=opts)
    driver.get("https://mbasic.facebook.com/")

    userName = input("email/phone: ")
    userPass = getpass("password: ")
    
    print("\nLogging in...\n")

    email = driver.find_element_by_xpath('.//*[@id="m_login_email"]')
    email.send_keys(userName)

    pswd = driver.find_element_by_css_selector('.bo')
    pswd.send_keys(userPass)

    loginBtn = driver.find_element_by_css_selector('.bq')
    loginBtn.click()

    driver.get("https://mbasic.facebook.com/messages/")
    success = True
    friend = input("\nFriend: ")
    count = 1
    searched = False
    while searched == False:
        try:
            searched = True
            success = True
            frndName = driver.find_element_by_link_text(friend)
            frndName.click()
        except:
            success = False
            count += 1
            searched = False
            try:
                try:
                    seeOlder = driver.find_element_by_link_text("See Older Messages")
                except:
                    try:
                        seeOlder = driver.find_element_by_link_text("See older messages")
                    except:
                        seeOlder = driver.find_element_by_link_text("see older messages")
                print("See older messages")
                seeOlder.click()
            except:
                break
    if success:
        message = driver.find_element_by_css_selector("#composerInput")
        msg = input("\nEnter message:")
        message.send_keys(msg)

        print("\nSending...\n")


        sendBtn = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[3]/div/div/form/table/tbody/tr/td[2]/input")
        sendBtn.click()
        print(f"\nMessage successfully sent to {friend}\n")
    else:
        print("Friend Not found")
    driver.close()
except:
    print("Unable to open backend browser.")