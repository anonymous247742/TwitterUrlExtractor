#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re, sys, getopt, os
from datetime import datetime
import urllib2


def main(argv):
    d = datetime.now()
    date = str(d.year) + '' + str(d.month) + '' + str(d.day) + '' + str(d.hour) + '' + str(d.minute) + '' + str(d.second)
    output = "./twitterUrlList_"+date+".txt"
    input_f = None
    url = None
    data = None

    try:
        opts, args = getopt.getopt(argv, "hf:u:o:", ["input-file=", "input-url=", "output-file=", "help"])
    except getopt.GetoptError:
        print 'Use --help for help'
        sys.exit(2)

    for opt, arg in opts:
        print opt
        if opt in ("-h", "--help"):
            print 'Usage: %s <options> \n' % (os.path.basename(__file__))
            print '     -h, --help              this help'
            print '     -f, --input-file FILE   Use file for extract urls twitter'
            print '     -u, --input-url URL     Use url for extract urls twitter'
            print '     -o, --output-file FILE  Output file for urls twitter'
            sys.exit()
        elif opt in ("-f", "--input-file"):
            input_f = arg
        elif opt in ("-u", "--input-url"):
            url = arg
        elif opt in ("-o", "--output-file"):
            output = arg

    if not input_f and not url:
        print 'Use --help for help'
        sys.exit(2)

    if url:
        response = urllib2.urlopen(url)
        data = response.read()
    elif input_f:
        textfile = open(input_f, 'r')
        data = textfile.read()
        textfile.close()

    URL_REGEX = r"""(?i)\b((?:https:\/\/)?(?:http:\/\/)?(?:www\.)?twitter\.com\/[^\s]+)\b/?(?!@)"""
    urls = re.findall(URL_REGEX, data)

    o = open(output, 'w')
    for tw_url in urls:
        o.write(tw_url+'\n')
    o.close()

    print "finished extraction, result in %s" % (output)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.stdout.write('\nQuit by keyboard interrupt sequence!')
