
# Менеджер Poetry

[**Poetry**](https://python-poetry.org/) - это инструмент для управления зависимостями в Python проектах
(аналог встроенного pip). Он похож по функционалу на рассмотренный ранее `pipenv`.

**Poetry** позволяет эффективно управлять зависимостями и пакетами в Python. Он выполняет ту же роль, что и `setup.py`
или
`pipenv`, но обладает большей гибкостью и функциональностью. Вы можете объявить библиотеки, от которых зависит ваш
проект,
в файле `pyproject.toml`. После этого `poetry` будет устанавливать или обновлять их по требованию. Кроме того, этот
инструмент позволяет инкапсулировать рабочий проект в изолированное окружение. Наконец, вы можете использовать `poetry`
для прямой публикации вашего пакета на `Pypi`.

:::info

Использование файлов `pypoproject.toml` и `poetry.lock` делает его похожим на Node Package Manager (`npm`) для Node.js.

:::

## Установка

Установить `poetry` можно
через [Windows (Powershell)](https://python-poetry.org/docs/#installing-with-the-official-installer)

```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

:::note

Poetry можно установить вручную с помощью `pip` и модуля `venv`. Поступая таким образом, вы, по сути, выполните шаги,
выполняемые официальным установщиком.

```shell
python3 -m venv $VENV_PATH
$VENV_PATH/bin/pip install -U pip setuptools
$VENV_PATH/bin/pip install poetry
```

Poetry будет доступен по адресу `$VENV_PATH/bin/poetry` и может быть вызван напрямую или по символической ссылке в
другом
месте. Чтобы удалить Poetry, просто удалите весь каталог `$VENV_PATH`.

:::

## Создание нового проекта

После установки мы можем создавать "poetry-проекты" с помощью команды
`poetry new <имя проекта>`.

Предположим, что мы ввели команду `poetry new solution`, тогда мы получим следующую структуру каталогов:

```text
├── solution
│   └── __init__.py
├── pyproject.toml
├── README.rst
└── tests
    ├── __init__.py
    └── test_solution.py
```

Мы видим, что в проекте `solution` был создан одноимённый пакет — директория
`solution` с соответствующим `__init__.py`. Любой poetry-проект всегда содержит
хотя бы один пакет.

Кроме пакета `solution`, в проекте уже есть пакет `tests` с первым тестом и мы должны понимать, что настоящие проекты
всегда имеют тесты.

В файле `README.rst` должно быть описание проекта. Это файл формата
[reStructuredText](https://ru.wikipedia.org/wiki/ReStructuredText).

Как видим `Poetry` автоматически создал все необходимые файлы для будущего
пакета, но наибольший интерес представляет файл с названием `pyproject.toml`,
этот файл продвинутая альтернатива `requirements.txt`.

Содержимое файла `pyproject.toml` будет следующее:

```ini
[tool.poetry]
name = "solution"
version = "0.1.0"
description = ""
authors = ["FirstName LastName <youremail@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

Формат файла [TOML](https://github.com/toml-lang/toml). Раздел `tool.poetry`
предназначен для описания проекта: название, версия, краткая информация о
проекте и т.д. Далее следует `tool.poetry.dependencies`, именно здесь указаны
все `production` зависимости. Раздел `tool.poetry.dev-dependencies` предназначен
для зависимостей, которые используются во время разработки, например `pytest`
для тестов.

## Инициализация уже существующего проекта

Чтоб инициализировать `poetry`, в уже готовом проекте, надо выполнить команду:

```shell
poetry init
```

После будет запущен процесс опроса по подобию как ниже:

```shell
This command will guide you through creating your pyproject.toml config.

Package name [test_poetry]:  
Version [0.1.0]:  
Description []:  
Author [FirstName LastName <youremail@gmail.com>, n to skip]:  
License []:  

Would you like to define your main dependencies interactively? (yes/no) [yes]
You can specify a package in the following forms:
  - A single name (requests)
  - A name and a constraint (requests@^2.23.0)
  - A git url (git+https://github.com/python-poetry/poetry.git)
  - A git url with a revision (git+https://github.com/python-poetry/poetry.git#develop)
  - A file path (../my-package/my-package.whl)
  - A directory (../my-package/)
  - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Search for package to add (or leave blank to continue):

Would you like to define your development dependencies interactively? (yes/no) [yes]
Search for package to add (or leave blank to continue): 

Generated file

[tool.poetry]
name = "test_poetry"
version = "0.1.0"
description = ""
authors = ["FirstName LastName <youremail@gmail.com>"]

[tool.poetry.dependencies]
python = "3.10"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes]
```

Для активации виртуального окружения необходимо выполнить команду:

```shell
poetry shell
```

Но лучше инициализировать проект через **PyCharm**, чтобы в терминале мы
работали в виртуальном окружении автоматически.

![poetry](/img/poetry.png)

:::caution

Не забудьте указать параметр `Poetry executable`, чтобы **PyCharm** знал где установлен `poetry`

:::

## Основные команды

Чтобы добавить к проекту зависимость в виде `aiosqlite`. Необходимо выполнить
команду

```shell
poetry add aiosqlite
```

**Poetry** при этом автоматически создаст виртуальное окружение если оно не было
создано. Все окружения находятся по пути `~/.cache/pypoetry/virtualenvs`

После команды в файле `pyproject.toml` должна появится запись в разделе
зависимостей `tool.poetry.dependencies`

Чтобы добавить зависимость для разработки, достаточно указать флаг `--dev`:

```shell
poetry add pytest --dev
```

Этот пакет должен попасть в `pyproject.toml` в раздел
`tool.poetry.dev-dependencies]`

Чтобы удалить зависимость, нужно выполнить команду `remove`:

```shell
poetry remove aiosqlite
```

Если надо подтянуть существующий проект и установить его зависимости для локальной разработки, вводим команду:

```shell
poetry install
```

Если при запуске установки поэзии уже есть файл `poetry.lock`, а также файл
`pyproject.toml`, это означает, что вы выполнили команду установки ранее, либо кто-то еще в проекте выполнил команду
установки и зафиксировал файл `poetry.lock`.

В любом случае запуск установки при наличии файла `poetry.lock` разрешает и устанавливает все зависимости, которые вы
указали в `pyproject.toml`, но **Poetry** использует точные версии, перечисленные в `poetry.lock`, чтобы гарантировать,
что
версии пакетов непротиворечивы для всех, кто работает над вашим проектом.

Обновить все зависимости к последним версиям:

```shell
poetry update
```

Чтобы просмотреть все доступные пакеты, вы можете использовать команду `show`.

```shell
poetry show
```

## Версии зависимостей

При установке пакета можно указать точную версию проекта, например:

```ini
[tool.poetry.dependencies]
pygame = "2.1.0"
```

Но иногда есть необходимость указать диапазон версий пакета, чтобы получать обновления, в таком случае есть несколько
способов указать диапазон, с помощью специальных символов `^~*`:

```ini
[tool.poetry.dependencies]
pygame = "^2.1"
pygame = "~2.1"
pygame = "2.1.*"
pygame = "*"
```

Вот какие диапазоны принимают данные префиксы версий при установке или обновлении такой зависимости:

| Зависимость | Минимальная версия | Максимальная версия |
|-------------|--------------------|---------------------|
| ^1.2.3      | от 1.2.3           | до 2.0.0            |
| ^1.2        | от 1.2.0           | до 2.0.0            |
| ^1          | от 1.0.0           | до 2.0.0            |
| ^0.2.3      | от 0.0.3           | до 0.0.4            |
| ~1.2.3      | от 1.2.3           | до 1.3.0            |
| ~1.2        | от 1.2.0           | до 1.3.0            |
| ~1          | от 1.0.0           | до 2.0.0            |
| *           | от 0.0.0           | до  последней       |
| 1.*         | от 1.0.0           | до 2.0.0            |
| 1.2.*       | от 1.2.0           | до 1.3.0            |

Для более подробного изучения проекта посетите страницу
[Poetry](https://python-poetry.org/docs/).
