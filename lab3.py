
class Animal(object):
	def __init__(self,sound,name,age,fav_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.fav_color=fav_color

	def eat(self,food):
		print("yummy"+self.name+"is eating"+food)
	def description(self):
		print(self.name+"is"+self.age+"years old and loves the color"+self.fav_color)
	def make_sound(self,signature):
		for i in range(3):
			print(self.sound+"his signature"+signature)
		rep = input("how many times you wish to repeat sound?")
		for m in range (rep):
			print(self.sound)
class person(object):
	def __init__(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def eat2(self,breakfast):
		print(self.name+"is eating his favorite "+breakfast)
	def sport(self,sport):
		print(self.name+"is plaing his favorite "+sport)
	def person_det(self):
		print("Name: " + self.name + ".\n" 
			  + "Age: " + str(self.age) + ".\n"
			  + "City: " + self.city + ".\n"
			  + "Gender: "+ self.gender+".\n"
			  + "============================\n" )

class song(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics
	def sing_me_a_song(self,song):	
		self.song=song
	def print_song(self): 
		for x in self.lyrics:
			print(x)
class bird(object):
	def __init__(self,name,color, speed):
		self.name=name
		self.color = color 
		self.speed = speed 
	def get_speed(self):
		return self.speed
	def race(self,b):
		if(self.speed == b.speed):
			print("they have the same speed so both will finish in the same time.")
		elif (self.speed > b.speed) :
			print("bird " + self.name + " will win the race")
		else:
			print("bird " + b.name + " will win the race")
	def bird_sing(self,s): 
		print ("bird " + self.name + " will sing this song:" + s.lyrics)

	
#intializing from person class 	
person1=person("ameer",21,"bethlehem","male")
# initial from song
flower_song = song(["roses are red,","violets are blue,","i wrote this poem for u."])


person1.person_det() 
flower_song.print_song()

bird1 = bird("birdA" , "Yellow", 213)
bird2 = bird("birdB" , "green" , 567)


bird1.race(bird2)
