import pytest
from base.base_action import BaseAction
from pages.pages import Pages
import time
import allure


@allure.feature('首次进入app')
class TestPrivacyPolicy:
    base_action = BaseAction()

    def setup(self):
        # 清除app数据
        self.base_action.clear_app()
        # 启动app
        self.base_action.start_app()
        time.sleep(3)

    def teardown(self):
        # 杀掉app
        self.base_action.kill_app()

    @allure.story('一直点击不同意退出app')
    # 点击同意进入登录页
    def test_01_disagreePrivacyPolicy(self):
        with allure.step('点击不同意'):
            Pages().privacy_policy.click_disagree_button()
            time.sleep(1)
        with allure.step('点击仍不同意'):
            Pages().privacy_policy.click_disagree_button()
            time.sleep(1)
        with allure.step('点击退出'):
            Pages().privacy_policy.click_disagree_button()
            time.sleep(1)
        with allure.step('检查手机号登陆按钮是否存在, 如果存在则截图'):
            result = Pages().privacy_policy.check_loginByPhoneButton_is_existed()
        # 如果存在保存截图
        if result:
            self.base_action.get_screenshot('退出app失败.png')
        with allure.step('断言'):
            assert not result

    @allure.story('一直点击同意进入登陆首页')
    # 点击同意进入登录页
    def test_02_agreePrivacyPolicy(self):
        with allure.step('点击同意按钮'):
            Pages().privacy_policy.click_agree_button()
        time.sleep(1)
        with allure.step('点击允许权限'):
            Pages().privacy_policy.click_permission_allowed_button()
        time.sleep(1)
        with allure.step('检查手机号登陆按钮是否存在，如果不存在则截图'):
            result = Pages().privacy_policy.check_loginByPhoneButton_is_existed()
        # 如果不存在保存截图
        if not result:
            self.base_action.get_screenshot('进入登陆页失败截图.png')
        with allure.step('断言'):
            assert result


if __name__ == '__main__':
    pytest.main(['-v', 'test_001_checkPrivacyPolicy.py'])