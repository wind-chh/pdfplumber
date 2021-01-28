#!/usr/bin/env python3

import os
import pdfplumber
# import pandas as pd

# pdf_file = '/home/huan_cheng/Documents/pdf_files/A1.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/B1.pdf'
# pdf_file = '/home/huan_cheng/workspace/test/pdf2txt/bold_font_test.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/table_edge_debug.pdf'
# pdf_file = '/home/huan_cheng/workspace/algrithm/pdfplumber/tests/pdfs/issue-13-151201DSP-Fond-581-90D.pdf'

# pdf = pdfplumber.open(pdf_file)
# p = pdf.pages[0]
# # print(len(p.rects))
# # print(len(p.curves))
# tables = p.extract_tables()
# # print(tables)
# # print(len(p1.objects['curve']))


pdf_dir = '/home/huan_cheng/Documents/pdf_files'
for root, dirs, files in os.walk(pdf_dir):
    for f in files:
        # if not f.endswith(".pdf"):
        if not f.endswith(".large"):
            continue
        full_path = os.path.join(root, f)
        pdf = pdfplumber.open(full_path)
        # print(f"Page Number: {len(pdf.pages)}, {full_path}")
        index = 1
        for p in pdf.pages:
            print(f"Page: {index}@{len(pdf.pages)}, {full_path}")
            tables = p.extract_tables()
            print(len(tables))
            index += 1


