from typing import List

from pydantic import BaseModel, Field

NF = "not found"
NA = "N/A"

# WAMINSURANCE


##################
# KID GOVERNANCE #
##################
class IsDisclaimerThere(BaseModel):
    is_disclaimer_there: bool = Field(False, description="è presente il disclaimer 'State per acquistare un prodotto che non è semplice e può essere di difficile comprensione'")

##############
# KIDCREDEM #
##############
class TabellaScenariPerformanceCredem(BaseModel):
    moderato_return_rhp: str = Field(NF, description="Rendimento percentuale(%) a RHP anni scenario moderato")
    favorable_return_rhp: str = Field(NF, description="Rendimento percentuale(%) a RHP anni scenario favorevole")

