import pymorphy2
import tkinter as tk
import copy
from ui import MainWindowClass
from gensim.models import Word2Vec
from thems import PSNTList
from vector_math import *

model = Word2Vec.load("./word2vec.model")
SIZE = 100


PSNTList_ = copy.deepcopy(PSNTList)
PSNTVectors = copy.deepcopy(PSNTList)
morph = pymorphy2.MorphAnalyzer()#Нормализатор
for letter in PSNTList:# Проходим по каждой букве
    for them in range(len(PSNTList[letter])):# Проходим по каждой теме
        words = PSNTList[letter][them].lower()
        words ="".join([i for i in words if i in ("йцукенгшщзхъэждлорпавыфячсмитьбюё ")])
        words = words.split() # Разделяем тему на слова
        count = 0 # Счетчик для найденных слов
        sum_word = [0 for i in range(SIZE)] # Сумма векторов
        for word in words:# проходим по каждолму слову
            try:# Пробуем получить для него вектор
                ans = model.wv[morph.parse(word)[0].normal_form]
            except:# Если вектор получить не вышло то мы не будем увеличивать счетчик
                continue
            sum_word = sum_v(ans, sum_word)
            count+=1
        PSNTVectors[letter][them] = divide(sum_word,count)# Получаем среднее значения деля на число вошедших слов


def calc(text_label,input_string,res):
    input_vector = [0] * SIZE
    words = input_string.split()
    count = 0
    for word in words:
        try:
            ans = model.wv[morph.parse(word)[0].normal_form]
        except:
            continue
        input_vector = sum_v(ans, input_vector)
        count += 1
    input_vector = divide(input_vector, count)
    title=""
    print(f"input vector :{input_vector}")
    ANS_LETTER,ANS_VAL = "a",0
    for i,letter in enumerate(PSNTVectors):
        print(letter,end=":")
        max_v = 0
        for j,v in enumerate(PSNTVectors[letter]):
            max_v = max(max_v,cos(v,input_vector))
            if(max_v>ANS_VAL):
                ANS_VAL = max_v
                ANS_LETTER = letter
                title = PSNTList_[letter][j]
        print(f"\t{max_v}")
        text_label[i].set(f"{letter}:{max_v}")
    res.delete(1.0, tk.END)
    res.insert(1.0, f"{ANS_LETTER}:{title}")
a = MainWindowClass(calc)
a.start()
