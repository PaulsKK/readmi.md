import logging
import logging.handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO, filename='log.log')

logger = logging.getLogger(__name__)

smtp_handler = logging.handlers.SMTPHandler(mailhost=('smtp.gmail.com', 587),
                                            fromaddr='pauls.konov@gmail.com',
                                            toaddrs='pauls.konov@gmail.com',
                                            subject='Error',
                                            credentials=(
                                                'pauls.konov@gmail.com',
                                                'vpbemywqlypkzdmz'),
                                            secure=())
logger.addHandler(smtp_handler)


def error(err_name, err):
    """Log Errors"""

    logger.warning('error "%s" caused error "%s"', err_name, err)

def main():
    print("Cau")
    def dalisana():
     try:
        a = 10/0
     except ZeroDivisionError as err:
         error('Handling run-time error:', err)
    dalisana()
if __name__ == '__main__':
    main()
