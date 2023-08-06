# netbox-plugin-unacceptable-events


```bash
pip3 install netbox-unacceptable-events-users-computers
```



Добавить в файле netbox/netbox/configuration.py

```
PLUGINS = [
    'ptueventsuserscomputers'
]
```

В командной строке
```
./manage.py migrate
```

Перезапустить сервер netbox.