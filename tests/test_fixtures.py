"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser


def test_github_desktop(browser_resolution_desktop):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_resolution_mobile):
    browser.open('https://github.com')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
