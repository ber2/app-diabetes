import streamlit as st


def calcular_objetivo_hba1c(edad: str, evolucion_diabetes: str, comorbilidades: bool) -> float:
    if edad == "<=65":
        if not comorbilidades and evolucion_diabetes == "<15":
            return 7.0
        else:
            return 8.0
    elif edad == ">65,<=75":
        if not comorbilidades and evolucion_diabetes == "<15":
            return 7.0
        elif not comorbilidades and evolucion_diabetes == ">=15":
            return 8.0
        else:
            return 8.5
    else:
        return 8.5



st.title("App Diabetes")

edad = st.radio("Edad (años)", ("<=65", ">65,<=75", ">75"))

evolucion_diabetes = st.radio("Años de evolución de la Diabetes", ("<15", ">=15"))

#años de evolución: más de 15 años, sí o no

# Valor de hemoglobina, en porcentaje
hba1c = st.slider("HbA1c", min_value=4.5, max_value=15.0, step=0.1)

comorbilidades = st.checkbox("Comorbilidades", False)
# enfermedad_cardiovascular = st.checkbox("Enfermedad Cardiovascular", False)
# insuficiencia_cardiaca = st.checkbox("Insuficiencia cardíaca", False)
# retinopatia_diabetica = st.checkbox("Retinopatía diabética", False)
# enfermedad_renal = st.checkbox("Enfermedad renal", False)

if st.button("Calcular valor HbA1c objetivo"):
    hba1c_target = calcular_objetivo_hba1c(edad, evolucion_diabetes, comorbilidades)

    st.metric("Objetivo HbA1c", hba1c_target)

    delta = hba1c - hba1c_target
    st.metric("Delta", delta)

# Reportar: valor de hemoglobina objetivo

# Luego, en funcion de la diferencia entre real y objetivo, recomendar pauta de tratamiento.


# Preguntar las comorbilidades precisas después.
# """
