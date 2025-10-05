import os
from datetime import datetime
import allure
import base64

def save_screenshot(driver, name, folder_name="screenshots"):
    """
    Saves a full-page screenshot in the specified folder and attaches it to the Allure Pytest report.
    """
    # Project root
    project_root = os.path.dirname(os.path.dirname(__file__))
    screenshot_dir = os.path.join(project_root, folder_name)
    os.makedirs(screenshot_dir, exist_ok=True)

    # Timestamped file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, file_name)

    # Capture full-page screenshot
    screenshot_base64 = driver.execute_cdp_cmd("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": True})["data"]

    #save the screenshot
    with open(screenshot_path, "wb") as f:
        f.write(base64.b64decode(screenshot_base64))

    # Attach to Allure report
    with open(screenshot_path, "rb") as f:
        allure.attach(f.read(), name=name, attachment_type=allure.attachment_type.PNG)

    return screenshot_path