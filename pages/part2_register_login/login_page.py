from base.base_action import BaseAction
from base.base_readYaml import ReadYaml


class Login:
    base_action = BaseAction()
    phone = ReadYaml().read_yaml_data('test_phone_user.yaml')['test_phone_user']['phone']
    password = ReadYaml().read_yaml_data('test_phone_user.yaml')['test_phone_user']['password']
    # 关闭
    close_button = 'com.huiian.timing:id/activity_banner_back_iv'
    # 手机号输入框
    phone_et1 = 'com.huiian.timing:id/phone_et'
    phone_et2 = 'com.huiian.timing:id/et_phone'
    # 密码输入框
    password_et = 'com.huiian.timing:id/et_password'
    # 获取验证码
    get_captcha_button = 'com.huiian.timing:id/login_verify_tv'
    # 密码登录
    login_by_password_button = 'com.huiian.timing:id/activity_banner_right_tv'
    # 同意协议
    agree_check_button = 'com.huiian.timing:id/iv_check'
    # 登录
    login_button = 'com.huiian.timing:id/et_password'
    # 首页发现
    find_tab = 'com.huiian.timing:id/cl_tab_find'

    def click_close_button(self):
        self.base_action.click_element(self.close_button)

    def input_phone_et(self):
        self.base_action.set_text(self.phone_et1, self.phone)

    def click_get_captcha_button(self):
        self.base_action.click_element(self.get_captcha_button)

    def click_login_by_password_button(self):
        self.base_action.click_element(self.login_by_password_button)

    def click_agree_check_button(self):
        self.base_action.click_element(self.agree_check_button)

    def input_password_et(self):
        self.base_action.set_text(self.password_et, self.password)

    def click_login_button(self):
        self.base_action.click_element(self.login_button)

    def check_findTab_is_existed(self):
        return self.base_action.is_element_existed(self.find_tab)
