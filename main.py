from kivy.config import Config
Config.read('config.ini')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.core.window import Window
from math import cos, sin, pi
import random

Builder.load_file('gravity.kv')
random.seed(-6)


class MainScreen(FloatLayout):
	pass


class Planet(Widget):

	def __init__(self, radius, dist, nome, parent_planet, **kwargs):
		super().__init__(**kwargs)
		# Parametros que eu criei
		self.dist = dist
		self.angle = 0 # starts at 0
		self.nome = Label(text='', color=(0 / 255, 0 / 255, 0 / 255, 1))
		self.add_widget(self.nome)
		self.speed = random.uniform(-0.05, 0.05)
		self.parent_planet = parent_planet

		# Parametros de Widget
		self.size = radius, radius
		if self.parent_planet is None:
			self.center_x = Window.width/2 + self.dist * cos(self.angle)
			self.center_y = Window.height/2 + self.dist * sin(self.angle)
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
		self.mercurio = Planet(radius=30, dist=90, nome='Mercurio', parent_planet=None)
		self.venus = Planet(radius=45, dist=130, nome='Venus', parent_planet=None)
		self.terra = Planet(radius=50, dist=200, nome='Terra', parent_planet=None)
		self.lua = Planet(radius=15, dist=45, nome='Lua', parent_planet=self.terra)
		self.marte = Planet(radius=35, dist=260, nome='Marte', parent_planet=None)
		self.jupiter = Planet(radius=80, dist=340, nome='Jupiter', parent_planet=None)
		self.saturno = Planet(radius=60, dist=420, nome='Saturno', parent_planet=None)


		# Movimento
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def build(self):
		self.main.add_widget(self.sol)
		self.main.add_widget(self.lua)
		self.main.add_widget(self.terra)
		self.main.add_widget(self.mercurio)
		self.main.add_widget(self.venus)
		self.main.add_widget(self.marte)
		self.main.add_widget(self.jupiter)
		self.main.add_widget(self.saturno)
		self.Anel = []
		for i in range(50):
			lua = Planet(radius=5, dist=50, nome='', parent_planet=self.saturno)
			self.Anel.append(lua)
			self.main.add_widget(self.Anel[i])
		return self.main


	def orbit(self, planet1):
		planet1.angle = planet1.angle + planet1.speed
		if planet1.parent_planet is None:
			planet1.center_x = Window.width/2 + planet1.dist * cos(planet1.angle)
			planet1.center_y = Window.height/2 + planet1.dist * sin(planet1.angle)
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
		self.orbit(self.mercurio)
		self.orbit(self.venus)
		self.orbit(self.marte)
		self.orbit(self.jupiter)
		self.orbit(self.saturno)
		for i in range(50):
			self.orbit(self.Anel[i])
		return



if __name__ == '__main__':
	MainApp().run()