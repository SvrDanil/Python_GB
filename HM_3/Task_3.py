# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import string

text = "Солнечное затмение — астрономическое явление, при котором Луна полностью или частично покрывает Солнце на некоторое время при наблюдении с определённой части Земли. " \
       "Солнечные затмения происходят только в новолуние, причём из-за наклона орбиты Луны к плоскости эклиптики они случаются не в каждое новолуние, а только от 2 до 5 раз в год, " \
       "когда Луна в новолунии оказывается вблизи узла своей орбиты. " \
       "Солнечные затмения делятся на полные, частные, кольцеобразные и гибридные. При полном затмении где-либо на Земле можно наблюдать полное покрытие Солнца Луной,  " \
       "при частном полного покрытия не наблюдается нигде. При кольцеобразном затмении полного покрытия также не происходит, но, в отличие от частного затмения, где-либо на Земле можно наблюдать, " \
       "как Луна оказывается на фоне диска Солнца и не может закрыть его целиком, имея меньший угловой размер, чем у Солнца. При гибридном затмении на Земле есть области, " \
       "где в какой-то момент затмение наблюдается как кольцеобразное, а в другое время в других областях — как полное." 
       
      
text = text.translate(str.maketrans('', '', string.punctuation)).lower().split()

res = {}
for letter in text:
    res[letter] = res.get(letter, 0) + 1

srt = [i for i, j in sorted(res.items(), key=lambda item: item[1], reverse=True)[:10]]
print(srt)