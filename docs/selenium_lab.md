# Selenium Lab

This lab will focus on using [Welcome to Formy](<https://formy-project.herokuapp.com/>), a project with various web elements specifically designed for practicing web automation. The goal is for students to learn by doing, creating automated tests for different scenarios.

## Lab Objective

Students will create 5 automated test scripts using Selenium for interacting with the [Welcome to Formy](<https://formy-project.herokuapp.com/>) project. The focus will be on creating test scripts with Selenium and using pytest for running these test scripts, providing an introduction to one of the most popular Python testing frameworks.

## Prerequisites

- Basic understanding of Python (for Selenium scripts).
- Basic understanding of web technologies (HTML, CSS).
- An installed version of Python 3.6 or later.
- A GitHub account and basic familiarity with Git commands.
- Familiarity with virtual environments in Python.

## Instructions

### Step 1: Environment Setup

1. Install Python: Ensure Python 3.6 or later is installed on your machine. You can download it from the official Python website.

2. Create and Activate a Virtual Environment
    - Navigate to your project directory and create a virtual environment:

    ```bash
    python -m venv venv
    ```

    - Activate the virtual Environment:

3. Install Selenium and Pytest: Open your terminal or command prompt and run the following commands:

    ```bash
    pip install selenium pytest
    ```

4. Install Web Drivers (for Selenium)

- For Selenium, you need to download the web drivers for the browsers you intend to automate (e.g., ChromeDriver for Google Chrome, GeckoDriver for Firefox).
- Place the downloaded drivers in a directory that is in your system’s PATH.

### Step 2: Download the Starter Repository

1. Clone the GitHub Classroom Repository:
    - Use the link provided by your instructor to access the GitHub Classroom assignment.
    - Click on the 'Accept this assignment' button.
    - Once the repository is prepared, click on the link to open it and then clone it to your local machine using Git.

### Step 3: Creating Test Scripts

Students will create the following test scripts. Each script should interact with a different component on the  [Welcome to Formy](<https://formy-project.herokuapp.com/>) project site.

- Test file names should start with test_(e.g., test_text_field_lastname.py) (lastname is your lastname).
- Test functions within those files should start with test_(e.g., def test_text_input():).


1. Text Field Input:

    - Navigate to the formy project text field page.
    - Input text into the text field and submit the form.
    - Verify the submission was successful.
2. Checkbox Selection:

    - Navigate to the checkbox page.
    - Select and then deselect a checkbox.
    - Verify the state of the checkbox.

3. Radio Button Selection:

    - Navigate to the radio button page.
    - Select each radio button and verify the selection.

4. Date Picker Interaction:

    - Navigate to the date picker page.
    - Select a date from the date picker.
    - Verify the correct date was selected.

5. Drag and Drop:

    - Navigate to the drag and drop page.
    - Perform a drag and drop action.
    - Verify the item was dropped in the correct location.

For each scenario, provide a brief explanation of the code and the web elements interacted with. Encourage the use of explicit waits to ensure the reliability of tests.

### Step 4: Running Tests

- Using Pytest

  - Navigate to Your Test Directory. Ensure you're in the director containing your test scripts
    - Run Pytest. Execute the following command to run all tests:

    ```bash
    pytest
    ```

    - Pytest will automatically discover and run any test functions defined in the files matching the pattern `test_**.py` or `*-test.py`
- Using the Command Line and run each test separately
  - Run Selenium tests from the command line.
  - For Selenium: `python test_script_name.py`

### Step 5: Submitting Work

1. Commit Changes:
    - Use Git to add the new test scripts to the repository.
    - Commit the changes with a meaningful message.

2. Push to GitHub:
    - Push the commits to the GitHub repository.

3. Create a Pull Request:
    - Navigate to the repository on GitHub.
    - Click on 'New Pull Request'.
    - Compare your branch with the original assignment repository.
    - Submit the pull request for review.

## Step by Step

 It is `important` that as you do each step you **understand why you are doing each step.** Given that the environment is correctly set up and the repository has been cloned, here are the step-by-step instructions to implement( This assumes the use of Google Chrome as the browser for testing):

### Test Script #1 (Text Field Input)

### Step 1: Identify the Web Elements

First, navigate to the `formy` text field input page in your browser. Use the browser's developer tools to inspect the text field and submit button. Note the attributes that can be used to identify them, such as `id`, `name`, or `class`.

### Step 2: Write the Test Script

Create a new Python file in your tests directory. Name it `test_text_field-lastname.py`.

1. **Import Selenium WebDriver**:
   Begin by importing the necessary components from Selenium.

   ```python
   from selenium import webdriver
   from selenium.webdriver.common.keys import Keys
   from selenium.webdriver.common.by import By
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   ```

2. **Set Up WebDriver**:
   Initialize the WebDriver for Chrome.

   ```python
   driver = webdriver.Chrome()
   ```

3. **Navigate to the Web Page**:
   Use the `get` method to navigate to the text field input page.

   ```python
   driver.get("URL_OF_THE_TEXT_FIELD_PAGE")
   ```

   Replace `URL_OF_THE_TEXT_FIELD_PAGE` with the actual URL of the text field page on the `formy` project site.

4. **Locate the Text Field**:
   Find the text field element by one of its attributes (e.g., `id`).

   ```python
   text_field = driver.find_element(By.ID, "text_field_element_id")
   ```

   Replace `"text_field_element_id"` with the actual `id` (or use another attribute) of the text field element.

5. **Enter Text into the Field**:
   Send text to the text field element.

   ```python
   text_field.send_keys("Hello, World!")
   ```

6. **Submit the Form**:
   If the form is submitted by clicking a button, locate the button and click it. If hitting enter submits the form, simulate that instead.

   ```python
   submit_button = driver.find_element(By.ID, "submit_button_id")
   submit_button.click()
   ```

   Or, if pressing enter submits the form:

   ```python
   text_field.send_keys(Keys.ENTER)
   ```

7. **Verify Submission (Optional)**:
   If there's a way to verify submission (like a success message), wait for it and verify it's displayed.

   ```python
   success_message = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.ID, "success_message_id"))
   )
   assert "expected_success_text" in success_message.text
   ```

8. **Clean Up**:
   Close the browser after the test.

   ```python
   driver.quit()
   ```

### Step 3: Running the Test Script

- Open a terminal or command prompt.
- Navigate to the project directory where your `test_text_field.py` script is located.
- Execute the script using Python:

  ```bash
  python test_text_field.py
  ```

This script will automatically open Chrome, navigate to the specified page, input text into the text field, submit the form, and then close the browser. If implemented the verification step, it will also check for the success message.

Remember to replace placeholder values like `"text_field_element_id"`, `"submit_button_id"`, `"success_message_id"`, and `"URL_OF_THE_TEXT_FIELD_PAGE"` with actual values based on the `formy` project's text field page you're testing.

### Test Script #2 (Checkbox Selection)

Implementing Test Script #2, involves selecting and then deselecting a checkbox on the `formy` project site.

### Step 1: Identify the Checkbox Web Elements

Open the `formy` checkbox page in your browser. Use the browser’s developer tools (usually accessible by right-clicking the checkbox and selecting "Inspect") to examine the checkbox element. Identify attributes such as `id`, `name`, or `class` that can uniquely identify the checkbox you want to interact with.

### Step 2: Write the Test Script

Create a new Python file for this test in your project directory. You might name it `test_checkbox_selection_lastname.py`.

1. **Import Selenium WebDriver**:
   Import the necessary components from Selenium at the beginning of your Python script.

   ```python
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   ```

2. **Initialize WebDriver for Chrome**:
   Set up the WebDriver to use Google Chrome.

   ```python
   driver = webdriver.Chrome()
   ```

3. **Navigate to the Checkbox Page**:
   Use the `.get()` method with WebDriver to navigate to the checkbox page.

   ```python
   driver.get("URL_OF_THE_CHECKBOX_PAGE")
   ```

   Replace `"URL_OF_THE_CHECKBOX_PAGE"` with the actual URL of the checkbox page on the `formy` project site.

4. **Locate and Select the Checkbox**:
   Find the checkbox using one of its attributes and click it to select.

   ```python
   checkbox = driver.find_element(By.ID, "checkbox_id")
   checkbox.click()
   ```

   Replace `"checkbox_id"` with the actual `id` of the checkbox element. Ensure the checkbox is selected by clicking it.

5. **Verify Checkbox is Selected (Optional)**:
   Verify that the checkbox has been selected.

   ```python
   assert checkbox.is_selected()
   ```

6. **Deselect the Checkbox**:
   Click the checkbox again to deselect it.

   ```python
   checkbox.click()
   ```

7. **Verify Checkbox is Deselected (Optional)**:
   Confirm that the checkbox is no longer selected.

   ```python
   assert not checkbox.is_selected()
   ```

8. **Clean Up**:
   Close the browser once the test is complete.

   ```python
   driver.quit()
   ```

### Step 3: Running the Test Script

To run your test script:

- Open a terminal or command prompt.
- Change directories to where your `test_checkbox_selection.py` script is saved.
- Run the script with Python:

  ```bash
  python test_checkbox_selection.py
  ```

Executing this script will automatically open a Chrome browser window, navigate to the checkbox page, interact with the checkbox as specified, and verify the actions if those steps are included. Finally, it will close the browser window.

This hands-on exercise with Selenium not only reinforces understanding of web element interaction but also solidifies the concept of assertions in test scripts to validate web application behavior.

### Test Script #3 (Radio Buttons)

To implement Test Script #3, which involves selecting radio buttons on the `formy` project site, follow these step-by-step instructions. This test script will demonstrate how to interact with radio buttons using Selenium WebDriver in Python.

### Step 1: Identify the Radio Button Web Elements

First, visit the `formy` radio button page in your web browser. Utilize the browser’s developer tools to inspect the radio button elements. Note the attributes (such as `id`, `name`, or `class`) that can uniquely identify the radio buttons you intend to interact with.

### Step 2: Write the Test Script

Create a new Python file for this script in your project directory. You might name it `test_radio_button_selection_lastname.py`.

1. **Import Selenium WebDriver**:
   Start by importing the necessary components from Selenium at the beginning of your script.

   ```python
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   ```

2. **Set Up WebDriver for Chrome**:
   Initialize the WebDriver to use Google Chrome.

   ```python
   driver = webdriver.Chrome()
   ```

3. **Navigate to the Radio Button Page**:
   Use the `.get()` method with WebDriver to open the radio button page.

   ```python
   driver.get("URL_OF_THE_RADIO_BUTTON_PAGE")
   ```

   Replace `"URL_OF_THE_RADIO_BUTTON_PAGE"` with the actual URL of the radio button page on the `formy` project site.

4. **Locate and Select a Radio Button**:
   Find the first radio button by one of its unique attributes and click it to select.

   ```python
   radio_button1 = driver.find_element(By.ID, "radio_button_1_id")
   radio_button1.click()
   ```

   Verify the radio button is selected (optional).

   ```python
   assert radio_button1.is_selected()
   ```

   Replace `"radio_button_1_id"` with the actual `id` of the first radio button element.

5. **Select a Second Radio Button**:
   Similarly, locate and select a second radio button, ensuring it differs from the first.

   ```python
   radio_button2 = driver.find_element(By.ID, "radio_button_2_id")
   radio_button2.click()
   ```

   Verify the second radio button is selected and the first is deselected (optional).

   ```python
   assert radio_button2.is_selected()
   assert not radio_button1.is_selected()
   ```

   Replace `"radio_button_2_id"` with the actual `id` of the second radio button element.

6. **Clean Up**:
   Close the browser once the test is concluded.

   ```python
   driver.quit()
   ```

### Step 3: Running the Test Script

To run your Selenium test script:

- Open your terminal or command prompt.
- Navigate to the directory containing your `test_radio_button_selection.py` script.
- Execute the script using Python by running:

  ```bash
  python test_radio_button_selection.py
  ```

This script execution will open Chrome, navigate to the specified radio button page, perform interactions to select different radio buttons, optionally verify the selections, and finally close the browser window.

By following these steps, you’ll gain hands-on experience with Selenium WebDriver, enhancing your understanding of how to automate interactions with radio buttons in web testing scenarios.

### Test Script #4 (datepicker)

Implementing Test Script #4 involves interacting with a date picker on the `formy` project site using Selenium WebDriver. This script demonstrates selecting a date from a date picker widget. Here's how to approach it:

### Step 1: Identify the Date Picker Web Element

Visit the `formy` date picker page in your browser and use the developer tools to inspect the date picker input field. Identify attributes (such as `id`, `name`, or `class`) that can uniquely identify the date picker element.

### Step 2: Write the Test Script

Create a new Python file in your project directory for this test. You might name it `test_date_picker_lastname.py`.

1. **Import Selenium WebDriver**:
   Import the necessary components from Selenium at the start of your script.

   ```python
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   ```

2. **Initialize WebDriver for Chrome**:
   Set up the WebDriver to use Google Chrome.

   ```python
   driver = webdriver.Chrome()
   ```

3. **Navigate to the Date Picker Page**:
   Use the `.get()` method with WebDriver to navigate to the date picker page.

   ```python
   driver.get("URL_OF_THE_DATE_PICKER_PAGE")
   ```

   Replace `"URL_OF_THE_DATE_PICKER_PAGE"` with the actual URL of the date picker page on the `formy` project site.

4. **Locate the Date Picker Input Field**:
   Find the date picker element by one of its unique attributes.

   ```python
   date_picker = driver.find_element(By.ID, "datepicker_id")
   ```

   Replace `"datepicker_id"` with the actual `id` of the date picker input field.

5. **Enter a Date into the Date Picker**:
   Send a date string to the date picker input field. Ensure the format matches what the date picker expects (e.g., "MM/DD/YYYY").

   ```python
   date_picker.send_keys("12/25/2023")
   date_picker.send_keys(Keys.RETURN)  # Press Enter to close the date picker widget
   ```

   This step assumes the date picker accepts input in the "MM/DD/YYYY" format. Adjust the format according to the specific requirements of the date picker you are testing.

6. **Verify the Date Selection (Optional)**:
   After setting the date, you might want to verify that the correct date has been set. This can involve reading the value from the date picker input field and asserting it matches the expected date.

   ```python
   assert date_picker.get_attribute('value') == "12/25/2023"
   ```

7. **Clean Up**:
   Close the browser after the test is complete.

   ```python
   driver.quit()
   ```

### Step 3: Running the Test Script

To run the test script:

- Open a terminal or command prompt.
- Navigate to the directory where your `test_date_picker.py` script is saved.
- Execute the script with Python:

  ```bash
  python test_date_picker.py
  ```

Executing this script will automatically open Chrome, navigate to the date picker page, interact with the date picker to set a specific date, optionally verify the date has been set correctly, and then close the browser window.

This exercise with Selenium WebDriver provides practical experience in automating interactions with complex web elements like date pickers, a common requirement in web application testing.

### Test Script #5 (Drag and Drop)

Implementing Test Script #5 involves automating a drag-and-drop action on the `formy` project site using Selenium WebDriver. This script will demonstrate how to perform drag-and-drop operations, which are common user interactions in web applications. Here’s how to approach it:

### Step 1: Identify the Drag-and-Drop Web Elements

Navigate to the `formy` drag-and-drop page in your browser. Use the developer tools to inspect both the element you will drag and the target element where you intend to drop it. Note the attributes (such as `id`, `name`, or `class`) that can uniquely identify these elements.

### Step 2: Write the Test Script

Create a new Python file in your project directory for this test, possibly naming it `test_drag_and_drop_lastname.py`.

1. **Import Selenium WebDriver and ActionChains**:
   Import the necessary components from Selenium at the start of your Python script.

   ```python
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   from selenium.webdriver.common.action_chains import ActionChains
   ```

2. **Initialize WebDriver for Chrome**:
   Set up the WebDriver to use Google Chrome.

   ```python
   driver = webdriver.Chrome()
   ```

3. **Navigate to the Drag-and-Drop Page**:
   Use the `.get()` method with WebDriver to open the drag-and-drop page.

   ```python
   driver.get("URL_OF_THE_DRAG_AND_DROP_PAGE")
   ```

   Replace `"URL_OF_THE_DRAG_AND_DROP_PAGE"` with the actual URL of the drag-and-drop page on the `formy` project site.

4. **Locate the Draggable and the Drop Target Elements**:
   Find both the element to drag and the target element by their unique attributes.

   ```python
   draggable = driver.find_element(By.ID, "draggable_element_id")
   drop_target = driver.find_element(By.ID, "drop_target_element_id")
   ```

   Replace `"draggable_element_id"` and `"drop_target_element_id"` with the actual `id` values of the elements.

5. **Perform the Drag-and-Drop Action**:
   Use `ActionChains` to perform the drag-and-drop operation.

   ```python
   action_chains = ActionChains(driver)
   action_chains.drag_and_drop(draggable, drop_target).perform()
   ```

6. **Verify the Action (Optional)**:
   After performing the drag-and-drop, you might want to verify that the action was successful. This could involve checking for changes in the DOM, such as class changes or the presence of new text, indicating a successful drop.

   ```python
   success_message = drop_target.text
   assert "expected_success_message" in success_message
   ```

   Adjust the verification step based on the specific indicators of a successful drag-and-drop on your target page.

7. **Clean Up**:
   Close the browser after completing the test.

   ```python
   driver.quit()
   ```

### Step 3: Running the Test Script

To execute your test script:

- Open a terminal or command prompt.
- Change to the directory where your `test_drag_and_drop_lastname.py` file is located.
- Run the script using Python:

  ```bash
  python test_drag_and_drop.py
  ```

Running this script will automatically open Chrome, navigate to the drag-and-drop page, perform the drag-and-drop action, optionally verify the action's success, and then close the browser.

This exercise provides practical experience with automating drag-and-drop actions using Selenium WebDriver, teaching how to use `ActionChains` to simulate more complex user interactions in web applications.

### Using Pytest Runner to Run the Tests

To run all the Selenium test scripts at once, you can use a test runner like `pytest` or organize them into a test suite using Python's built-in `unittest` framework. Here is how to use Pytest.

### Using Pytest

`Pytest` is a popular testing framework that can discover and run tests written in Python, including Selenium tests. To use `pytest`:

1. **Install Pytest**:
   If you haven't installed `pytest` yet, do so by running:

   ```bash
   pip install pytest
   ```

2. **Organize Your Test Scripts**:
   Ensure all your test scripts are in the same directory and follow the naming convention `test_*.py` or `*_test.py`. For instance, you might have `test_text_field-lastname.py`, `test_checkbox_selection_lastname.py`, etc.

3. **Run Pytest**:
   Open a terminal, navigate to the directory containing your test scripts, and run:

   ```bash
   pytest
   ```

   `Pytest` will automatically discover and run all tests in the files matching its naming conventions.

## Assessment Criteria

The assessment of the student's work will be based on the following criteria:

1. Correct Implementation of Selenium Test Scripts

    - Functionality: Each test script correctly interacts with the web elements as per the given requirements (text field input, checkbox selection, radio button selection, date picker interaction, drag and drop).
    - Use of Selenium Webdriver: Proper use of Selenium WebDriver methods to locate and interact with web elements.
    - Error Handling: Implementation of basic error handling to manage exceptions thrown by Selenium, improving the robustness of test scripts.

2. Adherence to Pytest Conventions

    - Naming Conventions: Test files and test functions are named according to pytest conventions (test_*.py for files and test_* for function names).
    - Assertion Usage: Effective use of pytest assertions to validate test outcomes, demonstrating understanding of pytest’s assertion methods.
    - Fixtures (if used): Correct use of pytest fixtures to set up and tear down test environments or web drivers, showcasing an advanced understanding of pytest features.

3. Code Quality and Readability

    - Code Structure: Clear and logical organization of code, making it easy to understand and maintain.
    - Comments and Documentation: Adequate comments and documentation within the test scripts explaining the purpose of the code and any complex logic.
    - PEP 8 Compliance: Adherence to PEP 8 style guide for Python code, ensuring code consistency and readability.

4. Submission and Version Control

    - Git Usage: Correct use of Git for version control, including meaningful commit messages and proper branching where applicable.
    - Pull Request: Successful submission of work through a pull request to the main repository, demonstrating the ability to contribute to collaborative projects.

## Feedback and Grading

Feedback will be provided based on these criteria, highlighting strengths and areas for improvement. The grading can be structured as follows:

- A (Excellent): Meets all the above criteria with high code quality, demonstrating advanced understanding and application of Selenium and pytest.
- B (Good): Meets most criteria with minor issues in code quality or completeness, showing a good understanding of Selenium and pytest.
- C (Satisfactory): Meets the basic requirements but has several areas for improvement in understanding or application of Selenium, pytest, or code quality.
- D/F (Needs Improvement/Fail): Does not meet the basic requirements, showing significant gaps in understanding or application of Selenium, pytest, or general coding practices.
