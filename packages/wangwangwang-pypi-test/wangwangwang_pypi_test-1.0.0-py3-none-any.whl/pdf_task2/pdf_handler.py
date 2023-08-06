import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
import glob
import os

import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]

pdf_path = os.path.join(curPath, "effective python.pdf")
saveDir= os.path.join(curPath, "temp")

#提取PDF文字
def extract_pdf_text():
    # 提取pdf指定页的文字
    with pdfplumber.open(pdf_path) as pdf:
        page01 = pdf.pages[0]  # 指定页码
        text = page01.extract_text()  # 提取文本
        print(f"第一页pdf的文本内容为：{text}",end='\n')

    #提取所有页pdf文字
    with pdfplumber.open(pdf_path) as pdf:
        print(f"所有页pdf的文本内容如下：")
        for page in pdf.pages:  #遍历所有页
            text = page.extract_text()  # 提取当前页的文本
            print(text)

#提取PDF表格
def extract_pdf_table():
    with pdfplumber.open(pdf_path) as pdf:
        print(f"所有页pdf的表格内容如下：")
        for page in pdf.pages:  # 遍历所有页
            table = page.extract_table()  # 提取当前页的文本
            print(table)

#分割PDF
def split_pdf():
    #如果使用PdfFileReader会抛出异常：PyPDF2.errors.DeprecationError: PdfFileReader is deprecated and was removed in PyPDF2 3.0.0. Use PdfReader instead.
    file_reader = PdfReader(pdf_path)  #实例化pdf reader对象
    # getNumPages() 获取总页数会报错：PyPDF2.errors.DeprecationError: reader.getNumPages is deprecated and was removed in PyPDF2 3.0.0. Use len(reader.pages) instead.
    for page in range(len(file_reader.pages)):
        file_writer = PdfWriter()  #实例化pdf writer对象
        # 将遍历的每一页对象添加到pdf writer对象中，使用file_reader.getPage(page)会报错：PyPDF2.errors.DeprecationError: reader.getPage(pageNumber) is deprecated and was removed in PyPDF2 3.0.0. Use reader.pages[page_number] instead.
        file_writer.add_page(file_reader.pages[page])  #PyPDF2.errors.DeprecationError: addPage is deprecated and was removed in PyPDF2 3.0.0. Use add_page instead.
        with open(f'{os.path.join(saveDir,str(page)+".pdf")}', 'wb') as out:
            file_writer.write(out)


if __name__ == '__main__':
    # extract_pdf_text()
    # extract_pdf_table()
    # split_pdf()
    pass