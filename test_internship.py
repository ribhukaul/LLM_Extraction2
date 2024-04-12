
from extractors.custom_extractors.waminsurance.kid_governance import WamInsuranceKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.gkid_governance import WamInsuranceGKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.kid_credem import WamInsuranceKidCredemExtractor
from extractors.custom_extractors.waminsurance.kid_module import WamInsuranceKidModuleExtractor
from AWSInteraction.EnvVarSetter import EnvVarSetter
from extractors.custom_extractors.wamasset.fullkid import WamAssetKidExtractor
from extractors.custom_extractors.wamasset.kidtable import WamassetKidTableextractor

env_setter = EnvVarSetter()
env_setter.configure_local_env_vars()


file_path = 'data_test\priipkid\priipkid_IT0000380649_PIC.pdf'

extractor =  WamassetKidTableextractor(file_path)
extraction = extractor.process()

extraction.to_excel('C:/Users/simone.mugnai/Desktop/integration.xlsx', index=False)

print(extraction)
# print("Costi:")
# for key, value in cost_dict.items():
#     print(f"{key}: {value}")
# print("\nGestione:")
# for key, value in gestione_dict.items():
#     print(f"{key}: {value}")





