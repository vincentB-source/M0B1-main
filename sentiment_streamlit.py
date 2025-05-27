import streamlit as st
import requests
from loguru import logger


API_URL = "http://127.0.0.1:9000/"
logger.add("logs/sentiment_streamlit.log")

st.header("Testeur de sentiment")

# Fonction pour tester une phrase
def analyse_sentiment(phrase):
    try:
        response = requests.post(f"{API_URL}/analyse_sentiment/", json={"phrase": phrase})
        return response.json()
    # traitement de la réponse
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de connexion à l'API : {e}")
        logger.error(f"Erreur de connexion à l'API : {e}")
    except Exception as e :
        st.error(f"Une erreur est survenue: {e}")
        logger.error(f"Une erreur est survenue: {e}")



with st.form("analyse_sentiment_form"):
  phrase = st.text_area("Entrez la nouvelle phrase")
  submitted = st.form_submit_button("Analyser")
  if submitted:
    result = analyse_sentiment(phrase)
    #gestion de la réponse à ce niveau ?
    st.write(result)
    logger.info(f"analyse_sentiment_form appelée avec la phrase {phrase}. Retour {result} ")

