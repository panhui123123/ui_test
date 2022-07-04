import pytest
from base.base_action import BaseAction
from pages.pages import Pages
import time
import allure


@allure.feature('手机号登录')
class TestLoginByPhone:
    base_action = BaseAction()

    def setup(self):
        # 启动app
        self.base_action.start_app()
        time.sleep(5)

    def teardown(self):
        # 杀掉app
        self.base_action.kill_app()

    @allure.story('手机号密码登录')
    def test_01_loginByPhone(self):
        with allure.step('点击同意协议'):
            Pages().login_home.click_agree_check_button()
        with allure.step('点击手机号登录按钮'):
            Pages().login_home.click_login_by_phone_button()
        with allure.step('输入手机号'):
            Pages().login.input_phone_et()
        with allure.step('点击同意协议'):
            Pages().login_home.click_agree_check_button()
        with allure.step('点击密码登录'):
            Pages().login.click_login_by_password_button()
        with allure.step('输入密码'):
            Pages().login.input_password_et()
        with allure.step('点击登录'):
            Pages().login.click_login_button()
        with allure.step('断言'):
            assert Pages().login.check_findTab_is_existed()


if __name__ == '__main__':
    pytest.main(['-v', 'test_002_loginByPhone.py'])


