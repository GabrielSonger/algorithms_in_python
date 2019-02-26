
class SingletonStrict:
	"""Restrict to only one object by modifying __new__"""
	class __SingletonStrict:
		def __init__(self):
			self.val = None

		def __str__(self):
			return self.val

	instance = None

	# __new__ always a class method
	def __new__(cls):
		if not cls.instance:
			cls.instance = cls.__SingletonStrict()

		return cls.instance

	def __getattr__(self, name):
		return self.getattr(self.instance, name)

	def __setattr__(self, name):
		return self.setattr(self.instance, name)


class Borg:
	_shared_state = {}
	def __init__(self):
		self.__dict__ = self._shared_state


class SingletonBorg(Borg):
	""" Store the same set of data, allow multiple instances"""
	def __init__(self, arg):
		super().__init__()
		self.val = arg

	def __str__(self):
		return self.val


#Test
strict_x = SingletonStrict()
strict_x.val = 'cat'
print (strict_x)

strict_y = SingletonStrict()
strict_y.val = 'dog'
print (strict_y)

strict_z = SingletonStrict()
strict_z.val = 'zebra'
print (strict_z)
print (strict_x)
print (strict_y)


borg_x = SingletonBorg('x')
print (borg_x)
borg_y = SingletonBorg('y')
print (borg_y)
borg_z = SingletonBorg('z')
print (borg_z)
print (borg_x)
print (borg_y)



