from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from getpass import getpass
from time import sleep

# Menu function 
def menu(driver):
    while(True):
        print("\n1. Messages")
        print("2. Notifications")
        print("3. Exit")
        ch = int(input("\n=> "))

        if ch == 1:
            messages(driver)
        elif ch == 2:
            notifications(driver)
        elif ch == 3:
            print("Bye, see you again.")
            break
        else:
            print("Invalid input")


# Messages function
def messages(driver):
    driver.get("https://mbasic.facebook.com/messages/")
    # print("\nMessages accessed")
    
    loop2 = 0
    while loop2 == 0:
        Frnds = driver.find_elements_by_tag_name('h3')
        nameList = {}
        i = 0
        for Frnd in Frnds:
            i+=1
            if i<2 :
                continue
            else:
                if (i-2)%3 == 0:
                    if Frnd.text.upper() == "SEARCH FOR MESSAGES":
                        continue
                    else:
                        nameList.update({int(i/3)+1 : Frnd.text})
                        print(f"\n{int(i/3)+1}. {Frnd.text}")
                else:
                    pass
        nameList.update({ 55 : "See more friends"})
        nameList.update({ 66 : "Back to messages"})
        print("\n55. See more friends")
        print("\n66. Back to messages")
        friendNo = int(input("\n=> "))
        if friendNo not in nameList.keys():
            print("\nInvalid input")
            sleep(2)
        elif friendNo == 55:
            try:
                seeOlder = driver.find_element_by_link_text("See Older Messages")
            except:
                try:
                    seeOlder = driver.find_element_by_link_text("See older messages")
                except:
                    seeOlder = driver.find_element_by_link_text("see older messages")
            print("\nPlease wait while we load more of your friends...")
            seeOlder.click()
        elif friendNo == 66:
            menu(driver)
            loop2 = 1
            success = False
            break
        elif friendNo in nameList.keys() and friendNo != 55 and friendNo != 66:
            friend = nameList[friendNo]
            count = 1
            success = True
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
                msg = input(f"\nEnter message for {friend}: ")
                message.send_keys(msg)

                print("\nSending message...\n")


                sendBtn = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[3]/div/div/form/table/tbody/tr/td[2]/input")
                sendBtn.click()
                print(f"\nMessage successfully sent to {friend}\n")
                sleep(2)
                messages(driver)
            else:
                print("Friend Not found")
        else:
            print("Error 100")
# Notifications function 
def notifications(driver):
    driver.get("https://mbasic.facebook.com/notifications")
    print("\nRecent Notifications\n")
    allNotif = driver.find_elements_by_class_name("cb")
    i = 1
    for oneNotif in allNotif:
        print(f"-> {oneNotif.text}\n")
        i += 1

# Main Program

opts = Options()
opts.headless = True

print("\nLoading...\n")
driver = webdriver.Firefox(options=opts)
# driver = webdriver.Firefox()

try:
    print("\nConnecting to Facebook.com\n")
    while True:
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

        driver.get("http://mbasic.facebook.com/settings/")

        errorPage = driver.find_element_by_class_name('bd')
        if "you must log" in errorPage.text.lower():
            print("\nInvalid credentials! Try again.\n")
            continue
        else:
            print("\nLogged in successfully.\n")
            break

    menu(driver)
    driver.close()

except:
    print("Oops! Some error occured.")
#     sleep(3)
