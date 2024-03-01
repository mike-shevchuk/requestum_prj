 

# Test project
  https://docs.google.com/document/d/1O2iWCAk1TYcVcK4jAB1xK8p4AA2Rz92UrfftCta4vHw/edit#heading=h.aow0jx8t0f1q


  * Опис
  Необхідно написати сервіс, якому можна передати урл репозиторію на гітхаб,
  і який поверне для нього топ 5 проектів з найбільшим числом спільних контриб'юторів.


  Приклади роботи сервера
  https://github.com/encode/starlette
  ![[Pasted image 20240220180532.png]]


  *  Не орієнтуйтеся на результати в прикладі, оскільки список контриб'юторів 
  динамічно змінюється і, найімовірніше, не збігатиметься з наведеним у цьому прикладі.


  Вимоги
  * [ ] У сервісу має бути елементарний веб-інтерфейс для тестування.
  * [ ] Сервіс має конфігуруватися через змінні середовища.
  * [ ] До рішення має додаватися докер файл і docker compose для запуску.
   
  Критерії оцінки
  * [ ] Відповідність завданню 
  * [ ] Ефективність рішення з алгоритмічної точки зору
  * [ ] Лаконічність і читабельність коду
  * [ ] Відповідність стилю коду основним угодам, прийнятим у ком'юніті



# Tech stack 
  I use pyenv-virtualenv and python 3.12.1


  ```bash
  pyenv install 3.12.1
  pyenv virtualenv 3.12.1 requestum_prj
  pyenv local requestum_prj

  pip install -r requirements.txt


  dotenv set GIT_TOKEN ${{ secrets.GIT_TOKEN }}

  python3 main.py
  ```

  ## Docker setup
    You need docker and docker compose installed on your system

    After this go to Dockerfile and set your GITHUB_TOKEN

## Issue

  If you get this message

  ```python
  "message":"API rate limit exceeded for 46.219.224.86. 
  (But here\'s the good news: Authenticated requests get a higher rate'
  ```

  it is mean that you go under limit, you need to change token or try again later

