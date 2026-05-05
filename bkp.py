<<<<<<< HEAD
    info_logger.info("Login test method started..!")
    try:
        debug_logger.debug("Launchin browser..!")
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        debug_logger.debug("Entering username: Admin")
        page.get_by_role("textbox", name="username").fill("Admin")

        debug_logger.debug("Entering Password: admin123")
        page.get_by_role("textbox", name="password").fill("admin123")

        debug_logger.debug("Clicking login button")
        page.get_by_role("button", name="Login").click()

        page.get_by_text("Dashbord")
    except Exception as e:
        error_logger.error("Test failed due to exception", exc_info=True)
=======
    info_logger.info("Login test method started..!")
    try:
        debug_logger.debug("Launchin browser..!")
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        debug_logger.debug("Entering username: Admin")
        page.get_by_role("textbox", name="username").fill("Admin")

        debug_logger.debug("Entering Password: admin123")
        page.get_by_role("textbox", name="password").fill("admin123")

        debug_logger.debug("Clicking login button")
        page.get_by_role("button", name="Login").click()

        page.get_by_text("Dashbord")
    except Exception as e:
        error_logger.error("Test failed due to exception", exc_info=True)
>>>>>>> 106abb0a0b3535a928a14e821645fd80ad4f68b6
    info_logger.info("Login test method Ran successfully..!")