class Post(object):
	def __init__(self,text):
		self.text=text
class User(object):
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]

	def add_friend(self,email):
		print(self.name+ " has added "+email+" as a friend")
		self.friends_list.append(email)
	def remove_friend(self,email):
		print(self.name+" has remove"+ email+"as a friend")
		self.friends_list.remove(email)
	def post(self,text):
		self.text=text
		post1=Post(text)
		print(self.name+" has posted "+text )
	def get_userInfo(self):
		print("name: " + self.name+ "email: "+self.email+ "password: "+self.password+ "friend: "+self.password+"friends: "+str(self.friends_list)+"posts: "+str(self.posts))  
User1 = User( "loai" , "Loai17@meet.mit.edu" , "123" )
User2 = User( "meera" , "meera.paraskiva@gmail.com" , "mmm" )
User1.add_friend("meera")
User1.post("how r u???")
User1.get_userInfo()
User2.get_userInfo()
User1.remove_friend("meera")

