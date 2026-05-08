from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError
from utils.logger import LogGen

logger = LogGen.loggen()


@given(u'User launches Demoblaze application')
def step_impl(context):
    logger.info('Demoblaze URL loaded')


@when(u'User clicks on Sign up menu')
def step_impl(context):



@when(u'User enters signup username "useraaaaa"')
def step_impl(context):


@when(u'User enters signup password "pwdaaaaa"')
def step_impl(context):


@when(u'User clicks Signup button')
def step_impl(context):


@then(u'User should see signup success message')
def step_impl(context):