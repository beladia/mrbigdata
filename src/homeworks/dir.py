import os
for i in range(1,8):
	os.mkdir("group" + str(i))
	t = "echo \'This dir is for group" + str(i) + "\' > " + "group" + str(i) + "/README"
	os.system(t)
	for j in range(1,6):
		c = "group" + str(i)
		d = "week" + str(j)
		s = c + '/' + d
		if not os.path.exists(s):
			os.mkdir("group" + str(i) + "/week" + str(j))
			os.mkdir("group" + str(i) + "/week" + str(j) + "/submissions" )
			t = "echo \'This dir is for submitting homework for group" + str(i) + " for week " + str(j) + "\' >> " + s + "/submissions/README"
			os.system(t)

