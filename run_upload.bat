python setup.py sdist
twine check dist/*
twine upload -r pypi dist/*
