from pythonforandroid.recipe import PythonRecipe


class TypingExtensionsRecipe(PythonRecipe):
    version = '4.4.0'
    url = 'https://pypi.python.org/packages/source/t/typing-extensions/typing_extensions-{version}.tar.gz'
    depends = ['typing_extensions']
    call_hostpython_via_targetpython = False
    install_in_hostpython = True


recipe = TypingExtensionsRecipe()
