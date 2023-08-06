Test
python -m unittest tests/s3_handler_tests.py
python -m unittest tests/folders_handler_tests.py

python setup.py sdist bdist_wheel
python -m twine upload dist/\* --verbose
