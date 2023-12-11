from urllib.parse import urljoin

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from elements import MOSWAR_URL


def convert_relative_url(relative_url: str) -> str:
    """
    Converts a relative URL to an absolute URL.
    Args:
        relative_url (str): The relative URL to be converted.
    Returns:
        str: The absolute URL.
    """
    return urljoin(MOSWAR_URL, relative_url) if relative_url else MOSWAR_URL


def get_by_id(driver, elem_id):
    """
    Find and return an element from the web page by its ID.

    Parameters:
    - driver: The WebDriver instance used to interact with the web page.
    - elem_id: The ID of the element to find.

    Returns:
    - The WebElement object representing the found element, or None if the element is not found.
    """
    try:
        return driver.find_element(By.ID, elem_id)
    except NoSuchElementException:
        return None


def get_by_name(driver, elem_name):
    """
        Finds and returns an element in the DOM using its name attribute.

        Args:
            driver (WebDriver): The WebDriver instance to use for finding the element.
            elem_name (str): The name attribute of the element to be found.

        Returns:
            WebElement or None: The WebElement object representing the found element,
            or None if no element with the given name attribute is found.
    """
    try:
        return driver.find_element(By.NAME, elem_name)
    except NoSuchElementException:
        return None


def get_by_class(driver, class_id):
    """
    Find and return an element by its class name using the given driver.

    :param driver: The driver used to find the element.
    :type driver: WebDriver

    :param class_id: The class name of the element.
    :type class_id: str

    :return: The element found with the given class name, or None if not found.
    :rtype: WebElement or None
    """
    try:
        return driver.find_element(By.CLASS_NAME, class_id)
    except NoSuchElementException:
        return None


def get_by_css(driver, css):
    """
    Find and return an element in the web page using a CSS selector.

    Parameters:
        driver (WebDriver): The WebDriver object used to interact with the web page.
        css (str): The CSS selector used to locate the element.

    Returns:
        WebElement or None: The WebElement object if an element is found, None otherwise.
    """
    try:
        return driver.find_element(By.CSS_SELECTOR, css)
    except NoSuchElementException:
        return None


def get_by_linktext(driver, linktext):
    """
    Find and return an element in the web page using the given link text.

    Parameters:
        driver (WebDriver): The WebDriver object used to interact with the web page.
        linktext (str): The link text of the element to be found.

    Returns:
        WebElement or None: The WebElement object if the element is found, otherwise None.
    """
    try:
        return driver.find_element(By.LINK_TEXT, linktext)
    except NoSuchElementException:
        return None


def get_by_xpath(driver, xpath):
    """
    Find and return an element located by the given XPath expression.

    Args:
        driver (WebDriver): The instance of the WebDriver.
        xpath (str): The XPath expression used to locate the element.

    Returns:
        WebElement or None: The element located by the XPath expression, or None if no element is found.
    """
    try:
        return driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return None


def put_text(driver, elem_id, text):
    """
    Set the text of an element with the given ID.

    Parameters:
        driver (WebDriver): The WebDriver object used to interact with the browser.
        elem_id (str): The ID of the element to set the text of.
        text (str): The text to set.

    Returns:
        None
    """
    try:
        elem = get_by_id(driver, elem_id)
        elem.clear()
        elem.send_keys(text)
    except NoSuchElementException:
        return


def click(driver, classname, bt_id):
    """
    Clicks on the element with the given classname and bt_id using the provided driver.

    Parameters:
        driver (WebDriver): The WebDriver instance to use for finding the element and performing the click.
        classname (str): The classname of the element to click.
        bt_id (str): The bt_id of the element to click.

    Returns:
        None
    """
    try:
        element = driver.find_element(classname, bt_id)
        element.click()
    except NoSuchElementException:
        print(f"Element with locator {classname} and by {bt_id} not found")
