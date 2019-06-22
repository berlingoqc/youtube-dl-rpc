from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher

from ydlrpc.downloading_thread import download


@Request.application
def application(request):
    dispatcher["ydl.getQueue"] = download.GetQueue
    dispatcher["ydl.addQueue"] = download.AddItemQueue
    dispatcher["ydl.setSettings"] = download.SetSettings
    dispatcher["ydl.getSettings"] = download.GetSettings

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')
