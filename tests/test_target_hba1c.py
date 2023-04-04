import pytest

from app_diabetes.dataclasses import Comorbilities, Age, YearsOfEvolution
from app_diabetes.target_hba1c import compute_target_hba1c


@pytest.fixture
def no_comorbility() -> Comorbilities:
    return Comorbilities(False, False, False, False)

@pytest.fixture
def some_comorbility() -> Comorbilities:
    return Comorbilities(True, False, False, False)


@pytest.mark.parametrize(
    "age,years_of_evolution,comorbilities,expected_value",
    [
        (Age.UNDER_66, YearsOfEvolution.LESS_THAN_15, "no_comorbility", 7.0),
        (Age.UNDER_66, YearsOfEvolution.LESS_THAN_15, "some_comorbility", 8.0),
        (Age.UNDER_66, YearsOfEvolution.AT_LEAST_15, "no_comorbility", 8.0),
        (Age.UNDER_66, YearsOfEvolution.AT_LEAST_15, "some_comorbility", 8.0),
        (Age.BETWEEN_66_AND_75, YearsOfEvolution.LESS_THAN_15, "no_comorbility", 7.0),
        (Age.BETWEEN_66_AND_75, YearsOfEvolution.AT_LEAST_15, "no_comorbility", 8.0),
        (Age.BETWEEN_66_AND_75, YearsOfEvolution.LESS_THAN_15, "some_comorbility", 8.5),
        (Age.BETWEEN_66_AND_75, YearsOfEvolution.AT_LEAST_15, "some_comorbility", 8.5),
        (Age.OVER_76, YearsOfEvolution.LESS_THAN_15, "no_comorbility", 8.5),
        (Age.OVER_76, YearsOfEvolution.LESS_THAN_15, "some_comorbility", 8.5),
        (Age.OVER_76, YearsOfEvolution.AT_LEAST_15, "no_comorbility", 8.5),
        (Age.OVER_76, YearsOfEvolution.AT_LEAST_15, "some_comorbility", 8.5),
    ]
)
def test_target_hba1c(age, years_of_evolution, comorbilities, expected_value, request):
    cm = request.getfixturevalue(comorbilities)
    actual_value = compute_target_hba1c(age, years_of_evolution, cm)
    assert expected_value == actual_value
