# run-web-pycode

A simple package to execute remote python scripts

Install:

``` bash
pip install run-web-pycode
```

Example:

``` bash
# run_web_pycode https://raw.githubusercontent.com/AngusWG/run-web-pycode/master/tests/a_script.py
pyw run https://raw.githubusercontent.com/AngusWG/run-web-pycode/master/tests/a_script.py

# set proxy
pyw set_proxy http https://127.0.0.1:9999
pyw set_proxy http # for unset

# get help
pyw --help
pyw run --help
pyw set_proxy --help
```

> when you use `pyw run https://raw.githubusercontent.com/AngusWG/run-web-pycode/master/tests/a_script.py`  
> it's equal `python -c "from urllib.request import urlopen ;exec(urlopen('https://github.com/AngusWG/cookiecutter-py-package/raw/master/git_pre_commit_hook.py').read())"`

* pyw is simplified command as run_web_pycode

## Features

- [x] Run code by Url
- [x] A simple entry point `pyw`
- [x] Set proxy
- [x] package to pypi
- [ ] Convert GitHub.com url to raw.githubusercontent.com url

> Please feel free to suggest issue and contribute code.

## For Contributor

* [Black formatter](https://github.com/psf/black)

> This project use black, please set `Continuation indent` = 4  
> Pycharm - File - Settings - Editor - Code Style - Python - Tabs and Indents

* [Flake8 lint](https://github.com/PyCQA/flake8)

> Use flake8 to check your code style.

* [Cookiecutter maker](https://github.com/AngusWG/cookiecutter-py-package)

> This project is made by [AngusWG\cookiecutter-py-package](https://github.com/AngusWG/cookiecutter-py-package)
