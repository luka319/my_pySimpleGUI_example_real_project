import PySimpleGUI as sg      

# на базе работающего my_si_05.py 

font01 = 'Times New Roman', 20                                                                               
#font11 = 'Arial', 24                                                                                        
font11 = 'Consolas', 18  # пропорциональный !!!!                                                             
font02 = 'Times New Roman', 14                                                                               
font16 = 'Times New Roman', 16                                                                               
font_size=20                                                                                                 
                                                                                                             
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
                                                                                                             
]                                                                                                            

                                                                                                             
lay01_xim_e_in = [                                                                                                
                                                                                                             
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
              for z, x in enumerate (xim_elem)                                                               
                     #======================== 01 ряд === конец ======                                       
              ] # lay01                                                                                      
                                                                                                             
lay02_xim_e_in =  [                                                                                               
                 [sg.Submit(), sg.Cancel()]                                                                  
            ]                                                                                                
                                                                                                             
#layout = lay01 + lay02                                                                                   
layout_xim_experim_in = lay01_xim_e_in + lay02_xim_e_in
                                                                                                             
"""                                                                                                      
    window = sg.Window('My new window', layout)                                                              
                                                                                                             
    while True:             # Event Loop                                                                     
        event, values = window.read()                                                                        
        if event == sg.WIN_CLOSED:                                                                           
            break                                                                                            
"""                                                                                                      
                                                                                                             
#window = sg.Window('Хим. эксперимент внесение данных').Layout(layout)                                            

def xim_exp_in():
    window = sg.Window('Хим. эксперимент внесение данных').Layout(layout_xim_experim_in)
                                                                                                             
    while True:                                                                                              
                                                                                                             
        event, values = window.read()                                                                        
        if event == sg.WIN_CLOSED:                                                                           
            break                                                                                            
        #window['-TEXT-'].update('My new text value')                                                        
                                                                                                             
        print(event, values)                                                                                 
                                                                                                             
                                                                                                             
        for z, x in enumerate (xim_elem):                                                                    
          if not values is None:
             if values['-input_'+x[0]+'-'] != '':
                 window['-text_'+x[0]+'-'].update(background_color=('yellow'), text_color=('red') )            
                                                                                                             
             if values['-input_'+x[1]+'-'] != '':
                 window['-text_'+x[1]+'-'].update(background_color=('yellow'), text_color=('red') )            
                                                                                                             
             if values['-input_'+x[2]+'-'] != '':                                                               
                 window['-text_'+x[2]+'-'].update(background_color=('yellow'), text_color=('red') )            
                                                                                                             
                                                                                                             
          #window['text_C'].background_color=('green')                                                       
                                                                                                             
        #window['-TEXT-'].update('My new text value', background_color=('green'))                            

   
