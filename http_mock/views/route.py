from django.http import HttpResponse
import logging
import time

# Get an instance of a logger
logger = logging.getLogger(__name__)


def execute(request, **kwargs):
    logger.info('request headers:' +
                'ContentType = ' + request.META.get('HTTP_'+'ContentType'.upper(), 'unknown') +
                ', AppKey = ' + request.META.get('HTTP_'+'AppKey'.upper(), 'unknown') +
                ', CurTime = ' + request.META.get('HTTP_'+'CurTime'.upper(), 'unknown') +
                ', MD5 = ' + request.META.get('HTTP_'+'MD5'.upper(), 'unknown') +
                ', CheckSum = ' + request.META.get('HTTP_'+'CheckSum'.upper(), 'unknown')
                )
    logger.info('request body:' + request.body)

    if kwargs.has_key('sleep'):
        sleep = kwargs.get('sleep')
        time.sleep(sleep)

    logger.info("route ack:" + kwargs.get('response', 'unknown'))
    return HttpResponse(kwargs.get('response'))
