import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # 设置最低日志级别

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - [%(funcName)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)  # 终端输出INFO及以上级别

file_handler = logging.FileHandler(
    filename="/mnt/mechanical/projects/toolbox/toolbox.log",
    encoding='utf-8',
    mode='a'
)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # 文件记录DEBUG及以上级别

if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

if __name__ == "__main__":
    logger.debug("调试信息示例")
    logger.info("普通信息示例")
    logger.warning("警告信息示例")
