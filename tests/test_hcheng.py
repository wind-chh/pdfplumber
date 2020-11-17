#!/usr/bin/env python3

import sys
sys.path.insert(0, "/home/huan_cheng/workspace/algrithm/pdfplumber")
print(sys.path)

import pdfplumber
import pandas as pd


pdf_file = '/home/huan_cheng/workspace/test/pdf2txt/A1.pdf'
# pdf_file = '/home/huan_cheng/workspace/test/pdf2txt/bold_font_test.pdf'

pdf = pdfplumber.open(pdf_file)
page2 = pdf.pages[2]

# for c in page1.chars:
#     print(c['render'], type(c['render']))
#     print(c['matrix'], type(c['matrix'][2]))
# print("Done!")

# page2 = pdf.pages[1]
# page3 = pdf.pages[2]


# text = page1.extract_text()
words = page2.extract_words()
for w in words:
    print(w['text'])

# tables = page2.extract_tables()
# print(tables)

# # print(pd.DataFrame(tables[0]))
# for w in words:
#     print(w['text'])

