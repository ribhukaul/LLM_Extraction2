
from extractors.custom_extractors.waminsurance.kid_governance import WamInsuranceKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.gkid_governance import WamInsuranceGKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.kid_credem import WamInsuranceKidCredemExtractor
from extractors.custom_extractors.waminsurance.kid_module import WamInsuranceKidModuleExtractor
from extractors.custom_extractors.wamasset.kidtable import WamassetKidTableextractor
from AWSInteraction.EnvVarSetter import EnvVarSetter
from extractors.custom_extractors.wamasset.fullkid import WamAssetKidExtractor
from extractors.custom_extractors.wamasset.kidtable import WamassetKidTableextractor

env_setter = EnvVarSetter()
env_setter.configure_local_env_vars()



file_path = 'data_test\priipkid\priipkid_LU1504218964.pdf'

extractor =  WamassetKidTableextractor(file_path)
extraction = extractor.process()

extraction.to_excel('C:/Users/simone.mugnai/Desktop/integration.xlsx', index=False)

print(extraction)



