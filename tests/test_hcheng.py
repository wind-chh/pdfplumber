#!/usr/bin/env python3

from os import set_blocking
import pdfplumber
# import pandas as pd

# pdf_file = '/home/huan_cheng/Documents/pdf_files/A1.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/B1.pdf'
# pdf_file = '/home/huan_cheng/workspace/test/pdf2txt/bold_font_test.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/table_edge_debug.pdf'
pdf_file = '/home/huan_cheng/workspace/algrithm/pdfplumber/tests/pdfs/issue-13-151201DSP-Fond-581-90D.pdf'

pdf = pdfplumber.open(pdf_file)
# for pnum, page in enumerate(pdf.pages):
#     # print(page.extract_text())
#     tables = page.extract_tables()
#     print(f"Page: {pnum}, Tables: {len(tables)}")

p1 = pdf.pages[0]
tables = p1.extract_tables()
# print(tables)
# print(len(p1.objects['curve']))


# for c in page1.chars:
#     print(c['render'], type(c['render']))
#     print(c['matrix'], type(c['matrix'][2]))
# print("Done!")

# page2 = pdf.pages[1]
# page3 = pdf.pages[2]


# text = page1.extract_text()
# words = page2.extract_words()
# for w in words:
#     print(w['text'])

# tables = page2.extract_tables()
# print(tables)

# # print(pd.DataFrame(tables[0]))
# for w in words:
#     print(w['text'])

