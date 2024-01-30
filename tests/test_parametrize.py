"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser


@pytest.mark.parametrize('browser_resolution_desktop', [(1920, 1080)], indirect=True)
def test_github_desktop(browser_resolution_desktop):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_resolution_mobile', [(640, 960)], indirect=True)
def test_github_mobile(browser_resolution_mobile):
    browser.open('https://github.com')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
