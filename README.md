"RISC, an open-source Python package data generator. RISC generates look-alike automobile "
                    "insurance contracts based on the Quebec regulatory insurance form in French and English."

does not work in 3.11 due to SciPy
> > En Python 3.9


- Juste nouvelle affaires
- Pas de multiproduit
- Contrat de 12 mois

We have automatically/manually extracted the text of AMF contract.
We have removed the contract margin text (the insurance company logo on the left and the FPQ 1 policy number of type of policy).
We have cleaned remove all page reference as <PAGE_NUMBER>.
The text does not include page number.

The simulated contract are new customer. Ca

V1:
- Contrat juste avec un véhicule et un assuré

V2:
- Contract avec plus d'un véhicule et un assuré


