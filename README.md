# Saucedemo Test Automation Project

This project is a comprehensive test automation suite for the Saucedemo website using Selenium, Python, and pytest. 
It covers various functionalities including login, cart, product search and checkout processes.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-green)
![Pytest](https://img.shields.io/badge/Pytest-6.0+-orange)

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Test Cases](#test-cases)
- [Usage](#usage)
- [Fixtures](#fixtures)

## Project Structure

```plaintext
Saucedemo_Test_Automation/
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── logout_page.py
│   ├── product_page.py
│   └── social_media_links_page.py
├── tests/
│   ├── conftest.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_product_search.py
│   └── test_social_media_links.py
├── utils/
│   ├── config.py
│   ├── conftest.py
├── requirements.txt
└── README.md
```
## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ekuletskaia/saucedemo_testing.git
   ```

2. **Navigate to the project directory:**

    ```bash
    cd saucedemo_testing
    ```
   
3. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    ```
   
4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```
   
## Usage

1. **Run the tests:**

    ```bash
    pytest

    ```
   
2. **Generate HTML reports:**

    ```bash
    pytest --html=report.html
    ```
   
## Test Cases

The project includes a comprehensive suite of test cases covering various functionalities of the Saucedemo website. Below is a summary of the different categories of test cases:

### Login Tests
- Valid user login
- Invalid user login

### Logout Tests
- User logout functionality

### Cart Tests
- Add item to cart
- Remove item from cart
- Verify items in the cart
- Verify cart total price

### Product Search Tests
- Filter the products on the page
- Verify filter results

### Checkout Tests
- Verify checkout page elements
- Complete checkout process
- Verify error messages for empty fields

### Social Media Link Tests
- Verify social media links

For the complete list of test cases, please refer to the test files in the `tests` directory.

   
## Fixtures

The project uses `pytest` fixtures for setup and teardown processes. 
The fixtures are defined in `conftest.py` and `utils/config.py`.

### conftest.py:

- **`setup_browser`**: Initializes the WebDriver and opens the browser.
- **`login`**: Logs in a valid user before running the test.
- **`setup_cart_and_checkout`**: Adds an item to the cart and proceeds to the checkout page before running the test.

### utils/config.py:

- Contains configuration data such as URLs, valid/invalid credentials, and user information.

