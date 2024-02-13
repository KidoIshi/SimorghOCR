# SimorghOCR

SimorghOCRは、ペルシア語に特化した光学文字認識（OCR）アプリケーションです。

## 特徴

- Tesseract OCRおよびEasyOCR
- 画像ファイル（JPEG、PNG、BMP、TIFFなど）とPDFドキュメントの両方を処理可能
- CustomTkinterで構築されたユーザーフレンドリーなGUI
- ペルシア語（ファルシ）に焦点を当てた言語サポート
- 抽出されたテキストを簡単な編集とフォーマットのためにMicrosoft Word（DOCX）形式に直接変換

## インストール

SimorghOCRをインストールする前に、アプリケーションで使用される主要なOCRエンジンの1つであるTesseract OCRの事前インストールされているが必要です。[こちら](https://github.com/tesseract-ocr/tesseract)からTesseract OCRをダウンロードしてインストールしてください。

Tesseract OCRがインストールされたら、以下の手順でSimorghOCRをインストールしてください：

```bash
# リポジトリをクローン
git clone https://github.com/KidoIshi/SimorghOCR.git

# クローンしたディレクトリに移動
cd SimorghOCR

# 必要なPythonパッケージをインストール
pip install -r requirements.txt
# SimorghOCR
```
OCRエンジンを選びます<br>
画像またはPDFファイルをアップロードします<br>
OCR処理が完了すると、抽出されたテキストがアプリケーションウィンドウに表示され、Wordドキュメントとしてダウンロードできます
## ライセンス
GNU GPL version 3
