from assertpy import assert_that
from utils.logger import logger


class Assert:
    @classmethod
    def element_text_is_correct(cls, element, expected_text):
        logger.info(f"actual text: {element.text}, expected_text: {expected_text}")
        assert_that(element.text, description="Unexpected element text.").is_equal_to(expected_text)

    @classmethod
    def elements_are_equal(cls, element1, element2):
        assert_that(element1, description=f"{element1} is not equal {element2}").is_equal_to(element2)

