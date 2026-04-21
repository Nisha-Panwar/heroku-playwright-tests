class DropdownPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/dropdown"

        # Locators
        self.dropdown = page.locator("#dropdown")

    def navigate(self):
        self.page.goto(self.url)

    def select_by_value(self, value):
        """Select option using its value attribute e.g. '1' or '2'"""
        self.dropdown.select_option(value=value)

    def select_by_label(self, label):
        """Select option using visible text e.g. 'Option 1'"""
        self.dropdown.select_option(label=label)

    def get_selected_option(self):
        """Returns the currently selected option's visible text"""
        return self.page.eval_on_selector(
            "#dropdown",
            "el => el.options[el.selectedIndex].text"
        )
