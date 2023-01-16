## DemoqaProject - UI testing of [the form](https://demoqa.com/automation-practice-form "the form") of the website [demoqa](https://demoqa.com)

[tests/ui/test_registration_page.py](https://github.com/SvetlanaBedareva/DemoqaProject/blob/master/tests/ui/test_registration_page.py "tests/ui/test_registration_page.py") - a file with tests;

[pages/photo](https://github.com/SvetlanaBedareva/DemoqaProject/tree/master/pages/photo "pages/photo") - photos are used to upload to a student;

[pages/base_page.py](https://github.com/SvetlanaBedareva/DemoqaProject/blob/master/pages/base_page.py "pages/base_page.py") - basic data for testing(browser, url, timeout);

[pages/registration_page.py](https://github.com/SvetlanaBedareva/DemoqaProject/blob/master/pages/registration_page.py "pages/registration_page.py") - functions for tests;

[pages/locators.py](https://github.com/SvetlanaBedareva/DemoqaProject/blob/master/pages/locators.py "pages/locators.py") - locators for tests;

[pages/settings.py](https://github.com/SvetlanaBedareva/DemoqaProject/blob/master/pages/settings.py "pages/settings.py") - url of the form;

[requirements.txt](https://github.com/SvetlanaBedareva/DemoqaProject/blob/master/requirements.txt "requirements.txt") - exact versions of all installed packages


### Run tests
 pytest -v tests/ui/test_registration_page.py
