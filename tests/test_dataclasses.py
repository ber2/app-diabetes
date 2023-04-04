import pytest

from app_diabetes.dataclasses import Comorbilities


@pytest.mark.parametrize("cardiovascular_disease", [True, False])
@pytest.mark.parametrize("heart_failure", [True, False])
@pytest.mark.parametrize("diabetic_retinopathy", [True, False])
@pytest.mark.parametrize("renal_disease", [True, False])
def test_comorbilities(
    cardiovascular_disease, heart_failure, diabetic_retinopathy, renal_disease
):
    cm = Comorbilities(
        cardiovascular_disease, heart_failure, diabetic_retinopathy, renal_disease
    )
    assert bool(cm) == any(
        [cardiovascular_disease, heart_failure, diabetic_retinopathy, renal_disease]
    )
