import traceback
import logging
from django.http import HttpResponse

logger = logging.getLogger("main")


class LoggingVisit:
    def __init__(self, get_responce):
        self._get_responce = get_responce

    def __call__(self, request):
        if 'projects' in request.path:
            headers = request.headers
            user = None
            if request.user.is_authenticated:
                pass
            logger.info(f" Страница Проекты. Headers= {headers} ")
        responce = self._get_responce(request)
        return responce

    def process_exception(self, request, exception):
        tb = traceback.format_exc()
        logger.error(f"Ошибка {tb}")
        return HttpResponse("Ошибка")
