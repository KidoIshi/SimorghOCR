# SimorghOCR

SimorghOCRは、画像とPDFファイルからテキストを効率的に抽出するために設計されたシンプルでありながら強力な光学文字認識（OCR）アプリケーションです。ユーザーフレンドリーなインターフェイスで構築され、Tesseract OCRやEasyOCRなどの先進的なOCR技術を統合して、ペルシア語（ファルシ）を含む幅広い言語でテキスト認識の高い精度を提供します。

## 特徴

- 複数のOCRエンジンに対応：Tesseract OCRおよびEasyOCR。
- 画像ファイル（JPEG、PNG、BMP、TIFFなど）とPDFドキュメントの両方を処理可能。
- より良いユーザー体験のためにCustomTkinterで構築されたユーザーフレンドリーなGUI。
- ペルシア語（ファルシ）に焦点を当てた言語サポートで、他の言語への拡張が可能。
- 抽出されたテキストを簡単な編集とフォーマットのためにMicrosoft Word（DOCX）形式に直接変換。

## インストール

SimorghOCRをインストールする前に、アプリケーションで使用される主要なOCRエンジンの1つであるTesseract OCRがシステムにインストールされている必要があります。[こちら](https://github.com/tesseract-ocr/tesseract)からTesseract OCRをダウンロードしてインストールしてください。

Tesseract OCRがインストールされたら、以下の手順でSimorghOCRをインストールしてください：

```bash
# リポジトリをクローン
git clone https://github.com/KidoIshi/SimorghOCR.git

# クローンしたディレクトリに移動
cd SimorghOCR

# 必要なPythonパッケージをインストール
pip install -r requirements.txt
# SimorghOCR
