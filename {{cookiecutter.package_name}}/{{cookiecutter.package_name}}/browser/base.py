from five import grok

from seantis.plonetools.browser import BaseView as SharedBaseView
from seantis.plonetools.browser import BaseForm as SharedBaseForm

from {{ cookiecutter.package_name }}.interfaces import I{{ cookiecutter.package_name.split('.') | map('capitalize') | join('') }}Specific


class BaseView(SharedBaseView):

    grok.baseclass()
    grok.layer(I{{ cookiecutter.package_name.split('.') | map('capitalize') | join('') }}Specific)

    domain = '{{ cookiecutter.package_name }}'


class BaseForm(SharedBaseForm):

    grok.baseclass()
    grok.layer(I{{ cookiecutter.package_name.split('.') | map('capitalize') | join('') }}Specific)

    domain = '{{ cookiecutter.package_name }}'

