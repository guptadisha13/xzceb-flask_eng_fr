from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source='english', target='french').translate(text = englishText)
    return frenchText

def frenchToEnglish(frenchT):
    englishT = MyMemoryTranslator(source='french', target='english').translate(text = frenchT)
    return englishT
