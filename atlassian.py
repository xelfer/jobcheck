import urllib
import re
import pickle

def addjob(joblist, url, title):
	joblist[url] = title
	return joblist

def newjobsearch():
	jobs = []
	joburls = []
	alljobs = {}
	link = "https://www.atlassian.com/company/careers#jobSection"
	website = urllib.urlopen(link)
	for line in website:
		if line.find('location sydney') != -1:
			jobs.append(line.rstrip('\n'))

	for j in jobs:
		halfj = re.sub(r'<li class="location sydney" data-joblink="','', j)
		url = "http://www.atlassian.com" + re.sub(r'" data-locationname="Sydney">', '', halfj)
		joburls.append(url)

	for u in joburls:
		w = urllib.urlopen(u)
		for line in w:
			if line.find("<td colspan=2><hr width='100%' size='1' color='silver'></td></tr><tr><td colspan=2><h1>") != -1:
				jobtitle = re.sub(r"<td colspan=2><hr width='100%' size='1' color='silver'></td></tr><tr><td colspan=2><h1>", '', line).rstrip('\n')
				jobtitle = re.sub(r"</h1></td>", '', jobtitle)
				alljobs = addjob(alljobs, u, jobtitle)
	return alljobs

def main():
	j = newjobsearch()
	pickle.dump(j, open("tmp/atlassian.pickle.new", "wb"))

if __name__ == "__main__":
    main()
