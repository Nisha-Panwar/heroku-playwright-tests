import pytest
from pages.dropdown_page import DropdownPage

class TestDropdown:

    def test_select_option1_by_value(self, page):
        dropdown = DropdownPage(page)
        dropdown.navigate()
        dropdown.select_by_value("1")
        assert dropdown.get_selected_option() == "Option 1"

    def test_select_option2_by_value(self, page):
        dropdown = DropdownPage(page)
        dropdown.navigate()
        dropdown.select_by_value("2")
        assert dropdown.get_selected_option() == "Option 2"

    def test_select_option1_by_label(self, page):
        dropdown = DropdownPage(page)
        dropdown.navigate()
        dropdown.select_by_label("Option 1")
        assert dropdown.get_selected_option() == "Option 1"

    def test_select_option2_by_label(self, page):
        dropdown = DropdownPage(page)
        dropdown.navigate()
        dropdown.select_by_label("Option 2")
        assert dropdown.get_selected_option() == "Option 2"

    def test_default_option_is_not_selectable(self, page):
        dropdown = DropdownPage(page)
        dropdown.navigate()
        # Default selected should NOT be Option 1 or Option 2
        selected = dropdown.get_selected_option()
        assert selected != "Option 1"
        assert selected != "Option 2"
