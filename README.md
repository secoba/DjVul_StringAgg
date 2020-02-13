### Django CVE-2020-7471 SQLi

> CVE-2020-7471: Potential SQL injection via StringAgg(delimiter)
django.contrib.postgres.aggregates.StringAgg aggregation function was subject to SQL injection, using a suitably crafted delimiter.

### RUN

```bash
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

### 参考
- https://www.djangoproject.com/weblog/2020/feb/03/security-releases/
- https://code.djangoproject.com/ticket/30315
- https://docs.djangoproject.com/zh-hans/2.2/_modules/django/contrib/postgres/aggregates/general/