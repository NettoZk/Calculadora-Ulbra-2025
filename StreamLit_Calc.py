import streamlit as st

def calcular_mensalidade(curso, quantidade_creditos, prazo_parcelamento, desconto):    
    if curso in cursos:
        valor_credito = cursos[curso]
        mensalidade_sem_desconto = valor_credito * quantidade_creditos * 6 / prazo_parcelamento
        semestre_sem_desconto = valor_credito * quantidade_creditos * 6
        mensalidade_com_desconto = mensalidade_sem_desconto * (1 - desconto / 100)
        semestre_com_desconto = semestre_sem_desconto * (1 - desconto / 100)

        return {
            "Mensalidade com Desconto R$": mensalidade_com_desconto,
            "Mensalidade sem Desconto R$": mensalidade_sem_desconto,
            "Semestre com Desconto R$": semestre_com_desconto,
            "Semestre sem Desconto R$": semestre_sem_desconto,
            "Valor do Crédito": valor_credito            
        }

cursos = {
    "ADMINISTRAÇÃO": 40.74,
    "AGRONOMIA": 60.08,
    "ARQUITETURA E URBANISMO": 74.42,
    "BIOMEDICINA": 69.71,
    "CIÊNCIA DA COMPUTAÇÃO": 50.50,
    "CIÊNCIAS CONTÁBEIS": 40.76,
    "COMPLEMENTAÇÃO PSICOLOGIA": 43.49,
    "CURSO SUPERIOR DE TECNOLOGIA EM ESTETICA E COSMETICA": 41.88,
    "DIREITO": 68.97,
    "EDUCACAO FISICA - BACHARELADO": 42.38,
    "EDUCACAO FISICA - LICENCIATURA": 40.91,
    "ENFERMAGEM": 69.63,
    "ENGENHARIA CIVIL": 75.40,
    "ENGENHARIA DE MINAS": 83.44,
    "ENGENHARIA DE SOFTWARE": 50.50,
    "FARMÁCIA": 69.71,
    "FISIOTERAPIA": 69.71,
    "JOGOS DIGITAIS": 50.50,
    "MEDICINA": 340.90,
    "MEDICINA VETERINÁRIA": 154.05,
    "NUTRIÇÃO": 83.00,
    "ODONTOLOGIA": 168.34,
    "PSICOLOGIA": 80.72,
    "SISTEMAS DE INFORMAÇÃO": 52.17,
}

st.title("Calculadora de Mensalidades")

curso_selecionado = st.selectbox("Escolha o curso:", list(cursos.keys()))
quantidade_creditos = st.number_input("Quantidade de créditos:", min_value=1, step=1)
prazo_parcelamento = st.selectbox("Prazo de parcelamento (em meses):", list(range(1, 11)), index=5)
desconto = st.number_input("Desconto (de 0 a 100):", min_value=0, max_value=100, step=1)

if st.button("Calcular Mensalidade"):
    if curso_selecionado and quantidade_creditos > 0:
        resultado = calcular_mensalidade(curso_selecionado, quantidade_creditos, prazo_parcelamento, desconto)
        st.write(f"**Mensalidade com Desconto:** R$ {resultado['Mensalidade com Desconto R$']:.2f}")
        st.write(f"**Mensalidade sem Desconto:** R$ {resultado['Mensalidade sem Desconto R$']:.2f}")
        st.write(f"**Semestre com Desconto:** R$ {resultado['Semestre com Desconto R$']:.2f}")
        st.write(f"**Semestre sem Desconto:** R$ {resultado['Semestre sem Desconto R$']:.2f}")
        st.write(f"**Valor crédito do curso:** R$ {resultado['Valor do Crédito']:.2f}")
    else:
        st.error("Por favor, insira uma quantidade válida de créditos.")
