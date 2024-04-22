
from extractors.custom_extractors.waminsurance.kid_governance import WamInsuranceKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.gkid_governance import WamInsuranceGKidGovernanceExtractor
from extractors.custom_extractors.waminsurance.kid_credem import WamInsuranceKidCredemExtractor
from extractors.custom_extractors.waminsurance.kid_module import WamInsuranceKidModuleExtractor
from extractors.custom_extractors.wamasset.kidtable import WamassetKidTableextractor
from AWSInteraction.EnvVarSetter import EnvVarSetter

env_setter = EnvVarSetter()
env_setter.configure_local_env_vars()


file_path ="C:/Users/simone.mugnai/Desktop/priipkid_IT0000384641_PIC.pdf"

extractor =  WamassetKidTableextractor(file_path)
extraction = extractor.process()


print(extraction)



