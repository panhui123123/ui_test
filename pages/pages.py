from pages.part1_startup_app.privacy_policy_page import PrivacyPolicy
from pages.part2_register_login.login_home_page import LoginHome
from pages.part2_register_login.login_page import Login


class Pages:
    def __init__(self):
        self.privacy_policy = PrivacyPolicy()
        self.login_home = LoginHome()
        self.login = Login()