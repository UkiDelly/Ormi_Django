### 필요한 모듈 설치

pip install djangorestframework
pip install django-cors-headers
pip install django-rest-auth

---

### settings.py

```python
INSTALLED_APPS = [
  ...,
   <!-- django lib app 추가 -->
  'rest_framework',
  'rest-auth',
  'corsheaders',
  ...,
]

CORS_ORIGIN_ALLOW_ALL=True
CORS_ALLOW_CREDENTIALS=True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', #최상단 추가
    ...,
]
```

---

# DRF(Django Rest Framework) 테스트

blog > views.py
