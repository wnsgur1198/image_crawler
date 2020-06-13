from selenium import webdriver


def crawling(keyword, path, start):
    browser = webdriver.Chrome('chromedriver.exe')

    url = "https://www.google.com/search?q=" + keyword + "&source=lnms" + "&tbm=isch"
    browser.get(url)

    for i in range(10):
        browser.execute_script('window.scrollBy(0,100)')

    for idx, el in enumerate(browser.find_elements_by_class_name("rg_i.Q4LuWd.tx8vtf")):
        if idx == 50:   # 약 50개 이후 부터 공백이미지가 캡처됨
            break
        el.screenshot(path + str(start) + ".jpg")
        print("--- screenshot complete : " + str(start) + " ---")
        start += 1

    browser.close()
