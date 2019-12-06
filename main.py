from kivy.config import Config
Config.read('config.ini')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from math import cos, sin, pi
from kivy.uix.label import Label
import random

Builder.load_file('gravity.kv')
random.seed(2)


class MainScreen(FloatLayout):
	pass


class Planet(Widget):

	def __init__(self, radius, dist, nome, **kwargs):
		super().__init__(**kwargs)
		# Parametros que eu criei
		self.dist = dist
		self.angle = 0 # starts at 0
		self.nome = Label(text=nome, color=(0 / 255, 0 / 255, 0 / 255, 1))
		self.add_widget(self.nome)

		# Parametros de Widget
		self.size = radius, radius
		self.center_x = 640 + self.dist * cos(self.angle)
		self.center_y = 360 + self.dist * sin(self.angle)
		self.text = nome


class GravityApp(App):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# Tela principal
		self.main = MainScreen()

		# Objetos
		self.sol = Planet(radius=100, dist=0, nome='Sol')
		self.terra = Planet(radius=30, dist=120, nome='Terra')
		self.belindo = Planet(radius=50, dist=200, nome='Belindo')

		# Movimento
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def build(self):
		self.main.add_widget(self.sol)
		self.main.add_widget(self.terra)
		self.main.add_widget(self.belindo)
		return self.main


	def move(self, planet1):
		planet1.angle = planet1.angle + 0.01
		planet1.center_x = 640 + planet1.dist * cos(planet1.angle)
		planet1.center_y = 360 + planet1.dist * sin(planet1.angle)
		planet1.nome.center_x = planet1.center_x
		planet1.nome.center_y = planet1.center_y

	def move_horario(self, planet1):
		planet1.angle = planet1.angle - 0.01
		planet1.center_x = 640 + planet1.dist * cos(planet1.angle)
		planet1.center_y = 360 + planet1.dist * sin(planet1.angle)
		planet1.nome.center_x = planet1.center_x
		planet1.nome.center_y = planet1.center_y

	def update(self, dt):
		self.move(self.terra)
		self.move(self.sol)
		self.move_horario(self.belindo)


if __name__ == '__main__':
	GravityApp().run()

