import os
from datetime import datetime
import allure

def save_screenshot(driver, name, folder_name="screenshots"):
    """
    Saves a screenshot in the specified folder and attaches it to the Allure Pytest report.
    Works fully inside Python venv without requiring Allure CLI or Java.
    """
    # Project root
    project_root = os.path.dirname(os.path.dirname(__file__))
    screenshot_dir = os.path.join(project_root, folder_name)
    os.makedirs(screenshot_dir, exist_ok=True)

    # Timestamped file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, file_name)

    # Save screenshot
    driver.save_screenshot(screenshot_path)

    # Attach to Allure report
    with open(screenshot_path, "rb") as f:
        allure.attach(f.read(), name=name, attachment_type=allure.attachment_type.PNG)

    return screenshot_path
