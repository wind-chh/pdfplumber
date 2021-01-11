import sys

sys.path.insert(0, '/Users/wind/workspace/algorithm/pdfplumber')

from pdfplumber.contract import Contract
from glob import glob
from pprint import pprint

if __name__ == '__main__':
    for pdf_file in glob("/Users/wind/tmp/*1.pdf"):
        with open(pdf_file, 'rb') as fp:
            contract = Contract(pdf_file)
            contract.parse()
            print(f"{pdf_file}: {contract.title}")
            pprint(contract.fontsize_stat)

    # pdf_file = '/Users/wind/tmp/B1.pdf'
    # with open(pdf_file, 'rb') as fp:
    #     contract = Contract(pdf_file)
    #     contract.parse()
    #     print(contract.title)

