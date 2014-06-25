import hashlib
import pickle
import imp
import subprocess
import sys

# again, read this from an ini
sites = ['uow', 'atlassian']

# run sites.py for each site
for s in sites:
	if sys.modules.has_key(s) and isinstance(sys.modules[s], types.ModuleType):
		continue
	sys.modules[s] = __import__(s, globals(), locals(), [''])
	sys.modules[s].main()

# checksum calculator for each file to see if it has changed
def checksum(f):
    md5 = hashlib.md5()
    md5.update(open(f).read())
    return md5.hexdigest()

def sendemail(msg):
    process = subprocess.Popen(['mail', '-s', "New Jobs!", "nicolast@gmail.com"],
                               stdin=subprocess.PIPE)
    process.communicate(msg)

	
def whatsdifferent(file1, file2, emailmsg):
	jobsold = pickle.load(open(file1))
	jobsnew = pickle.load(open(file2))
	new = {}

	# this stuff was removed
	for key in jobsold.keys():
		if not key in jobsnew.keys():
			print jobsold[key] + " is gone"
			print key + " is gone"
			# mark removed in db
	
	# this stuff was added
	for key in jobsnew.keys():
		if not key in jobsold.keys():
			print jobsnew[key] + " is new"
			print key + " is new"
			# add to db
			new[key] = jobsnew[key]

	if (len(new) > 0):
		if not emailmsg:
			emailmsg = "New jobs:\n\n"
		for job in new:
			emailmsg += "%s - %s\n" % (job, new[job])
		# then write the jobsnew.pickle to the jobsold.pickle filename
		pickle.dump(jobsnew, open(file1, "wb"))

	return emailmsg
		

# main
def main():
	emailmsg = ""
	for s in sites:
		file1 = "tmp/" + s + ".pickle"
		file2 = "tmp/" + s + ".pickle.new"
		if checksum(file1) != checksum(file2):
			# find out why they're different
			emailmsg = whatsdifferent(file1, file2, emailmsg) 

	if (emailmsg):
		sendemail(emailmsg)
	else:
		sendemail("no new jobs")

if __name__ == "__main__":
    main()
