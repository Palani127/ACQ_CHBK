import re
from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=1000)
        yield browser
        browser.close()
        
@pytest.fixture(scope="function")
def authenticate(browser):
    context=browser.new_context(ignore_https_errors=True)
    page=context.new_page()
    #page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #page.get_by_role("textbox", name="username").fill("Admin")
    #page.get_by_role("textbox", name="password").fill("admin123")
    #page.get_by_role("button", name="Login").click()
    page.goto("https://10.162.2.6:8463/chargeback/common/ums_lp/u_1.rcn")
    page.get_by_text("Proceed to Login").nth(1).click()
    page.locator('#userid').fill("PALANI")
    page.locator('#password').fill("Recon@1234")
    page.locator('#loginas').fill("NIB")
    page.get_by_role("button",name="Submit").click()
    
    page.wait_for_load_state("networkidle")
    context.storage_state(path="auth.json")
    page.close()
    context.close()

@pytest.fixture(scope="function")
def context(browser,authenticate):
    context=browser.new_context(ignore_https_errors=True,storage_state="auth.json")
    yield context
    context.close()

@pytest.fixture
def page(context):
    page=context.new_page()
    #page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    page.goto("https://10.162.2.6:8463/chargeback/ums/um_hp/u_01.rcn")
    yield page
    page.close()
