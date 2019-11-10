class User(object):
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=friends_list[email]
		self.posts=[]

	def add_friend(self,email):
		print(self.name+ "has added"+email+"as a friend")
		self.friend_list.append(email)
	def remove_friend(self,email):
		print(self.name+"has remove"+ email+"as a friend")
		self.friend_list.remove(email)
	def post(self,text):
		self.text=text
		print(self.name+" has posted"+text )
	def get_userInfo(self)





