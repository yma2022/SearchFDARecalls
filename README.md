## Simple doc search project
This project is to use agentic LLM as tool to do quick and thorough search to find all relevant recalls of FDA regulated products by since 2009.

Q: Find recalls that are related to microbial contamination.

A: 
1. - **Brand**: KB, DK, more
   - **Company**: King Bio
   - **Date**: 8/22/18
   - **Product Description**: Homeopathic products
   - **Reason**: Microbial contamination
   - **URL**: [Link](https://www.fda.gov/Safety/Recalls/ucm617945.htm)

2. - **Brand**: Dr. King’s
   - **Company**: King Bio
   - **Date**: 8/27/18
   - **Product Description**: Homeopathic products
   - **Reason**: Microbial contamination
   - **URL**: [Link](https://www.fda.gov/Safety/Recalls/ucm618585.htm)


The current search output is not exaustive because of the naiveness of implementation for both prompt and agent. The proper tune of prompt input, addition of LLM chain and CoT may significantly increase the efficiency and accuracy of search.

It turns out that the exhaustive search could be too expensive for LLM. At current stage, searching for 1 best match may be a better choice.
Q: find a recall that is related to contamination

A:
- **Brand:** Bersih
- **Company:** Soluciones Cosmeticas
- **Date:** 7/14/20
- **Product Description:** Hand Sanitizer Gel
- **Reason:** Potential Methanol Contamination
- **URL:** [Link to Recall Information](https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts/soluciones-cosmeticas-issues-voluntary-nationwide-recall-bersih-hand-sanitizer-gel-due-potential)

Q: find a recall that is related to product defect
A: 
- **Brand:** Kotex
- **Company:** Kimberly-Clark
- **Date:** 12/11/18
- **Product Description:** Tampons
- **Reason:** Performance defect
- **URL:** [Link to Recall Information](https://www.fda.gov/Safety/Recalls/ucm628237.htm)

Q: find a recall that is related to particle problem
A:
- **Brand:** Mylan
- **Company:** Mylan Institutional LLC
- **Date:** 7/7/20
- **Product Description:** Daptomycin for Injection
- **Reason:** Presence of particulate matter
- **URL:** [Link to Recall Information](https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts/mylan-initiates-voluntary-nationwide-recall-one-lot-daptomycin-injection-due-presence-particulate)

The current process looks pretty accurate and the processing time < 1s. 

## Tech stack
LangChain, LangGraph

