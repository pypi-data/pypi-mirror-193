from pdf_task.pdf_handler import extract_pdf_text,extract_pdf_table,split_pdf
import os

if __name__ == '__main__':
    print("Hello world")
    extract_pdf_text()
    extract_pdf_table()
    split_pdf()
    os.system("pause")