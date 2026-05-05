import re
from playwright.sync_api import Page, expect, sync_playwright
from utils.logger import debug_logger, info_logger, error_logger


def test_valid_login(page: Page):
    info_logger.info("Add employee test method started")
    try:
        debug_logger.debug("Clicking PIM menu")
        page.get_by_role("link",name="PIM").click()
        page.get_by_role("button",name="Add").click()

        debug_logger.debug("Entering first name: John")
        page.get_by_placeholder("First Name").fill("Johnc1")

        debug_logger.debug("Entering Last name: Doe")
        page.get_by_placeholder("Last Name").fill("Doe")

        debug_logger.debug("Entering Employee ID: 12345")
        page.get_by_role("textbox").nth(4).fill("12675740")

        debug_logger.debug("Uploading profile.jpg file")
        page.locator('input[type="file"]').set_input_files("test_data/files/profile.jpg")
        info_logger.info("Profile picture uploaded successfully..!")

        page.get_by_role("checkbox").check(force=True)

        page.locator('div.oxd-input-group:has(label:text("Username")) input').fill("johndoe1772")

        page.get_by_role("radio",name="Disabled").check(force=True)

        page.locator('input[type="password"]').first.fill("Password@123")
        page.locator('input[type="password"]').nth(1).fill("Password@123") 


        debug_logger.debug("Clicking Save button")
        page.get_by_role("button",name="Save").click()

        page.wait_for_load_state("networkidle")

        page.get_by_role("heading",name="Personal Details").wait_for(state="visible")
        expect(page.get_by_role("heading",name="Personal Details")).to_be_visible()
        #expect(page).to_have_url(re.compile("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"))
        info_logger.info("Employee added successfully..!")

    except Exception as e:
        error_logger.error("Test failed due to exception",exc_info=True)

