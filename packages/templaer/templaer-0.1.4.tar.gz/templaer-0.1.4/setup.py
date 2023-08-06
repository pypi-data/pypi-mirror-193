# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['templaer']

package_data = \
{'': ['*']}

install_requires = \
['jinja2>=3.1.2,<4.0.0']

setup_kwargs = {
    'name': 'templaer',
    'version': '0.1.4',
    'description': '',
    'long_description': '# Templaer\n\n`Templaer` - универсальный CLI шаблонизатор конфигурационных файлов, основанный на `Jinja2`.\n\n- GitHub - <https://github.com/denisxab/templaer>\n- Pip - <https://pypi.org/project/templaer/>\n- Habr - <https://habr.com/ru/post/717996/>\n\n## Аналоги\n\nСуществует множество инструментов, основанных на `Jinja2`, которые можно использовать для шаблонизации конфигурационных файлов через `CLI`. Вот несколько примеров:\n\n- `j2cli`: это инструмент командной строки, который позволяет использовать Jinja2 для создания конфигурационных файлов. Он может принимать данные из файлов или стандартного ввода и применять их к шаблонам, включая конфигурационные файлы.\n- `cookiecutter`: это инструмент командной строки, который использует Jinja2 для генерации проектных шаблонов. Он также может использоваться для создания конфигурационных файлов. cookiecutter может быть установлен через pip.\n- `ansible`: это инструмент автоматизации, который использует Jinja2 для шаблонизации конфигурационных файлов и других файлов, используемых в автоматизации. ansible может быть установлен через pip.\n- `SaltStack`: это инструмент автоматизации, который использует Jinja2 для шаблонизации конфигурационных файлов и других файлов, используемых в автоматизации. SaltStack также может быть установлен через pip.\n- `mustpl` : <https://habr.com/ru/post/684898/>\n\nЯ создал `Templaer` потому что им удобнее пользоваться, и так как он на `Python`, его можно гибко кастомизировать. Если вам нравиться использовать другие шаблонизаторы конфигураций, то используйте их.\n\n## Установка\n\n1. Установить `templaer`\n\n    ```bash\n    pip install templaer\n    ```\n\n2. Получить подсказку по `CLI`\n\n    ```bash\n    python -m templaer\n    ```\n\n> Можете создать алиас в `.bashrc`/`.zshrc` для этой команды\n>\n> ```bash\n> alias templaer="python -m templaer"\n> ```\n\n## Примеры CLI\n\nВ файле `context.json` хранятся данные для шаблонов. В простом варианте это может быть словарь. Ключ - это имя переменной, значение ключа - это значение переменной.\n\n```json\n{\n    "DEBUG": false,\n    "PORT_D": 8080,\n    "PORT_R": 80\n}\n```\n\nПример шаблонного файла. Предлагаю для них указывать расширение `.tpl`. В данном случае этот файл называется `nginx.conf.tpl`. Новый собранный файл не будет иметь расширение `.tpl`, и будет называться `nginx.conf`.\n\n```nginx\nserver {\n    listen {{ PORT_R }};\n    server_name "localhost";\n\n    location / {\n        default_type text/html;\n        return 200 \'ok\';\n    }\n}\n```\n\n- Собрать указанные файлы (можно указывать несколько файлов).\n\n    ```bash\n    python -m templaer -c context.json -f Файл1.conf.tpl Файл2.tpl\n    ```\n\n- Поиск в указанной директории всех файлов, которые оканчиваются на .tpl, и сборка этих файлов (можно указывать несколько директорий).\n\n    ```bash\n    python -m templaer -c context.json -d Папка  \n    ```\n\n## Основы шаблонов на Jinja2\n\n### Тернарный условный оператор\n\nВ этом примере показано как в зависимости от переменной `DEBUG`, будет поставлено значение из переменной `PORT_D` или `PORT_R`.\n\n1. Содержание файла `context.json`:\n\n    ```json\n    {\n        "DEBUG": false,\n        "PORT_D": 8080,\n        "PORT_R": 80\n    }\n    ```\n\n2. Содержание файла `ЛюбойФайл.conf.tpl`:\n\n    ```nginx\n    server {\n        listen {{ PORT_D if DEBUG else PORT_R }};\n        server_name "localhost";\n\n        location / {\n            default_type text/html;\n            return 200 \'ok\';\n        }\n    }\n    ```\n\n3. Соберем файл используя команду:\n\n    ```bash\n    python -m templaer -c context.json -f ЛюбойФайл.conf.tpl\n    ```\n\n4. В итоге создастся(или перезапишитесь) новый файл `ЛюбойФайл.conf`, с содержанием:\n\n    ```nginx\n    server {\n        listen 80;\n        server_name "localhost";\n\n        location / {\n            default_type text/html;\n            return 200 \'ok\';\n        }\n    }\n    ```\n',
    'author': 'Denis',
    'author_email': 'pro-progerkustov@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
