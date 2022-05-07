from tkinter import Tk, YES
from tkinter import filedialog
from tkinter import messagebox

from UIwidgets import *
from appEntry import AppEntry
from appButton import AppButton


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('1600x900+150+30')
        self.configure(bg='#424242')
        self.title('C-Graph')

        '''Build all interface'''
        self.insert_app_title()
        self.build_app_menu()
        self.cache_graph_list = []

    def build_app_menu(self):

        def open_filename(mouse=None):
            _open.ask_open_filename(data)
        
        '''Open Button'''
        menu =  AppFrame(self)
        _open = AppButton(menu, '\u2A2E', 1, 0, command=open_filename)
        _open.bind('<Enter>', _open.mouse_in_button)
        _open.bind('<Leave>', _open.mouse_out_button)
        _open.bind('<Button-1>', _open)
        '''Refresh Button'''
        _reff = AppButton(menu, '\u2B6E', 0, 0)
        _reff.bind('<Enter>', _reff.mouse_in_button)
        _reff.bind('<Leave>', _reff.mouse_out_button)
        _reff.bind('<Button-1>', _reff)

        '''Entry One'''
        self.entry1 = AppEntry(menu, '1', 0, 1)
        self.entry1.bind('<Enter>', self.entry1.mouse_in_entry)
        self.entry1.bind('<Leave>', self.entry1.mouse_out_entry)
        '''Entry Two'''
        self.entry2 = AppEntry(menu, '2', 1, 1)
        self.entry2.bind('<Enter>', self.entry2.mouse_in_entry)
        self.entry2.bind('<Leave>', self.entry2.mouse_out_entry)

    def insert_app_title(self):
        '''Graph Frame'''
        self.app_graph = AppFrame(self, YES)
        self.graph_title = Label(self.app_graph, text='GRAPH', font=('Havletica', 22, 'bold'), bg='#424242')
        self.graph_title.pack(expand=YES)
        '''Data Frame'''
        self.app_data = AppFrame(self, YES)
        self.data_title = Label(self.app_data, text='DATA', font=('Havletica', 22, 'bold'), bg='#424242')
        self.data_title.pack(expand=YES)            

    def create_column_graph(self, title):

        def validate_data():
            if not self.entry1.get().isdigit() or not self.entry2.get().isdigit():
                messagebox.showinfo('Incorrect Value!',
                                    f'Please enter a number: 1-{len(data._dict[1])}')
                return

            if int(self.entry1.get()) > len(data._dict[1]) or int(self.entry2.get()) > len(data._dict[1]):
                messagebox.showinfo('Incorrect Value!',
                                    f'Przekroczona wartość!\nMaksymalna z możliwych: [{len(data._dict[1])}]')
                return
            return True

        def return_highest_value():
            '''looking for the longest column'''
            highest_value = int(str(data.highest_values()[-1]).replace('.',''))
            max_column = 100 - (data.len_titles() + data.len_values())
            incre = round(float(highest_value/max_column),2)
            return incre

        def clear_column_graph():
            '''removes graph column if a new file is open'''
            if self.cache_graph_list:
                for center_frame in self.cache_graph_list:
                    center_frame.destroy()

        if not validate_data():
            return
        incre = return_highest_value()
        clear_column_graph()

        '''create a centered frame'''
        self.graph_title.destroy()
        center_frame = Frame(self.app_graph, bg='#424242')
        center_frame.pack(expand=True)
        self.cache_graph_list.append(center_frame)

        ColumnTitle(ColumnFrame(center_frame), data.len_titles()+len(title), 'white', '#424242', title.title())
        for number, column, in enumerate(zip(ColumnGraph.column_color(),
                                             data.get_data_titles(int(self.entry1.get())-1),
                                             data.get_data_values(int(self.entry2.get())-1)
                                             ), 1):

            #if signs alpha exist, check lenghts and cut them
            if column[2][-1].isalpha():
                for sign in ['M', 'Mln', 'm', 'mln']:
                    if column[2].endswith(sign):
                        width = str(round(float(column[2][0:-len(sign)]), 1)).replace('.','')
                        break
            else:
                width = str(round(float(column[2]), 1)).replace('.','')

            '''Frame Center for: title, column, values'''
            fmc = ColumnFrame(center_frame)
            '''Column Graph'''
            tit = ColumnTitle(fmc, data.len_titles(), 'white', '#424242', column[1])
            col = ColumnGraph(fmc, round(float(width)/incre), column[0], None, number)
            val = ColumnValues(fmc, 0, 'white', '#424242', column[2])# Reading from file
            '''Event Bind'''
            col.bind('<Enter>', col.mouse_in_column)
            col.bind('<Leave>', col.mouse_out_column)
            col.bind('<Button-1>', col.mouse_click_column)


class Data:
    def __init__(self):
        self._dict = {}

    def create_data(self, file_name, file_title):
        if self._dict:
            self._dict.clear()

        file_open = open(file_name)
        for key, line in enumerate(file_open.readlines(), 1):
            if line.isspace():
                continue
            self._dict[key] = line.strip().split(',')
        file_open.close()
        app.create_column_graph(file_title)

    def get_data_titles(self, column=0):
        titles = []
        for title in self._dict.values():
            titles.append(title[column])
        return titles

    def get_data_values(self, column=1):
        values = []
        for value in self._dict.values():
            values.append(value[column])
        return values

    def len_titles(self):
        '''title (string) length for total column length'''
        len_title = self.get_data_titles(int(app.entry1.get())-1)
        len_title.sort(key=len)
        return len(len_title[-1])

    def len_values(self):
        '''value (string) length for total column length'''
        len_value = self.get_data_values(int(app.entry2.get())-1)
        len_value.sort(key=len)
        return len(len_value[-1])

    def highest_values(self):
        width_values = []
        len_values = self.get_data_values(int(app.entry2.get())-1)
        #if signs alpha exist, check lenghts and cut them
        for value in len_values:
            for sign in ['M', 'Mln', 'm', 'mln']:
                if value.endswith(sign):
                    value = value[0:-len(sign)]
                    break
            width_values.append(round(float(value), 1))
        width_values.sort()
        return width_values     


if __name__ == '__main__':
    app = App()
    data = Data()
    app.mainloop()
