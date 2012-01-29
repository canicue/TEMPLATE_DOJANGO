#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GPL (C) 2010 Iker Perez de Albeniz
# ported in Python from the Php code by HM2K (http://www.hm2k.com/projects/pagerank)
# http://www.ikeralbeniz.net/2010/03/05/contulta-tu-pagerank-de-google-con-python/

import sys
import urllib

from urllib import urlencode
from pprint import pprint

def strToNum(Str, Check, Magic):
        Int32Unit = 4294967296
        length = len(Str);
        for i in range(0, length):
            Check *= Magic;
            if (Check >= Int32Unit):
                Check = (Check - Int32Unit * int(Check / Int32Unit))
                if Check < -2147483648:
                    Check = Check + Int32Unit

            Check += ord(Str[i])
        return Check

def hashURL(string):
        check1 = strToNum(string, 0x1505, 0x21)
        check2 = strToNum(string, 0, 0x1003F)

        check1 >>= 2
        check1 = ((check1 >> 4) & 0x3FFFFC0) | (check1 & 0x3F)
        check1 = ((check1 >> 4) & 0x3FFC00) | (check1 & 0x3FF)
        check1 = ((check1 >> 4) & 0x3C000) | (check1 & 0x3FFF)

        T1 = ((((check1 & 0x3C0) << 4) | (check1 & 0x3C)) << 2) | (check2 & 0xF0F)
        T2 = ((((check1 & 0xFFFFC000) << 4) | (check1 & 0x3C00)) << 0xA) | (check2 & 0xF0F0000)

        return (T1 | T2);

def checkHash(hashnum):
        checkByte = 0;
        flag = 0;

        HashStr = '%s' % hashnum
        length = len(HashStr)

        for i in range(0, length):
            Re = int(HashStr[(length - 1) - i])
            if (1 == (flag % 2)):
                Re += Re
                Re = int((Re / 10) + (Re % 10))

            checkByte += int(Re)
            flag = flag + 1

        checkByte %= 10
        if (0 != checkByte):
            checkByte = 10 - checkByte
            if (1 == (flag % 2)):
                if (1 == (checkByte % 2)):
                    checkByte += 9

                checkByte >>= 1
        return '7%s%s' % (checkByte, HashStr)

def getCh(url):
    return checkHash(hashURL(url))

def main():

    response = "Error: No URL defined.\nUsage: googrng.py <url> [[proxyuser:proxypass@]proxyhost:poxyport]"
    if len(sys.argv) > 1:
        myurl = sys.argv[1]
        url = "http://toolbarqueries.google.es/search?features=Rank&sourceid=navclient-ff&client=navclient-auto-ff&googleip=O;208.117.235.17;97&iqrn=8VdB&querytime=4P&orig=0X557&swwk=-1&ch=%s&q=info:%s" % (getCh(myurl), urllib.quote_plus(myurl))
        if len(sys.argv) > 2:
                proxies = {'http': 'http://' + sys.argv[1]}
                f = urllib.urlopen(url, proxies=proxies)
        else:
                f = urllib.urlopen(url)
        response = f.read()
        f.close()
    print response

if __name__ == "__main__":
    main()
