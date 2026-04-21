class CheckboxesPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/checkboxes"

        # Locators — get all checkboxes as a list
        self.checkboxes = page.locator("input[type='checkbox']")
        self.checkbox1 = page.locator("input[type='checkbox']:nth-of-type(1)")
        self.checkbox2 = page.locator("input[type='checkbox']:nth-of-type(2)")

    def navigate(self):
        self.page.goto(self.url)

    def check(self, checkbox):
        """Check a checkbox only if it's not already checked"""
        if not checkbox.is_checked():
            checkbox.check()

    def uncheck(self, checkbox):
        """Uncheck a checkbox only if it's currently checked"""
        if checkbox.is_checked():
            checkbox.uncheck()

    def is_checked(self, checkbox):
        """Returns True if checkbox is checked"""
        return checkbox.is_checked()

    def get_total_checkboxes(self):
        """Returns total number of checkboxes on the page"""
        return self.checkboxes.count()
