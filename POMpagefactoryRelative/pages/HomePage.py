from seleniumpagefactory.Pagefactory import PageFactory


class HomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {

        # Username field relative to label or form structure
        'user_name': (
            'XPATH',
            "//label[contains(text(),'Username')]/following::input[1]"
        ),

        # Password field relative to label
        'password': (
            'XPATH',
            "//label[contains(text(),'Password')]/following::input[1]"
        ),

        # Login button relative to text or type
        'login_btn': (
            'XPATH',
            "//button[@id='login-btn' or contains(text(),'Login')]"
        ),

        # Search box relative to form/input hierarchy
        'search_box_field': (
            'XPATH',
            "//input[@name='search' or @placeholder='Search']"
        ),

        # Search button relative to search input form
        'search_button': (
            'XPATH',
            "//input[@name='search']/following::button[1]"
        )
    }

    def enter_product_into_search_box_field(self, product_name):
        self.search_box_field.set_text(product_name)

    def click_search_button(self):
        self.search_button.click()