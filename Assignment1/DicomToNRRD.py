import sys
import os
import DICOM
import DICOMScalarVolumePlugin

dicomDataDir = "/Users/JoshEhrlich/OneDrive - Queen's University/School/University/MSc/CISC881/Assignment1/DICOMFIleDownloadDirectory/PROSTATEx"  # input folder with DICOM files
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs
from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    print("Test")
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
    print("Test")
    

DW=DICOM.DICOMWidget()
DSVPC=DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()
			
DW.detailsPopup.dicomApp.onImportDirectory(dicomDataDir)

for patient in slicer.dicomDatabase.patients():
  for study in slicer.dicomDatabase.studiesForPatient(patient):
    for series in slicer.dicomDatabase.seriesForStudy(study):
      files = slicer.dicomDatabase.filesForSeries(series)
      if slicer.dicomDatabase.descriptionForSeries(series) == ("t2_tse_tra") or ("ADC" in slicer.dicomDatabase.descriptionForSeries(series)) or ("BVAL" in slicer.dicomDatabase.descriptionForSeries(series)):
        volumeFile=DSVPC.load(DSVPC.examine([files])[0])
        slicer.util.saveNode(volumeFile,"/Users/JoshEhrlich/OneDrive - Queen's University/School/University/MSc/CISC881/Assignment1/DICOMFileExport/"+patient+"/"+slicer.dicomDatabase.descriptionForSeries(series)+".nrrd")
