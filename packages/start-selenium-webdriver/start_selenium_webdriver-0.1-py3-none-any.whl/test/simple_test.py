from start_selenium_webdriver.webdriver_startup import start_web_driver

end_point = "https://www.google.com/"
driver = start_web_driver(end_point, num_sec_implicit_wait=0)

print("DOne")