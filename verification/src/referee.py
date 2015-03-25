from checkio_referee import RefereeCodeGolf
from checkio_referee import covercodes, validators, representations

import settings
import settings_env
from tests import TESTS


class AutoPaintingValidator(validators.BaseValidator):
    def validate(self, outer_result):
        steps, k, n = self._test["validation_data"]
        if not isinstance(outer_result, str):
            return validators.ValidatorResult(False, "This is not a string.")
        actions = outer_result.split(",")
        if len(actions) > steps:
            return validators.ValidatorResult(False, "It can be shorter.")
        details = [0 for _ in range(n)]
        good_ch = "".join(str(r) for r in range(n))
        good_ch += ","
        if any(ch not in good_ch for ch in outer_result):
            return validators.ValidatorResult(False, "Wrong symbol in the result.")
        for act in actions:
            if len(act) > k:
                return validators.ValidatorResult(
                    False, "The system can contain {0} detail(s).".format(k))
            if len(set(act)) < len(act):
                return validators.ValidatorResult(
                    False, "You can not place one detail twice in one load")
            for ch in act:
                details[int(ch)] += 1
        if any(d < 2 for d in details):
            return validators.ValidatorResult(False, "I see no painted details.")
        if any(d > 2 for d in details):
            return validators.ValidatorResult(False, "I see over painted details.")
        return validators.ValidatorResult(True)


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    DEFAULT_LENGTH = 100
    BASE_POINTS = 10
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
    VALIDATOR = AutoPaintingValidator
    CALLED_REPRESENTATIONS = {
        "python_3": representations.unwrap_arg_representation,
        "python_2": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation
    }
    ENV_COVERCODE = {
        "python_2": covercodes.py_unwrap_args,
        "python_3": covercodes.py_unwrap_args,
        "javascript": covercodes.py_unwrap_args
    }
