#!/usr/bin/env python
#-*- coding:utf-8 -*-

import cProfile, pstats
import sys
import stacked.GameMain

if "-p" in sys.argv:
    cProfile.run('stacked.GameMain.run()', '/tmp/profile')
    p = pstats.Stats('/tmp/profile')
    p.strip_dirs()
    p.sort_stats('time')
    p.print_stats(25)
else:
    stacked.GameMain.run()

