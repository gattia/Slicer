# -*- coding: utf-8 -*-
"""
Created on Thurs Oct 1 11:00:00 2015

@author: Gatti
"""
#volumesLogic = slicer.modules.volumes.logic()

import numpy 
import slicer

images = slicer.util.getNodes('*Result')
toProcess = images.keys ()

for x in range (0, len(toProcess)):
    seg = array(toProcess[x])
        
    MA = numpy.where(seg == 6145)
    LA = numpy.where(seg == 8193)
    MM = numpy.where(seg == 2049)
    LM = numpy.where(seg == 4097)
    MPat = numpy.where(seg == 14465)
    LPat = numpy.where(seg == 16513)
    MPost = numpy.where(seg == 10241)
    LPost = numpy.where(seg == 12289)
    
    whole = numpy.where(seg>0)
    seg[whole] = 0
    
    seg[MPost] = 1
    seg[LPost] = 2
    seg[MM] = 3
    seg[LM] = 4
    seg[MA] = 7
    seg[LA] = 9
    seg[MPat] = 16
    seg[LPat] = 68
    
    n = getNode(toProcess[x])
    n.GetImageData().GetPointData().Modified()
    n.Modified()
