Userdict = {}
username_stream = ["a", "a", "a1", "a1", "b", "b", "b", "a21", "a21", "a12"]
assigned = []


for users in username_stream:
	# print(users)
	if users in Userdict:
		Userdict[users]+=1
		# print(Userdict[users])
		string  = users + str(Userdict[users]-1)
		# print(string) 
		assigned.append(string)
		Userdict[string] = 1
	else:
		Userdict[users]=1
		assigned.append(users)

print(Userdict)
print(assigned)