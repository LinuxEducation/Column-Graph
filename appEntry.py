from tkinter import Entry, CENTER, SOLID, END


class AppEntry(Entry):
	def __init__(self, container, number, _column, _row):
		Entry.__init__(self, container)
		self.number = number

		settings = {'relief':               SOLID,
					'bg':                   '#424242', 
					'fg':                   'white',
					'width':                3,
					'font':                 ('Verdana', 24), 
					'highlightthickness':   0.1, 
					'highlightbackground':  'black', 
					'justify':              CENTER}

		geometry = {'column':   _column,
					'row':      _row,
					'ipadx':    1,
					'ipady':    3}
		
		self.insert(0, self.number)
		self.configure(**settings)
		self.grid(**geometry)

	def mouse_in_entry(self, mouse):
		self.delete(0, END)

	def mouse_out_entry(self, mouse):
		if self.get():
			mouse.widget.__dict__['number'] = self.get()
		else:
			self.insert(0, mouse.widget.__dict__['number'])

	def __dir__(self):
		return AppEntry.__dict__