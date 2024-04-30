from extractors.custom_extractors.waminsurance.kid_governance import WamInsuranceKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.kid_module import WamInsuranceKidModuleExtractor
from extractors.custom_extractors.waminsurance.gkid_governance import WamInsuranceGKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.kid_credem import WamInsuranceKidCredemExtractor
from extractors.custom_extractors.waminsurance.cga import WamInsuranceCGA
from extractors.custom_extractors.wamasset.kidtable import WamAssetKidFeesExtractor

from extractors.custom_extractors.wamderivati.complexity import WamDerivatiComplexity
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
        'complexity': WamDerivatiComplexity,
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
        'kidcertificatesrisk': WamDerivatiComplexity,
        'kidasset': WamAssetKidFeesExtractor,
        'cga': WamCGA,
    }
}

