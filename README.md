# KeywordsExtraction
Assignment 2:
Write a code to extract the keywords (like Inheritance, encapsulation, multithreading) from the document shared in the link http://bit.ly/epo_keyword_extraction_document, and upload the code in Github and also mention the keywords in order of their weightages in a Google doc or excel sheet

Written for python 3.6
Dependencies:
PyPDF2
gensim
pandas
nltk

The PDF document is initially read and the text is extracted using PyPDF2, then using Gensim keywords are extracted and a dataframe is made using pandas. The dataframe is then saved into excel .csv file.

There are many different methods for keywords extraction, some include using TF-TDF for multiple documents, TF-ISF for single document, using RAKE library, etc. 
