import math

decimal_hex_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

class Colour:
	def __init__(self, red=0, green=0, blue=0):
		self.red = red
		self.green = green
		self.blue = blue
		self.hex = self.rgb_to_hex()
	def rgb_to_hex(self):
		self.red_hex = decimal_hex_map[self.red // 16] + decimal_hex_map[self.red % 16]
		self.green_hex = decimal_hex_map[self.green // 16] + decimal_hex_map[self.green % 16]
		self.blue_hex = decimal_hex_map[self.blue // 16] + decimal_hex_map[self.blue % 16]
		return "#" + self.red_hex + self.green_hex + self.blue_hex