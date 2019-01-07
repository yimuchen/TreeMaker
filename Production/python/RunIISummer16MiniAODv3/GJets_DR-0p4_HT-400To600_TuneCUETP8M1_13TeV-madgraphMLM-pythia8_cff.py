import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/00DFA149-FAF0-E811-98A4-E0071B7A4550.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/02AB7274-E5F0-E811-ABD2-5065F38102F1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/02F32944-99F0-E811-B78E-5065F3818271.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/06A493E9-C5F0-E811-8860-E0071B7A5540.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/107FE84C-60F0-E811-A34C-A0369F3102B6.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/14FEEA68-FAF0-E811-B8F0-24BE05CEEC21.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/16296401-C6F0-E811-8068-5065F3817221.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/16E9B623-E6F0-E811-BA5C-E0071B7A5650.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/16EEC3E3-F5F0-E811-946A-506B4BB166AE.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/1A3A036A-C7F0-E811-A1C9-5065F38162B1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/1A3D89B6-B5F0-E811-8814-24BE05CEACA1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/1C7E9225-E6F0-E811-9512-E0071B7A5650.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/1CC38231-E6F0-E811-A3EE-24BE05C63651.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/1E6E63C4-C5F0-E811-9C3F-24BE05C33C71.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/20459340-A0F0-E811-B400-5065F382A241.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/20751F6C-C7F0-E811-81C8-5065F38162B1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/2217237E-E5F0-E811-AAD5-5065F3818271.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/22B198DB-A0F0-E811-8871-EC0D9A82262E.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/22E62AE2-EBF0-E811-B4B8-5065F382A241.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/24297176-E5F0-E811-B65E-24BE05C3CBD1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/24B0644A-B5F0-E811-B76C-5065F3818261.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/2C79F401-E8F0-E811-B4CF-24BE05C6D711.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/2E51F109-E6F0-E811-9581-24BE05C68671.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/303DD47A-E5F0-E811-BB5C-5065F38102F1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/3407489C-E6F0-E811-93ED-24BE05C6B701.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/3633EB2E-83F0-E811-A8C9-5065F3818291.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/404482A3-A2F0-E811-A7F3-24BE05C4D801.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/42393EE6-C5F0-E811-8DDB-E0071B7A5540.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/42C4B743-FAF0-E811-9D4D-E0071B7A4550.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/44D21B0C-E6F0-E811-8477-24BE05C68671.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/481B1498-9CF0-E811-B01F-EC0D9A8222DE.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/4C8DED8E-8DF0-E811-AFBD-EC0D9A822636.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/4C954B07-87F0-E811-A00B-506B4BB16AB6.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/4C9C2865-86F0-E811-8C46-24BE05CEED81.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/4E013D76-E5F0-E811-A7A8-24BE05C4D8C1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/5096098A-96F0-E811-A76B-24BE05C3EC61.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/58B9A58F-88F0-E811-A80D-24BE05CEEB81.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/5C11D06F-9FF0-E811-805C-506B4BB16ADE.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/6002B0C1-7DF0-E811-B3D7-EC0D9A8221CE.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/62937890-58F0-E811-826A-B8CA3A70B608.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/62AC3B61-E7F0-E811-AEFA-506B4BB134CE.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/62F8906C-9FF0-E811-9B0F-24BE05C68671.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/6CCEA707-9FF0-E811-8773-24BE05CEEB81.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/6E33AF57-E5F0-E811-AFA3-EC0D9A82264E.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/72C364AB-C5F0-E811-B1BE-EC0D9A82237E.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/7C242474-87F0-E811-99AC-24BE05CE2D41.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/7C26D41E-F3F0-E811-A934-24BE05CE3E61.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/7C5591FC-7EF0-E811-B706-E0071B73C620.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/7E372FD2-9FF0-E811-A8F6-E0071B749C80.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/801F4A12-A1F0-E811-ADCB-24BE05CE2E81.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/80AF5BE8-E7F0-E811-93D7-506B4BB16A96.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/80E4B8D7-01F1-E811-8ACF-5065F38172A1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/88B22213-96F0-E811-8A45-EC0D9A82260E.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/88D103E1-BDF0-E811-B44E-5065F3816251.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/8A1CA2BA-7BF0-E811-A185-506B4BB16AAE.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/8A8D7D79-F7F0-E811-A028-506B4BB16026.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/8E3C73A0-E6F0-E811-9AE0-24BE05C6B701.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/90068570-B0F1-E811-8FB8-24BE05CEEB31.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/96589FAD-C5F0-E811-854C-EC0D9A82237E.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/989EA391-95F0-E811-9D82-E0071B7AC710.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/98A746F6-75F0-E811-8356-E0071B7AC770.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/9A69CE38-05F1-E811-888B-24BE05CE3E61.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/9A74F869-9FF0-E811-A76A-EC0D9A8221DE.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/A026744A-E5F0-E811-8CD8-EC0D9A82264E.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/A05EEE62-F2F0-E811-810B-24BE05CE3E61.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/A64E4684-7EF0-E811-B77F-24BE05C4D851.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/A6EEE3B4-A1F0-E811-A8FC-24BE05C648A1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/A83ED875-E5F0-E811-83ED-24BE05C4D8C1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/A8C3E489-E5F0-E811-AB36-24BE05C6B701.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/AA0C476C-E7F0-E811-8C40-24BE05C6E7E1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/ACA439E7-71F0-E811-8B77-24BE05CEEB81.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/AE3ABD48-EAF0-E811-A424-EC0D9A82262E.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/B097EB79-E5F0-E811-B27B-24BE05C3CBD1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/B4273037-F0F0-E811-8C77-24BE05C63631.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/B4C5359A-EEF0-E811-A816-24BE05C44B91.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/B4D0F3B4-D3F0-E811-BCC1-506B4BB166B6.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/B64CB2C7-C5F0-E811-BBB2-24BE05C63741.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/B6B15D3E-94F0-E811-AA47-5065F381D2C1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/BC5B0784-E5F0-E811-8F9B-24BE05C63651.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/C8423974-02F1-E811-B258-506B4BB16AB6.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/CAEDDF83-E5F0-E811-B699-5065F3818271.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/CC925318-E6F0-E811-8EB6-24BE05CEDCF1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/D05A0771-E5F0-E811-B04E-EC0D9A82264E.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/D6075D0F-B7F0-E811-B60B-24BE05C6C7E1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/D697564E-02F1-E811-BCC4-5065F37D7121.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/D6D0B308-C0F1-E811-AD6A-24BE05C4D8C1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/DA2BDBC5-9BF0-E811-B3CF-24BE05C6D5A1.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/DCCB1F35-E6F0-E811-9134-24BE05C63651.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/E26C4ACA-C5F0-E811-B369-24BE05C33C71.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/E4DF2D2E-A0F0-E811-A504-24BE05C46B01.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/EC9A29D7-FBF0-E811-BC6A-5065F3818281.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/EE2CD2CB-C5F0-E811-A4ED-24BE05C63741.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/F056EA12-A9F0-E811-AC4F-5065F3815221.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/F4B8A942-EAF0-E811-8C71-EC0D9A8221FE.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/FC8832C3-BDF0-E811-AF48-24BE05C6E591.root',
       '/store/mc/RunIISummer16MiniAODv3/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2/00000/FE0444AE-C5F0-E811-9D49-EC0D9A82237E.root',
] )