import urllib
import re


def newjobsearch():
	joblist = {}
	link = "http://uow.employment.com.au/"
	website = urllib.urlopen(link)
	for line in website: 
		if line.find('/jobs/') != -1:
			result = re.search('"(.*)">(.*)<', line)
			joblist["http://uow.employment.com.au" + result.group(1)] = result.group(2)
	return joblist

def printjoblist(joblist):
	for key in joblist:
		print joblist[key] + " - " + key

joblist = newjobsearch()
printjoblist(joblist)
