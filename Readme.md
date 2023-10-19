# Selenium Registration Form Automation

This Python script uses the Selenium WebDriver to automate the registration process on a website. It fills out a registration form with various fields and options, clicks buttons, and submits the form. The script is organized into a class that encapsulates the functionality and provides methods for each step of the registration process.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your system.
- Install the libraries from requirements.py as follows

    ```bash
    pip install -r requirements.txt
    ```


## Usage

1. Clone this repository to your local machine.

2. Update the script with your desired input data (e.g., names, addresses, dates, etc.) and form field IDs. You can customize the values within the script to match your registration requirements.

4. Run the script:

    ```bash
    python registration_automation.py
    ```

5. The script will open a Chrome browser, navigate to the registration page, fill out the form, and submit it.

6. After completion, the browser will keep the session. You can close it

## Customization

You can customize the registration data and steps by modifying the `RegistrationFormAutomation` class within the script. Update the input values, field IDs, and steps according to the specific registration process you want to automate.

## Disclaimer

This script is provided as a sample automation solution. Please ensure that you have the appropriate permissions to use automation tools on any website. Use it responsibly and only on websites where you have permission to automate registration processes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
