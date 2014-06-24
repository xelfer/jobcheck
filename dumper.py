# dump each pickle contents

import pickle

# maybe read this from an ini file
sites = ['atlassian', 'uow']

# read a single pickle into a joblist dictionary
def readfile(filename):
	joblist = pickle.load(open("tmp/"+filename+".pickle"))
	return joblist



# main program
for s in range(len(sites)):
	joblist = readfile(sites[s])
	for url in joblist:
		print joblist[url] + " - " + url

