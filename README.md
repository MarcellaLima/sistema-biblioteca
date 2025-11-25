
# 📚 Sistema de Biblioteca

Projeto desenvolvido para a disciplina de Engenharia de Requisitos e Análise de Sistemas da Universidade de Vassouras – Campus Saquarema.  
O sistema apresenta um protótipo de interface em **média fidelidade (mid-fi)** utilizando **HTML + CSS**, além de um backend simulado em **Python**, usando apenas **listas e dicionários** para abstração do banco de dados.

---

## 🧾 Sumário

- Descrição Geral  
- Funcionalidades  
- Requisitos Funcionais  
- Requisitos Não Funcionais  
- Arquitetura do Projeto  
- Protótipo de Telas  
- Backend Simulado  
- Como Executar os Testes  
- Tecnologias Utilizadas  
- Autores  

---

## 📘 Descrição Geral

O **Sistema de Biblioteca** foi desenvolvido com o objetivo de gerenciar usuários, livros, empréstimos e multas de forma simples e eficiente.  
O projeto conta com:

- Interface mid-fi em tons de roxo  
- Protótipo navegável (HTML + CSS)  
- Backend simulado em Python  
- Testes automatizados para validação do sistema  

O sistema demonstra o fluxo completo de cadastro, consulta, empréstimo e gerenciamento do acervo.

---

## 🚀 Funcionalidades

- Cadastro e edição de usuários  
- Cadastro e edição de livros  
- Controle de exemplares  
- Empréstimos e devoluções  
- Cálculo automático de multas por atraso  
- Pesquisa com filtros  
- Área administrativa para bibliotecários  
- Interface responsiva e organizada  

---

## 📌 Requisitos Funcionais

- [RF001] Cadastrar e gerenciar usuários  
- O sistema deve permitir o cadastro, edição, consulta e exclusão de usuários, incluindo dados pessoais, tipo de usuário.
- [RF002] Cadastrar, atualizar e remover livros  
- O sistema deve permitir registrar livros com detalhes completos (autor, edição, editora, ano, gênero) e gerenciar seu estado (disponível, reservado, emprestado, danificado).
- [RF003] Controle de multas  
- O sistema deve calcular, registrar e emitir comprovante de multas por atraso, possibilitando pagamento e baixa no sistema.
- [RF004] Gestão do inventário físico  
- O sistema deve gerenciar o Acervo em dois níveis: metadados bibliográficos (título, autor, gênero) e unidades físicas (Cópias/Exemplares) e a gestão dos estados físicos da cópia (em reparo, extraviado, danificado).
- [RF005] Serviços de pesquisa e histórico do usuário  
- O sistema deve prover todas as ferramentas de consulta. Isso engloba a pesquisa do acervo com filtros avançados, e a consulta do histórico do usuário (itens emprestados, histórico de leitura e status das multas).

---

## 🔒 Requisitos Não Funcionais

- [RNF001] Usabilidade  
- O sistema deve apresentar interface clara, intuitiva e de fácil navegação para usuários e bibliotecários.
- [RNF002] Segurança  
- O sistema deve proteger dados sensíveis, aplicar autenticação obrigatória e utilizar criptografia para senhas.
- [RNF003] Desempenho  
- Consultas e buscas devem ser processadas em até 3 segundos.
- [RNF004] Confiabilidade 
- O sistema deve garantir integridade dos dados durante operações de empréstimo, devolução e atualização.
- [RNF005] Disponibilidade 
- O sistema deve permanecer disponível 24 horas por dia, salvo manutenção programada.

---

## 🏛 Arquitetura do Projeto

```
sistema-biblioteca/
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── livro.html
│   ├── admn_livros.html
│   ├── admn_usuario.html
│   └── styles.css
│
├── backend/
│   ├── library.py
│   └── test_library.py
│
└── README.md
```

---

# 🎨 Protótipo de Telas (Mid-Fidelity)

### 🟣 Tela de Login
![Tela de Login](login.png)

### 🟣 Tela do Catálogo
![Tela do Catálogo](catalogo.png)

### 🟣 Tela de Detalhes do Livro
![Tela de Livros](livros.png)

### 🟣 Tela do Bibliotecário
![Tela do Bibliotecário](adm-livros.png)

### 🟣 Tela do Usuário
![Tela do Usuário](adm-usuarios.png)

---

## 🐍 Backend Simulado em Python

O backend foi construído sem banco de dados, utilizando:

- Listas e Dicionários  
- Funções de CRUD  
- Controle de empréstimos  
- Cálculo de multa  
- Busca de livros  

Principais funções:

- add_user()  
- add_book()  
- borrow_book()  
- return_book()  
- pay_fine()  
- search_books()  

---

## 🧪 Como Executar os Testes

1. Abra o terminal na pasta `backend`  
2. Execute:

```
python -m unittest test_library.py
```

Os testes validam:

- Empréstimo disponível  
- Empréstimo indisponível  
- Devolução com e sem multa  
- Pagamento parcial de multa  
- Busca de livros  

---

## 🛠 Tecnologias Utilizadas

- HTML5  
- CSS3  
- Python 3  
- Estruturas de Dados  
- Paradigma Procedural  
- Testes Unitários  
- Organização de Requisitos  

---

## 👥 Autores

- Marcella Lima Nunes Azevedo  
- João Victor de Moraes da Cruz  
