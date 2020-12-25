import yaml
from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package= "com.xueqiu.android"
    _activity= ".view.WelcomeActivityAlias"
    def start(self):
        #判断driver是否赋值
        if self._driver is None:
            caps={}
            #caps={}报错  可以写成 caps = dict()字典
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps['noReset'] = True
            caps['udid'] = yaml.safe_load(open("../page/configuration.yaml"))['caps']['udid']
            # caps['skipServerInstallation'] = True
            # caps['skipDeviceInitialization'] = True

            #初始化driver
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package,self._activity)
        self._driver.implicitly_wait(3)
        #return self方便时用点语法
        return self

    #定义返回类型是Main
    def main(self) -> Main:
        return Main(self._driver)