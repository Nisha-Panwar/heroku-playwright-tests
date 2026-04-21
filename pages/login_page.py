class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/login"

        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator('button[type="submit"]')
        self.success_message = page.locator(".flash.success")
        self.error_message = page.locator(".flash.error")

    def navigate(self):
        self.page.goto(self.url)
        self.username_input.wait_for()

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
