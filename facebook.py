users=[]
posts=[]


class Post(object):
	def __init__(self,text,voice):
		self.text=text
		self.voice=voice
	def post(self, text):
		posts.append(self.text)




class User(object):
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]

	def add_friend(self,email):
		print(self.name+ " has added "+email+" as a friend")
		self.friends_list.append(email)

	def remove_friend(self,email):
		print(self.name+" has remove "+ email+" as a friend")
		self.friends_list.remove(email)

	def post(self,text,voice):
		self.text=text
		self.voice=voice
		post1=Post(text,voice)
		posts.append(text)


		

		print(self.name+" has posted "+text )
	def get_userInfo(self):
		print("name: " + self.name+ "email: "+self.email+ " password: "+self.password+ " friends: "+str(self.friends_list)+"posts: "+str(posts))  


test =Post("s","h")

User1 = User( "loai " , "Loai17@meet.mit.edu" , "123" )
User2 = User( "meera " , "meera.paraskiva@gmail.com" , "mmm" )
User1.add_friend("meera")
User1.post("how r u???",'meow')
User1.get_userInfo()
User2.get_userInfo()
User1.remove_friend("meera")
	
class Comment(Post):
	def __init__(self,text,name_):
		self.text=text	
		self.voice=voice

	
