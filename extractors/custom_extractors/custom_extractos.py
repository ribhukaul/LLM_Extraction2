from extractors.custom_extractors.waminsurance.kid_governance import WamInsuranceKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.kid_module import WamInsuranceKidModuleExtractor
from extractors.custom_extractors.waminsurance.gkid_governance import WamInsuranceGKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.kid_credem import WamInsuranceKidCredemExtractor
from extractors.custom_extractors.waminsurance.cgasimple import WamCGA
from extractors.custom_extractors.wamasset.kidtable import WamAssetKidFeesExtractor

from extractors.custom_extractors.wamderivati.demo import WamDerivatiDemo
from extractors.custom_extractors.wamderivati.bnpproduction import BNPDerivatiKidExtractor
from extractors.custom_extractors.wamderivati.rettifichebi import WamDerivatiRettifiche
from extractors.custom_extractors.wambond.bloombergss import WamBondBloombergSS

# SWITCH CASE FOR EXTRACTION MODEL SELECTION
custom_extractors = {
    'waminsurance': {
        'kidgovernance': WamInsuranceKidGovernanceExtractor,
        'gkidgovernance': WamInsuranceGKidGovernanceExtractor,
        'kidcredem': WamInsuranceKidCredemExtractor,
        'kidmodule':  WamInsuranceKidModuleExtractor ,
        'cga': WamCGA          
        },
    'wamderivati': {
        'complexity': WamDerivatiDemo,
        'productionderivatives':BNPDerivatiKidExtractor,
        'rettifichebi': WamDerivatiRettifiche

        },
    'wamfondi': {
        'peergroup': ''
    },
    'wambond': {
        'bloombergss': WamBondBloombergSS
    },
    'wamasset':{
        'kidasset': WamAssetKidFeesExtractor
    },
    'sim':{

    },
    'demo':{
        'kidinsurance': WamInsuranceKidGovernanceExtractor,
        'gkidinsurance': WamInsuranceGKidGovernanceExtractor,
        'certificatesrettificheborsait': WamDerivatiRettifiche,
        'kidcertificatesrisk': WamDerivatiDemo,
        'kidasset': WamAssetKidFeesExtractor,
        'cga': WamCGA,
    }
}

