# Consultor Inteligente de Carreiras em TI

Projeto acadêmico de Inteligência Artificial: sistema especialista baseado em regras que entrevista o usuário e recomenda uma das 10 trilhas profissionais descritas na atividade.

## Tecnologias
- Python 3.10 ou superior
- Experta: motor de inferência baseado em regras
- Streamlit: interface web
- Git/GitHub: controle de versão

## Instalação

Recomenda-se criar um ambiente virtual.

### Windows
```bash
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Execução
Na pasta do projeto, execute:
```bash
streamlit run app.py
```
O Streamlit exibirá um endereço local no terminal. Abra-o no navegador.

## Como funciona
1. O sistema coleta quatro dimensões: afinidade matemática/estatística, atividade preferida, ferramenta de maior afinidade e tipo de valor que deseja entregar.
2. O usuário responde às perguntas da interface.
3. O motor Experta dispara regras `@Rule` que correspondem às respostas e registra pontos e justificativas.
4. O sistema soma a pontuação de cada trilha, mostra a recomendação com maior pontuação e permite consultar as pontuações das demais trilhas.

## As 10 trilhas
1. Desenvolvimento Back-end
2. Desenvolvimento Front-end & UI/UX
3. Ciência de Dados e Machine Learning
4. Engenharia de Dados
5. Cibersegurança (Security / Pentesting)
6. DevOps & SRE
7. Computação em Nuvem (Cloud Architecture)
8. Desenvolvimento Mobile
9. Engenharia de Qualidade e Testes (QA)
10. Gestão de Produtos (Product Management)

## Personas para validação

Use os perfis abaixo na interface e compare o resultado com o esperado. A recomendação pode variar se as respostas forem alteradas.

| Persona | Matemática | Atividade | Ferramenta | Valor preferido | Resultado esperado |
|---|---|---|---|---|---|
| Perfil analítico | Alta | Analisar dados, encontrar padrões e fazer previsões | Python | Previsões, descobertas e decisões baseadas em dados | Ciência de Dados e Machine Learning |
| Perfil infraestrutura/segurança | Média | Investigar vulnerabilidades e proteger sistemas | Linux e redes | Sistemas protegidos contra ataques e acessos indevidos | Cibersegurança |
| Perfil visual | Média | Criar interfaces, layouts e experiências visuais | JavaScript | Uma interface fácil e agradável para o usuário | Front-end & UI/UX |
| Perfil negócios/produto | Baixa | Planejar funcionalidades, ouvir usuários e priorizar tarefas | Ferramentas ágeis de planejamento | Resolver problemas dos usuários e gerar valor para o negócio | Gestão de Produtos |

## Observações
- As regras e pontuações representam uma base de conhecimento inicial e podem ser ajustadas conforme testes com usuários.
- A pontuação é uma forma simples de comparar evidências; ela não representa uma avaliação psicológica ou garantia de carreira.
- A biblioteca Experta é antiga e pode apresentar incompatibilidades com versões recentes de Python. Se a instalação falhar, tente Python 3.10 em um ambiente virtual e consulte a documentação da biblioteca.

  ## Prints
<img width="1349" height="572" alt="Apresentação-tela inicial" src="https://github.com/user-attachments/assets/0d98ea72-9120-4b54-a62a-4b4b15476043" />
<img width="1349" height="572" alt="Persona perfil analítico-escolha opções" src="https://github.com/user-attachments/assets/4757b05e-99db-4091-be7c-e5ca36c3d6a8" />
<img width="1349" height="572" alt="Persona perfil analítico - trilha recomendada" src="https://github.com/user-attachments/assets/adc5d2a7-3ed9-4f74-8ded-4df7c586b8fd" />



 
