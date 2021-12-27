Implementation Test Automation Framework to testing https://www.onliner.by/

1. Clone repository: 
    $ clone https://github.com/kit-91-daniil/onliner_mobile_testing.git

2. Install virtual enviroment: 
    $ pipenv shell 
    $ pipenv install

3. For launch tests use commands below:
--- User can see logo 
    $ python -m pytest -v -m logo_presence --alluredir=allure_reports/


# Need to be fixed. XPATH Locators don't work correctly.

--- Cart should be empty
    $ python -m pytest -v -m verify_empty_cart --alluredir=allure_reports/

--- User can find product
    $ python -m pytest -v -m product_search --alluredir=allure_reports/

--- User can add product to cart
    $ python -m pytest -v -m add_product --alluredir=allure_reports/

4. OR for launch all the tests $ python -m pytest -v --alluredir=allure_reports/

5. To open allure reports use command below: $ allure serve allure_reports/