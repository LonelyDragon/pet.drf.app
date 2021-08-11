### Задача
Нужно реализовать HTTP сервис для голосования. Например, для выбора самого популярного покемона. UI не нужен, достаточно сделать JSON API сервис. Должна быть возможность:

- Создать новое голосование с разными вариантами ответов
- Отдать свой голос за какой-либо вариант
- Получить текущий результат голосования

### Реализовать методы:
- `POST /api/createPoll/` создать голосование c вариантами ответов
- `POST /api/poll/` проголосовать за конкретный вариант: <poll_id, choice_id>
- `POST /api/getResult/` получить результат по конкретному голосованию: <poll_id>

Структура и формат входных и выходных данных на ваше усмотрение.

### Описание идеального решения
- Задание декомпозировано, составлен иерархический список работ. Каждый пункт из этого списка может быть реализован за небольшое время.
- Составлена схема архитектуры со всеми сущностями и их связями в [Miro](https://miro.com)
- Код слабо связан, функции не имеют побочных эффектов
- История коммитов осмысленная. По ней видно, в каком порядке решалась задача.
- Покрытие тестами >70%

### Требования
- Язык: Go или Python 3.8+
- Результаты голосования должны храниться в базе данных. Мы обычно используем PostgreSQL и MongoDB, но можно выбрать любую другую.
- Код нужно выложить на github (просьба не делать форк этого репозитория, чтобы не плодить плагиат)
- Предоставить инструкцию по запуску приложения. В идеале (но не обязательно) – использовать контейнеризацию с возможностью запустить проект командой [`docker-compose up`](https://docs.docker.com/compose/)
- Сервис должен отвечать на 8000 порту
