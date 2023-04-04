from .dataclasses import Age, Comorbilities, YearsOfEvolution


def compute_target_hba1c(
    age: Age, years_of_evolution: YearsOfEvolution, comorbilities: Comorbilities
) -> float:
    if age == Age.UNDER_66:
        if not comorbilities and years_of_evolution == YearsOfEvolution.LESS_THAN_15:
            return 7.0
        else:
            return 8.0
    elif age == Age.BETWEEN_66_AND_75:
        if not comorbilities and years_of_evolution == YearsOfEvolution.LESS_THAN_15:
            return 7.0
        elif not comorbilities and years_of_evolution == YearsOfEvolution.AT_LEAST_15:
            return 8.0
        else:
            return 8.5
    else:
        return 8.5
