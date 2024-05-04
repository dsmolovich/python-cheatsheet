"""
1. pip install playwright
2. playwright install chromium
3. playwright codegen
4. record actions in the browser
5. copy/pasted the code
6. run it
"""
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://taasty.net/auth/login/?redirect=L2Rhc2hib2FyZC8%3D")
    page.get_by_placeholder("Email address").click()
    page.get_by_placeholder("Email address").fill("demo@taasty.net")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("demo")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("row", name="ver.2.3.2  ").get_by_role("link").nth(1).click()
    page.get_by_role("link", name="Customer UI").click()
    page.get_by_role("link", name="Customer accounts").click()
    page.get_by_role("link", name="User registers as a customer").click()
    expect(page.locator("#scenario-run-395259").get_by_text("Your browser does not support")).to_be_visible()
    page.get_by_role("link", name="Admin UI").click()
    page.get_by_role("link", name="Create customer").click()
    page.get_by_role("link", name="Magento admin creates").click()
    expect(page.locator("#scenario-run-395260").get_by_text("Your browser does not support")).to_be_visible()
    page.get_by_role("link", name="Shipment functionality").click()
    page.get_by_role("link", name="Magento admin updates").click()
    expect(page.locator("#scenario-run-395261").get_by_text("Your browser does not support")).to_be_visible()
    page.locator("#example-navbar-collapse").get_by_role("link", name="Dashboard").click()
    expect(page.get_by_role("cell", name="TaaSty.net : #2 ver.2.3.2 ")).to_be_visible()
    expect(page.get_by_role("cell", name="ver.2.3.2", exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name="master", exact=True)).to_be_visible()
    expect(page.locator("tbody:nth-child(5) > .passed-current > td:nth-child(8)")).to_be_visible()
    page.get_by_role("link", name="Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)