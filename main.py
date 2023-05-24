import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import config


def main():
    driver = config.set_test_web_driver()
    driver.get(config.BASE_URL)
    # Request Form
    # Fill out the required fields with data from config and submit
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "name"))).send_keys(
        config.REQUEST_FORM_NAME)

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "type"))).send_keys(
        config.REQUEST_FORM_TYPE)

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "business_unit"))).send_keys(
        config.REQUEST_FORM_BUSINESS_UNIT)

    driver.find_element(By.ID, 'submit').click()
    time.sleep(config.LOAD_WAIT_TIME)

    # General Information Form
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "username"))).send_keys(
        config.GENERAL_FORM_USERNAME)

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "requesters_email"))).send_keys(
        config.GENERAL_FORM_REQUESTERS_EMAIL)

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "managers_email"))).send_keys(
        config.GENERAL_FORM_MANAGERS_EMAIL)

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "business_unit"))).send_keys(
        config.GENERAL_FORM_TEAM_DL)

    # WebDriverWait(driver,
    #               config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "team_dl"))).send_keys(
    #     config.GENERAL_FORM_TEAM_DL)

    # WebDriverWait(driver,
    #               config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "business_unit"))).send_keys(
    #     config.GENERAL_FORM_BUSINESS_UNIT)

    driver.find_element(By.ID, 'submit').click()
    time.sleep(config.LOAD_WAIT_TIME)

    # Process Information Form
    description = ''
    use_case = ''
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "description"))).send_keys(
        description)

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "use_case"))).send_keys(
        use_case)

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "frequency"))).click()
    # Select daily from dropdown

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "environment"))).click()
    # Select GCP from dropdown

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Calendar"))).click()
    # Interact with calendar and select current date

    driver.find_element(By.ID, 'submit').click()
    time.sleep(config.LOAD_WAIT_TIME)

    # BigQuery Code Form
    ddl_sql = ''
    ddm_sql = ''
    uc4_chain_dependency = ''
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Data Definition"))).send_keys(
        ddl_sql)

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Data Manipulation"))).send_keys(
        ddm_sql)

    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Chain Dependency"))).send_keys(
        uc4_chain_dependency)

    driver.find_element(By.ID, 'submit').click()
    time.sleep(config.LOAD_WAIT_TIME)

    # Table Dependency Menu
    final_table = ''
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Verify Databases"))).click()
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, final_table))).click()

    driver.find_element(By.ID, 'submit').click()
    time.sleep(config.LOAD_WAIT_TIME)

    # Toggle Admin mode
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Admin Mode"))).click()

    # Wait until 'Status' field reads READY TO DEPLOY

    # Click 'More Options' or the three dot menu
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "More Options"))).click()

    # Click on 'Open Deployment Dashboard' from dropdown
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(
        ec.element_to_be_clickable((By.ID, "Open Deployment Dashboard"))).click()

    # Press Commit/Persist to GitHub button
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Commit"))).send_keys(
    )

    # Wait for Hash to be presented to confirm git operation

    # Choose the appropriate 'DALM app'
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "DALM app"))).click()
    # Select correct option from dropdown

    # Click the 'Create DALM tickets' button
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(
        ec.element_to_be_clickable((By.ID, "Create DALM tickets"))).send_keys()

    # Click on Adhoc link
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Ad Hoc Link"))).click()

    # Wait for Manifest status == Available

    # click Run Component button
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Run Component"))).click()

    # Select Production in the popup menu
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Production"))).click()

    # Select the correct manifest ID
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Manifest ID"))).click()
    # Is this a menu? Popup?

    # click run
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Run"))).click()

    # When 'Status' field reads 'COMPLETED'

    # Go to UC4 workflow Link
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "UC4 Workflow Link"))).click()

    # Click on the Run button.
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Run"))).click()

    # Select Batch Date from pop up
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Batch Date"))).click()
    # Select Correct option the resulting popup

    # Click Run Workflow
    WebDriverWait(driver,
                  config.CLICKABLE_WAIT_TIME).until(ec.element_to_be_clickable((By.ID, "Run Workflow"))).click()


if __name__ == "__main__":
    main()
