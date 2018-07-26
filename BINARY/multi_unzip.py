# -*- coding: utf-8 -*-
import os
from time import sleep
from shutil import rmtree

# pip install PyPDF2
from PyPDF2 import PdfFileReader

# pip install textract
from textract import process

# pip install python-magic-bin
from magic import from_file

# Windows OS
path_7z = r'C:\Program Files\7-Zip\7z.exe'

def is_int(s):
    try:
        int(s)
        return True
    except:
        return False

# There will only be 1~2 files in one directory after decompression
# 1 file means compression with no password
# 2 files mean compression with password
# return compression file name, and password file name
def get_file(d):
    a = os.listdir(d)
    if len(a) == 1:
        return os.path.join(d, a[0]), ''
    elif len(a) == 2:
        if is_int(a[0]) and not is_int(a[1]):
            return os.path.join(d, a[0]), os.path.join(d, a[1])
        elif not is_int(a[0]) and is_int(a[1]):
            return os.path.join(d, a[1]), os.path.join(d, a[0])
    raise

# decompress file
def de(f, pw=''):
    if pw:
        os.system('""%s" x -p%s "%s"'%(path_7z, pw, f))
    else:
        os.system('""%s" x "%s"'%(path_7z, f))

# get password from txt file
def txt_pw(f):
    r = open(f, 'rb').read()
    return r if len(r) == 10 else ''

# get password from pdf file
def pdf_pw(f):
    try:
        return PdfFileReader(f).getPage(0).extractText().strip()
    except:
        return ''

# get password from xlsx file
def xls_pw(f):
    os.rename(f, f+'.xlsx')
    try:
        return process(f+'.xlsx').strip()
    except:
        return ''

# get password from docx file
def doc_pw(f):
    os.rename(f, f+'.docx')
    try:
        return process(f+'.docx')
    except:
        return ''

# get password from pptx file
def ppt_pw(f):
    os.rename(f, f+'.pptx')
    try:
        for i in process(f+'.pptx').split():
            if len(i) == 10:
                return i
    except:
        pass
    return ''

# while identifying docx/pptx, get same result
# try get password from two extensions
def doc_ppt(f):
    a = open(f, 'rb').read()
    open(f+'.docx', 'wb').write(a)
    open(f+'.pptx', 'wb').write(a)
    return doc_pw(f+'.docx')+ppt_pw(f+'.pptx')

# identify file type, and use the corresponding function to get the password
def ext_pw(f):
    filetype = {
        'ASCII text, with no line terminators': txt_pw,
        'PDF document, version 1.3': pdf_pw,
        'Microsoft Excel 2007+': xls_pw,
        'Microsoft OOXML': doc_ppt,
    }
    t = from_file(f)
    try:
        return filetype[t](f)
    except:
        print t
        raise

# decompress file without password
def de_no_pw(d):
    f = get_file(d)
    if len(f[1]) == 0:
        de(f[0])
        rmtree(d)
        return True
    else:
        return False

# decompress file with password
def de_pw(d, ext=''):
    f = get_file(d)
    pw = {'txt':txt_pw, 'pdf':pdf_pw, 'xls':xls_pw, 'doc':doc_pw, 'ppt':ppt_pw, '':ext_pw}[ext](f[1])
    if pw:
        de(f[0], pw)
        rmtree(d)
        return True
    else:
        return False

if __name__ == '__main__':
    os.mkdir('1201')
    open('1201/1200', 'wb').write(open('BINARY/1200', 'rb').read())
    for i in range(1201, 801, -1):
        de_no_pw(str(i))
    for i in range(801, 501, -1):
        de_pw(str(i), 'txt')
    for i in range(501, 401, -1):
        de_pw(str(i), 'pdf')
    for i in range(401, 301, -1):
        de_pw(str(i), 'xls')
    for i in range(301, 201, -1):
        de_pw(str(i), 'doc')
    for i in range(201, 101, -1):
        de_pw(str(i), 'ppt')
    for i in range(101, 1, -1):
        de_pw(str(i))

