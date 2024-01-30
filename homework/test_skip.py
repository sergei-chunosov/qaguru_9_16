"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser


@pytest.mark.desktop
def test_github_desktop(check_resolution_browser):
    if check_resolution_browser:
        browser.open('https://github.com')
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip('Mobile')


@pytest.mark.mobile
def test_github_mobile(check_resolution_browser):
    if not check_resolution_browser:
        browser.open('https://github.com')
        browser.element('.Button--link').click()
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip('Desktop')
