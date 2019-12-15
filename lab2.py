

list1=[1,2,3,4]
list2=[2,4,6,8]
list3=[]
def lists(list1,list2):

	for i in list1:
		if i in list2:
			list3.append(i)
	return list3

print (lists(list1,list2))

def listen()