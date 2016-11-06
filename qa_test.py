import unittest

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support.select import Select


class QA(unittest.TestCase):
    def test_email_sudah_terdaftar(self):
        driver = webdriver.Chrome()
        wait = ui.WebDriverWait(driver, 10)
        url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        driver.get(url)

        email = driver.find_element_by_id('email_create')
        email.send_keys('khayatunnufus@gmail.com')
        driver.find_element_by_id('SubmitCreate').click()

        msg = 'An account using this email address has already been registered. Please enter a valid password or request a new one.'
        wait.until(lambda driver: driver.find_element_by_css_selector('#create_account_error > ol > li'))
        self.assertEqual(msg, driver.find_element_by_css_selector('#create_account_error > ol > li').text)

    def test_email_belum_terdaftar(self):
        driver = webdriver.Chrome()
        wait = ui.WebDriverWait(driver, 10)
        url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        driver.get(url)

        email = driver.find_element_by_id('email_create')
        email.send_keys('khayatunnufus_@gmail.com')
        driver.find_element_by_id('SubmitCreate').click()

        wait.until(lambda driver: driver.find_element_by_css_selector('#submitAccount'))
        self.assertTrue(driver.find_element_by_id('submitAccount'))

    def test_isi_data_akun_success(self):
        driver = webdriver.Chrome()
        wait = ui.WebDriverWait(driver, 10)
        url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        driver.get(url)

        email = driver.find_element_by_id('email_create')
        email.send_keys('khayatunnufus_4@gmail.com')
        driver.find_element_by_id('SubmitCreate').click()

        wait.until(lambda driver: driver.find_element_by_css_selector('.radio-inline'))
        driver.find_element_by_css_selector('#id_gender2').click()
        driver.find_element_by_css_selector('#customer_firstname').send_keys('Gina')
        driver.find_element_by_css_selector('#customer_lastname').send_keys('Khayatunnufus')
        driver.find_element_by_css_selector('#passwd').send_keys('password')
        Select(driver.find_element_by_id('days')).select_by_value('1')
        Select(driver.find_element_by_id('months')).select_by_value('5')
        Select(driver.find_element_by_id('years')).select_by_value('1992')
        driver.find_element_by_css_selector('#address1').send_keys('Alamat Gina Khayatunnufus')
        driver.find_element_by_css_selector('#city').send_keys('Cirebon')
        Select(driver.find_element_by_id('id_state')).select_by_value('2')
        driver.find_element_by_css_selector('#postcode').send_keys('40000')
        Select(driver.find_element_by_id('id_country')).select_by_value('21')
        driver.find_element_by_css_selector('#phone_mobile').send_keys('085212345678')
        driver.find_element_by_css_selector('#submitAccount').click()

        msg = 'Welcome to your account. Here you can manage all of your personal information and orders.'
        self.assertEqual(msg, driver.find_element_by_css_selector('.info-account').text)

    def test_isi_data_akun_failed(self):
        driver = webdriver.Chrome()
        wait = ui.WebDriverWait(driver, 10)
        url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        driver.get(url)

        email = driver.find_element_by_id('email_create')
        email.send_keys('khayatunnufus_5@gmail.com')
        driver.find_element_by_id('SubmitCreate').click()

        wait.until(lambda driver: driver.find_element_by_css_selector('.radio-inline'))
        driver.find_element_by_css_selector('#id_gender2').click()
        # driver.find_element_by_css_selector('#customer_firstname').send_keys('Gina')
        driver.find_element_by_css_selector('#customer_lastname').send_keys('Khayatunnufus')
        driver.find_element_by_css_selector('#passwd').send_keys('password')
        Select(driver.find_element_by_id('days')).select_by_value('1')
        Select(driver.find_element_by_id('months')).select_by_value('5')
        Select(driver.find_element_by_id('years')).select_by_value('1992')
        driver.find_element_by_css_selector('#address1').send_keys('Alamat Gina Khayatunnufus')
        driver.find_element_by_css_selector('#city').send_keys('Cirebon')
        Select(driver.find_element_by_id('id_state')).select_by_value('2')
        driver.find_element_by_css_selector('#postcode').send_keys('40000')
        Select(driver.find_element_by_id('id_country')).select_by_value('21')
        driver.find_element_by_css_selector('#phone_mobile').send_keys('085212345678')
        driver.find_element_by_css_selector('#submitAccount').click()

        msg = 'There is 1 error'
        self.assertEqual(msg, driver.find_element_by_css_selector('#center_column > div > p').text)

    def test_login(self):
        driver = webdriver.Chrome()
        url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        driver.get(url)

        email = driver.find_element_by_id('email')
        email.send_keys('khayatunnufus_1@gmail.com')
        email = driver.find_element_by_id('passwd')
        email.send_keys('password')
        driver.find_element_by_id('SubmitLogin').click()

        msg = 'Welcome to your account. Here you can manage all of your personal information and orders.'
        self.assertEqual(msg, driver.find_element_by_css_selector('.info-account').text)


if __name__ == '__main__':
    unittest.main()
