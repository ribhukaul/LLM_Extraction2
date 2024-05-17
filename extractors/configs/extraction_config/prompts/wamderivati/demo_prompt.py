
# demo
demo_system = "You are a helpful extractor of data from document"

demo_human = """At the beginnig I will tell you some information that will be useful to answer the question I will ask on the document.
        Final barrier:
         - Europea if the final redemption amount is calculated on a value measured on a single final valuation date(final observation date) or on a series of final valuation dates on which an average is calculated;
         - Americana if the final redemption amount is calculated on a value measured in a continuous interval between the initial valuation date and the final valuation date;
         - None if the Certificate has a floor level/ protection of 100%
        From the following certificate's document {input}
        recover the following information:
        - Isin, Description or type of product, Issuer, Specified Currency, Listing, Nominal Amount, Floor Amount or Floor Level(if it is not present is not a problem), Protection, Guaranteed level, Barrier Level, strike level,
        - tell me if the final barrier is europea or americana or None, in order to respond use the info in the document and the context provided an the beginnig of my message, give me your response based on your reasoning.
        - Additional Unconditional Amount, Additional Conditional Amount(m), Additional Conditional Amount (it is the number of EUR in the table) , Additional Conditional Amount Payment Level(the percentage level in the table),
        - the Additional Conditional Amount Payment with Memory, memory effect: yes if there s the phrase 'less all additional conditional amounts (m) paid on the preceding additional conditional amount', memory effect: if in the description there is MEMORY,
        - maximum payment, underlyings of the certificate specifying Bloomberg code and Isin code, issue date, final payment date.
        - tell me if there is an Early Redemption event, do not consider MREL Disqualification Event in order to respond to this question.
        - if there is a callability mechanism, if there is a putability mechanism.
        - Tell me if there is an Early Redemption Amount greater than the Final Redempton Amount (so greater than 1000), if yes give me the first Early Redemption Amount greater than the Final Redempton Amount ((so greater than 1000))"""

