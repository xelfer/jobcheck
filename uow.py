import urllib
import re
import pickle


def newjobsearch():
	joblist = {}
	link = "http://uow.employment.com.au/"
	website = urllib.urlopen(link)
	for line in website: 
		if line.find('/jobs/') != -1:
			result = re.search('"(.*)">(.*)<', line)
			joblist["http://uow.employment.com.au" + result.group(1)] = result.group(2)
	return joblist

def test():
	print "hello"

def main():
	j = newjobsearch()
	pickle.dump(j, open("tmp/uow.pickle.new", "wb"))

if __name__ == "__main__":
    main()

