import yaml
from yaml.loader import SafeLoader

import streamlit as st
import streamlit_authenticator as stauth

from app_diabetes.dataclasses import Age, Comorbilities, Pharmacy, YearsOfEvolution
from app_diabetes.target_hba1c import compute_target_hba1c

with open("config.yaml") as fp:
    config = yaml.load(fp, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:

    authenticator.logout("Logout", "main")

    st.title("App Diabetes")

    st.subheader("Datos del paciente")
    edad = st.radio("Edad (años)", ("<=65", ">65,<=75", ">75"))
    age = Age(edad)

    evolucion_diabetes = st.radio("Años de evolución de la Diabetes", ("<15", ">=15"))
    years_of_evolution = YearsOfEvolution(evolucion_diabetes)

    # años de evolución: más de 15 años, sí o no

    # Valor de hemoglobina, en porcentaje
    hba1c_current: float = st.slider("HbA1c", min_value=4.5, max_value=15.0, step=0.1)

    st.subheader("Comorbilidades")
    enfermedad_cardiovascular = st.checkbox("Enfermedad Cardiovascular", False)
    insuficiencia_cardiaca = st.checkbox("Insuficiencia cardíaca", False)
    retinopatia_diabetica = st.checkbox("Retinopatía diabética", False)
    enfermedad_renal = st.checkbox("Enfermedad renal", False)


    st.subheader("Pauta de medicación actual")
    col1, col2 = st.columns(2)
    metformin = col1.checkbox("Metformina", False)
    isglt2 = col1.checkbox("iSGLT2", False)
    arglp1 = col1.checkbox("arGLP1", False)
    iddp4 = col1.checkbox("iDPP4", False)
    su = col1.checkbox("SU", False)
    pio = col2.checkbox("Pio", False)
    repa = col2.checkbox("Repa", False)
    basal_insuline = col2.checkbox("Insulina basal", False)
    rapid_insuline = col2.checkbox("Insulina rápida", False)

    st.subheader("Extra")


    if st.button("Calcular valor HbA1c objetivo"):
        comorbilities = Comorbilities(
            enfermedad_cardiovascular,
            insuficiencia_cardiaca,
            retinopatia_diabetica,
            enfermedad_renal,
        )
        pharmacy = Pharmacy(
            metformin, isglt2, arglp1, iddp4, su, pio, repa, basal_insuline, rapid_insuline
        )

        hba1c_target = compute_target_hba1c(age, years_of_evolution, comorbilities)

        st.metric("Objetivo HbA1c", hba1c_target)

        delta = hba1c_current - hba1c_target
        st.metric("Delta", delta)

    # Reportar: valor de hemoglobina objetivo

    # Luego, en funcion de la diferencia entre real y objetivo, recomendar pauta de tratamiento.


    # Preguntar las comorbilidades precisas después.
    # """

elif authentication_status == False:
    st.error("Credenciales inválidas")

elif authentication_status is None:
    st.warning("Por favor, introduce nombre y contraseña")
