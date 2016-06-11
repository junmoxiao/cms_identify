#!/usr/bin/env python
#coding=utf-8
import glob,urllib, urllib2, re, sys, requests

def scan():
    host = sys.argv[1]
    header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    cms_list = glob.glob('./cms/*')
    amount = len(cms_list)
    count = 0
    for cms in cms_list:
        for line in open(cms, 'r'):
            line = line.strip().split('------')
            if len(line) != 3:
                continue            
            try:
                r = requests.get(host + line[0])
                if r.status_code != 200:
                    continue
            except:
                continue
            data = r.text
            if re.compile(r'(?i)'+line[1]).search(data):
                    print 'Identified: '+host +' is ' + line[2]
                    sys.exit(0)
        count += 1
        print 'complete %d/%d' % (count, amount)
    print 'can\'t identify it......'

if __name__ == '__main__':
    if len(sys.argv) != 2 or 'http://' not in sys.argv[1]:
        print '''\
        Example: python cmsIdentify.py http://www.baidu.com\
        '''
        sys.exit(1)
    scan()
