import hashlib
import pickle
import imp
import subprocess

# again, read this from an ini
sites = ['uow']

# run sites.py for each site
import uow
uow.main()
import atlassian
atlassian.main()

# checksum calculator for each file to see if it has changed
def checksum(f):
    md5 = hashlib.md5()
    md5.update(open(f).read())
    return md5.hexdigest()

def sendemail(msg):
    process = subprocess.Popen(['mail', '-s', "New Jobs!", "nick@triso.me"],
                               stdin=subprocess.PIPE)
    process.communicate(msg)

	
def whatsdifferent(file1, file2):
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
		emailmsg = "New jobs:\n"
		for job in new:
			emailmsg += "%s - %s\n" % (job, new[job])
		sendemail(emailmsg)
		

# main
def main():
	for s in sites:
		file1 = "tmp/" + s + ".pickle"
		file2 = "tmp/" + s + ".pickle.new"
		if checksum(file1) != checksum(file2):
			# find out why they're different
			whatsdifferent(file1, file2) 

if __name__ == "__main__":
    main()
