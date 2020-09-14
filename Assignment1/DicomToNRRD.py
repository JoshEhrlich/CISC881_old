dicomDataDir = "/Users/JoshEhrlich/OneDrive\ -\ Queen\'s\ University/School/University/MSc/CISC881/Assignment1/DICOMFIleDownloadDirectory/PROSTATEx"  # input folder with DICOM files
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs
from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
    
