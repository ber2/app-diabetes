from dataclasses import dataclass
from enum import Enum


class Age(Enum):
    UNDER_66 = "<=65"
    BETWEEN_66_AND_75 = ">65,<=75"
    OVER_76 = ">75"


class YearsOfEvolution(Enum):
    LESS_THAN_15 = "<15"
    AT_LEAST_15 = ">=15"


@dataclass(frozen=True)
class Comorbilities:
    cardiovascular_disease: bool
    heart_failure: bool
    diabetic_retinopathy: bool
    renal_disease: bool

    def __bool__(self) -> bool:
        return any(
            [
                self.cardiovascular_disease,
                self.heart_failure,
                self.diabetic_retinopathy,
                self.renal_disease,
            ]
        )


@dataclass(frozen=True)
class Pharmacy:
    metformin: bool
    isglt2: bool
    arglp1: bool
    idpp4: bool
    su: bool
    pio: bool
    repa: bool
    basal_insuline: bool
    rapid_insuline: bool
