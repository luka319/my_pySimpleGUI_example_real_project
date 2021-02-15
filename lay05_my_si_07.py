# W:\(_work)\_my_lay5\lay05_my_si_07.py
# на базе my_si_07.py
# !!!! Хим. склад - ввод


import PySimpleGUI as sg      

# Very basic window.  Return values as a list      

def xim_table():

    mytheme = 'SandyBeach'                                                                              
    sg.theme('SystemDefaultForReal')                                                                    
                                                                                                        
                                                                                                        
    font01 = 'Times New Roman', 20                                                                      
    #font11 = 'Arial', 24                                                                               
    font11 = 'Consolas', 20  # пропорциональный !!!!                                                    
    font02 = 'Times New Roman', 14                                                                      
    font16 = 'Times New Roman', 16                                                                      
    font_size=20                                                                                        
                                                                                                        
    from pprint import pprint                                                                           
                                                                                                        
    #========================================                                                           
    from fname01.fname02 import myfname, myfname_experim, db_full_name
    import sqlite3                                                                                      
    #conn = sqlite3.connect("gui_07.db") 
    conn = sqlite3.connect(db_full_name)                                                                

    cursor = conn.cursor()                                                                              
    #========================================                                                           
    #global cursor                                                                                                    
                                                                                                        
    xim_elem = [                                                                                        
                                                                                                        
          ('C ',  'N ', 'Zr'),                                                                          
          ('Si',  'Sn', 'Zn'),                                                                          
          ('Mn',  'Nb', 'As'),                                                                          
          ('P ',  'Ti', 'Se'),                                                                          
          ('S ',  'V ', 'Sb'),                                                                          
          ('Cr',  'Ca', 'Ta'),                                                                          
          ('Cu',  'Pb', 'B '),                                                                          
          ('Al',  'La', 'Bi'),                                                                          
          ('Ni',  'Co', 'Te'),                                                                          
          ('Mo',  'W ', 'Mg'),                                                                          
          #('',  ' ', ''),                                                                              
                                                                                                        
    ]                                                                                                   
                                                                                                        
    lay00 = [                                                                                           
                 [sg.Text('id_хто_внiс_хiм_склад',                                                      
                           font=font11, text_color=('cyan'),                                            
                           background_color=('DarkGray'),                                               
                           key='-text_id_хто_внiс_хiм_склад-' ), #silver = #c0c0c0                      
                  sg.Input('', key='-input_id_хто_внiс_хiм_склад-',size=(6, None),                      
                           font=font11),                                                                
                                                                                                        
                  sg.Text('Марка',                                                                      
                           font=font11, text_color=('cyan'),                                            
                           background_color=('DarkGray'),                                               
                           key='-text_Марка-' ), #silver = #c0c0c0                                      
                  sg.Input('', key='-input_Марка-',size=(6, None),                                      
                           font=font11),                                                                
                                                                                                        
                  sg.Text('C_plus_Si',                                                                  
                           font=font11, text_color=('cyan'),                                            
                           background_color=('DarkGray'),                                               
                           key='-text_C_plus_Si-' ), #silver = #c0c0c0                                  
                  sg.Input('', key='-input_C_plus_Si-',size=(6, None),                                  
                           font=font11),                                                                
                                                                                                        
                  sg.Submit(),                                                                          
                  sg.Cancel()                                                                           
                 ]                                                                                      
            ] # lay00                                                                                   
                                                                                                        
    lay01 = [                                                                                           
                                                                                                        
                     [ sg.Text(x[0]+' ',font=font11, text_color=('cyan'),                               
                           background_color=('DarkGray'), key='-text_'+x[0]+'-' ), #silver = #c0c0c0    
                       sg.Input('', key='-input_'+x[0]+'-',size=(6, None),                              
                                font=font11),                                                           
                       sg.Slider(range=(1,3),                                                           
                               default_value=2,                                                         
                               size=(10,15),                                                            
                               orientation='horizontal',                                                
                               #font=('Helvetica', 12)                                                  
                               ), # [sg.Slider                                                          
                       sg.Text(' ',font=font11),                                                        
                       #01 колонка 1                                                                    
                                                                                                        
                       sg.Text(x[1]+' ',font=font11, text_color=('red'),                                
                           background_color=('#a9a9c0'), key='-text_'+x[1]+'-' ),                       
                       sg.Input('', key='-input_'+x[1]+'-',size=(6, None),                              
                                font=font11),                                                           
                       sg.Slider(range=(1,3),                                                           
                               default_value=2,                                                         
                               size=(10,15),                                                            
                               orientation='horizontal',                                                
                               #font=('Helvetica', 12)                                                  
                               ), # [sg.Slider                                                          
                       sg.Text(' ',font=font11),                                                        
                       #01 колонка 2                                                                    
                                                                                                        
                       sg.Text(x[2]+' ',font=font11, text_color=('red'),                                
                           background_color=('DarkGray'), key='-text_'+x[2]+'-' ),                      
                       sg.Input('', key='-input_'+x[2]+'-',size=(6, None),                              
                                font=font11),                                                           
                       sg.Slider(range=(1,3),                                                           
                               default_value=2,                                                         
                               size=(10,15),                                                            
                               orientation='horizontal',                                                
                               #font=('Helvetica', 12)                                                  
                               ), # [sg.Slider                                                          
                       sg.Text(' ',font=font11),                                                        
                       #01 колонка 3                                                                    
                                                                                                        
                     ]                                                                                  
              for z, x in enumerate (xim_elem)                                                          
                     #======================== 01 ряд === конец ======                                  
              ] # lay01                                                                                 
                                                                                                        
    lay02 =  [                                                                                          
                 [sg.Submit(key='-Submit_bottom-'), sg.Cancel(key='-Cancel_bottom-')]                   
            ] # lay02                                                                                   
                                                                                                        
    layout = lay00 + lay01 + lay02                                                                      
    #layout = lay01 + lay02                                                                             
                                                                                                        
                                                                                                        
    """                                                                                                 
    window = sg.Window('My new window', layout)                                                         
                                                                                                        
    while True:             # Event Loop                                                                
        event, values = window.read()                                                                   
        if event == sg.WIN_CLOSED:                                                                      
            break                                                                                       
    """                                                                                                 
                                                                                                        
    #window = sg.Window('Simple data entry window').Layout(layout)                                      
    window = sg.Window('Get filename example', layout, font='Courier 20')                               
                                                                                                        
    while True:                                                                                         
                                                                                                        
        event, values = window.read()                                                                   
        if event == sg.WIN_CLOSED or event == 'Cancel' or event == '-Cancel_bottom-':                   
        #if event == sg.WIN_CLOSED:                                                                     
            break                                                                                       
        #window['-TEXT-'].update('My new text value')                                                   
                                                                                                        
        #print(event, values)                                                                           
                                                                                                        
        #if event == '-Submit_bottom-':                                                                 
        #    print("=== -- sg.Submit низ -- ====================")                                      
                                                                                                        
        #if event == '-Cancel_bottom-':                                                                 
        #    print("=== -- Cancel низ -- ====================")                                         
                                                                                                        
        if event == sg.Submit or event == 'Submit' or event == '-Submit_bottom-':                       
        #if event == sg.WIN_CLOSED:                                                                     
            print("=== sg.Submit верх ====================")                                            
            # !!! вот тут запись в базу                                                                 
                                                                                                        
            #to_db = cursor.execute(f"""INSERT INTO                                                     
            #                      ;"""))                                                               
                                                                                                        
            # =============================================                                             
            gruppa = [                                                                                  
              (                                                                                         
                                                                                                        
    	  values['-input_id_хто_внiс_хiм_склад-'],                                                  
    	  values['-input_Марка-'],                                                                  
              #values['-input_Вуглець_С-'],                                                             
              #values['-input_Кремній_Si-'],                                                            
    	  #values['-input_Марганець_Mn-'],	                                                    
              #values['-input_Сірка_S-'],                                                               
              #values['-input_Фосфор_P-'],                                                              
    	  #values['-input_Хром_Cr-'],                                                               
                                                                                                        
                                                                                                        
              values['-input_C_plus_Si-'],                                                              
                                                                                                        
              values['-input_C -'],                                                                     
              values['-input_Si-'],                                                                     
              values['-input_Mn-'],                                                                     
              values['-input_P -'],                                                                     
              values['-input_S -'],                                                                     
              values['-input_Cr-'],                                                                     
              values['-input_Cu-'],                                                                     
              values['-input_Al-'],                                                                     
              values['-input_Ni-'],                                                                     
              values['-input_Mo-'],                                                                     
                                                                                                        
                                                                                                        
                                                                                                        
              values['-input_N -'],                                                                     
              values['-input_Sn-'],                                                                     
              values['-input_Nb-'],                                                                     
              values['-input_Ti-'],                                                                     
              values['-input_V -'],                                                                     
              values['-input_Ca-'],                                                                     
              values['-input_Pb-'],                                                                     
              values['-input_La-'],                                                                     
              values['-input_Co-'],                                                                     
              values['-input_W -'],                                                                     
                                                                                                        
              values['-input_Zr-'],                                                                     
              values['-input_Zn-'],                                                                     
              values['-input_As-'],                                                                     
              values['-input_Se-'],                                                                     
              values['-input_Sb-'],                                                                     
              values['-input_Ta-'],                                                                     
              values['-input_B -'],                                                                     
              values['-input_Bi-'],                                                                     
              values['-input_Te-'],                                                                     
              values['-input_Mg-']                                                                      
                                                                                                        
              )                                                                                         
              #   ("Мастер и Маргарита", 1, 1, 670.99, 3),                                              
              #   ("Белая гвардия", 1, 1, 540.50, 5),                                                   
             ]                                                                                          
    	                                                                                            
            cursor.executemany("""INSERT INTO experim_Хiмiчний_склад (                                  
    	'id_хто_внiс_хiм_склад',                                                                    
    	'Марка','C_plus_Si',                                                                        
            'C',   'N',  'Zr',                                                                          
            'Si',  'Sn', 'Zn',                                                                          
            'Mn',  'Nb', 'As',                                                                          
            'P',   'Ti', 'Se',                                                                          
            'S',   'V',  'Sb',                                                                          
            'Cr',  'Ca', 'Ta',                                                                          
            'Cu',  'Pb', 'B',                                                                           
            'Al',  'La', 'Bi',                                                                          
            'Ni',  'Co', 'Te',                                                                          
            'Mo',  'W',  'Mg'                                                                           
                     )                                                                                  
      VALUES (?,?,?,  ?,?,?,?,?,?,?,?,?,?,  ?,?,?,?,?,?,?,?,?,?,                                        
              ?,?,?,?,?,?,?,?,?,?                                                                       
              )""",                                                                                     
                                                                                                        
             gruppa)                                                                                    
            conn.commit()                                                                               
            #VALUES (?,?,?,?,?,?,?,?,?, ?,?,?,?,?,?,?,?,?,?, ?,?,?,?,?,?,?,?,?,?, ?,?,?,?)",            
            # =============================================                                             
                                                                                                        
                                                                                                        
        #sg.Popup(f"{values = }", f"{event = }",                                                        
        #              font=font01)                                                                     
                                                                                                        
        #print("values =", values)                                                                      
        #print("event =", event)                                                                        
                                                                                                        
        #pprint(values)                                                                                 
        #pprint(event)                                                                                  
                                                                                                        
                                                                                                        
                                                                                                        
        for z, x in enumerate (xim_elem): #!!! обновление и покраска по энтеру !!!                      
                                                                                                        
          if not values is None:                                                                        
            #if values['-input_'+x[0]+'-']:                                                             
            if values['-input_'+x[0]+'-'] != '':                                                        
                  window['-text_'+x[0]+'-'].update(background_color=('yellow'), text_color=('red') )    
                                                                                                        
            if values['-input_'+x[1]+'-'] != '':                                                        
                  window['-text_'+x[1]+'-'].update(background_color=('yellow'), text_color=('red') )    
                                                                                                        
            if values['-input_'+x[2]+'-'] != '':                                                        
                  window['-text_'+x[2]+'-'].update(background_color=('yellow'), text_color=('red') )    
                                                                                                        
                                                                                                        
          #window['text_C'].background_color=('green')                                                  
                                                                                                        
        #window['-TEXT-'].update('My new text value', background_color=('green'))                       
                                                                                                        
                                                                                                        