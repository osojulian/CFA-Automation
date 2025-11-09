import os
from datetime import datetime


def take_screenshot(driver, name):
    os.makedirs("evidencias", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"evidencias/{name}_{timestamp}.png")