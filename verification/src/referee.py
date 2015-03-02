from checkio_referee import RefereeBase
from checkio_referee.covercode import py_unwrap_args
from checkio_referee.validators import BaseValidator, ValidationError

import settings
import settings_env
from tests import TESTS


class AutoPaintingValidator(BaseValidator):
    def validate(self, outer_result):
        steps, k, n = self._test["validation_data"]
        if not isinstance(outer_result, str):
            self.additional_data = "This is not a string."
            raise ValidationError
        actions = outer_result.split(",")
        if len(actions) > steps:
            self.additional_data = "It can be shorter."
            raise ValidationError
        details = [0 for _ in range(n)]
        good_ch = "".join(str(r) for r in range(n))
        good_ch += ","
        if any(ch not in good_ch for ch in outer_result):
            self.additional_data = "Wrong symbol in the result."
            raise ValidationError
        for act in actions:
            if len(act) > k:
                self.additional_data = "The system can contain {0} detail(s).".format(k)
                raise ValidationError
            if len(set(act)) < len(act):
                self.additional_data = "You can not place one detail twice in one load"
                raise ValidationError
            for ch in act:
                details[int(ch)] += 1
        if any(d < 2 for d in details):
            self.additional_data = "I see no painted details."
            raise ValidationError
        if any(d > 2 for d in details):
            self.additional_data = "I see over painted details."
            raise ValidationError


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "paint"
    VALIDATOR = AutoPaintingValidator
    ENV_COVERCODE = {
        "python_2": py_unwrap_args,
        "python_3": py_unwrap_args,
        "javascript": None
    }
