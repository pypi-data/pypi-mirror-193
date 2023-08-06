import requests

from utils import *
from mecord_service import *

if __name__ == '__main__':
    import sys

    module = sys.argv[1]
    command = sys.argv[2]
    if module == 'service':
        service = MecordService()
        if command == 'start':
            if service.is_running():
                print('Service is already running.')
            else:
                print('Starting service...')
                service.start()
        elif command == 'stop':
            if not service.is_running():
                print('Service is not running.')
            else:
                print('Stopping service...')
                service.stop()
        elif command == 'restart':
            print('Restarting service...')
            service.restart()
        elif command == 'status':
            if service.is_running():
                print('Service is running.')
            else:
                print('Service is not running.')
    else:
        print("Unknown command:", command)
        print("Usage: python service.py [start|stop|restart|status]")
        sys.exit(0)
