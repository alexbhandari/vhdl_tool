class Entity:
	name = ""
	component = ""
	inputs = []
	outputs = []
	def __init__(self, name, component, inputs, outputs):
		self.name = name
		self.component = component
		self.inputs = inputs
		self.outputs = outputs
	def __str__(self):
		str = self.name + " : " + self.component + " port map( " + self.map(self.inputs) + ", " + self.map(self.outputs) + " )"
		return str

	def map(self, pins):
		first = True
		str = ""
		for key in pins.keys():
			if(not first):
				str += ","
			str += key + " => " + pins[key]
			first = False
		return str
