# djago-admin

## [model](#1)
## [admin](#2)
---

<h1 id="1">
 model
</h1>

- ### model.py宣告一個類別，建立資料表用以寫到資料庫:
```py

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


```

- ### 執行makemigrations，更新紀錄用以寫入資料庫:
```shell

python manage.py makemigrations

```

- ### 執行migrate，根據紀錄，把model寫入資料庫:
```shell

python manage.py migrate

```

---

<h1 id="2">
 admin
</h1>

- ### 建立超級用戶用以登入admin:
```shell

python manage.py createsuperuser

```

- ### 註冊model:
```py

from django.contrib import admin
from .models import Post


admin.site.register(Post)

```