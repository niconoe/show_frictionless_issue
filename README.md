Minimal reproducible example to illustrate https://github.com/frictionlessdata/frictionless-py/issues/956:

Tested on Python 3.8

When running `demo.py` as is, output is:

    
    ✕ valid package, errors:
    Errors for resource deployments:
    {'code': 'scheme-error',
     'description': 'Data reading error because of incorrect scheme.',
     'message': 'The data source could not be successfully loaded: [Errno 2] No '
                "such file or directory: 'deployments.csv'",
     'name': 'Scheme Error',
     'note': "[Errno 2] No such file or directory: 'deployments.csv'",
     'tags': []}
    Errors for resource media:
    {'code': 'scheme-error',
     'description': 'Data reading error because of incorrect scheme.',
     'message': 'The data source could not be successfully loaded: [Errno 2] No '
                "such file or directory: 'media.csv'",
     'name': 'Scheme Error',
     'note': "[Errno 2] No such file or directory: 'media.csv'",
     'tags': []}
    Errors for resource observations:
    {'code': 'scheme-error',
     'description': 'Data reading error because of incorrect scheme.',
     'message': 'The data source could not be successfully loaded: [Errno 2] No '
                "such file or directory: 'observations.csv'",
     'name': 'Scheme Error',
     'note': "[Errno 2] No such file or directory: 'observations.csv'",
     'tags': []}
    
However, those errors disappear and package is reported valid if we uncomment line #14 (`os.chdir(EXAMPLE_DESCRIPTOR_PATH.parent)`)