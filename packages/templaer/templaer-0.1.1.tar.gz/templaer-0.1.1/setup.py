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
    'version': '0.1.1',
    'description': '',
    'long_description': '# Templaer\n\nTemplaer - универсальный CLI шаблонизатор конфигурационных файлов, основанный на `Jinja2`.\n\n## Установка\n\n1. Установить `templaer`\n\n    ```bash\n    pip install templaer\n    ```\n\n2. Получить подсказку по CLI\n\n    ```bash\n    python -m templaer\n    ```\n\n## Примеры CLI\n\n- Поиск в указанной директории всех файлов с которые оканчиваются на `.tpl`, и сборка этих файлов.\n\n    ```bash\n    python -m templaer -c context.json -d Папка  \n    ```\n\n- Собрать указанные файлы.\n\n    ```bash\n    python -m templaer -c context.json -f Файл1.conf.tpl Файл2.tpl\n    ```\n\n## Основы шаблонов на Jinja2\n\n### Тернарный условный оператор\n\nВ этом примере показано как в зависимости от переменной `DEBUG`, будет поставлено значение из переменной `PORT_D` или `PORT_R`.\n\n1. Содержание файла `context.json`:\n\n    ```json\n    {\n        "DEBUG": false,\n        "PORT_D": 8080,\n        "PORT_R": 80\n    }\n    ```\n\n2. Содержание файла `ЛюбойФайл.conf.tpl`:\n\n    ```nginx\n    server {\n        listen {{ PORT_D if DEBUG else PORT_R }};\n        server_name "localhost";\n\n        location / {\n            default_type text/html;\n            return 200 \'ok\';\n        }\n    }\n    ```\n\n3. Соберем файл используя команду:\n\n    ```bash\n    python -m templaer -c context.json -f ЛюбойФайл.conf.tpl\n    ```\n\n4. В итоге создастся(или перезапишитесь) новый файл `ЛюбойФайл.conf`, с содержанием:\n\n    ```nginx\n    server {\n        listen 80;\n        server_name "localhost";\n\n        location / {\n            default_type text/html;\n            return 200 \'ok\';\n        }\n    }\n    ```\n',
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
