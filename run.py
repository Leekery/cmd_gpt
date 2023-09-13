import g4f
import sys
import os

sys.stderr = open(os.devnull, 'w')

response_accumulator = ""  # Переменная для накопления ответов

# Создаем список для хранения сообщений
messages_history = []
print('Для выхода прописать - exit. Для продолжения генерации - продолжи')

while True:
   user_input = input('User: ')
   if user_input.lower() == 'exit':
      break

   if "продолжи" in user_input.lower() and response_accumulator:
      # Если пользователь сказал "продолжи" и есть недописанный ответ модели,
      # добавляем предыдущие сообщения в историю перед созданием нового запроса
      messages_history.append({"role": "user", "content": user_input})
      messages_history.extend([{"role": "user", "content": msg} for msg in response_accumulator.split('\n') if msg.strip()])

   else:
      # Добавляем новое сообщение в историю сообщений
      messages_history.append({"role": "user", "content": "Язык ответа по умолчанию: Русский. " + user_input})

   response = g4f.ChatCompletion.create(
      model="gpt-3.5-turbo",
      provider=g4f.Provider.DeepAi,
      messages=messages_history,  # Передаем всю историю сообщений
      stream=True,
   )

   response_accumulator = ""  # Сбрасываем хранилище перед обработкой нового ответа
   print('Model: ', end='')
   for message in response:
      print(message, end='')
   print()

#Список рабочих моделей
# AItianhu
# Acytoo
# Ails
# Ylokh
# Aivvm
# ChatBase
# CodeLinkAva
# DeepAi
# Raycast
# Yqcloud
# Vitalentum