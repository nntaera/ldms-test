#!/usr/bin/python3

import os
import sys
import json

from ldmsdutils import *

ldms.init(1024*1024*1024)

def good_dirs(dirs):
    return [ d for d in dirs if d.flags[0] == 'C' ]

def ready_sets(prdcr_set_status_resp):
    resp = prdcr_set_status_resp
    return [ s for s in resp['sets'] if s['state'] == 'READY' ]

samp_list = LDMSDSampler.allDaemons()
l1_list = LDMSD_L1.allDaemons()
l2_list = LDMSD_L2.allDaemons()
l3_list = LDMSD_L3.allDaemons()
aggs = l1_list + l2_list + l3_list
daemons = { a.name: a for a in samp_list + l1_list + l2_list + l3_list }

if True:
    samp = samp_list[0]
    samp_dirs = samp.dir()
    samp_good = good_dirs(samp_dirs)
    print("samp_good:", len(samp_good))
    print("samp_dirs:", len(samp_dirs))
    if False:
        samp.lookup()
        samp.update()

if True:
    l1 = l1_list[0]
    l1_dirs = l1.dir()
    l1_good = good_dirs(l1_dirs)
    print("l1_good:", len(l1_good))
    print("l1_dirs:", len(l1_dirs))
    if False:
        l1.lookup()
        l1.update()

if False:
    l2 = l2_list[0]
    l2_dirs = l2.dir()
    l2_good = good_dirs(l2_dirs)
    print("l2_good:", len(l2_good))
    print("l2_dirs:", len(l2_dirs))
    if True:
        l2.lookup()
        l2.update()
