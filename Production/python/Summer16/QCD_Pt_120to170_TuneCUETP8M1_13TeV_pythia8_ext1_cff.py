import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/0052A1B6-B4C2-E611-BA23-0CC47A78A408.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/06B96A6A-A7C2-E611-8518-0CC47A4D7614.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/082078AF-B4C2-E611-B7EA-0025905B858E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/08B9CDAC-B4C2-E611-A896-0025905A611C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/0A8A62AE-B4C2-E611-8544-0025905A60A8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/0AF8F1B3-A7C2-E611-AA0F-0025905A60FE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/0EB5F68E-7FC2-E611-8E23-008CFA1111C4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/10BBE4B1-A7C2-E611-90E2-0CC47A4C8E22.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/127DCDB1-B4C2-E611-A051-0025905B8612.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/12A1C5D2-B3C2-E611-91B7-0CC47A7C353E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/1A143D9D-74C2-E611-AD19-0025905B85B2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/1A2FAD0F-7CC2-E611-9944-0025905A6084.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/1E66C77C-B4C2-E611-9BE6-0CC47A7C345C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/2A592F16-A5C2-E611-A79E-0CC47A78A4A0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/2C0E58B3-B4C2-E611-89D8-0025905B85C6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/3876B989-72C2-E611-821A-047D7B881D1E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/3C0143AC-B4C2-E611-BE1F-0CC47A4D7640.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/40434D16-A5C2-E611-993C-0CC47A7C34E6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/52F7A44A-CBC2-E611-A213-0025905A60F4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/54BFD405-9EC2-E611-88FA-0CC47A4D7602.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/5CB0D441-B4C2-E611-BFF0-0CC47A7C356A.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/5CBBEABE-A7C2-E611-AACB-0025905B85DE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/6432BB3A-A5C2-E611-A580-0CC47A78A33E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/6A5201B0-B4C2-E611-9DCF-0025905B85B2.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/6E8E3085-7FC2-E611-867B-008CFA1112B0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/6ECE0014-7CC2-E611-9603-0CC47A4D767A.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/74C6DD4E-BBC2-E611-BB56-0CC47A7C345E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/783B3E86-B4C2-E611-9697-0CC47A7C3412.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/788BF63E-CBC2-E611-8872-0025905B859A.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/78C67ACC-C9C2-E611-A4D2-002590DB9252.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/7C185B45-BBC2-E611-BDF2-0CC47A4D7600.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/7CFC16AC-B4C2-E611-84F5-0CC47A78A42E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/86B6B161-B4C2-E611-A3D6-0CC47A78A340.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/8A2A6A0E-5FC2-E611-B5C3-70106F4A9994.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/8CDE01A6-74C2-E611-9036-003048FFD7CE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/98B87F80-72C2-E611-9595-047D7B881D1E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/9E2EA6B2-A7C2-E611-8FD0-0025905A60DE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/A269B1D4-B3C2-E611-AD26-0CC47A4D7618.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/A696E049-BBC2-E611-BC91-0CC47A78A3EE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/AA78D833-A8C2-E611-8DC6-0CC47A4C8E0E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/AC9F47E2-A7C2-E611-98E3-0CC47A4C8F30.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/AEFBF878-7FC2-E611-A4B8-008CFA1979FC.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/B00CFE0E-7CC2-E611-816B-0CC47A4C8F08.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/BC237A3A-BBC2-E611-9BCE-0CC47A4C8EE8.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/BC62CA12-7CC2-E611-A6EF-0025905B8610.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/C8DBCBA7-74C2-E611-B753-0025905A60A6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/D825B916-A5C2-E611-AE55-0CC47A78A3B4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/DC54A6AF-B4C2-E611-9BFD-0CC47A7C345E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/DE0E6B12-7CC2-E611-A936-0CC47A74525A.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/E20342B2-A7C2-E611-9331-0025905A48BC.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/E2FF2453-B4C2-E611-8B7C-0CC47A78A4A0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/E6681FFF-C8C2-E611-9A81-1CB72C1B64E6.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/EA723B5E-72C2-E611-950D-0CC47A7E69CE.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/EEE3ADD5-B3C2-E611-81DB-0CC47A4D769C.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/F0DA7D62-72C2-E611-8B80-0CC47A7E0180.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/F643B9AF-A7C2-E611-8C8C-0CC47A78A4BA.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/F6E4F4B1-B4C2-E611-BE0C-0025905B85E8.root',
] )
