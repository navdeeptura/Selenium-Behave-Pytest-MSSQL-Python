from pytest_bdd import scenario, given, when, then

@scenario("hello_world.feature", "User successfully logs in with valid credentials")
def test_hello_world():
    pass

@given('the user is on the login page')
def _():
    # code to ensure user is on login page
    pass

@when('the user enters valid credentials')
def _():
    # code to simulate entering valid credentials
    pass

@then('the user should be redirected to the dashboard')
def _():
    # code to check user is redirected to dashboard
    pass
