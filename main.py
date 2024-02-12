import customtkinter as ctk  # CustomTkinterをインポート
from tkinter import filedialog
from PIL import Image
import pytesseract
from docx import Document
from pdf2image import convert_from_path
import easyocr  # EasyOCRをインポート
import numpy as np

def main():
    ctk.set_appearance_mode("Light")

    # Tesseractのパスを設定
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # EasyOCRのリーダーを初期化（ここでペルシア語を指定）
    reader = easyocr.Reader(['fa'])  # 'fa'はペルシア語の言語コード

    def pdf_to_ocr(filename, ocr_engine):
        images = convert_from_path(filename)
        text = ""
        for image in images:
            text += perform_ocr(image, ocr_engine)
        return text

    def perform_ocr(input, ocr_engine):
        if not isinstance(input, Image.Image):
            input = Image.open(input)
        input = input.convert('L')
        if ocr_engine == "Tesseract":
            return pytesseract.image_to_string(input, lang='fas')
        elif ocr_engine == "EasyOCR":
            input_numpy = np.array(input)
            results = reader.readtext(input_numpy, detail=0)
            return "\n".join(results)
        else:
            return "未対応のOCRエンジンです"

    app = ctk.CTk()
    app.title("SimorghOCR")
    app.geometry("600x400")

    ocr_text = ctk.CTkTextbox(app, height=500, width=1000, fg_color="white")
    ocr_text.pack(pady=10)

    ocr_engines = ["Tesseract", "EasyOCR"]
    ocr_engine_selected = ctk.StringVar(value=ocr_engines[0])
    ocr_engine_dropdown = ctk.CTkOptionMenu(app, variable=ocr_engine_selected, values=ocr_engines)
    ocr_engine_dropdown.pack(pady=5)

    def upload_image():
        filename = filedialog.askopenfilename(title='ファイルを選択', filetypes=(("Supported Files", "*.pdf;*.png;*.jpg;*.jpeg;*.bmp;*.tif;*.tiff"),))
        if filename:
            if filename.lower().endswith('.pdf'):
                text = pdf_to_ocr(filename, ocr_engine_selected.get())
            else:
                text = perform_ocr(filename, ocr_engine_selected.get())
            
            ocr_text.delete("1.0", "end")
            ocr_text.insert("1.0", text)

    upload_button = ctk.CTkButton(app, text="ファイルをアップロード", command=upload_image, fg_color="#800080")
    upload_button.pack(pady=5)

    def download_word():
        doc = Document()
        doc.add_paragraph(ocr_text.get("1.0", "end"))
        save_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word ファイル", "*.docx")])
        if save_path:
            doc.save(save_path)
            ctk.CTkMessageBox.show_info("保存完了", f"ファイルが {save_path} に保存されました。")

    download_button = ctk.CTkButton(app, text="Wordファイルとしてダウンロード", command=download_word, fg_color="#800080")
    download_button.pack(pady=5)

    app.mainloop()

if __name__ == "__main__":
    main()
