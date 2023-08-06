import logging


def init_logging(log_file_path, is_debug=False):
    """
    初始化日志设置
    Args:
        log_file_path: 文件日志路径
        is_debug: 是否开启调试模式  True(开启): 命令行日志和文件INFO级别日志; False(不开启): 仅文件WARNING级别日志

    Returns:

    """
    # 命令行日志
    console_handler = logging.StreamHandler()

    # 文件日志
    # 设置utf-8编码(不设置编码跟随系统)
    file_handler = logging.FileHandler(filename=log_file_path, encoding="utf-8")

    log_level = logging.WARNING
    log_handlers = [
        file_handler,
    ]
    if is_debug:
        log_level = logging.INFO
        log_handlers.append(console_handler)

    logging.basicConfig(
        # 日志级别
        level=log_level,
        # 日志格式
        format='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s',
        # 文件日志文件名, 无法设置日志编码
        # filename=os.path.join(".", "err_list.txt"),  # 这里无法设置日志文件编码
        # 日志handlers, 可以设置多个
        handlers=[
            file_handler,
            console_handler,
        ],
    )
