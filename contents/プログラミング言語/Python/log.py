import logging


def log_test(comment: str):
    logging.debug(comment)
    logging.critical('critical')
    logging.error('error')
    logging.warning('warning')
    logging.info('info')
    logging.debug('debug')


if __name__ == "__main__":

    # ログレベルを DEBUG に変更
    # フォーマットを定義
    formatter = '%(levelname)s : %(asctime)s : %(message)s'
    logging.basicConfig(filename='logger.log',
                        level=logging.DEBUG, format=formatter)

    log_test("ログレベルを DEBUG に変更")

    # logging のみの書き方
    logging.info('info %s %s', 'test', 'test')
