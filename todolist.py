import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class Line(Label):

	def remove(self):
		self.root.todo.remove(self.text)
		self.root.remove_widget(self)

class Menu(Widget):
	todo = ListProperty([])
	
	def __init__(self):
		super(Menu, self).__init__()
		adder = Button(text='Add')
		adder.bind(on_press=self.add)

	def load():
		try:
			f = open('todolist.dat', 'r')
			for line in list(f):
				self.todo.append(Line(text=line))
				self.add_widget(Line(line))
		except FileNotFoundError:
			f = open('todolist.dat', 'w')
			
		
	def add():
		new = Popup(text='New Entry:')
		line = TextInput(multiline=False)
		self.todo.append(Line(text=line))
		f = open('todolist.dat', 'r+')
		f.read()
		f.write(line, '\n')
		f.close()
		

class TodoList(App):
	def build(self):
		return Menu().load()
		
if __name__ == '__main__':
	TodoList().run()
