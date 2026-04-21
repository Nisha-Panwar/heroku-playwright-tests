import pytest
from pages.checkboxes_page import CheckboxesPage

class TestCheckboxes:

    def test_total_checkboxes_on_page(self, page):
        cb = CheckboxesPage(page)
        cb.navigate()
        # There should be exactly 2 checkboxes
        assert cb.get_total_checkboxes() == 2

    def test_checkbox1_is_unchecked_by_default(self, page):
        cb = CheckboxesPage(page)
        cb.navigate()
        # Checkbox 1 starts UNCHECKED
        assert not cb.is_checked(cb.checkbox1)

    def test_checkbox2_is_checked_by_default(self, page):
        cb = CheckboxesPage(page)
        cb.navigate()
        # Checkbox 2 starts CHECKED
        assert cb.is_checked(cb.checkbox2)

    def test_check_checkbox1(self, page):
        cb = CheckboxesPage(page)
        cb.navigate()
        cb.check(cb.checkbox1)
        assert cb.is_checked(cb.checkbox1)

    def test_uncheck_checkbox2(self, page):
        cb = CheckboxesPage(page)
        cb.navigate()
        cb.uncheck(cb.checkbox2)
        assert not cb.is_checked(cb.checkbox2)

    def test_check_and_uncheck_checkbox1(self, page):
        cb = CheckboxesPage(page)
        cb.navigate()
        # Check it
        cb.check(cb.checkbox1)
        assert cb.is_checked(cb.checkbox1)
        # Now uncheck it
        cb.uncheck(cb.checkbox1)
        assert not cb.is_checked(cb.checkbox1)

    def test_both_checkboxes_checked(self, page):
        cb = CheckboxesPage(page)
        cb.navigate()
        cb.check(cb.checkbox1)
        cb.check(cb.checkbox2)
        assert cb.is_checked(cb.checkbox1)
        assert cb.is_checked(cb.checkbox2)

    def test_both_checkboxes_unchecked(self, page):
        cb = CheckboxesPage(page)
        cb.navigate()
        cb.uncheck(cb.checkbox1)
        cb.uncheck(cb.checkbox2)
        assert not cb.is_checked(cb.checkbox1)
        assert not cb.is_checked(cb.checkbox2)
