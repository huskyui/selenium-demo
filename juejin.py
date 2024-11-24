from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    service =  Service(executable_path="/usr/bin/chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service,options=options)
    driver.get("https://www.juejin.cn")
    # 添加 Cookie // todo here
    cookies = [

    ]

    # 添加 Cookie
    for cookie in cookies:
        driver.add_cookie(cookie)

    # 刷新页面以应用 Cookie
    driver.refresh()
    title = driver.title
    print(title)
    driver.implicitly_wait(5)
    try:
        button = driver.find_element(By.XPATH, "//span[@class='btn-text' and text()='去签到']")
        if button is not None:
            button.click()
    except Exception as e:
        print("去签到没找到",e)

    try:
        button = driver.find_element(By.XPATH, "//span[@class='btn-text signed-text' and text()='已签到']")
        if button is not None:
            button.click()
    except Exception as e:
        print("已签到没找到", e)

    driver.implicitly_wait(5)

    button = driver.find_element(By.XPATH, "//button[@class='signedin btn']")
    button.click()

    driver.implicitly_wait(5)
    try:
        button = driver.find_element(By.XPATH, "//button[@class='btn' and text()='去抽奖']")
        if button is not None:
            button.click()
    except Exception as e:
        print("去签到没找到",e)


    for i in range(10):
        try:
            button = driver.find_element(By.ID, "turntable-item-0")
            if button is not None:
                button.click()
        except Exception as e:
            print("单抽按钮没找到", e)

        driver.implicitly_wait(2)
        # 通过类名和文本内容的组合定位
        title_element = driver.find_element(By.XPATH, "//*[contains(@class, 'title') and text()='当前矿石不足']")
        if title_element is not None:
            print("砖石不足")
            break
        try:
            # 使用 XPath 定位 SVG 图标
            button = driver.find_element(By.XPATH, "//*[local-name()='svg' and @class='close-icon']")
            if button is not None:
                button.click()
        except Exception as e:
            print("关闭按钮没找到", e)

        driver.implicitly_wait(2)
