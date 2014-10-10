from zope.interface import Interface


class I{{ cookiecutter.package_name.split('.') | map('capitalize') | join('') }}Specific(Interface):
    """ Browser Layer for {{ cookiecutter.package_name }}. """

