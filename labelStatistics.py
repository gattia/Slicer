import numpy 
import slicer 

segmentations = slicer.util.getNodes('')
T2maps = slicer.util.getNodes('')

grayNode = getNode ('3655*resampled')
labelNode = getNode ('3655*Result')

resampledGrayNode = volumesLogic.ResampleVolumeToReferenceVolume(grayNode, labelNode)
resampledLabelNode = volumesLogic.ResampleVolumeToReferenceVolume(labelNode, grayNode)

label = array('3655*Result_1')
gray = array('3655*resampled')
zeros = numpy.where(gray == 0)

label[zeros] = 10

n = getNode('3655_Result_1')
n.GetImageData().GetPointData().Modified()
n.Modified()

updateLabelNode = getNode ('3655_Result_1')

LabelStatisticsLogic(grayNode, updateLabelNode).saveStats('test_3655')








#LabelStatisticsLogic(grayNode, labelNode)

#LabelStatisticsWidget.onSave

#fileName = ('') #name based on loop 

#statsAsCSC (self)

#saveStats (self, fileName)

#LabelStatisticsWidget
