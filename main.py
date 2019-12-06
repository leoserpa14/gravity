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
random.seed(-1)


class MainScreen(FloatLayout):
	pass


class Planet(Widget):

	def __init__(self, radius, dist, nome, parent_planet, **kwargs):
		super().__init__(**kwargs)
		# Parametros que eu criei
		self.dist = dist
		self.angle = 0 # starts at 0
		self.nome = Label(text=nome, color=(0 / 255, 0 / 255, 0 / 255, 1))
		self.add_widget(self.nome)
		self.speed = random.uniform(-0.05, 0.05)
		self.parent_planet = parent_planet

		# Parametros de Widget
		self.size = radius, radius
		if self.parent_planet is None:
			self.center_x = 640 + self.dist * cos(self.angle)
			self.center_y = 360 + self.dist * sin(self.angle)
		else:
			self.center_x = self.parent_planet.center_x + self.dist * cos(self.angle)
			self.center_y = self.parent_planet.center_y + self.dist * sin(self.angle)
		self.text = nome


class MainApp(App):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# Tela principal
		self.main = MainScreen()

		# Objetos
		self.sol = Planet(radius=100, dist=0, nome='Sol', parent_planet=None)
		self.terra = Planet(radius=50, dist=200, nome='Terra', parent_planet=self.sol)
		self.lua = Planet(radius=30, dist=120, nome='Lua', parent_planet=self.terra)

		# Movimento
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def build(self):
		self.main.add_widget(self.sol)
		self.main.add_widget(self.lua)
		self.main.add_widget(self.terra)
		return self.main


	def orbit(self, planet1):
		planet1.angle = planet1.angle + planet1.speed
		if planet1.parent_planet is None:
			planet1.center_x = 640 + planet1.dist * cos(planet1.angle)
			planet1.center_y = 360 + planet1.dist * sin(planet1.angle)
		else:
			planet1.center_x = planet1.parent_planet.center_x + planet1.dist * cos(planet1.angle)
			planet1.center_y = planet1.parent_planet.center_y + planet1.dist * sin(planet1.angle)
		planet1.nome.center_x = planet1.center_x
		planet1.nome.center_y = planet1.center_y
		return


	def update(self, dt):
		self.orbit(self.sol)
		self.orbit(self.terra)
		self.orbit(self.lua)


if __name__ == '__main__':
	MainApp().run()

