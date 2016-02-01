#!/usr/bin/env python

import synapseclient
import os,sys,string,shutil,getopt
syn = synapseclient.Synapse()
syn.login('venkatmi')



executed_urls=[]
used=[]
options, remainder = getopt.getopt(sys.argv[1:],'', ['dir=','parent=','description=','urls=','used='])
for opt, arg in options:
    if opt == '--dir': file_dir=arg
    elif opt == '--parent': parent_syn=arg
    elif opt == '--description': description=arg
    elif opt == '--urls': executed_urls.append(arg) ### options are: all, junction, exon, reference
    elif opt == '--used': used.append(arg)

file = synapseclient.File(file_dir, parent=parent_syn, description=description)
file = syn.store(file,executed=executed_urls,used=used)
