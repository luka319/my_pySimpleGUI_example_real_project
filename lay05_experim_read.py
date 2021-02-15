import PySimpleGUI as sg

from pprint import pprint
import subprocess

st_marka = []                                                          

font01 = 'Times New Roman', 20
font02 = 'Times New Roman', 14                                         
font16 = 'Times New Roman', 16                                         
font_size=20                                                           

from fname01.fname02 import thermoEx, FiltrData_Thermal
# ===========================================

def exp_02():

    header_list01 = ["Метал", "Марка", "Класифікація", "Доповнення", 
                           "Де_використовують"]

                                                                        
    #data = [['shiny','001'],['adh','002']]                              
    tab1_marka = [[sg.Table(values=st_marka, # spisok_standart_marka  
    #layout = [[sg.Table(values=st_marka, # spisok_standart_marka        
    #layout = [[sg.Table(values=spisok_standart_marka,                  
                                headings=header_list01,
                                #max_col_width=55,                       
                                auto_size_columns=True,                 
                                justification='centre',                 
                                font = font16,                          
                               # alternating_row_color='lightblue',     
                                num_rows=min(len(st_marka), 20))],          
              [sg.Button('Exit')]] # tab1_marka = [
             
                                                          
    #window = sg.Window('My first GUI', layout)                          
    #button, values = window.Read()  
                                                                        
    #print(button, values)                                               

    #!!!!!!!! 9 june 2020 ==============================================


    tab2_layout = [[sg.T('Хiмiчний_склад 567',font = font01 )],
                           [sg.In(key='in',font=font01)]
                          ]
    # !!!!!! тут остановился
    header_list02 = ["Метал", "Марка", "Класифікація", "Доповнення", 
                           "Де_використовують"]



    tab2_xim =  [[sg.Table(values=st_marka, # spisok_standart_marka  
    #layout = [[sg.Table(values=st_marka, # spisok_standart_marka        
    #layout = [[sg.Table(values=spisok_standart_marka,                  
                                headings=header_list02,
                                #max_col_width=55,                       
                                auto_size_columns=True,                 
                                justification='centre',                 
                                font = font16,                          
                               # alternating_row_color='lightblue',     
                                num_rows=min(len(st_marka), 20))],          
              [sg.Button('Exit')]] # tab1_marka = [





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

    tab7_layout = [
                   [sg.Button('Запустить ThermoEX', key='tab7_layout',font=font01,
                    button_color=(sg.YELLOWS[0], sg.GREENS[0]) )],

                  ]

    tab8_layout = [
                   [sg.Button('Запустить FiltrData_Thermal', key='tab8_layout',font=font01,
                    button_color=(sg.YELLOWS[0], sg.BLUES[0]) )],

                  ]

    tab9_layout = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )],
                           [sg.In(key='in',font=font01)]
                          ]

    tab10_layout = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )],
                           [sg.In(key='in',font=font01)]
                          ]

    # ======== <<< основная таблица из 2-х частей - верх и низ >>> ================
    layout_experim_tab = [                                                   
    # [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'],            
        [sg.Text('Експерiмент    ', font=font01, size=(40, 1))],             
                                                                             
        [sg.TabGroup([                                                       
            [sg.Tab('Марка', tab1_marka, tooltip='tip01',),                  
            #sg.Tab('Хiмiчний_склад', tab2_st_Xim_sklad,),                    
            #sg.Tab('Хiмiчний_склад 567', tab2_Xim_sklad, tooltip='tip02', ),
            sg.Tab('Хiмiчний_склад 567', tab2_layout, tooltip='tip02', ),
            sg.Tab('Механiчнi_властивостi', tab3_layout, tooltip='tip03', ), 
            sg.Tab('Фiзичнi_властивостi',tab4_layout,),                      
            sg.Tab('Швидкість охолодження',tab5_layout,),                    
            ] # [sg.Tab                                                      
            ],                                                               
            font=font01,                                                     
            tooltip='TIP2')                                                  
        ],  # sg.TabGroup([                                                  
                                                                             
        [sg.TabGroup([                                                       
            [sg.Tab('Фото розплаву',tab6_layout,),                           
            sg.Tab('Фільтрація ThermoEX',tab7_layout,),                      
            sg.Tab('Фільтрація адаптивна',tab8_layout,),                     
            sg.Tab('Порівняння кривих',tab9_layout,),                        
            sg.Tab('Фахівець',tab10_layout,),                                
            ] # [sg.Tab                                                      
            ],                                                               
            font=font01,                                                     
            tooltip='TIP2')                                                  
        ],  # sg.TabGroup([                                                  
                                                                             
    ] # layout_experim_tab = [                                               
    win_experim_tab = sg.Window('Експерiмент ', layout_experim_tab)          
    event, values = win_experim_tab.Read()                                      

    #sg.Popup(f"{values = }", f"{event = }", f"{values[1] =}",
    #                            font=font01)

    if event=="tab7_layout":

        #if values[1]=="Запустить ThermoEX":
           #run01()
           #subprocess.call("Z://(__go)//[go]_stepik//part_1//_1.7.3_iota//one_01.exe")
           subprocess.call(thermoEx)
           #print(f"{thermoEx = }")
           print("=== tab7_layout  subproceess.call ===")


    if event=="tab8_layout":

        #if values[1]=="Запустить ThermoEX":
           #run01()
           #subprocess.call("Z://(__go)//[go]_stepik//part_1//_1.7.3_iota//one_01.exe")
           subprocess.call(FiltrData_Thermal)
           #print(f"{thermoEx = }")
           print("=== tab8_layout subproceess.call ===")

    

#exp_02()


#def exp_01(poisk):   # !!!!!!!!
def exp_01():   # !!!!!!!!

      font01 = 'Times New Roman', 20
      font02 = 'Times New Roman', 14                                         
      font16 = 'Times New Roman', 16                                         
      font_size=20                                                           
      #===========================                                           
                                                                             
      import sqlite3                                                         
      #conn = sqlite3.connect("gui_05.db") #                                 
      #cursor = conn.cursor()                                                
                                                                             
      from fname01.fname02 import myfname, myfname_experim, db_full_name     
                                                                             
      conn = sqlite3.connect(db_full_name)                                   
      cursor = conn.cursor()                                                 
      print(f"{db_full_name =}")                                             

      #!!!!!!

      spisok_experim = []                                                                          
      #spisok_experim = list(set(cursor.execute("SELECT `Марка` FROM `experim_загальне`")))
      spisok_experim = list( cursor.execute("SELECT `Марка` FROM `experim_загальне`") )
      #pprint(f"{spisok_experim =}")
      #input("==== press key ===")
      layout_experim = [                                                                           
           # [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'],                            
           [sg.Text('Експерiмент    ', font=font01, size=(40, 1))],                                 
           [sg.Listbox(values=spisok_experim,                                                       
                font=font16,                                                                 
                size=(30, 6))],                                                              
                                                                                             
           [sg.Submit(font=font01),                                                                 
           # sg.Cancel(font=font01)                                                               
           ]                                                                                        
                                                                                             
      ]  #    layout_experim = [      
       
      win_experim = sg.Window('Експерiмент ', layout_experim)

      # spisok2 = []
      while True:
            event_experim, values_experim = win_experim.read()
            # !!! == (начало) == запись в базу =============================== начало
            # !!! == (конец) == запись в базу =============================== конец

            if event_experim in (None, 'Cancel'):
                break


            sg.Popup(f"{values_experim = }", f"{event_experim = }",
                                    font=font01)


            zzz = values_experim[0][0][0]
            #!!!!!!
            #==========================                                            
            #st_marka = []


            #values_standart = []
            #values_standart.append('КЧ70-2')
            #values_standart.append('КЧ30-6') # !!!!!!!!

            #zzz = poisk
            #zzz = values_standart[0]

            #print(f"{zzz =}")
            #input("=== press key ===")


            spisok_standart_marka = list(cursor.execute(f"""SELECT * FROM `experim_загальне`
                                   WHERE `Марка` LIKE '{zzz}%';"""))                         

                                   #WHERE `Марка`= '{values_standart[0][0][0]}';"))
            ##st_marka = [] # !!!!!
            global st_marka

            for z in spisok_standart_marka:                                                  
                  st_marka.append(z[3:])                                                     

            #print(f" experim_read exp_01 {st_marka =}")
            #input("=== press key ===")

            if not st_marka:

               print("st_marka пустой!!!")
               input("=== press key ===")
               exit()

            exp_02()
