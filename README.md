# Ansible Collection - my_own_namespace.yandex_cloud_elk

## Описание
Коллекция содержит собственный модуль и роль, которые создают текстовый файл на хосте с заданным содержимым.

## Требования
- Ansible Core

## Состав коллекции

### Модуль: `my_own_module`
Создаёт текстовый файл по указанному пути и записывает в него заданный контент.

**Параметры**
- `path` (str, обязателен): путь к файлу.
- `content` (str, обязателен): содержимое файла.

**Пример**
```yaml
- name: Create file with content
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/my_own_module.txt
    content: hello world
```

### Роль: `my_own_role`
Обёртка над модулем с дефолтными параметрами.

**Defaults**
- `my_own_module_path`: `/tmp/my_own_module.txt`
- `my_own_module_content`: `hello world`

**Пример**
```yaml
- name: Test my_own_role
  hosts: localhost
  gather_facts: false
  roles:
    - role: my_own_role
```

## Локальная проверка
Используйте `inventory.ini`, `playbook.yml` (single task) или `playbook_role.yml` (роль).
