导入 sys
导入 os

sys.path.追加(os.路径.绝对路径(r'G:\grasspy_zwmodules\pysimplegui\zwpysimplegui\src'))

import 快手 as sg      

sg.ChangeLookAndFeel('GreenTan')      

# ------ Menu Definition ------ #      
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
            ['Help', 'About...'], ]      

# ------ Column Definition ------ #      
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      

layout = [      
    [sg.Menu(menu_def, tearoff=True)],      
    [sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],    
    [sg.Text('Here is some text.... and a place to enter text')],      
    [sg.输入框('人民万岁')],      
    [sg.Frame(layout=[      
      [sg.复选框('复选框', 大小=(10,1)),  sg.复选框('又一个复选框!', 默认值=True)],      
      [sg.单选按钮('第一个单选按钮!     ', "RADIO1", 默认值=True, 大小=(10,1)), sg.单选按钮('第二个单选按钮!', "RADIO1")]], title='Options',title_color='red',relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],      
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),      
        sg.Multiline(default_text='A second multi-line', size=(35, 3))],      
    [sg.组合框(('组合框 1', '组合框 2'), 大小=(20, 1)),      
        sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],      
    [sg.选项菜单(('选项菜单 1', '选项菜单 2', '选项菜单 3'))],      
    [sg.列表框(值选项=('列表框 1', '列表框 2', '列表框 3'), 大小=(30, 3)),      
        sg.Frame('Labelled Group',[[      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),      
        sg.Column(column1, background_color='#F7F3EC')]])],      
    [sg.Text('_'  * 80)],      
    [sg.Text('Choose A Folder', size=(35, 1))],      
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
        sg.输入框('默认文件夹'), sg.FolderBrowse()],      
    [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
]      


window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)      

event, values = window.read()      

window.close()    

sg.popup('Title',      
            'The results of the window.',      
            'The button clicked was "{}"'.format(event),      
            'The values are', values)      