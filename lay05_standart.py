
# lay05_standart.py

import PySimpleGUI as sg
from pprint import pprint
mytheme = 'SandyBeach'
sg.theme('SystemDefaultForReal')

from fname01.fname02 import db_full_name
font01 = 'Times New Roman', 20
font02 = 'Times New Roman', 14
font_size=20


import sqlite3
#conn = sqlite3.connect("gui_05.db")
conn = sqlite3.connect(db_full_name)
cursor = conn.cursor()

def st02():
  
      spisok_standart = []                                                                       
      spisok_standart = list(set(cursor.execute("SELECT `Марка` FROM `st_Сплави`")))             
      layout_standart = [                                                                        
          # [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'],                          
          [sg.Text('Стандарти    ', font=font01, size=(40, 1))],                                 
          [sg.Listbox(values=spisok_standart,                                                    
                      font=font01,                                                               
                      size=(30, 6))],                                                            
                                                                                                 
          [sg.Submit(font=font01),                                                               
            # sg.Cancel(font=font01)                                                             
          ]                                                                                      
                                                                                                 
      ]  #    layout_standart = [                                                                
                                                                                                 
      win_standart = sg.Window('Стандарти ', layout_standart)                                    
                                                                                                 
      # spisok2 = []                                                                             
      while True:                                                                                
          event_standart, values_standart = win_standart.read()                                  
          # !!! == (начало) == запись в базу =============================== начало              
          # !!! == (конец) == запись в базу =============================== конец                
                                                                                                 
          if event_standart in (None, 'Cancel'):                                                 
              break                                                                              
                                        
          zzz = values_standart[0][0][0]
          print(f"{values_standart[0][0][0] =}")
          # =============== начало tab1_marka ====================
          spisok_standart_marka = list(cursor.execute(f"SELECT * FROM `st_Сплави` \
                           WHERE `Марка`= '{zzz}';"))                       
          print(f"{zzz =}")
          # pprint(f"{spisok_standart_marka[:][:][2:] =}")                                       
          st_marka = []                                                                          
          # print("== spisok_standart_marka ==")                                                 
          # pprint(spisok_standart_marka[0][2:]) # OK!!! по одному - дает                        
          for z in spisok_standart_marka:                                                        
              st_marka.append(z[2:])                                                             
          header_list = ["Метал", "Марка", "Класифікація", "Доповнення", "Де_використовують"]    
          data = st_marka                                                                        

          tab1_marka = [                                                                         
              [sg.Table(values=data,                                                             
                              headings=header_list,                                              
                              max_col_width=55,                                                  
                              auto_size_columns=True,                                            
                              # auto_size_rows=True,  # такого нет                               
                              justification='centre',                                            
                              alternating_row_color='lightblue',                                 
                              font=font02,                                                       
                              num_rows=min(len(data), 50))],                                     
                                                                                                 
          ]  # tab1_marka = [                                                                    
          #zzz = values_standart[0][0][0]
          # =============== конец tab1_marka ====================

          # =============== начало tab2_st_Xim_sklad ====================
          spisok_standart_Xim_sklad = list(cursor.execute(f"""SELECT * FROM `st_Хiмiчний_склад`  
                                       WHERE `Марка` LIKE '%{zzz}';"""))                         
                                                                                                 
          st_Xim_sklad = []                                                                      
          for z in spisok_standart_Xim_sklad:                                                    
              st_Xim_sklad.append(z[2:])                                                         
          header_list_st_Xim = ["Марка", "Вуглець_С", "Кремній_Si", "Марганець_Mn", "Сірка_S",   
                         "Фосфор_P", "Хром_Cr", "C_plus_Si"]
          data2 = st_Xim_sklad                                                                   
                                                                                                 
          tab2_st_Xim_sklad = [[sg.Table(values=data2,                                           
                              headings=header_list_st_Xim,                                       
                              max_col_width=55,                                                  
                              auto_size_columns=True,                                            
                              # auto_size_rows=True,  # такого нет                               
                              justification='centre',                                            
                              alternating_row_color='lightblue',                                 
                              font=font01,                                                       
                              num_rows=min(len(data2), 50))],                                     
          ] # tab2_st_Xim_sklad                                                                  
          

          # =============== начало tab3_layout ====================
          spisok_standart_Mex_vlast = list(cursor.execute(f"""SELECT * FROM `st_Механiчнi_властивостi`  
                                       WHERE `Назва` LIKE '%{zzz}%';"""))                         
          st_Mex_vlast = []                                                                      
          for z in spisok_standart_Mex_vlast:                                                    
              st_Mex_vlast.append(z[2:])                                                         
          header_list_Mex_vlast = ["Назва","Сортамент",
                           "Межа к-часн. міцн.", "Межа пропорц.",
                           "Віднос. подовж. при розр.","Віднос. звуж.",
                           "Ударна в'язк.","Термообр.","Тверд. за Брин."]
          """                                                    
          "Назва","Сортамент", 
          "Межа_короткочасн_міцн_МПа",                           
          #"Межа_короткочасної_міцності_МПа",                    
          "Межа_пропорційн_МПа",
          "Відносне_подовж_при_разриві",
          #"Відносне_подовження_при_разриві",
          "Відносне_звуження",                                   
          "Ударна в'язкість",                                    
          #"Ударна_в_язкість_кДж_м2",                            
          "Термообробка",
                                        
          "Твердість_за_Бринелем"                                
          #"Твердість_за_Бринелем_МПа_КЧ30_6_ГОСТ_1215_79"       
          """                                                    
                             
          data3 = st_Mex_vlast                                                                   
                                                                                                 
          tab3_st_Mex_vlast = [[sg.Table(values=data3,                                           
                              headings=header_list_Mex_vlast,                                       
                              max_col_width=25,                                                  
                              auto_size_columns=True,                                            
                              # auto_size_rows=True,  # такого нет                               
                              justification='left',                                            
                              alternating_row_color='lightblue',                                 
                              font=font01,                                                       
                              num_rows=min(len(data3), 30))]
          ] # tab3_st_Mex_vlast

          # =============== конец tab3_layout ====================
          # =============== начало tab4_layout ====================
          
          #spisok_standart_Fiz_vlast = list(cursor.execute(f"""SELECT * FROM `st_Фiзичнi_властивостi`  
          #                             WHERE `Марка` LIKE '%{zzz}%';"""))                         
          
          #st_Fiz_vlast = []                                                                      
          #for z in spisok_standart_Fiz_vlast:                                                    
          #    st_Fiz_vlast.append(z[2:])                                                         

          header_list_Fiz_vlast = [
                 "id хто внiс фiз властив","Марка",
                 "Модуль упругості першого роду",
                 "Коефіцієнт температурного лінійного розширення",
	         "Коэффициент теплопроводности теплоемкость материала",
                 "Щільність матеріалу",
                 "C Питома теплоємність матеріалу",
                 "R_10_9 Питомий електроопір Om_m"
                 ]  # header_list_Fiz_vlast = [

          #data4 = st_Fiz_vlast                                                                   
          """                                                                                       
          tab4_st_Fiz_vlast = [[sg.Table(values=data4,  
                              #headings=header_list_Fiz_vlast,                                       
                              #max_col_width=25,                                                  
                              auto_size_columns=True,                                            
                              # auto_size_rows=True,  # такого нет                               
                              justification='left',                                            
                              alternating_row_color='lightblue',                                 
                              font=font01,                                                       
                              num_rows=min(len(data4), 30))]
          ] # tab4_st_Fiz_vlast
          """
          # =============== конец tab4_layout ====================

          
          tab4_st_Fiz_vlast = [[sg.T('Ось тут щось: Фiз. власти',font = font01 )],                     
                         [sg.In(key='in',font=font01)]                                           
                        ]  
          
                                                                                              
          layout_standart_tab = [                                                                
          # [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'],                          
              [sg.Text('Стандарти    ', font=font01, size=(40, 1))],                             
                                                                                                 
                                                                                                 
              [sg.TabGroup([                                                                     
                  [sg.Tab('Марка', tab1_marka, tooltip='tip01',), 
                  sg.Tab('Хiмiчний_склад', tab2_st_Xim_sklad, tooltip='tip02',), 
                  sg.Tab('Механiчнi_властивостi', tab3_st_Mex_vlast, tooltip='tip03', ),
                  sg.Tab('Фiзичнi_властивостi',tab4_st_Fiz_vlast, tooltip='tip04',),
                  ]                                                                              
                  ], 
                  font=font01,                                                                   
                  tooltip='TIP2')
              ],  # sg.TabGroup([                                                                
                                                                                                 
          ] # layout_standart_tab = [                                                            
                                                                                                 
          win_standart_tab = sg.Window('Стандарти ', layout_standart_tab)                        
                                                                                                 
      # spisok2 = []                                                                             
          while True:                                                                            
              event_standart_tab, values_standart_tab = win_standart_tab.read()                  
          # !!! == (начало) == запись в базу =============================== начало              
          # !!! == (конец) == запись в базу =============================== конец                
                                                                                                 
              if event_standart_tab in (None, 'Cancel'):                                         
                  break                                                                          
                                                                                                 
                                                                                                 
                                                                                                 