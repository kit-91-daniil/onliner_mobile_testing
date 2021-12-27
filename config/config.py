import os


class DriverConfig:
    launching_timeout = 15
    command_executor = "http://localhost:4723/wd/hub"
    chrome_driver_path = os.path.abspath("binaries/chromedriver")
    desired_capability = {
        "platformName": "Android",
        "platformVersion": "9",
        "automationName": "uiautomator2",
        "appium:deviceName": "emulator-5554",
        "browserName": "Chrome",
        "appium:chromedriverExecutable": chrome_driver_path
    }
