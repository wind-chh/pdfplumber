#!/usr/bin/env python3

import os
import time
import pdfplumber as pp
import pickle
# import pandas as pd

pdf_file = '/home/huan_cheng/Documents/pdf_files/A1.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/B1.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/C1.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/D1.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/G1.pdf'
# pdf_file = '/home/huan_cheng/workspace/algrithm/contractsimilarity/data/pdf/TemplateB.pdf'
# pdf_file = '/home/huan_cheng/workspace/test/pdf2txt/bold_font_test.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/table_edge_debug.pdf'
# pdf_file = '/home/huan_cheng/workspace/algrithm/pdfplumber/tests/pdfs/issue-13-151201DSP-Fond-581-90D.pdf'
# pdf_file = '/home/huan_cheng/Documents/pdf_files/bold_font_test.pdf'

# pdf_file = '/home/huan_cheng/Downloads/wfirma_Faktura_FV_1_2021.pdf'

st = time.time()
with pp.open(pdf_file) as pdf:
    # for index, p in enumerate(pdf.pages):
    #     for c in p.chars:
    #         print(f"{c['text']}, {c['fontname']}")
    #     # print(p.extract_text())
    p2 = pdf.pages[1]
    img = p2.to_image()
    img.save('/tmp/test.png')

et = time.time()
print(f"Time: {et - st}")

# with open('/tmp/A1.pk', 'wb') as fp:
#     pickle.dump(page_objs, fp)

##############################################
# with open('/tmp/A1.pk', 'rb') as fp:
#     page_objs = pickle.load(fp)

# st = time.time()
# with pp.open(pdf_file, parsed_objects=page_objs) as pdf:
#     for page in pdf.pages:
#         print(page.extract_text())
# et = time.time()
# print(f"Time: {et - st}")
##############################################

# print(len(p.rects))
# print(len(p.curves))
# text = p.extract_text()
# for c in p.chars:
#     print(f"{c['text']}, {c['render']}, {c['fontname']}")
# print(text)

# tables = p.extract_tables()
# for c in p.chars:
#     print(f"{c['render']}, {c['matrix']}")

# print(tables)
# print(len(p1.objects['curve']))


# pdf_dir = '/home/huan_cheng/Documents/pdf_files'
# for root, dirs, files in os.walk(pdf_dir):
#     for f in files:
#         # if not f.endswith(".pdf"):
#         if not f.endswith(".large"):
#             continue
#         full_path = os.path.join(root, f)
#         pdf = pdfplumber.open(full_path)
#         # print(f"Page Number: {len(pdf.pages)}, {full_path}")
#         index = 1
#         for p in pdf.pages:
#             print(f"Page: {index}@{len(pdf.pages)}, {full_path}")
#             tables = p.extract_tables()
#             print(len(tables))
#             index += 1
