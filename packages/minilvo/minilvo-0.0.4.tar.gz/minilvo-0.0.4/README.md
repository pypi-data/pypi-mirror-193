## How to update the package on pip
1) In setup.py, change the version number (e.g. from 0.0.3 to 0.0.4)
2) Run these commands down below
```
python setup.py sdist bdist_wheel
# pip install twine
twine upload dist/*
```
3) Twine will ask for the PyPI credentials:
    - username: ilvo_vlaanderen
    - password: vgJg6V7t_FQd2Pd
4) Check the new version on https://pypi.org/project/minilvo/#history - It will be available on pip in ~15 seconds
5) Install/update the package in your env: pip install minilvo --upgrade
