from tkinter import Frame, Label, LEFT, BOTH, NW, W, SE, SW

class AppFrame(Frame):
    def __init__(self, container, _expand=None):
        Frame.__init__(self, container)

        settings = {'background':           '#424242',
                    'highlightthickness':   1.2,
                    'highlightbackground':  'black'}

        geometry = {'anchor':   NW,
                    'side':     LEFT,
                    'fill':     BOTH,
                    'expand':   _expand,
                    'padx':     20,
                    'pady':     25}

        self.configure(**settings)
        self.pack(**geometry)


class ColumnFrame(Frame):
    '''Frame object for Column Graph: title, color column and values'''
    def __init__(self, container, _bg='#424242'):
        Frame.__init__(self, container, bg=_bg)
        self.pack(anchor=W)


class GraphLabel(Label):
    '''Shared Namespace for: ColumnTitlem GraphTitle, ColumnValues'''
    def __init__(self, container, _width, _fcolor, _bcolor, _text):
        Label.__init__(self, container)

        self.width = _width
        self.fcolor = _fcolor
        self.bcolor = _bcolor
        self.text = _text

    def label_settings(self):
        settings = {'text':         self.text,
                    'width':        self.width,
                    'fg':           self.fcolor,
                    'bg':           self.bcolor,
                    'font':         ['Verdana', 16, 'bold', 'italic']}
        return settings

    def label_geometry(self):
        geometry = {'side':     LEFT,
                    'padx':     2,
                    'ipady':    5,
                    'pady':     1}
        return geometry


class ColumnTitle(GraphLabel):
    def __init__(self, container, _width=15, _fcolor='black', _bcolor='white', _text='Text'):
        GraphLabel.__init__(self, container, _width, _fcolor, _bcolor, _text)

        self.configure(**self.label_settings(), anchor=SE)
        self.pack(**self.label_geometry())


class ColumnGraph(GraphLabel):
    def __init__(self, container, _width=10, _bcolor='green', _bg=None, _text=None):
        GraphLabel.__init__(self, container, _width, _bg, _bcolor, _text)

        self.configure(**self.label_settings(), anchor=SW)
        self.pack(**self.label_geometry())
        self['highlightthickness'] = 1
        self['highlightbackground'] = 'black'

    def mouse_in_column(self, mouse):
        self['bg'] = 'white'    
    def mouse_out_column(self, mouse):
        self['bg'] = mouse.widget.__dict__['bcolor']

    def mouse_click_column(self, mouse):
        print('Column', mouse.widget.cget('text'))
        #key = mouse.widget.cget('text')
        #print('Key:', key, data._dict[(key)])

    def column_color():
        color = ['#E81123', '#F7630C', '#FFB900',
                '#006381', '#0078D1', '#0099BC',
                '#018574', '#00B294', '#00CC6A', 
                '#7B1FA2', '#744DA9', '#8764B8',
                '#9E9D24', '#AFB42B', '#C0CA43',
                '#795548', '#4E342E', '#5D4037',]
        return color

class ColumnValues(GraphLabel):
    def __init__(self, container, _width=0, _fcolor='black', _bcolor=None, _text=0):
        GraphLabel.__init__(self, container, _width, _fcolor, _bcolor, _text)

        self.configure(**self.label_settings(), anchor=SW)
        self.pack(**self.label_geometry())