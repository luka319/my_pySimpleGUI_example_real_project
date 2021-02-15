## https://ru.stackoverflow.com/questions/535318/Текущая-директория-в-python

import inspect
import os
import sys

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)

#print(f"{get_script_dir() = }")
full_name = get_script_dir()
#print(f"{full_name = }")


path = os.path.normpath(full_name)  
itog = path.split(os.sep)
itog = itog[:-1]
itog2 = itog[:]
itog3 = itog[:]

itog.append('database_')
itog_join =[z+os.sep for z in itog]
itog_join2 = ''.join(itog_join)

itog2.append('thermo_new')
itog2_join =[z+os.sep for z in itog2]
itog2_thermoEx = ''.join(itog2_join)

itog3.append('FiltrData_Thermal')
itog3_join =[z+os.sep for z in itog3]
itog3_FiltrData_Thermal = ''.join(itog3_join)
#"W:\(_work)\_my_lay5\FiltrData_Thermal\FiltrData.exe" 


#print(f"{itog_join =}")
#print(f"{itog_join2 =}")

#print(f"{itog2_join =}")
#print(f"{itog2_thermoEx =}")


