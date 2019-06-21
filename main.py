import sys
import rpc
import ws

from settings import Settings


if __name__ == "__main__":
    config = 'config.json'
    # Args 1 should be the config file if not use the default config.json
    if len(sys.argv) > 1:
        config = str(sys.argv[1])
        print('Config file override by ', config)

    settings = Settings.fromFile(config)

    rpc.run_simple(settings.rpc['url'], settings.rpc['port'], rpc.application)
    ws.run(settings.ws['url'], settings.ws['port'])
