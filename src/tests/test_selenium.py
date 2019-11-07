import unittest

from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        # браузер закрывается сразу после исполнения теста,
        # эта опция позволила избегать закрытия
        self.driver = Chrome(options=opts)

        self.login = 'login'
        self.pass_word = 'password'

    def test_login_to_yandex(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth/")
        self.assertIn("Авторизация", driver.title)
        elem = driver.find_element_by_name("login")
        elem.send_keys(self.login)
        elem.send_keys(Keys.RETURN)
        driver.implicitly_wait(30)
        elem2 = driver.find_element_by_name('passwd')
        elem2.send_keys(self.pass_word)
        elem2.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        pass
        # self.driver.close()


if __name__ == "__main__":
    unittest.main()
