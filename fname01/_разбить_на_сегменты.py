import pathlib

>>> pathlib.Path.cwd()
WindowsPath('W:/(_work)/_my_lay5')
a = pathlib.Path.cwd()
>>> a.parts
('W:\\', '(_work)', '_my_lay5')

