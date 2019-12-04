from kivy.config import Config
Config.read('config.ini')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import random
from math import sqrt

Builder.load_file('gravity.kv')
random.seed(2)


class MainScreen(FloatLayout):
	pass

class Planet(Widget):
	def __init__(self, radius, mass, x, y, **kwargs):
		super().__init__(**kwargs)
		# Parametros que eu criei
		self.radius = radius
		self.mass = mass
		# Parametros de Widget
		self.size = self.radius, self.radius
		self.center_x = x
		self.center_y = y


G = 6.71*(pow(10, -11)) # N * m² / kg²
print(f'{G:e}')


def force(planet1, planet2):

	pos1 = [planet1.center_x, planet1.center_y]
	pos2 = [planet2.center_x, planet2.center_y]
	v = [pos2[0] - pos1[0], pos2[1] - pos1[1]]
	print(v)

	dist = sqrt( pow(v[0], 2) + pow(v[1], 2) )
	print(dist)

	# Força ocorrendo no planeta 1 pelos efeitos do planeta 2 tal que  F = G * M * m / d²
	f12 = G * planet1.mass * planet2.mass / (pow(dist, 2))
	print(f12)

	#TODO: Estudar operação com vetores em numpy
	return f12


def move(planet1, planet2):
	pass




class GravityApp(App):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# Tela principal
		self.main = MainScreen()

		# Objetos
		self.sol = Planet(radius=50, mass=15, x=Window.width/2, y=Window.height/2)
		self.terra = Planet(20, 5, Window.width*2/3, Window.height*3/4)

	def build(self):

		self.main.add_widget(self.sol)
		self.main.add_widget(self.terra)


		force(self.terra, self.sol)

		return self.main



if __name__ == '__main__':
	GravityApp().run()

