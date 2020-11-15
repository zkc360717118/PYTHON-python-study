from docx import Document

path = "G:\\projects\\PYTHON-python-study\\office\\temp.docx"
document = Document(path)
for paragraph in document.paragraphs:
    print(paragraph.text)


# 写入
