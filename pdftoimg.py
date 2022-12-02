import glob
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

from pdfminer.layout import LAParams, LTTextBox, LTLine, LTTextContainer, LTChar, LTTextLineHorizontal, LTTextBoxHorizontal, LTFigure
from pdfminer.pdfpage import PDFPage

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

from pdfminer.high_level import extract_pages

from PIL import Image, ImageDraw
import os, re
import argparse
from pdf2image import convert_from_path



def read_files(resPath):
    
    if resPath:
        pdfTarget = os.path.join(resPath, 'pdf/', '*.pdf')
        pdfList = glob.glob(pdfTarget)

    imgList = []
    for pdf in pdfList:
        pdf_fn = re.split(r"\.|\/", pdf)[-2] # os.sep
        img_dir = os.path.join(resPath, pdf_fn)
        imgs = glob.glob(img_dir)
        imgList.append(imgs)
    
    return pdfList, imgList

def get_pdfs(pdfDir):
    
    os.chdir(pdfDir)
    pdf_list = sorted(glob.glob(os.path.abspath('.')+'**/*.pdf', recursive=True))

    return pdf_list

def get_imgs(imgDir):
    
    os.chdir(imgDir)
    img_list = sorted(glob.glob(os.path.abspath('.')+'**/*.jpg', recursive=True))
    
    return img_list

def pdf_to_img(pdf_list, PJT_DIR):
    
    for pdf in pdf_list:
        
        fn = pdf.split("\\")[-1]
        fn = fn.split(".")[0]
        
        dn = os.path.join(PJT_DIR, './pdftoimg')
        
        if not os.path.exists(dn):
            os.makedirs(dn)
        
        images = convert_from_path(pdf, 
                                   fmt='jpg', 
                                   output_folder=dn, 
                                   dpi=300, 
                                   poppler_path='C:\\poppler-22.04.0\\Library\\bin',
                                   output_file = fn)

'''
get gt_boxes & pdf page size info concurrently 
'''

def get_gt_boxes(pdf_list):
    
    docs_info = []
    skip_list = []
    
    for pdf in pdf_list:
        
        # doc_info = {}
        
        pdf_fn = re.split(r"\.|\/", pdf)[-2] # os.sep
        
        # doc_info["pdf_fn"] = pdf_fn

        fp = open(pdf, 'rb')
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        
        try:
            pages = PDFPage.get_pages(fp, check_extractable=True)
        except:
            # 어차피 이 file에서는 아무것도 안 나옴... 
            print(pdf_fn)

        pages_info = []
        for page_idx, page in enumerate(pages):
            
            page_width = page.mediabox[2]
            page_height = page.mediabox[3]

            interpreter.process_page(page)
            layout = device.get_result()
            
            textlines = []
            for lobj in layout:
                if isinstance(lobj, LTTextBoxHorizontal):
                    for line in lobj:
                        if isinstance(line, LTTextLineHorizontal):
                        # x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                            text = line.get_text()
                            x0, y0, x1, y1 = line.bbox
                            new_y0 = page_height-y0
                            new_y1 = page_height-y1
                            
                            textlines.append({
                                "transcription": text,
                                "points":[[x0, new_y0], [x1, new_y1]]
                                })
                            # print("text: ", text, "coor_orig: ", line.bbox, "new_orig: ", [[x0, new_y0], [x1, new_y1]])
            if len(textlines) == 0:
                print("{}'s {}th page is scanned pdf".format(pdf_fn, page_idx))
                # pdf to img file name 지정 방식에 맞게끔 filename 만들어서 append 
                # skip_list.append("")

            pages_info.append({
                "page_size": (page_width, page_height),
                "textlines": textlines
            })
            
        docs_info.append({
            "pdf_fn": pdf_fn,
            "pages_info": pages_info
        })

    return docs_info


def fit_to_img(docs_info):
    # docs_info, img_list 가지고 이제 transcript 파일 만들기
    
    pass


# def draw_bboxes(pdf_list, img_list):
    
#     for img in img_list:
        
#         img_fn = re.split(r"\.|\/", img)[-2]

if __name__ == "__main__":
    
    # 현재 프로젝트 디렉토리 
    PJT_DIR = os.getcwd()
    
    # get pdf files list
    PDF_PATH = "C:\\Exception\\Downloads\\document_crawler\\selenium_alert_handled"
    pdf_list = get_pdfs(PDF_PATH)
    
    a = get_gt_boxes(pdf_list)
    quit()
    # pdf_to_img(pdf_list, PJT_DIR)

    # # img_path = "C:\\Users\\ejpark\\Desktop\\generate_ocr_dataset\\pdftoimg"
    # # img_list = get_imgs(img_path)
    # # os.chdir()이 있기 때문에 이거 하면 안 됨... 
    
    # docs_info = get_gt_boxes(pdf_list)
    # # draw_bboxes(pdf_list, img_list)

