import pytest
from base.base_action import BaseAction
from pages.pages import Pages
import time


class TestPrivacyPolicy:
    def setup(self):
        self.base_action = BaseAction()
        # 清除app数据
        self.base_action.clear_app()
        # 启动app
        self.base_action.start_app()
        time.sleep(3)

    def teardown(self):
        # 杀掉app
        self.base_action.kill_app()

    @pytest.mark.run(order=1)
    # 点击同意进入登录页
    def test_agreePrivacyPolicy(self):
        # 点击同意按钮
        Pages().privacy_policy.click_agree_button()
        time.sleep(1)
        # 点击允许权限
        Pages().privacy_policy.click_permission_allowed_button()
        time.sleep(1)
        # 检查手机号登陆按钮是否存在
        result = Pages().privacy_policy.check_loginByPhoneButton_is_existed()
        # 如果不存在保存截图
        if not result:
            self.base_action.get_screenshot('进入登录页失败截图.png')
        else:
            pass
        # 断言
        assert result

    @pytest.mark.run(order=2)
    # 点击同意进入登录页
    def test_disagreePrivacyPolicy(self):
        # 点击不同意
        Pages().privacy_policy.click_disagree_button()
        time.sleep(1)
        # 点击仍不同意
        Pages().privacy_policy.click_disagree_button()
        time.sleep(1)
        # 点击退出
        Pages().privacy_policy.click_disagree_button()
        time.sleep(1)
        # 检查手机号登陆按钮是否存在
        result = Pages().privacy_policy.check_loginByPhoneButton_is_existed()
        # 如果存在保存截图
        if result:
            self.base_action.get_screenshot('进入登录页失败截图.png')
        else:
            pass
        # 断言
        assert not result


if __name__ == '__main__':
    pytest.main(['-v', 'test_001_checkPrivacyPolicy.py'])