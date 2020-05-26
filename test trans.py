from googletrans import Translator
translator = Translator()
tr_results = translator.translate('안녕하세요')
a=tr_results.text
print(a)
