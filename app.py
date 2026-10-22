import streamlit as st
from experta import Fact, KnowledgeEngine, Rule, MATCH, P

st.set_page_config(page_title="Consultor de Carreiras em TI", page_icon="💻", layout="centered")

CAREERS = {
    "backend": "Desenvolvimento Back-end",
    "frontend": "Desenvolvimento Front-end & UI/UX",
    "data_science": "Ciência de Dados e Machine Learning",
    "data_engineering": "Engenharia de Dados",
    "security": "Cibersegurança (Security / Pentesting)",
    "devops": "DevOps & SRE",
    "cloud": "Computação em Nuvem (Cloud Architecture)",
    "mobile": "Desenvolvimento Mobile",
    "qa": "Engenharia de Qualidade e Testes (QA)",
    "product": "Gestão de Produtos (Product Management)",
}

class Profile(Fact):
    """Respostas fornecidas durante a entrevista."""

class Recommendation(Fact):
    """Pontuação e justificativa produzidas por uma regra."""

class CareerExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.explanations = []

    def add_recommendation(self, career, points, reason):
        self.declare(Recommendation(career=career, points=points, reason=reason))

    # Back-end: lógica, APIs, bancos de dados e regras de negócio
    @Rule(Profile(activity="Escrever algoritmos e regras de negócio"))
    def backend_activity(self):
        self.add_recommendation("backend", 3, "Você prefere escrever algoritmos e regras de negócio.")

    @Rule(Profile(tool="Python"))
    def backend_python(self):
        self.add_recommendation("backend", 1, "Sua afinidade com Python pode ser aproveitada no desenvolvimento de serviços.")

    @Rule(Profile(value="Funcionalidades e serviços que processam informações"))
    def backend_value(self):
        self.add_recommendation("backend", 3, "Você prefere entregar funcionalidades e serviços que processam informações.")

    # Front-end e UI/UX: interfaces, experiência e aspectos visuais
    @Rule(Profile(activity="Criar interfaces, layouts e experiências visuais"))
    def frontend_activity(self):
        self.add_recommendation("frontend", 4, "Você demonstra preferência por interfaces e experiências visuais.")

    @Rule(Profile(tool="JavaScript"))
    def frontend_javascript(self):
        self.add_recommendation("frontend", 2, "JavaScript é bastante utilizado na construção de interfaces web.")

    @Rule(Profile(value="Uma interface fácil e agradável para o usuário"))
    def frontend_value(self):
        self.add_recommendation("frontend", 4, "Sua prioridade é a experiência de quem utiliza o produto.")

    # Ciência de Dados e ML
    @Rule(Profile(activity="Analisar dados, encontrar padrões e fazer previsões"))
    def data_science_activity(self):
        self.add_recommendation("data_science", 4, "Você gosta de analisar dados, padrões e previsões.")

    @Rule(Profile(math="Alta", tool="Python"))
    def data_science_math_python(self):
        self.add_recommendation("data_science", 3, "A combinação de afinidade matemática alta e Python favorece análises e modelos.")

    @Rule(Profile(value="Previsões, descobertas e decisões baseadas em dados"))
    def data_science_value(self):
        self.add_recommendation("data_science", 4, "Você quer gerar conhecimento e previsões a partir dos dados.")

    # Engenharia de Dados
    @Rule(Profile(activity="Organizar grandes volumes de dados e criar pipelines"))
    def data_engineering_activity(self):
        self.add_recommendation("data_engineering", 4, "Você prefere organizar dados e construir pipelines de processamento.")

    @Rule(Profile(tool="SQL e bancos de dados"))
    def data_engineering_sql(self):
        self.add_recommendation("data_engineering", 3, "Sua afinidade com SQL e bancos de dados combina com a preparação de dados.")

    @Rule(Profile(value="Dados organizados e disponíveis para outras equipes"))
    def data_engineering_value(self):
        self.add_recommendation("data_engineering", 4, "Você valoriza disponibilizar dados confiáveis para outras equipes.")

    # Cibersegurança
    @Rule(Profile(activity="Investigar vulnerabilidades e proteger sistemas"))
    def security_activity(self):
        self.add_recommendation("security", 4, "Você se interessa por investigar vulnerabilidades e proteger sistemas.")

    @Rule(Profile(tool="Linux e redes"))
    def security_linux(self):
        self.add_recommendation("security", 3, "Linux e redes são conhecimentos importantes em segurança cibernética.")

    @Rule(Profile(value="Sistemas protegidos contra ataques e acessos indevidos"))
    def security_value(self):
        self.add_recommendation("security", 4, "Sua prioridade é proteger sistemas e informações.")

    # DevOps & SRE
    @Rule(Profile(activity="Automatizar tarefas, implantar e monitorar aplicações"))
    def devops_activity(self):
        self.add_recommendation("devops", 4, "Você prefere automatizar implantações e monitorar aplicações.")

    @Rule(Profile(tool="Docker, Git ou ferramentas de CI/CD"))
    def devops_tools(self):
        self.add_recommendation("devops", 3, "Sua afinidade com Docker, Git ou CI/CD combina com práticas DevOps.")

    @Rule(Profile(value="Implantações confiáveis e sistemas sempre disponíveis"))
    def devops_value(self):
        self.add_recommendation("devops", 4, "Você prioriza confiabilidade e disponibilidade dos sistemas.")

    # Computação em Nuvem
    @Rule(Profile(activity="Planejar servidores, infraestrutura e serviços em nuvem"))
    def cloud_activity(self):
        self.add_recommendation("cloud", 4, "Você se interessa por infraestrutura e arquitetura em nuvem.")

    @Rule(Profile(tool="AWS, Azure ou Google Cloud"))
    def cloud_tools(self):
        self.add_recommendation("cloud", 3, "Sua afinidade com plataformas de nuvem está alinhada a essa trilha.")

    @Rule(Profile(value="Infraestrutura escalável e recursos disponíveis sob demanda"))
    def cloud_value(self):
        self.add_recommendation("cloud", 4, "Você prefere entregar infraestrutura escalável e flexível.")

    # Desenvolvimento Mobile
    @Rule(Profile(activity="Criar aplicativos para celulares e tablets"))
    def mobile_activity(self):
        self.add_recommendation("mobile", 4, "Você prefere desenvolver aplicativos para dispositivos móveis.")

    @Rule(Profile(tool="Flutter ou React Native"))
    def mobile_tools(self):
        self.add_recommendation("mobile", 3, "Flutter e React Native são ferramentas voltadas a aplicações móveis.")

    @Rule(Profile(value="Aplicativos úteis para uso em dispositivos móveis"))
    def mobile_value(self):
        self.add_recommendation("mobile", 4, "Você quer entregar aplicações diretamente aos usuários de celulares e tablets.")

    # Qualidade e testes
    @Rule(Profile(activity="Testar aplicações, encontrar falhas e validar requisitos"))
    def qa_activity(self):
        self.add_recommendation("qa", 4, "Você prefere testar aplicações e identificar falhas.")

    @Rule(Profile(tool="Ferramentas de testes automatizados"))
    def qa_tools(self):
        self.add_recommendation("qa", 3, "Sua afinidade com testes automatizados combina com a área de QA.")

    @Rule(Profile(value="Software confiável, estável e com menos defeitos"))
    def qa_value(self):
        self.add_recommendation("qa", 4, "Você prioriza a qualidade e a confiabilidade do software.")

    # Gestão de Produtos
    @Rule(Profile(activity="Planejar funcionalidades, ouvir usuários e priorizar tarefas"))
    def product_activity(self):
        self.add_recommendation("product", 4, "Você gosta de planejar funcionalidades e priorizar necessidades.")

    @Rule(Profile(tool="Ferramentas ágeis de planejamento"))
    def product_tools(self):
        self.add_recommendation("product", 2, "Ferramentas de planejamento ágil são comuns na gestão de produtos.")

    @Rule(Profile(value="Resolver problemas dos usuários e gerar valor para o negócio"))
    def product_value(self):
        self.add_recommendation("product", 4, "Você quer conectar necessidades dos usuários aos objetivos do negócio.")


def recommend(answers):
    engine = CareerExpert()
    engine.reset()
    engine.declare(Profile(**answers))
    engine.run()

    scores = {key: 0 for key in CAREERS}
    reasons = {key: [] for key in CAREERS}
    for fact in engine.facts.values():
        if isinstance(fact, Recommendation):
            key = fact["career"]
            scores[key] += fact["points"]
            reasons[key].append(fact["reason"])

    # A pontuação matemática funciona como critério adicional para perfis analíticos.
    if answers["math"] == "Alta":
        scores["data_science"] += 1
        reasons["data_science"].append("A afinidade matemática alta também favorece a análise e a modelagem.")
    elif answers["math"] == "Baixa":
        scores["product"] += 1
        reasons["product"].append("A trilha de produto também permite maior foco em necessidades e prioridades de negócio.")

    winner = max(scores, key=scores.get)
    # Se nenhuma regra específica disparar, a recomendação fica baseada nas respostas mais próximas.
    if scores[winner] == 0:
        winner = "backend"
        reasons[winner] = ["Como as respostas não ativaram regras específicas, esta é uma recomendação inicial; revise as respostas para melhorar o resultado."]
    return winner, scores, reasons


st.title("Consultor Inteligente de Carreiras em TI")
st.write("Responda às perguntas para receber uma sugestão de trilha profissional e entender quais regras contribuíram para o resultado.")
st.caption("O sistema oferece uma orientação inicial com base nas respostas; não substitui pesquisa, experiência prática ou aconselhamento profissional.")

with st.form("career_form"):
    math = st.radio("1. Como você avalia sua afinidade com matemática e estatística?", ["Baixa", "Média", "Alta"], horizontal=True)
    activity = st.selectbox("2. Qual atividade mais combina com você?", [
        "Escrever algoritmos e regras de negócio",
        "Criar interfaces, layouts e experiências visuais",
        "Analisar dados, encontrar padrões e fazer previsões",
        "Organizar grandes volumes de dados e criar pipelines",
        "Investigar vulnerabilidades e proteger sistemas",
        "Automatizar tarefas, implantar e monitorar aplicações",
        "Planejar servidores, infraestrutura e serviços em nuvem",
        "Criar aplicativos para celulares e tablets",
        "Testar aplicações, encontrar falhas e validar requisitos",
        "Planejar funcionalidades, ouvir usuários e priorizar tarefas",
    ])
    tool = st.selectbox("3. Qual linguagem ou ferramenta mais desperta seu interesse?", [
        "Python", "JavaScript", "SQL e bancos de dados", "Linux e redes",
        "Docker, Git ou ferramentas de CI/CD", "AWS, Azure ou Google Cloud",
        "Flutter ou React Native", "Ferramentas de testes automatizados",
        "Ferramentas ágeis de planejamento", "Nenhuma/Iniciante"
    ])
    value = st.selectbox("4. Que tipo de resultado você mais gostaria de entregar?", [
        "Funcionalidades e serviços que processam informações",
        "Uma interface fácil e agradável para o usuário",
        "Previsões, descobertas e decisões baseadas em dados",
        "Dados organizados e disponíveis para outras equipes",
        "Sistemas protegidos contra ataques e acessos indevidos",
        "Implantações confiáveis e sistemas sempre disponíveis",
        "Infraestrutura escalável e recursos disponíveis sob demanda",
        "Aplicativos úteis para uso em dispositivos móveis",
        "Software confiável, estável e com menos defeitos",
        "Resolver problemas dos usuários e gerar valor para o negócio",
    ])
    submitted = st.form_submit_button("Analisar meu perfil")

if submitted:
    answers = {"math": math, "activity": activity, "tool": tool, "value": value}
    winner, scores, reasons = recommend(answers)
    st.divider()
    st.subheader("Trilha recomendada")
    st.success(CAREERS[winner])
    st.write("**Por que essa trilha foi recomendada:**")
    if reasons[winner]:
        for reason in reasons[winner]:
            st.write(f"- {reason}")
    else:
        st.write("- A recomendação considera a combinação geral das respostas informadas.")
    with st.expander("Ver pontuação de todas as trilhas"):
        ordered = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        for key, score in ordered:
            st.write(f"**{CAREERS[key]}:** {score} ponto(s)")
