from emoji import *

LSD_start = f"""
<b>[{star}] LSD Assistant
[{code}] Автор: @kwiken | @Unsupported_characters


[{menu}] Меню</b>

[{toch}] <code>LSD.start</code> — Старт.
[{toch}] <code>LSD.help</code> — Помощь.
[{toch}] <code>LSD.ping</code> — Задержка.
[{toch}] <code>LSD.wiki</code> — Wikipedia.
[{toch}] <code>LSD.rand</code> — Рандом.
[{toch}] <code>LSD.clear</code> — Очищает все сообщения. (Смотреть инструкцию!)
[{toch}] <code>LSD.dice</code> — Отправляет dice emoji.
[{toch}] <code>LSD.ch</code> — Отправляет сообщения в канал.
[{toch}] <code>LSD.info</code> — Информация.
[{toch}] <code>LSD.mute</code> — Мут.
"""

LSD_help = f"""
<b>[{star}] Помощь
[{code}] Автор: @kwiken | @Unsupported_characters


[{menu}] Использование:</b>

[{toch}] <code>LSD.help<команда></code> — Инструкция к <команда>.
"""





LSD_ping = f"""
<b>[{star}] PING
[{code}] Автор: @kwiken | @Unsupported_characters</b>

[{menu}] <b>[]</b> ms
"""

LSD_wiki = f"""
<b>[{star}] Wikipedia
[{code}] Автор: @kwiken | @Unsupported_characters</b>

[{menu}] Поисковой запрос — <X>

[{toch}] <Заголовок статьи> — <a href="https://www.wikipedia.org/">Читать полностью</a>
"""

LSD_wiki_error1 = f"""
<b>[{star}] Wikipedia
[{code}] Автор: @kwiken | @Unsupported_characters</b>

[{menu}] Ошибка

[{toch}] Укажите поисковой запрос после LSD.wiki
[{skrep}] Пример: <code>LSD.wiki Telegram</code>
"""

SD_wiki_error2 = f"""
<b>[{star}] Wikipedia
[{code}] Автор: @kwiken | @Unsupported_characters</b>

[{menu}] Ошибка

[{toch}] Результатов не найдено
"""

LSD_wiki_error3 = f"""
<b>[{star}] Wikipedia
[{code}] Автор: @kwiken | @Unsupported_characters</b>

[{menu}] Ошибка

[{toch}] Страница не найдена
"""

LSD_wiki_error4 = f"""
<b>[{star}] Wikipedia
[{code}] Автор: @kwiken | @Unsupported_characters</b>

[{menu}] Ошибка

[{toch}] []
"""

LSD_wiki_error5 = f"""
<b>[{star}] Wikipedia
[{code}] Автор: @kwiken | @Unsupported_characters</b>

[{menu}] Ошибка

[{toch}] Уточните запрос: []
"""

LSD_rand = f"""
[{star}] Random
[{code}] Автор: @kwiken | @Unsupported_characters


[{menu}] Результат

[{toch}] <rand>
"""

LSD_rand_help = f"""
<b>[{star}] Random 
[{code}] Автор: @kwiken | @Unsupported_characters


[{menu}] LSD.rand</b>

[{toch}] <code>LSD.rand +num +1-100</code>
[{toch}] <code>LSD.rand +word +letter_f +8</code>
[{skrep}] +num — рандомное число. [!]
[{skrep}] +word — рандомное  слово. [!]
[{skrep}] (+num) +1-100 — Задает диапазон рандомного числа. (Тут от 1 до 100)
[{skrep}] (+word) +letter_f — Задает первую букву в рандомном слове (тут f)
[{skrep}] (+word) +8 — Задает количество букв в рандомном слове (тут 8)

[⭐️] [!] Обязательный аргумент.
"""


LSD_clear_me = f"""
[{star}] Clear
[{code}] Автор: @kwiken | @Unsupported_characters


[{menu}] Ваши сообщения очищены.
"""

LSD_clear_all = f"""
[{star}] Clear
[{code}] Автор: @kwiken | @Unsupported_characters


[{menu}] Все сообщения очищены.
"""

LSD_clear_wait = f"""
[{star}] Clear
[{code}] Автор: @kwiken | @Unsupported_characters


[{menu}] Ожидание подтверждения.

[{toch}] Ответьте на это сообщение «LSD.clear.YES» для подтверждения или «LSD.clear.NO» для отмены
"""

LSD_help_wiki = f"""
[{star}] Помощь 
[{code}] Автор: @kwiken | @Unsupported_characters


[{menu}] LSD.wiki

[{toch}] LSD.wiki X
[{skrep}] X — поисковой запрос
"""

LSD_help_rand = f"""
[{star}] Помощь 
[{code}] Автор: @kwiken | @Unsupported_characters


[{menu}] LSD.rand

[{toch}] LSD.rand +num +1-100
[{toch}] LSD.rand +word +letter_f +8
[{skrep}] +num — рандомное число. [!]
[{skrep}] +word — рандомное  слово. [!]
[{skrep}] (+num) +1-100 — Задает диапазон рандомного числа. (Тут от 1 до 100)
[{skrep}] (+word) +letter_f — Задает первую букву в рандомном слове (тут f)
[{skrep}] (+word) +8 — Задает количество букв в рандомном слове (тут 8)

[{star_two}] [!] Обязательный аргумент.
"""