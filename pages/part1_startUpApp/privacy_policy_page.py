from base.base_action import BaseAction
import time


class PrivacyPolicy:
    base_action = BaseAction()
    # 同意、再次查看按钮
    agree_button = 'com.huiian.timing:id/tv_agree'
    # 不同意按钮、仍不同意、退出APP按钮
    disagree_button = 'com.huiian.timing:id/tv_disagree'
    # 允许权限按钮
    permission_allowed_button = 'com.android.packageinstaller:id/permission_allow_button'
    # 手机号登陆按钮
    login_by_phone_button = 'com.huiian.timing:id/iv_phone'

    def click_agree_button(self):
        '''
        点击同意、再次查看按钮
        :return:
        '''
        self.base_action.click_element(self.agree_button)

    def click_disagree_button(self):
        '''
        点击不同意、仍不同意、退出按钮
        :return:
        '''
        self.base_action.click_element(self.disagree_button)

    def click_permission_allowed_button(self):
        '''
        点击允许权限按钮
        :return:
        '''
        self.base_action.click_element(self.permission_allowed_button)

    def check_loginByPhoneButton_is_existed(self):
        '''
        检查手机号登陆按钮是否存在
        :return: 布尔值
        '''
        return self.base_action.is_element_existed(self.login_by_phone_button)





