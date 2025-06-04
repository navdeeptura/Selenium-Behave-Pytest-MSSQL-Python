from asyncio import to_thread

from pytest_bdd import scenario, given, when, then, parsers

scenario("argument.feature", "Test Arguments")
def test_arguments():
    pass

scenario("argument.feature", "Test Zero cucumbers")
def test_zero_arguments():
    pass

@given(parsers.parse("there are {start:d} cucumbers"), target_fixture="cucumbers")
def given_fruits():
    return {
        "start": start,
        "eat": 0
    }

@when(parsers.parse("I eat {eat:d} cucumbers"))
def eat_cucumbers(cucumbers, eat):
    cucumbers['eat'] = cucumbers['eat'] + eat
    print (cucumbers['eat'])

@then(parsers.parse("I should have {left:d} cucumbers"))
def should_have_left(cucumbers, left):
    assert cucumbers['start'] - cucumbers['eat'] == left