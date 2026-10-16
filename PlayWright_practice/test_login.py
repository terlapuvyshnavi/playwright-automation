from playwright.sync_api import Page
import random
def test_open_website(page: Page):

    # ==========================
    # Step 1: Open Website
    # ==========================
    page.goto("https://automationexercise.com")
    page.wait_for_timeout(2000)

    print("Page Title:", page.title())
    print("Website Opened Successfully")

    # ==========================
    # Step 2: Click Signup/Login
    # ==========================
    page.get_by_role("link", name="Signup / Login").click()
    page.wait_for_timeout(2000)
    print("Signup/Login page opened successfully.")

    # ==========================
    # Step 3 : Verify Signup Page
    # ==========================
    assert page.get_by_text("New User Signup!").is_visible()
    assert page.get_by_text("Login to your account").is_visible()

    print("Signup and Login sections are visible")

    # ==========================
    # Step 4 : Enter Name
    # ==========================
    page.locator("input[data-qa='signup-name']").fill("Vyshu")

    page.wait_for_timeout(1000)

    # ==========================
    # Step 5 : Enter Email
    # ==========================
    email = f"vyshu{random.randint(1000,9999)}@gmail.com"
    page.locator("input[data-qa='signup-email']").fill(email)
    print("Email Used:", email)
    page.wait_for_timeout(1000)
    print("Name and Email Entered Successfully")

        # ==========================
    # Step 6 : Click Signup
    # ==========================
    page.locator("button[data-qa='signup-button']").click()

    page.wait_for_timeout(2000)

    print("Signup Button Clicked Successfully")

    # ==========================
    # Step 7 : Verify Account Information Page
    # ==========================
    assert page.get_by_text("Enter Account Information").is_visible()

    print("Enter Account Information Page Opened")

    page.wait_for_timeout(2000)


    # ==========================
    # Step 8 : Select Title
    # ==========================
    page.locator("#id_gender1").check()     # Mr.
    page.locator("#id_gender2").check()   # Mrs.

    page.wait_for_timeout(1000)
    

    # ==========================
    # Step 9 : Enter Password
    # ==========================
    page.locator("#password").fill("Password123")

    page.wait_for_timeout(1000) 


    # ==========================
    # Step 10 : Select Date of Birth
    # ==========================
    page.locator("#days").select_option("10")
    page.locator("#months").select_option("5")
    page.locator("#years").select_option("2005")
    page.wait_for_timeout(1000)


    # ==========================
    # Step 11 : Select Check Boxes
    # ==========================
    page.locator("#newsletter").check()
    page.locator("#optin").check()
    page.wait_for_timeout(1000)

    # ==========================
    # Step 12 : Address Information
    # ==========================
    page.locator("#first_name").fill("Vyshu")
    page.locator("#last_name").fill("Kumar")
    page.locator("#company").fill("SITAM College")
    page.locator("#address1").fill("Dwarapudi")
    page.locator("#address2").fill("Near Bus Stand")
    page.locator("#country").select_option("India")
    page.locator("#state").fill("Andhra Pradesh")
    page.locator("#city").fill("Vizianagaram")
    page.locator("#zipcode").fill("535003")
    page.locator("#mobile_number").fill("9876543210")
    page.wait_for_timeout(2000)
    print("Address Information Entered Successfully")

    # ==========================
    # Step 13 : Click Create Account
    # ==========================
    page.locator("button[data-qa='create-account']").click()
    page.wait_for_timeout(2000)
    


    # ==========================
    # Step 14 : Click Continue
    # ==========================
    page.get_by_role("link", name="Continue").click()
    page.wait_for_timeout(2000)
    print("Continue Button Clicked Successfully")
   

    # ==========================
    # Step 15 : Verify User Login
    # ==========================
    page.wait_for_timeout(2000)
    assert page.get_by_text("Logged in as").is_visible()
    print("User Logged In Successfully")
 

    # ==========================
    # Step 15 : Open Products
    # ==========================
    page.get_by_role("link", name="Products").click()
    page.wait_for_timeout(2000)
    print("Products Page Opened Successfully")
    

    # ==========================
    # # Step 16 : Search Product
    # # ==========================
    # # Verify Search Box
    assert page.locator("#search_product").is_visible()
    # Enter Product Name
    page.locator("#search_product").fill("Blue Top")
    page.wait_for_timeout(1000)
    print("Product Name Entered Successfully")
    # Verify Search Button
    assert page.locator("#submit_search").is_visible()
    # Click Search  Button
    page.locator("#submit_search").click()
    page.wait_for_timeout(1000)
    print("Search Button Clicked Successfully")
    # Verify Search Results
    assert page.get_by_text("Searched Products").is_visible()
    assert page.get_by_text("Blue Top").first.is_visible()
    page.wait_for_timeout(1000)
    print("Search Completed Successfully")
    

    # ==========================
    # Step 17 : Add Product to Cart
    # ==========================
    # Hover over the first product (required to show the overlay)
    page.locator(".product-image-wrapper").first.hover()
    page.wait_for_timeout(2000)
    # Click Add to Cart
    page.locator("//div[@class='overlay-content']//a[@class='btn btn-default add-to-cart'][normalize-space()='Add to cart']").first.click()
    page.wait_for_timeout(2000)
    print("Product Added to Cart Successfully")

    # ==========================
    # Step 18 : Continue Shopping
    # ==========================
    # # Click Continue Shopping button
    page.locator("//button[@class='btn btn-success close-modal btn-block']").click()
    page.wait_for_timeout(2000)
    print("Continue Shopping Button Clicked Successfully")

    # ==========================
    # Step 19 : Open Cart
    # ==========================
    # Click Cart
    page.locator("body > header:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)").click()
    page.wait_for_timeout(2000)
    assert page.get_by_text("Shopping Cart").is_visible()
    print("Shopping Cart Opened Successfully")

    # ==========================
    # Step 20 : Proceed To Checkout
    # ==========================
    # Verify Proceed To Checkout button
    assert page.locator(".btn.btn-default.check_out").is_visible()
    # Click Proceed To Checkout
    page.locator(".btn.btn-default.check_out").click()
    # Wait for Checkout Page
    page.wait_for_timeout(3000)
    print("Proceed To Checkout Button Clicked Successfully")
     
