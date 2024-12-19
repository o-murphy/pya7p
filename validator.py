from pathlib import Path
from dataclasses import dataclass
from typing import Callable, Any, Tuple

from a7p import profedit_pb2, A7PFile, A7PDataError
from a7p.logger import logger

__all__ = ['Validator', 'Criterion', 'A7PValidationError']


@dataclass
class Violation:
    path: Path | str
    value: any
    reason: str

    def format(self) -> str:
        is_stringer = isinstance(self.value, (str, int, float, bool))
        path = f"Path: {self.path}" if isinstance(self.path, Path) else self.path
        value = f"{self.value if is_stringer else '<object>'}"
        return f"Violation:\n\t{path}:\t{value}\n\tReason:\t{self.reason}"

def is_list_of_violations(violations: str | list[Violation]):
    """Check if a variable is a list of Violation objects."""
    return isinstance(violations, list) and all(isinstance(item, Violation) for item in violations)


# Define a custom type for the return value
ValidationResult = Tuple[bool, str | list[Violation]]

# Define the type annotation for the callable
ValidatorFunction = Callable[[Any, Path, list], ValidationResult]
FlexibleValidatorFunction = Callable[..., ValidationResult]


@dataclass
class Criterion:
    path: Path
    validate: FlexibleValidatorFunction


class A7PValidationError(A7PDataError):
    def __init__(self, violations: list[Violation]):
        self.violations = violations


class Validator:
    def __init__(self):
        self.criteria = {}

        self.register("~", lambda x, *args, **kwargs: (True, ""))

    def register(self, path: Path | str, criteria: FlexibleValidatorFunction):
        if path in self.criteria:
            raise KeyError(f"criterion for {path} already exists")
        self.criteria[path] = Criterion(Path(path), criteria)

    def unregister(self, key: str):
        self.criteria.pop(key, None)

    def get_criteria(self, path: Path) -> Criterion:
        key = path.name
        criterion = self.criteria.get(key, None)
        if criterion is None:
            criterion = self.criteria.get(path.as_posix())
        # for key, value in self.criteria.items():
        #     if key
        # if criterion is None:
        #     print(
        #         f"NoValidatorsRegistered\t{path.as_posix()}")
        return criterion

    def validate(self, data: any, path: Path = Path("~/"),
                 violations: list[Violation] = None) -> (bool, list[Violation]):

        if violations is None:
            violations = []
        if isinstance(data, dict):

            # If `data` is a dictionary, iterate over its key-value pairs
            for key, value in data.items():
                current_path = path / key
                self.validate(value, current_path, violations)

        elif isinstance(data, list):

            # If `data` is a list, iterate over its elements
            for i, item in enumerate(data):
                item_path = path / f"[{i}]"
                self.validate(item, item_path, violations)

        criterion = self.get_criteria(path)
        if isinstance(criterion, Criterion):
            is_valid, reason = criterion.validate(data, path, violations)
            if not is_valid:
                violations.append(Violation(path, data, str(reason)))
                # raise A7PValidationError(f"{path.as_posix()} has not valid value: {data}. Reason: {reason}")
        return len(violations) == 0, violations


_check_profile_name = lambda x, *args, **kwargs: (len(x) < 50, "expected string shorter than 50 characters")
_check_cartridge_name = lambda x, *args, **kwargs: (len(x) < 50, "expected string shorter than 50 characters")
_check_caliber = lambda x, *args, **kwargs: (len(x) < 50, "expected string shorter than 50 characters")
_check_bullet_name = lambda x, *args, **kwargs: (len(x) < 50, "expected string shorter than 50 characters")
_check_device_uuid = lambda x, *args, **kwargs: (len(x) < 50, "expected string shorter than 50 characters")
_check_short_name_top = lambda x, *args, **kwargs: (len(x) < 8, "expected string shorter than 8 characters")
_check_short_name_bot = lambda x, *args, **kwargs: (len(x) < 8, "expected string shorter than 8 characters")
_check_user_note = lambda x, *args, **kwargs: (len(x) < 1024, "expected string shorter 1024 characters")
_check_zero_x = lambda x, *args, **kwargs: (-200.0 <= x / 1000 <= 200.0, "expected value in range [-200.0, 200.0]")
_check_zero_y = lambda x, *args, **kwargs: (-200.0 <= x / 1000 <= 200.0, "expected value in range [-200.0, 200.0]")
_check_sc_height = lambda x, *args, **kwargs: (
    -5000.0 <= x / 1000 <= 5000.0, "expected value in range [-5000.0, 5000.0]")
_check_r_twist = lambda x, *args, **kwargs: (0.0 <= x / 10 <= 100.0, "expected value in range [0.0, 100.0]")
_check_c_muzzle_velocity = lambda x, *args, **kwargs: (
    10.0 <= x / 10 <= 3000.0, "expected value in range [10.0, 3000.0]")
_check_c_zero_temperature = lambda x, *args, **kwargs: (-100.0 <= x <= 100.0, "expected value in range [-100.0, 100.0]")
_check_c_t_coeff = lambda x, *args, **kwargs: (0.0 <= x / 1000 <= 5.0, "expected value in range [0.0, 5.0]")
_check_c_zero_air_temperature = lambda x, *args, **kwargs: (
    -100.0 <= x <= 100.0, "expected value in range [-100.0, 100.0]")
_check_c_zero_air_pressure = lambda x, *args, **kwargs: (
    300.0 <= x / 10 <= 1500.0, "expected value in range [300.0, 1500.0]")
_check_c_zero_air_humidity = lambda x, *args, **kwargs: (0.0 <= x <= 100.0, "expected value in range [0.0, 100.0]")
_check_c_zero_w_pitch = lambda x, *args, **kwargs: (-90.0 <= x <= 90, "expected value in range [-90.0, 90.0]")
_check_c_zero_p_temperature = lambda x, *args, **kwargs: (
    -100.0 <= x <= 100.0, "expected value in range [-100.0, 100.0]")
_check_c_zero_b_diameter = lambda x, *args, **kwargs: (
    0.001 <= x / 1000 <= 50.0, "expected value in range [0.001, 50.0]")
_check_c_zero_b_weight = lambda x, *args, **kwargs: (1.0 <= x / 10 <= 6553.5, "expected value in range [1.0, 6553.5]")
_check_c_zero_b_length = lambda x, *args, **kwargs: (0.01 <= x / 1000 <= 200.0, "expected value in range [0.01, 200.5]")
_check_bc_type = lambda x, *args, **kwargs: (x in ['G7', 'G1', 'CUSTOM'], "expected one of ['G7', 'G1', 'CUSTOM']")
_check_twist_fir = lambda x, *args, **kwargs: (x in ['RIGHT', 'LEFT'], "expected one of ['RIGHT', 'LEFT']")
_check_c_zero_distance_idx = lambda x, *args, **kwargs: (0 <= x <= 200, "expected integer value in range [0, 200]")


def _check_switches(profile: list, path: Path, *args, **kwargs):
    return True, "NOT IMPLEMENTED"


def _check_coef_rows(profile: dict, path: Path, *args, **kwargs):
    return True, "NOT IMPLEMENTED"


def _check_distances(distances: list[int], path: Path, *args, **kwargs):
    reasons = []
    invalid_distances = []
    if not (0 < len(distances) < 200):
        reasons.append("distances count have been between 0 and 200 values")
    for i, d in enumerate(distances):
        path / f"[{i}]"
        if 1.0 <= d / 100 <= 3000.0:
            continue
        else:
            invalid_distances.append(d)
    if len(invalid_distances) > 0:
        reasons.append(f"Invalid distances: {invalid_distances}")
    return len(reasons) == 0, f"[ {', '.join(reasons)} ]"


def _check_dependency_distances(zero_distance_index: int, distances: list[int]):
    return zero_distance_index >= len(distances) + 1, "zero distance index > len(distances)"


def _check_profile(profile: dict, path: Path, violations: list[Violation], *args, **kwargs):
    v = Validator()
    v.register("~/profile/distances", _check_distances)
    v.register("~/profile/cZeroDistanceIdx", _check_c_zero_distance_idx)

    v.register("~/profile/switches", _check_switches)
    v.register("~/profile/coefRows", _check_coef_rows)

    v.validate(profile, path, violations)

    is_valid, reason = _check_dependency_distances(profile["cZeroDistanceIdx"], profile["distances"])
    print(is_valid)
    if not is_valid:
        violations.append(Violation("Distances", "Distance dependency error", reason))

    return is_valid, "Found problems in profile"


def validate(payload: profedit_pb2.Payload):
    data = A7PFile.to_dict(payload)
    v = Validator()
    v.register("profileName", _check_profile_name)
    v.register("cartridgeName", _check_cartridge_name)
    v.register("caliber", _check_caliber)
    v.register("bulletName", _check_bullet_name)
    v.register("deviceUuid", _check_device_uuid)
    v.register("shortNameTop", _check_short_name_top)
    v.register("shortNameBot", _check_short_name_bot)
    v.register("userNote", _check_user_note)
    v.register("zeroX", _check_zero_x)
    v.register("zeroY", _check_zero_y)
    v.register("scHeight", _check_sc_height)
    v.register("rTwist", _check_r_twist)
    v.register("cMuzzleVelocity", _check_c_muzzle_velocity)
    v.register("cZeroTemperature", _check_c_zero_temperature)
    v.register("cTCoeff", _check_c_t_coeff)
    v.register("cZeroAirTemperature", _check_c_zero_air_temperature)
    v.register("cZeroAirPressure", _check_c_zero_air_pressure)
    v.register("cZeroAirHumidity", _check_c_zero_air_humidity)
    v.register("cZeroPTemperature", _check_c_zero_p_temperature)
    v.register("cZeroWPitch", _check_c_zero_w_pitch)
    v.register("bLength", _check_c_zero_b_length)
    v.register("bWeight", _check_c_zero_b_weight)
    v.register("bDiameter", _check_c_zero_b_diameter)
    v.register("bcType", _check_bc_type)
    v.register("twistDir", _check_twist_fir)
    v.register("~/profile", _check_profile)

    is_valid, violations = v.validate(data)
    if not is_valid:
        raise A7PValidationError(violations)


if __name__ == '__main__':
    # with open("a7p/test.a7p", "rb") as fp:
    with open("broken.a7p", "rb") as fp:
        payload = A7PFile.load(fp, False)
    try:
        validate(payload)
    except A7PValidationError as e:
        for v in e.violations:
            logger.warning(v.format())
