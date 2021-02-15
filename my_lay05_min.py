import PySimpleGUI as sg
from pprint import pprint
mytheme = 'SandyBeach'
sg.theme('SystemDefaultForReal')

"""
import sqlite3
conn = sqlite3.connect("gui_05.db")
cursor = conn.cursor()


from pathlib import Path as Path2
import sys
from os import path
import openpyxl
import xlrd
"""

from fname01.fname02 import myfname, myfname_experim, db_full_name
from lay05_standart import st02
from lay05_experim_read import exp_01, exp_02

from lay05_xim_experim_input import lay02_xim_e_in, lay01_xim_e_in
from lay05_xim_experim_input import xim_elem, font11, layout_xim_experim_in 

# список и layout
#from lay05_xim_experim_input import xim_exp_in # def all

#from lay05_my_si_05_2 import xim_table
from lay05_my_si_07 import xim_table

import sqlite3
#conn = sqlite3.connect("gui_05.db")
conn = sqlite3.connect(db_full_name)
cursor = conn.cursor()

#print(f"{db_full_name =}")
#input("=== press key ===")
#
# ======================================================
font01 = 'Times New Roman', 20
font02 = 'Times New Roman', 14
font16 = 'Times New Roman', 16
font_size=20
layout = [

    # [sg.Text('Старт', size=(15, 1), font=("Times New Roman", 20)),
    [sg.Text('Старт', font=font01, size=(15, 1)),
     sg.Text('Пошук за маркою метала',
              font=font01,
              size=(25,1), key='-OUTPUT-'),
     sg.InputText("                        ",
                  font=font01,
                  key='-poisk-')
    ],
     # [sg.Image(r'PySimpleGUI_Logo_320.png')],
     [sg.Text('     ', font=font01, size=(40, 1)),
       sg.Image(r"лого_АРМ_Ливарник.png")],

    [sg.R(f'Стандарти {1}', "RADIO1",
          font=font01,
          size=(30, 20),
          key="-standart-"),
     # sg.Image(r'PySimpleGUI_Logo_320.png'),
    ],

    [sg.R(f'Экспериментальнi даннi {2}', "RADIO1",
          font=font01,
          size=(30, 20),
          key="-experim-")
     ],

    [sg.R(f'Внесення новоi iнформацii {3}', "RADIO1",
          font=font01,
          size=(30, 20),
          key="-new-")
     ],

    # [sg.Submit(font01), sg.Cancel(font01)]
    [sg.Submit(font=font01),
     sg.Cancel(font=font01)

     ]
]

window = sg.Window('Simple data entry window', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break

    if event == 'Submit':
        # change the "output" element to be the value of "input" element
        a = values['-poisk-']
        values['-poisk-'] = "==>> Принято: " + a
        window['-OUTPUT-'].update(values['-poisk-'])
        window['-poisk-'].update('')

    if values['-standart-']:
        st02() # from lay05_standart import st02  # lay05_standart.py

    if values['-experim-']:                                                                          
        exp_01()  # from lay05_experim_read import exp_01, exp_02
        #exp_01('БГ-2020')
        exp_02()

    if values['-new-']:

        layout2 = [
            [sg.R(f'внесення новоi iнформацii \n - Стандарти', "RADIO2",
                  font=font01,
                  size=(30, 20),
                  key="-new_standart-")

             ],

            [sg.R(f'внесення новоi iнформацii \nЭкспериментальнi даннi', "RADIO2",
                  font=font01,
                  size=(30, 20),
                  key="-new_experim-")
             ],

            [sg.Submit(font=font01),  # это события, а не значения
             ]
        ]  # layout2 = [

        win2 = sg.Window('внесення новоi iнформацii', layout2)

        while True:
            event2, values2 = win2.read()
            # !!! == (начало) == запись в базу =============================== начало
            # !!! == (конец) == запись в базу =============================== конец

            if event2 in (None, 'Cancel'):  # Cancel из этого окна не срабатывает
                break

            if values2["-new_standart-"]:
                layout3_new_standart = [
                [sg.Text('Даннi по ДСТу ', size=(20, 1), font=("Helvetica", 18))],
                [sg.FileBrowse('Вибрати файл (1)', font=("Helvetica", 20)),
                   sg.Text('було вибрано: ', size=(40, 1), font=("Helvetica", 18)),
                ],
                [sg.Submit('Завантажити _ Ok', font="Helvetica " + str(font_size))
                     # ,sg.Button('Cancel', font="Helvetica " + str(font_size))
                ] #  sg.Submit('Завантажити _ Ok
                # sg.popup_ok_cancel('PopupOKCancel')

                ] # layout3_new_standart =

                if layout3_new_standart:
                    win3 = sg.Window('Даннi по ДСТу внесення новоi iнформацii', layout3_new_standart)

                    while True:
                        event3, values3 = win3.read()
                        # !!! == (начало) == запись в базу =============================== начало
                        # !!! == (конец) == запись в базу =============================== конец

                        if event3 in (None, 'Cancel'):  # Cancel из этого окна не срабатывает
                            break

                        if values3['Вибрати файл (1)']:
                            myfname(values3['Вибрати файл (1)'])

                            sg.Popup("Удачно запаисал в стандартную базу",
                                    font=font01)
            if values2["-new_experim-"]:

                tab1_marka = [                                             
     
                [sg.Text('Сплав',font=font01), 
                 sg.Input(key='Сплав',size=(40, None),font=font01)], 

                [sg.Text('Марка',font=font01), 
                 sg.Input(key='Марка',size=(40, None),font=font01)], 

                [sg.Text('Класифiкацiя',font=font01), 
                 sg.Input(key='Класифiкацiя',size=(40, None),font=font01)], 

                [sg.Text('Доповнення',font=font01), 
                 sg.Input(key='Доповнення',size=(40, None),font=font01)], 
                
                [sg.Text('Де використовують',font=font01), 
                 sg.Input(key='Де використовують',size=(40, None),font=font01)], 

                [sg.Text('Iнформацiя внесена',font=font01), 
                 sg.Input(key='Iнформацiя внесена',size=(40, None),font=font01)], 

                [sg.Text('Фахiвець',font=font01), 
                 sg.Input(key='Фахiвець',size=(40, None),font=font01)], 

       		[sg.OK(font=font01), sg.Cancel(font=font01)],
                                                                              
                ]  # tab1_marka = [                                             


                tab2_Xim_sklad = [

                     [sg.Button('внести хим. эксперим.', 
                      key='tab2_st_Xim_sklad_',font=font01,
                      button_color=(sg.YELLOWS[0], sg.GREENS[0]) )],
                
                     #lay01_xim_e_in,
                     """
                     [ sg.Text(x[0]+' ',font=font11, text_color=('cyan'),                                    
                           background_color=('DarkGray'), key='-text_'+x[0]+'-' ), #silver = #c0c0c0         
                       sg.Input(key='-input_'+x[0]+'-',size=(6, None),                                       
                                font=font11),                                                                
                       sg.Slider(range=(1,3),                                                                
                               default_value=2,                                                              
                               size=(10,15),                                                                 
                               orientation='horizontal',                                                     
                               font=('Helvetica', 12)), # [sg.Slider                                         
                       sg.Text(' ',font=font11),                                                             
                       #01 колонка 1                                                                         
                                                                                                             
                       sg.Text(x[1]+' ',font=font11, text_color=('red'),                                     
                           background_color=('#a9a9c0'), key='-text_'+x[1]+'-' ),                            
                       sg.Input(key='-input_'+x[1]+'-',size=(6, None),                                       
                                font=font11),                                                                
                       sg.Slider(range=(1,3),                                                                
                               default_value=2,                                                              
                               size=(10,15),                                                                 
                               orientation='horizontal',                                                     
                               font=('Helvetica', 12)), # [sg.Slider                                         
                       sg.Text(' ',font=font11),                                                             
                       #01 колонка 2                                                                         
                                                                                                             
                       sg.Text(x[2]+' ',font=font11, text_color=('red'),                                     
                           background_color=('DarkGray'), key='-text_'+x[2]+'-' ),                           
                       sg.Input(key='-input_'+x[2]+'-',size=(6, None),                                       
                                font=font11),                                                                
                       sg.Slider(range=(1,3),                                                                
                               default_value=2,                                                              
                               size=(10,15),                                                                 
                               orientation='horizontal',                                                     
                               font=('Helvetica', 12)), # [sg.Slider                                         
                       sg.Text(' ',font=font11),                                                             
                       #01 колонка 3                                                                         
                     ]
                     """
                #for z, x in enumerate (xim_elem)
                     #======================== 01 ряд === конец ======                                       
                # lay01                                                                                      

                ] #tab2_Xim_sklad                                    
                

                #tab2_Xim_sklad = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )], 
                #               [sg.In(key='in',font=font01)]                       
                #              ]                                                    


                tab2_layout = [ 

                               [sg.Button('внести хим. эксперим.', 
                                key='tab2_Xim_sklad',font=font01,
                                button_color=(sg.YELLOWS[0], sg.GREENS[0]) )],
                               
                              ]                                                    

            
                tab3_layout = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )], 
                               [sg.In(key='in',font=font01)]                       
                              ]                                                    
                tab4_layout = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )], 
                               [sg.In(key='in',font=font01)]                       
                              ]                                                    
                tab5_layout = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )], 
                               [sg.In(key='in',font=font01)]                       
                              ]                                                    
                                                                                   
                tab6_layout = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )], 
                               [sg.In(key='in',font=font01)]                       
                              ]                                                    
                                                                                   
                tab7_layout = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )], 
                               [sg.In(key='in',font=font01)]                       
                              ]                                                    
                                                                                   
                tab8_layout = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )], 
                               [sg.In(key='in',font=font01)]                       
                              ]                                                    
                                                                                   
                tab9_layout = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )], 
                               [sg.In(key='in',font=font01)]                       
                              ]                                                    
                                                                                   
                tab10_layout = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )],
                               [sg.In(key='in',font=font01)]                       
                              ]                                                    
            


                layout4_new_experim_tab = [
            # [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'],
                [sg.Text('Експерiмент внесення нових   ', font=font01, size=(40, 1))],
#=========================
#=========================
                [sg.TabGroup([
                    [sg.Tab('Марка', tab1_marka, tooltip='tip01'),
                     #sg.Tab('Хiмiчний склад',tab2_Xim_sklad, tooltip='tip02' ),
                     sg.Tab('Хiмiчний склад', tab2_layout, tooltip='tip02', ),
                     sg.Tab('Механiчнi властивостi', tab3_layout, tooltip='tip03', ),
                     sg.Tab('Фiзичнi властивостi',tab4_layout,),
                     sg.Tab('Швидкість охолодження',tab5_layout,),
                    ] # [sg.Tab
                    ],font=font01)
                    #], font=font01,
                    #   tooltip='TIP2')
                ],  # sg.TabGroup([
                [sg.TabGroup([
                    [sg.Tab('Фото розплаву',tab6_layout,),
                    sg.Tab('Фільтрація ThermoEX',tab7_layout,),
                    sg.Tab('Фільтрація адаптивна',tab8_layout,),
                    sg.Tab('Порівняння кривих',tab9_layout,),
                    sg.Tab('Фахівець',tab10_layout,),
                    ] # [sg.Tab
                    ],font=font01)
                    #], font=font01,
                    #   tooltip='TIP2')
                ]  # sg.TabGroup([

                ]  # layout4_new_experim_tab = [

                """
                layout4_new_experim = [
                [sg.Text('Экспериментальнi даннi ', size=(20, 1), font=("Helvetica", 18))],
                [sg.FileBrowse('Вибрати файл (2)', font=("Helvetica", 20)),
                  sg.Text('було вибрано: ', size=(40, 1), font=("Helvetica", 18))
                ],
                [sg.Button('Завантажити _ Ok', font="Helvetica " + str(font_size)),
                     # sg.Button('Cancel', font="Helvetica " + str(font_size))
                ],

                ] #    layout4_new_experim =
                

                if layout4_new_experim:
                    win4 = sg.Window('Экспериментальнi даннi внесення новоi iнформацii', layout4_new_experim)

                    while True:
                        event4, values4 = win4.read()
                        # !!! == (начало) == запись в базу =============================== начало
                        # !!! == (конец) == запись в базу =============================== конец

                        if event4 in (None, 'Cancel'):  # Cancel из этого окна не срабатывает
                            break

                        if values4['Вибрати файл (2)']:
                            myfname_experim(values4['Вибрати файл (2)'])

                            sg.Popup("Удачно записал в экспериментальную базу",
                                    font=font01)
                """
                # =============================
                if layout4_new_experim_tab:

                    win4 = sg.Window('Экспериментальнi даннi внесення новоi iнформацii', layout4_new_experim_tab)

                    while True:
                        event4, values4 = win4.read()
                        # !!! == (начало) == запись в базу =============================== начало
                        # !!! == (конец) == запись в базу =============================== конец

                        if event4 in (None, 'Cancel'):  # Cancel из этого окна не срабатывает
                            break

                        sg.Popup(f"{values4 = }", f"{event4 = }",
                                    font=font01)


                        if event4 == "tab2_Xim_sklad":
                                #xim_exp_in()
                                #lay05_my_si_05_2
                                xim_table()
                                pass



                        # ==================================                                     
                        # БД                                                                     
                        if values4['Сплав'] or values4['Марка']:                                 
                                                                                                 
                              gruppa = [                                                               
                                        (                                                              
                                  values4['Фахiвець'],values4['Iнформацiя внесена'],           
                                  values4['Сплав'],values4['Марка'],values4['Класифiкацiя'],   
                                  values4['Доповнення'],values4['Де використовують']           
                                        ),                                                             
                                       ]                                                               
                              	                                                                 
                              cursor.executemany("""INSERT INTO `experim_загальне`(`id_фахiвець_який_внiс_сплав`,
                                        	'дата_внесення_даних', 
                                        	`Сплав`,`Марка`, `Класифікація`,
                                                `Доповнення`,`Де_використовують`)
                                                 VALUES (?,?,?,?,?,?,?)""", gruppa)                     
                              conn.commit()                                                            

 
                        #if values4['Вибрати файл (2)']:
                        #    myfname_experim(values4['Вибрати файл (2)'])

                        sg.Popup("Удачно записал в экспериментальную базу",
                                    font=font01)
