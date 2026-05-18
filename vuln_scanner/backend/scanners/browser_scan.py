from selenium import webdriver


def browser_test(url):

    driver = webdriver.Firefox()

    driver.get(url)

    title = driver.title

    driver.quit()

    return title
