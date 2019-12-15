users=[]
posts=[]


class post_class(object):
	def __init__(self,text):
		self.text=text
		self.likes = 0 
		self.comments = [] 
		#1self.messages=[]
		#add to global part X 
		posts.append(self)
	#overWrite
	def __str__(self):
		return ("\tpost Text: " + self.text +".\n\tnumber of like|s: " + str(self.likes)+ ".\n\tcomment|s is|are:" + str(self.comments))#+ "\n\tmessage|s is|are:" + str(self.messages)) 
#	def post(self, text):
		#posts.append(self.text)

		#print(messages:"hi how r u?")


class User(object):
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts_list =[]
		users.append(self) #part X 
		
	def add_friend(self,email):
		print("\n"+self.name+ " has added "+email+" as a friend")
		self.friends_list.append(email)

	def remove_friend(self,email):
		print("\n"+self.name+" has removed "+ email+" from friend list")
		self.friends_list.remove(email)

	def post(self,text):
		#self.text=text
		#self.voice=voice
		p = post_class(text)
		self.posts_list.append(p)
		#post1=Post(text,voice)
		#posts.append(text)
		print("\n"+self.name+" has posted: "+text )


	def get_userInfo(self):
		print("\n___________________________" 
			+"\nName: " + self.name
			+ ".\nEmail: "+self.email
			+ ".\nPassword: "+self.password
			+ ".\nFriends: "+ str(self.friends_list) 
			+ ".\nPosts: " )
		if (len(self.posts_list) == 0):#no posts for this user
			print("no posts are made by this user")
		else: 
			for n in self.posts_list: # n is a variable and here the type of n is post_class
				print(str(n))	
		print("\n___________________________" )


#test =Post("s","h")


u1 = User( "loai " , "Loai17@meet.mit.edu" , "myhiddenpassword123" )
u2 = User( "meera " , "meera.paraskiva@gmail.com" , "mmsajdhm" )
u3 = User( "ellie " , "ellie@meet.mit.edu" , "myhiddenpassword1234567" )
u4 = User( "ameer " , "ameer@meet.mit.edu" , "myhiddenpassword" )


u1.add_friend(u2.email)
u1.add_friend(u3.email)
u2.add_friend(u4.email)
u2.add_friend(u3.email)
u2.add_friend(u1.email)



u1.post("how r u???")

u1.get_userInfo()
u2.get_userInfo()
u3.get_userInfo()
u4.get_userInfo()

u2.remove_friend(u1.email)
u2.get_userInfo()




while(1==1): 
    flag = 0 
    yes = 1
    print("\n-------------------------------\n"
		+"Press: \n"
		+"1. log in."
		+ "\n2. to sign up."
		+ "\n3. to exit."
		+"\n-------------------------------\n")
    choice= input("please select your option : ")
	
    #===================================================================
    if (int(choice) == 1):
        email  = input("please enter you email: ")
        for n in users: 
            if(n.email == email):
                password1 = input("please enter your password: ")
                flag = 1 
                if (n.password == password1 ):
                    while (1==1):
                        print("\n-------------\n"
							+"please select the choice you want to do: \n"
							+ "1. add friend.\n"
							+ "2. Delete a Friend.\n"
							+ "3. make a post.\n"
							+ "4. log out."
							+"\n-------------")
                        choice1 = input()
						
                        #============================================
                        if (int(choice1) == 1):  
                            add_flag = 0
                            email1 = input("please enter your friend's email: ")
                            for x in users:
                                if(x.email == email1):
                                    add_flag = 1
                                    break
                                    


                            if(add_flag == 1):
                                if(email1 in n.friends_list):
                                    print("\nthis user is already in your Friend list.")
                                else: 
                                    n.add_friend(email1)
                            else: 
                                print("\nthis user is not registered in our system.")

                        #=======================================================


                        elif(int(choice1) == 2):
                            email1 = input("please enter your friend's email: ")
                            if(email1 in n.friends_list):
                                n.remove_friend(email1)
                            else: 
                                print("\nthis user is not in "+ n.name + " friend list.")

                        #=======================================================
                                
                        elif(int(choice1)==3):
                            text1 = input("please enter your post text: ")
                            n.post(text1)

                        #====================================================== 

                        elif (int(choice1) == 4): #log out 
                            flag = 0 
                            yes = 0
                            print("\nlogged out! have a good day.")
                            break
                        #=======================================================

                        else: 
                            print("\n**you entered unsupported letter or number... try again.")

                else:
                    print("\nyour password is wrong, please try again.")
                    flag = 0 
                    yes = 0
            else:
                yes = 1
        if (flag == 0 and yes==1): 
            print("\nThis email does not exist please sign up.")
	
	                                    
        #===========================================================
    elif (int(choice) == 2 ):  #sign up 
        flag1 = 0
        name2 = input("please enter your name:")
        email2 = input("please enter your email: ")
        password2 = input("please enter your password : ")
        for y in users: 
            if(y.email == email2):
                flag1 = 1 
                break
        if (flag1 == 0):
            users.append(User(name2,email2,password2))
            print("\ndone! Welcome to our world :)\n")
        else: 
            print("\nthis email is already exisits and used with different user please try again.\n")

    #========================================================
    elif (int(choice) == 3 ): 
        print("\nthank you for using Meera Products. Have a good Day! :)")
        exit()
	#========================================================
    else: 
        print("\n**you entered unsupported letter or number... try again.")
	





















'''
class Comment(Post):
	def __init__(self,text,name_):
		self.text=text	
		self.voice=voice
'''
	
