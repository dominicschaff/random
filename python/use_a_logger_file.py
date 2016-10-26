import logging as l
l.basicConfig(
    filename="test.log",
    format="%(asctime)s:%(levelname)s - %(filename)s.%(module)s.%(funcName)s.%(lineno)s = %(message)s",
    level=0
)

l.error("error message")
l.fatal("fatal message")
l.warning("warning message")
l.debug("debug message")
l.info("informational message")
