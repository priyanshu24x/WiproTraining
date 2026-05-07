from behave import given,when,then
from selenium import webdriver
from selenium

@given(u'Buyer is on the OLX home page')
def step_impl(context):
    context.driver = webdriver.Edge
    context.driver.maximize_window()
    context.driver.get("https://www.olx.in/")


@given(u'Buyer types product in searchbar')
def step_impl(context):
    searchbar = context.driver.fi
    searchbar.se

@given(u'search results should be displayed')
def step_impl(context):
    pass