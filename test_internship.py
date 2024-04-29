
from extractors.custom_extractors.waminsurance.kid_governance import WamInsuranceKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.gkid_governance import WamInsuranceGKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.kid_credem import WamInsuranceKidCredemExtractor
from extractors.custom_extractors.waminsurance.kid_module import WamInsuranceKidModuleExtractor
#from extractors.custom_extractors.wamasset.kidtable import WamassetKidTableextractor
from AWSInteraction.EnvVarSetter import EnvVarSetter
import pandas as pd

env_setter = EnvVarSetter()
env_setter.configure_local_env_vars()


file_path =r"C:\Users\simone.mugnai\Desktop\Data_test_insurancr\202306_Prudente_AZ Infinity Life.pdf"

extractor =  WamInsuranceKidModuleExtractor(file_path)
extraction = extractor.process()
print(extraction)




