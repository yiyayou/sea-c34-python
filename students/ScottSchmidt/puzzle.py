# coding=utf-8
import sys

lang = u"English"


if (len(sys.argv) > 1):
    lang = sys.argv[1]
    verify = {u"English": u"Hello, world!", u"Arabic": u"مرحبا بالعالم!",
              u"Spanish": u"Hola Mundo!", u"Chinese": u"你好世界！",
              u"Danish": u"Hej, verden!", u"Dutch": u"Hallo wereld!",
              u"French": u"Bonjour le monde!", u"German": u"Hallo Welt!",
              u"Irish": u"Dia duit, domhan!", u"Italian": u"Ciao mondo!",
              u"Japanese": u"こんにちは世界！", u"Korean": u"안녕하세요, 세계!"}

    for word in verify:
        if lang == word:
            print verify[word]

print lang

# Add elif branches here to handle other languages!

# else:
#     raise RuntimeError(u"This shouldn't happen!")
