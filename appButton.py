from tkinter import Label
from tkinter import filedialog

class AppButton(Label):
    '''AppButton, specjalized Class object:'''
    def __init__(self, container, _text='Text', _column=None, _row=None, command=None):
        Label.__init__(self, container)
        self._text = _text
        self.command = command

        settings = {'text':                 _text,
                    'font':                 ('Havletica', 24),
                    'foreground':           'white',
                    'background':           '#424242',
                    'highlightthickness':   1,
                    'highlightbackground':  'black'}

        geometry = {'row':      _row,
                    'column':   _column,
                    'ipadx':    14,
                    'ipady':    0,
                    'padx':     0,
                    'pady':     6}

        self.configure(**settings)
        self.grid(**geometry)

    def mouse_in_button(self, mouse):
        self['fg'] = 'red'

    def mouse_out_button(self, mouse):
        self['fg'] = 'white'
        self['highlightbackground'] = 'black'

    def ask_open_filename(self, data):
        self['highlightbackground'] = 'red'
        
        filetypes = (('CSV files', '*.csv'),
                     ('TXT files', '*.txt'),
                     ('ALL files', '*.*'))

        file_name = filedialog.askopenfilename(
                            title='Open a file',
                            filetypes=filetypes)
        
        if file_name:
            file_title = file_name.split('/')[-1]\
                                  .split('.')[-2]   
            data.create_data(file_name, file_title)

    def refresh(self, mouse):
        if data._dict:
            for x in data._dict.values():
                print(f'{x[int(app.entry1.get())-1]:12}', x[int(app.entry2.get())-1])

    def __str__(self):
        return 'AppButton: ' + self._text

    def __dir__(self):
        return AppButton.__dict__

    def __call__(self, mouse):
        if self.command:
            return self.command()
        print(self.__str__())