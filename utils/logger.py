from loguru import logger


logger.add("logs/debug/debug.log", format="{time:YY-MM-DD HH:mm:ss} {level:<6} {message} ",
           level="DEBUG", rotation="1 day", compression="zip")
