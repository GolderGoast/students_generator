<h1>Скрипт для получения отчета по группам и студентам университета в форматах xlsx, pdf и json.</h1>

![Build status](https://github.com/GolderGoast/get_report_about_groups_and_students_in_university/actions/workflows/linters.yml/badge.svg?branch=master)

<h3>При запуске скрипта отредактировать файл [config.py](app/config.py):</h3>

GROUPS_COUNT - количество групп в университете;  
STUDENTS_IN_GROUP_COUNT - количество студентов в каждой группе;  
TYPE_REPORT - формат получаемого отчета, можно указать 'xlsx', 'pdf'' или 'json'

<h3>При запуске скрипта из консоли можно использовать флаги:</h3>

--gc после указать необходимо количество групп  
--sc после указать необходимо количество студентов в каждой группе  
--rtype после указать необходимый тип отчета, xlsx, pdf или json

Если какой-то флаг не указан, его значение будет браться из файла [config.py](app/config.py)
