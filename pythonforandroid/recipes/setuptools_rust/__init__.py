from pythonforandroid.recipe import PythonRecipe


class SetuptoolsRustRecipe(PythonRecipe):
    version = '1.5.2'
    url = 'https://pypi.python.org/packages/source/s/setuptools-rust/setuptools-rust-{version}.tar.gz'
    call_hostpython_via_targetpython = False
    install_in_hostpython = True


recipe = SetuptoolsRustRecipe()