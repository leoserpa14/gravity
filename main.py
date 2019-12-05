from kivy.config import Config
Config.read('config.ini')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
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
	def __init__(self, radius, mass, x, y, vel_lin, **kwargs):
		super().__init__(**kwargs)
		# Parametros que eu criei
		self.radius = radius
		self.mass = mass # Provavelmente não será necessário
		self.vel_lin = vel_lin

		# Parametros de Widget
		self.size = self.radius, self.radius
		self.center_x = x
		self.center_y = y


# Provavelmente não vou precisar
G = 6.71*(pow(10, -11)) # N * m² / kg²


class GravityApp(App):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# Tela principal
		self.main = MainScreen()

		# Objetos
		self.sol = Planet(radius=200.510, x=Window.width/2, y=Window.height/2, vel=[0, 0])
		self.terra = Planet(radius=63.71, x=Window.width*2/3, y=Window.height*3/4, vel=[0, 0])

		Clock.schedule_interval(self.update, 1.0 / 60.0)

	def build(self):

		self.main.add_widget(self.sol)
		self.main.add_widget(self.terra)
		return self.main

	def force(self, planet1, planet2):
		pos1 = [planet1.center_x, planet1.center_y]
		pos2 = [planet2.center_x, planet2.center_y]
		v = [pos2[0] - pos1[0], pos2[1] - pos1[1]]
		print(v)

		dist = sqrt(pow(v[0], 2) + pow(v[1], 2))
		print(dist)

		# Força ocorrendo no planeta 1 pelos efeitos do planeta 2 tal que  F = G * M * m / d²
		f12 = G * planet1.mass * planet2.mass / (pow(dist, 2))
		print(f12)

		# TODO: Estudar operação com vetores em numpy, talvez
		return f12


	def move(self, planet1, planet2):
		# Mover o planeta 1 pela força realizada pelo planeta 2
		f = self.force(planet1, planet2)
		dist = sqrt(pow(planet1.center_x - planet2.center_x, 2) + pow(planet1.center_y - planet2.center_y, 2))

		fx = f * (planet2.center_y - planet1.center_y) / dist
		fy = f * (planet2.center_x - planet1.center_x) / dist

		ax = fx / planet1.mass
		ay = fy / planet1.mass

		planet1.vel[0] = planet1.vel[0] + ax * 1
		planet2.vel[1] = planet2.vel[1] + ay * 1

		planet1.center_x = planet1.center_x + planet1.vel[0] * 1 + ax * (1) * (1) / 2
		planet1.center_y = planet1.center_y + planet1.vel[1] * 1 + ay * (1) * (1) / 2


		return

	def update(self, dt):
		self.move(self.terra, self.sol)


if __name__ == '__main__':
	GravityApp().run()

