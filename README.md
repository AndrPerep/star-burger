# Сайт доставки еды Star Burger

Это сайт сети ресторанов Star Burger. Здесь можно заказать превосходные бургеры с доставкой на дом.

![скриншот сайта](https://dvmn.org/filer/canonical/1594651635/686/)


Сеть Star Burger объединяет несколько ресторанов, действующих под единой франшизой. У всех ресторанов одинаковое меню и одинаковые цены. Просто выберите блюдо из меню на сайте и укажите место доставки. Мы сами найдём ближайший к вам ресторан, всё приготовим и привезём.

На сайте есть три независимых интерфейса. Первый — это публичная часть, здесь можно выбрать блюда из меню, и быстро оформить заказ без регистрации и SMS.

Второй интерфейс предназначен для менеджера. Здесь происходит обработка заказов. Менеджер видит поступившие новые заказы и контакты этих клиентов. Он выбирает ближайший ресторан, где будет готовиться заказ и откуда произойдет доставка, затем созванивается с клиентом, чтобы подтвердить заказ. Подтверждённые заказы менеджер передаёт непосредственно в ресторан на исполнение.

Третий интерфейс — это админка. Он используется программистами при разработке сайта. Также админкой пользуется менеджер, когда надо обновить меню Star Burger.

## Как запустить dev-версию сайта

Для запуска сайта нужно запустить **одновременно** бэкенд и фронтенд, в двух терминалах.

### Как собрать бэкенд

Скачайте код:
```sh
git clone https://github.com/devmanorg/star-burger.git
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `parcel` установлен и корректно настроен. Запустите его в командной строке :
```sh
python --version
```
Возможно вмето `python` нужно использовать `python3`, это зависит от операционной системы и от того, установлена ли у вас вторая версия Python. Версия Python должна быть на ниже 3.6.

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:
- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`

Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

Создайте базу данных и отмигрируйте её следующей командой:
```sh
python manage.py migrate
```

Запустите сервер:
```sh
python manage.py runserver
```

По адресу [127.0.0.1](http://127.0.0.1/) в браузере должна отобразиться такая страница:

![](https://dvmn.org/filer/canonical/1594651900/687/)

После сборки, чтобы запустить сайт повторно, достаточно войти в виртуальное окружение и запустить сервер:
```sh
python manage.py runserver
```

### Собрать фронтенд

**Откройте новый терминал**. `runserver` выключать не надо, все операции ниже нужно проделать отдельно, в новом терминале. Для запуска сайта нужно запустить **одновременно** бэкенд и фронтенд, в двух терминалах.

[Установите NodeJS](https://nodejs.org/en/), если этого ещё не сделали.

Проверьте, установился-ли Node.js и его пакетный менеджер. Терминал выводет их версии:
```sh
node --version
npm --version
```

В каталоге проекта запустите
```sh
npm install --dev
```

Установите [parcel](https://parceljs.org/). Это упаковщик веб-приложений, наподобие [Webpack](https://webpack.js.org/), но не требует настроек для упаковки проекта:

```sh
npm install -g parcel-bundler
```

Проверьте, что `parcel` установлен. Запустите его в командной строке:

```sh
parcel --version
```

Запустите сборку фронтенда. Parcel будет работать в фоне и следить за изменениями в JS-коде:

```sh
parcel watch bundles-src/index.js -d bundles --public-url="./"
```

Parcel будет следить за файлом `index.js` в каталоге `bundles-src`, а также за всеми теми файлами, что импортируются внутри этого `index.js`. Parcel будет собирать все импортированные мелкие файлы в большие бандлы `bundles/index.js` и `bundles/index.css`. Весь каталог `bundles` предназначен исключительно для результатов сборки фронтенда и потому исключён из репозитория с помощью `.gitignore`.

**Сбросьте кэш браузера <kbd>Ctrl-F5</kbd>.** Браузер при любой возможности старается кэшировать файлы статики: CSS, картинки и js-код. Порой это приводит к странному поведению сайта, когда код уже давно изменился, но браузер не знает и продолжает использовать старую закэшированную версию. В норме Parcel решает эту проблему самостоятельно. Он следит за  пересборкой фронтенда и предупреждает JS-код в браузере о необходимости подтянуть свежий код. Но если вдруг у вас что-то идёт не так, то начните со сброса браузерного кэша, жмите <kbd>Ctrl-F5</kbd>.


## Как запустить prod-версию сайта

Собрать фронтенд:

```sh
parcel build bundles-src/index.js -d bundles --public-url="./"
```


### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны следующие переменные:
TODO: переменные окружения

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org). За основу был взят код проекта [FoodCart](https://github.com/Saibharath79/FoodCart).

Где используется репозиторий:

- Второй и третий урок [учебного модуля Django](https://dvmn.org/modules/django/)
