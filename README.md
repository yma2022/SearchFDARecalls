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

## Tech stack
LangChain, LangGraph

