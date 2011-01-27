import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Configuration.JetCorrectionServices_cff import *


#
# SINGLE LEVEL CORRECTION SERVICES
#

# L1 (offset) Correction Services
ak7CaloL1Offset = ak5CaloL1Offset.clone()
kt4CaloL1Offset = ak5CaloL1Offset.clone()
kt6CaloL1Offset = ak5CaloL1Offset.clone()
ic5CaloL1Offset = ak5CaloL1Offset.clone()

ak7PFL1Offset   = ak5PFL1Offset.clone()
kt4PFL1Offset   = ak5PFL1Offset.clone()
kt6PFL1Offset   = ak5PFL1Offset.clone()
ic5PFL1Offset   = ak5PFL1Offset.clone()

ak7JPTL1Offset  = ak5CaloL1Offset.clone()

# SPECIAL L1JPTOffset
ak7L1JPTOffset = ak5L1JPTOffset.clone()

# L2 (relative eta-conformity) Correction Services
ak7CaloL2Relative = ak5CaloL2Relative.clone( algorithm = 'AK7Calo' )
kt4CaloL2Relative = ak5CaloL2Relative.clone( algorithm = 'KT4Calo' )
kt6CaloL2Relative = ak5CaloL2Relative.clone( algorithm = 'KT6Calo' )
ic5CaloL2Relative = ak5CaloL2Relative.clone( algorithm = 'IC5Calo' )

ak7PFL2Relative   = ak5PFL2Relative.clone  ( algorithm = 'AK7PF' )
kt4PFL2Relative   = ak5PFL2Relative.clone  ( algorithm = 'KT4PF' )
kt6PFL2Relative   = ak5PFL2Relative.clone  ( algorithm = 'KT6PF' )
ic5PFL2Relative   = ak5PFL2Relative.clone  ( algorithm = 'IC5PF' )

# L3 (absolute) Correction Services
ak7CaloL3Absolute = ak5CaloL3Absolute.clone( algorithm = 'AK7Calo' )
kt4CaloL3Absolute = ak5CaloL3Absolute.clone( algorithm = 'KT4Calo' )
kt6CaloL3Absolute = ak5CaloL3Absolute.clone( algorithm = 'KT6Calo' )
ic5CaloL3Absolute = ak5CaloL3Absolute.clone( algorithm = 'IC5Calo' )

ak7PFL3Absolute   = ak5PFL3Absolute.clone  ( algorithm = 'AK7PF' )
kt4PFL3Absolute   = ak5PFL3Absolute.clone  ( algorithm = 'KT4PF' )
kt6PFL3Absolute   = ak5PFL3Absolute.clone  ( algorithm = 'KT6PF' )
ic5PFL3Absolute   = ak5PFL3Absolute.clone  ( algorithm = 'IC5PF' )

# Residual Correction Services
ak7CaloResidual   = ak5CaloResidual.clone()
kt4CaloResidual   = ak5CaloResidual.clone()
kt6CaloResidual   = ak5CaloResidual.clone()
ic5CaloResidual   = ak5CaloResidual.clone()

ak7PFResidual     = ak5PFResidual.clone()
kt4PFResidual     = ak5PFResidual.clone()
kt6PFResidual     = ak5PFResidual.clone()
ic5PFResidual     = ak5PFResidual.clone()

# L6 (semileptonically decaying b-jet) Correction Services
ak7CaloL6SLB = ak5CaloL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('ak7CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('ak7CaloJetsSoftMuonTagInfos')
    )
kt4CaloL6SLB = ak5CaloL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('kt4CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('kt4CaloJetsSoftMuonTagInfos')
    )
kt6CaloL6SLB = ak5CaloL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('kt6CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('kt6CaloJetsSoftMuonTagInfos')
    )
ic5CaloL6SLB = ak5CaloL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('ic5CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('ic5CaloJetsSoftMuonTagInfos')
    )

ak7PFL6SLB = ak5PFL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('ak7PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('ak7PFJetsSoftMuonTagInfos')
    )
kt4PFL6SLB = ak5PFL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('kt4PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('kt4PFJetsSoftMuonTagInfos')
    )
kt6PFL6SLB = ak5PFL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('kt6PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('kt6PFJetsSoftMuonTagInfos')
    )
ic5PFL6SLB = ak5PFL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('ic5PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('ic5PFJetsSoftMuonTagInfos')
    )


#
# MULTIPLE LEVEL CORRECTION SERVICES
#

# L2L3 CORRECTION SERVICES
ak7CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7CaloL2Relative','ak7CaloL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
kt4CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt4CaloL2Relative','kt4CaloL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
kt6CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt6CaloL2Relative','kt6CaloL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
ic5CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ic5CaloL2Relative','ic5CaloL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )

ak7PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7PFL2Relative','ak7PFL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
kt4PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt4PFL2Relative','kt4PFL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
kt6PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt6PFL2Relative','kt6PFL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
ic5PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ic5PFL2Relative','ic5PFL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )

#--- JPT needs the L1JPTOffset to account for the ZSP changes.
#--- L1JPTOffset is NOT the same as L1Offset !!!!!
ak7JPTL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7L1JPTOffset','ak7JPTL2Relative','ak7JPTL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )

# L1L2L3 CORRECTION SERVICES
ak7CaloL1L2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7CaloL1Offset','ak7CaloL2Relative','ak7CaloL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
kt4CaloL1L2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt4CaloL1Offset','kt4CaloL2Relative','kt4CaloL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
kt6CaloL1L2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt6CaloL1Offset','kt6CaloL2Relative','kt6CaloL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
ic5CaloL1L2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ic5CaloL1Offset','ic5CaloL2Relative','ic5CaloL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )

ak7PFL1L2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7PFL1Offset','ak7PFL2Relative','ak7PFL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
kt4PFL1L2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt4PFL1Offset','kt4PFL2Relative','kt4PFL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
kt6PFL1L2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt6PFL1Offset','kt6PFL2Relative','kt6PFL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
ic5PFL1L2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ic5PFL1Offset','ic5PFL2Relative','ic5PFL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )
#--- JPT needs the L1JPTOffset to account for the ZSP changes.
#--- L1JPTOffset is NOT the same as L1Offset !!!!!
ak7JPTL1L2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7JPTL1Offset','ak7L1JPTOffset','ak7JPTL2Relative','ak7JPTL3Absolute'),
    useCondDB = cms.untracked.bool(True)
    )

# L2L3Residual CORRECTION SERVICES
ak7CaloL2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7CaloL2Relative','ak7CaloL3Absolute','ak7CaloResidual')
    )
kt4CaloL2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt4CaloL2Relative','kt4CaloL3Absolute','kt4CaloResidual')
    )
kt6CaloL2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt6CaloL2Relative','kt6CaloL3Absolute','kt6CaloResidual')
    )
ic5CaloL2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ic5CaloL2Relative','ic5CaloL3Absolute','ic5CaloResidual')
    )

ak7PFL2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7PFL2Relative','ak7PFL3Absolute','ak7PFResidual')
    )
kt4PFL2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt4PFL2Relative','kt4PFL3Absolute','kt4PFResidual')
    )
kt6PFL2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt6PFL2Relative','kt6PFL3Absolute','kt6PFResidual')
    )
ic5PFL2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ic5PFL2Relative','ic5PFL3Absolute','ic5PFResidual')
    )

# L1L2L3Residual CORRECTION SERVICES
ak7CaloL1L2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7CaloL1Offset','ak7CaloL2Relative','ak7CaloL3Absolute','ak7CaloResidual'),
    useCondDB = cms.untracked.bool(True)
    )
kt4CaloL1L2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt4CaloL1Offset','kt4CaloL2Relative','kt4CaloL3Absolute','kt4CaloResidual'),
    useCondDB = cms.untracked.bool(True)
    )
kt6CaloL1L2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt6CaloL1Offset','kt6CaloL2Relative','kt6CaloL3Absolute','kt6CaloResidual'),
    useCondDB = cms.untracked.bool(True)
    )
ic5CaloL1L2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ic5CaloL1Offset','ic5CaloL2Relative','ic5CaloL3Absolute','ic5CaloResidual'),
    useCondDB = cms.untracked.bool(True)
    )

ak7PFL1L2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7PFL1Offset','ak7PFL2Relative','ak7PFL3Absolute','ak7PFResidual'),
    useCondDB = cms.untracked.bool(True)
    )
kt4PFL1L2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt4PFL1Offset','kt4PFL2Relative','kt4PFL3Absolute','kt4PFResidual'),
    useCondDB = cms.untracked.bool(True)
    )
kt6PFL1L2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt6PFL1Offset','kt6PFL2Relative','kt6PFL3Absolute','kt6PFResidual'),
    useCondDB = cms.untracked.bool(True)
    )
ic5PFL1L2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ic5PFL1Offset','ic5PFL2Relative','ic5PFL3Absolute','ic5PFResidual'),
    useCondDB = cms.untracked.bool(True)
    )
#--- JPT needs the L1JPTOffset to account for the ZSP changes.
#--- L1JPTOffset is NOT the same as L1Offset !!!!!
ak7JPTL1L2L3Residual = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7JPTL1Offset','ak7L1JPTOffset','ak7JPTL2Relative','ak7JPTL3Absolute','ak7JPTResidual'),
    useCondDB = cms.untracked.bool(True)
    )

# L1FastL2L3 CORRECTION SERVICES
ak7CaloL1FastL2L3 = ak7CaloL2L3.clone()
ak7CaloL1FastL2L3.correctors.insert(0,'L1Fastjet')
kt4CaloL1FastL2L3 = kt4CaloL2L3.clone()
kt4CaloL1FastL2L3.correctors.insert(0,'L1Fastjet')
kt6CaloL1FastL2L3 = kt6CaloL2L3.clone()
kt6CaloL1FastL2L3.correctors.insert(0,'L1Fastjet')
ic5CaloL1FastL2L3 = ic5CaloL2L3.clone()
ic5CaloL1FastL2L3.correctors.insert(0,'L1Fastjet')

ak7PFL1FastL2L3 = ak7PFL2L3.clone()
ak7PFL1FastL2L3.correctors.insert(0,'L1Fastjet')
kt4PFL1FastL2L3 = kt4PFL2L3.clone()
kt4PFL1FastL2L3.correctors.insert(0,'L1Fastjet')
kt6PFL1FastL2L3 = kt6PFL2L3.clone()
kt6PFL1FastL2L3.correctors.insert(0,'L1Fastjet')
ic5PFL1FastL2L3 = ic5PFL2L3.clone()
ic5PFL1FastL2L3.correctors.insert(0,'L1Fastjet')

ak5TrackL1FastL2L3 = ak5TrackL2L3.clone()
ak5TrackL1FastL2L3.correctors.insert(0,'L1Fastjet')


# L2L3L6 CORRECTION SERVICES
ak7CaloL2L3L6 = ak7CaloL2L3.clone()
ak7CaloL2L3L6.correctors.append('ak7CaloL6SLB')
kt4CaloL2L3L6 = kt4CaloL2L3.clone()
kt4CaloL2L3L6.correctors.append('kt4CaloL6SLB')
kt6CaloL2L3L6 = kt6CaloL2L3.clone()
kt6CaloL2L3L6.correctors.append('kt6CaloL6SLB')
ic5CaloL2L3L6 = ic5CaloL2L3.clone()
ic5CaloL2L3L6.correctors.append('ic5CaloL6SLB')

ak7PFL2L3L6 = ak7PFL2L3.clone()
ak7PFL2L3L6.correctors.append('ak7PFL6SLB')
kt4PFL2L3L6 = kt4PFL2L3.clone()
kt4PFL2L3L6.correctors.append('kt4PFL6SLB')
kt6PFL2L3L6 = kt6PFL2L3.clone()
kt6PFL2L3L6.correctors.append('kt6PFL6SLB')
ic5PFL2L3L6 = ic5PFL2L3.clone()
ic5PFL2L3L6.correctors.append('ic5PFL6SLB')


# L1L2L3L6 CORRECTION SERVICES
ak7CaloL1FastL2L3L6 = ak7CaloL1L2L3.clone()
ak7CaloL1FastL2L3L6.correctors.append('ak7CaloL6SLB')
kt4CaloL1FastL2L3L6 = kt4CaloL1L2L3.clone()
kt4CaloL1FastL2L3L6.correctors.append('kt4CaloL6SLB')
kt6CaloL1FastL2L3L6 = kt6CaloL1L2L3.clone()
kt6CaloL1FastL2L3L6.correctors.append('kt6CaloL6SLB')
ic5CaloL1FastL2L3L6 = ic5CaloL1L2L3.clone()
ic5CaloL1FastL2L3L6.correctors.append('ic5CaloL6SLB')

ak7PFL1FastL2L3L6 = ak7PFL1FastL2L3.clone()
ak7PFL1FastL2L3L6.correctors.append('ak7PFL6SLB')
kt4PFL1FastL2L3L6 = kt4PFL1FastL2L3.clone()
kt4PFL1FastL2L3L6.correctors.append('kt4PFL6SLB')
kt6PFL1FastL2L3L6 = kt6PFL1FastL2L3.clone()
kt6PFL1FastL2L3L6.correctors.append('kt6PFL6SLB')
ic5PFL1FastL2L3L6 = ic5PFL1FastL2L3.clone()
ic5PFL1FastL2L3L6.correctors.append('ic5PFL6SLB')
