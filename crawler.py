from selenium import webdriver

chromedriver = '/home/kykevin/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(3)
driver.maximize_window()
driver.get('https://news.ycombinator.com/')

a = 0
for n in range (1,91,3):
    a += 1
    title = driver.find_element_by_xpath(f"""/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[{n}]/td[3]/a""")
    print(a)
    print(title.text)
    print(title.get_attribute('href'))

##/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[1]/td[3]/a
##/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[4]/td[3]/a
##/html/body/center/table/tbody/tr[3]/td/table/tbody/tr[7]/td[3]/a
