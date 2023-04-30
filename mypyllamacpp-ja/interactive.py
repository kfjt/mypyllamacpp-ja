from sys import argv

from pyllamacpp.model import Model
import argostranslate.package
import argostranslate.translate


JA_EN = ('ja', 'en')
EN_JA = ('en', 'ja')

def install_package(from_code, to_code):
  # Download and install Argos Translate package
  argostranslate.package.update_package_index()
  available_packages = argostranslate.package.get_available_packages()
  package_to_install = next(
      filter(
          lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
      )
  )
  argostranslate.package.install_from_path(package_to_install.download())

def translate(orignalText, from_code, to_code):
  translatedText = argostranslate.translate.translate(orignalText, from_code, to_code)
  return translatedText

def new_text_callback(text):
    print(text, end="", flush=True)

def translatedPrompt():
  model = Model('/gpt4all-lora-quantized-ggjt.bin', n_ctx=512)
  while True:
    try:
      prompt_ja = input('You: ')
      if prompt_ja == '':
        continue
      prompt_en = translate(prompt_ja, *JA_EN)
      new_text_en = model.generate(prompt_en, n_predict=55, new_text_callback=new_text_callback, n_threads=8)
      new_text_ja = translate(new_text_en, *EN_JA)
      print(f'AI: {new_text_ja}')
    except KeyboardInterrupt:
      break

def main():
  install_package(*JA_EN)
  install_package(*EN_JA)
  translatedPrompt()

if __name__ == '__main__':
  main()
