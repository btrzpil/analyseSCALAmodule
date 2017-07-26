class Volume:
	def __init__(self,name):
		self.name=name




class Cylinder(Volume):
	def __init__(self,name,parameters):
		Volume.__init__(self, name)
		self.setParameters(parameters)
	def setParameters(self,parameters):
		print(self.name)

		x =parameters[0]
		y =parameters[1]
		z1=parameters[2]
		z2=parameters[3]
		r =parameters[4]

	
		self.x=x
		self.y=y
		self.r=r
		if z1>z2:
			self.zmin=z2
			self.zmax=z1
		else:
			self.zmin=z1
			self.zmax=z2

	def checkPointVolume(self,x,y,z):

		if (((x-self.x)**2+(y-self.y)**2<=(self.r)**2)and(self.zmin<=z<=self.zmax)):
			return True
		else:
			return False


class Cuboid(Volume):

	def __init__(self,name,parameters):
		Volume.__init__(self, name)
		self.setParameters(parameters)
	def setParameters(self,parameters):
		print(self.name)

		x1=parameters[0]
		x2=parameters[1]
		y1=parameters[2]
		y2=parameters[3]
		z1=parameters[4]
		z2=parameters[5]

		if x1>x2:
			self.xmin=x2
			self.xmax=x1
		else:
			self.xmin=x1
			self.xmax=x2

		if y1>y2:
			self.ymin=y2
			self.ymax=y1
		else:
			self.ymin=y1
			self.ymax=y2

		if z1>z2:
			self.zmin=z2
			self.zmax=z1
		else:
			self.zmin=z1
			self.zmax=z2

	def checkPointVolume(self,x,y,z):

		if (self.xmin<=x<=self.xmax)and(self.ymin<=y<=self.ymax)and(self.zmin<=z<=self.zmax):
			return True
		else:
			return False

