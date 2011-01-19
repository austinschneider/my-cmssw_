def customise(process):

    # add particle flow local reconstruction
    process.load("RecoParticleFlow.PFClusterProducer.particleFlowCluster_cff")
    process.localReco += process.particleFlowCluster

    # avoid clustering in forward regions for dramatic timing improvement 
    process.particleFlowClusterPS.thresh_Pt_Seed_Endcap = cms.double(99999.)
    process.particleFlowClusterHFEM.thresh_Pt_Seed_Endcap = cms.double(99999.)
    process.particleFlowClusterHFHAD.thresh_Pt_Seed_Endcap = cms.double(99999.)

    process.load("RecoParticleFlow.PFTracking.pfTrack_cfi")
    process.pfTrack.UseQuality = cms.bool(True)   
    process.pfTrack.TrackQuality = cms.string('highPurity')   
    process.pfTrack.TkColList = cms.VInputTag("hiSelectedTracks")  
    process.pfTrack.GsfTracksInEvents = cms.bool(False)
 
    # run a trimmed down PF sequence with heavy-ion vertex, no electrons, etc.
    process.load("RecoParticleFlow.Configuration.RecoParticleFlow_cff")
    process.particleFlowBlock.useConvBremPFRecTracks = cms.bool(False)
    process.particleFlowBlock.usePFatHLT = cms.bool(True)
    process.particleFlowBlock.useIterTracking = cms.bool(False)
    process.particleFlowBlock.useNuclear = cms.bool(False)
    process.particleFlow.vertexCollection = cms.InputTag("hiSelectedVertex")
    process.particleFlow.usePFElectrons = cms.bool(False)
    process.particleFlowReco.remove(process.particleFlowTrackWithDisplacedVertex)
    process.particleFlowReco.remove(process.pfElectronTranslatorSequence)

    # define new high-level RECO sequence and add to top-level sequence
    process.load("RecoJets.Configuration.RecoPFJets_cff")
    process.highLevelRecoPbPb = cms.Sequence(process.pfTrack 
                                             * process.particleFlowReco
                                             * process.recoPFJets)
    process.reconstructionHeavyIons *= process.highLevelRecoPbPb

    return process
