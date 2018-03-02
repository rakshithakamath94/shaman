import pika

from pecan import expose, abort, request, conf
from pecan.secure import secure

from shaman.auth import basic_auth


class BusController(object):

    @expose(generic=True)
    def index(self):
        abort(405)

    @index.when(method='GET')
    def index_get(self):
        abort(405)

    @secure(basic_auth)
    @index.when(method='POST', template='json')
    def index_post(self, channel):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=conf.RABBIT_HOST))
        channel = connection.channel()

        channel.queue_bind(queue=channel)
        channel.basic_publish(exchange='', routing_key=channel, body=request.json)
        connection.close()
        return {}
