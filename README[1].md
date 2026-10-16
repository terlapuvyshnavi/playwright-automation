# Web Application Automation Testing (Playwright + Python)

[![Playwright tests](https://github.com/terlapuvyshnavi/playwright-automation/actions/workflows/playwright.yml/badge.svg)](https://github.com/terlapuvyshnavi/playwright-automation/actions/workflows/playwright.yml)

End-to-end UI test written with **Python, Playwright and pytest** for the practice e-commerce site
[automationexercise.com](https://automationexercise.com). The test runs automatically on every push with
**GitHub Actions**, and the HTML report is published with **GitHub Pages**.

🔗 **Latest test report:** https://terlapuvyshnavi.github.io/playwright-automation/

## What the test covers (`test_login.py`)
| Area | Steps automated |
|------|-----------------|
| Home page | Open the site and verify the page loads |
| Signup | Open Signup / Login, verify both sections, enter name and a random email |
| Account creation | Fill title, password, date of birth, newsletter options and the full address form, create the account |
| Login state | Click Continue and verify "Logged in as" is shown |
| Products | Open Products, search for "Blue Top", verify the search results |
| Cart | Hover the first product, add it to the cart, continue shopping, open the cart |
| Checkout | Verify the Proceed To Checkout button and click it |

Assertions check that key sections, buttons and search results are visible at each stage.

## Tech stack
Python · Playwright (sync API) · pytest · pytest-playwright · pytest-html · GitHub Actions · GitHub Pages

## Run locally
```bash
pip install -r requirements.txt
playwright install
pytest test_login.py -s --headed          # watch it run in a visible browser
pytest test_login.py --html=report.html --self-contained-html   # create an HTML report
```
Useful options: `--slowmo 500` (slow down), `--browser firefox` (another browser).

## Project structure
```
test_login.py                      the end-to-end test
requirements.txt                   dependencies
.github/workflows/playwright.yml   CI: run tests, publish report to GitHub Pages
```

## Notes and limitations
- The site is a public practice website, so a test can fail if its layout, popups or ads change.
- The test generates a random email each run; if that address already exists, run it again.
- The scenario is one long test with fixed waits (`wait_for_timeout`).

## Planned improvements
- Separate tests for signup, login with an existing account, product search and cart
- Replace fixed waits with Playwright auto-waiting and `expect` assertions
- Page Object Model, plus account deletion at the end of each run
