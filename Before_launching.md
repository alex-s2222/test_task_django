# Перед запуском 
Перед запуском нужно создать виртуальную среду:

<code>python3 -m venv <name_venv>
</code>

Активировать виртуальную среду:

<code>source <name_venv>/bin/activate (Mac)
<name_venv>\Scripts\activate.bat (Windows)
</code>


Установить библиотеки:

<code>asgiref             3.6.0
crispy-bootstrap5   0.7
Django              4.1.7
django-crispy-forms 2.0
mysqlclient         2.1.1
Pillow              9.4.0
pip                 22.3.1
setuptools          65.5.0
sqlparse            0.4.3
</code>

В настройках проекта изменить:
- [settings](https://github.com/alex-s2222/test_task/blob/main/booking/booking/settings.py)

В DATABASES - изменить на свои настройки Базы данных <br>
В SECRET_KET - изменить на свой персональный ключ