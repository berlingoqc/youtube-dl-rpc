from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

from main import addQueue, getQueue


@Request.application
def application(request):
    dispatcher["ydl.getQueue"] = getQueue
    dispatcher["ydl.addQueue"] = addQueue

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')
