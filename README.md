<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg" alt="996.icu" /></a>[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
# Extract-text-from-image-via-python
This project is using Python Tesseract OCR library, python version 3.7

Make sure you have already pre-install Tesseract library and relevant language version of trained data files.
Thanks to Tesseract community, you may get trained file via this link https://github.com/tesseract-ocr/tessdata

Sometimes it can't read the words directly, we need to perform simple image processing to invert image color before extract those text from an image.

Before invert
--------------
![alt text](https://github.com/arixlee/Extract-text-from-image-via-python/blob/master/trip%20cost.PNG)
<br>![alt text](https://github.com/arixlee/Extract-text-from-image-via-python/blob/master/cn_text.PNG)

After invert
--------------
![alt text](https://github.com/arixlee/Extract-text-from-image-via-python/blob/master/INVT_trip%20cost.png)
<br>![alt text](https://github.com/arixlee/Extract-text-from-image-via-python/blob/master/INVT_cn_text.png)

End result
----------
![alt text](https://github.com/arixlee/Extract-text-from-image-via-python/blob/master/end%20result.PNG)


Just a simple python code, hope you enjoy~ peace
