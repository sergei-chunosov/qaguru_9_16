from selene import browser
import pytest

# @pytest.fixture()
# def setup_browser():
#     browser.config.base_url = "https://demoqa.com/"
#     browser.config.window_width = '1900'
#     browser.config.window_height = '1080'
#     browser.config.timeout = 4
#
#     yield browser
#
#     browser.quit()

@pytest.fixture(params=[(1920, 1080), (3200, 1800), (1680, 1050)])
def browser_resolution_desktop(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.fixture(params=[(640, 960), (540, 960), (390, 844)])
def browser_resolution_mobile(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]