import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Define the remote URL based on your environment
# Use 'http://localhost:4444/wd/hub' when running from your host machine
# Use 'http://selenium-hub:4444/wd/hub' if running from another container

class Common_API:
   REMOTE_URL = "http://localhost:4444/wd/hub" 

   @pytest.fixture(scope="function")
   def driver():
    """Fixture to initialize and quit the remote webdriver."""
    print(f"\nConnecting to Selenium Hub at: {REMOTE_URL}")
    
    # Use webdriver.Remote to connect to the Selenium Hub
    # Specify the desired browser (e.g., 'chrome' or 'firefox')
    try:
        driver = webdriver.Remote(
            command_executor=REMOTE_URL,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        # Optional: Set an implicit wait time
        driver.implicitly_wait(10)
        yield driver
    except Exception as e:
        pytest.fail(f"Failed to connect to the Selenium Hub: {e}")
    finally:
        # Quit the driver after the test finishes
        if driver:
            driver.quit()

def test_website_title(driver):
    """A sample test that opens a website and checks the title."""
    driver.get("https://www.example.com")
    print(f"Page title: {driver.title}")
    assert "Example Domain" in driver.title
