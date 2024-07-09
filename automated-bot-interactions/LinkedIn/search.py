from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urllib.parse import quote

JOB_SEARCH = "Python Developer"


def search_for_job(driver):
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_box.send_keys(JOB_SEARCH, Keys.ENTER)

    easy_apply_filter = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH,
                                        f"//a[@href='https://www.linkedin.com/jobs/search?keywords={
                                        quote(JOB_SEARCH)
                                        }&f_AL=true']"))
    )
    easy_apply_filter.click()

    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//a[@tabindex=0]"))
    )
    job_links = driver.find_elements(By.XPATH, "//a[@tabindex=0]")

    i = 0
    job_links[i].click()
    easy_apply_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jobs-apply-button')]"))
    )
    easy_apply_button.click()

    button = driver.find_element(By.XPATH, "//button[@aria-label='Continue to next step']")
    driver.execute_script("arguments[0].click();", button)

    second_next_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continue to next step']"))
    )
    second_next_button.click()

    review_popup = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, "//div[@class='jobs-easy-apply-content']"))
    )
    review_popup.send_keys(Keys.END)
    review_button = driver.find_element(By.XPATH, "//button[@aria-label='Review your application']")
    review_button.click()

    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//li-icon[@type='error-pebble-icon']"))
        )
        close_button = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
        close_button.click()
        discard_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH,
                                            "//button[@data-control-name='discard_application_confirm_btn']"))
        )
        discard_button.click()
        job_skipped = True
    except Exception as error:
        print(f"error: {error}")

    if not job_skipped:
        apply_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Submit application']"))
        )
        apply_button.click()
