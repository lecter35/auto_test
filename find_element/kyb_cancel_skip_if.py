from appium import webdriver

# 模拟器配置
desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['deviceName'] = '127.0.0.1:62025'
# desired_caps['platforVersion'] = '5.1.1'

# 真机配置
desired_caps['deviceName'] = 'HUAWWEI Mate 10 Pro'
desired_caps['platforVersion'] = '9'
desired_caps['udid'] = ''

desired_caps['noReset'] = 'True'

desired_caps['app'] = r'D:\\Python\Appium\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

# 安装apk并启动
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# 取消->跳过（session: noReset=false）
cancelBtn = driver.find_element_by_id('android:id/button2')  # error：An element could not be located
skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')

if cancelBtn:
    cancelBtn.click()
else:
    print('no cancelBtn')

if skipBtn:
    skipBtn.click()
else:
    print('no skipBtn')
