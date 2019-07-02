import sys

from ydlrpc import rpc, ws, Settings

from threading import Thread

if __name__ == "__main__":
    config = 'config.json'
    # Args 1 should be the config file if not use the default config.json
    if len(sys.argv) > 1:
        config = str(sys.argv[1])
        print('Config file override by ', config)

    settings = Settings.fromFile(config)

    # Thread(target=(lambda: ws.run(
    #    settings.ws['url'], settings.ws['port']))).start()
    rpc.run_simple(settings.rpc['url'], settings.rpc['port'], rpc.application)
    #ws.run(settings.ws['url'], settings.ws['port'])
