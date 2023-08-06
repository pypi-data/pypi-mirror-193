from cad.main import CAD
import logging

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

def callback_func():
    print("TARGET")


if __name__ == '__main__':
    cad = CAD('http://127.0.0.1', 'admin', 'Assa+123', logger, callback_func, port=83)
    cad.mainloop()
