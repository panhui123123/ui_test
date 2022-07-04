from base.base_action import BaseAction
from base.base_readYaml import ReadYaml


class LoginHome:
    base_action = BaseAction()
    # 同意协议
    agree_check_button = 'com.huiian.timing:id/iv_check'
    # 手机号登录
    login_by_phone_button = 'com.huiian.timing:id/iv_phone'
    # 微信登录
    login_by_weixin_button = 'com.huiian.timing:id/iv_weixin'
    # QQ登录
    login_by_qq_button = 'com.huiian.timing:id/iv_qq'

    def click_agree_check_button(self):
        self.base_action.click_element(self.agree_check_button)

    def click_login_by_phone_button(self):
        self.base_action.click_element(self.login_by_phone_button)

    def click_login_by_weixin_button(self):
        self.base_action.click_element(self.login_by_weixin_button)

    def click_login_by_qq_button(self):
        self.base_action.click_element(self.login_by_qq_button)