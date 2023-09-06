from django.conf import settings
from django.core.cache import cache

class CacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 200 and request.path.startswith(settings.STATIC_URL):
            # Если это запрос статического файла и он успешный, кэшируем его в памяти
            cache.set(request.path, response.content)

        if request.method == 'GET':
            # Если это GET-запрос, пытаемся получить файл из кэша
            cached_content = cache.get(request.path)
            if cached_content:
                # Если файл есть в кэше, отдаем его из памяти
                response.content = cached_content

        return response