
# coding: utf-8

# In[228]:


import PyPDF2
from gensim.summarization import keywords
import pandas as pd
import nltk

file = open('JavaBasics-notes.pdf', 'rb')
readpdf = PyPDF2.PdfFileReader(file)
num_pages = readpdf.numPages
data = ""
for pages in range(num_pages):
    page = pdfReader.getPage(pages)
    data += page.extractText()
if data != "":
    data = data
values = keywords(data,scores=True, lemmatize= True)
print(values)
print(len(values))

dataframe = pd.DataFrame(values,columns=['keywords','weights'])
dataframe.to_csv("testcsv.csv", index=False)

