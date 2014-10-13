from seantis.plonetools import setuphandlers

indexes = [
    #('example_index', 'FieldIndex'),
]


def add_catalog_indexes(context, logger=None):
    if indexes:
        setuphandlers.add_catalog_indexes(
            '{{ cookiecutter.package_name }}', indexes, context, logger
        )


def import_indexes(context):
    if indexes:
        setuphandlers.import_indexes(
            '{{ cookiecutter.package_name }}', indexes, context
        )

