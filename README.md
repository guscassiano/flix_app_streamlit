# 🎬 Flix App - Frontend (Streamlit)

Interface web moderna desenvolvida em Streamlit para o sistema de gerenciamento de filmes Flix API.

## 📋 Sobre o Projeto

O Flix App é a interface frontend do sistema Flix API, proporcionando uma experiência de usuário intuitiva e responsiva para gerenciamento de filmes, atores, gêneros e avaliações. Desenvolvido em Streamlit com foco na usabilidade e performance.

> **📌 Nota**: Este repositório contém apenas o frontend da aplicação. O backend (Flix API) está disponível em repositório separado.

### ✨ Funcionalidades

- 🎭 **Interface de Atores**: Cadastro, listagem e edição de atores/atrizes
- 🎥 **Gerenciamento de Filmes**: Interface completa para o catálogo de filmes
- 🌟 **Sistema de Avaliações**: Interface para reviews com sistema de estrelas
- 🏷️ **Gestão de Gêneros**: CRUD completo de categorias de filmes
- 🔐 **Login Seguro**: Interface de autenticação com JWT
- 📊 **Dashboard Interativo**: Tabelas com AG-Grid e visualizações
- 📱 **Design Responsivo**: Interface adaptável a diferentes telas

## 🏗️ Estrutura do Projeto

```
streamlit/
├── actors/
│   ├── page.py          # Interface de atores
│   ├── service.py       # Lógica de negócio
│   └── repository.py    # Comunicação com API
├── genres/
│   ├── page.py          # Interface de gêneros
│   ├── service.py       # Lógica de negócio
│   └── repository.py    # Comunicação com API
├── movies/
│   ├── page.py          # Interface de filmes
│   ├── service.py       # Lógica de negócio
│   └── repository.py    # Comunicação com API
├── reviews/
│   ├── page.py          # Interface de avaliações
│   ├── service.py       # Lógica de negócio
│   └── repository.py    # Comunicação com API
├── login/
│   ├── page.py          # Interface de login
│   └── service.py       # Autenticação
├── home/
│   └── page.py          # Dashboard principal
├── app.py               # Aplicação principal
└── requirements.txt     # Dependências
```

## 🚀 Tecnologias Utilizadas

- **Streamlit** - Framework para interface web
- **Pandas** - Manipulação e análise de dados
- **AG-Grid** - Tabelas interativas avançadas
- **Requests** - Cliente HTTP para API
- **Python 3.8+** - Linguagem base

## 📦 Instalação e Configuração

### Pré-requisitos
- Python 3.8 ou superior
- Backend Flix API rodando (repositório separado)
- pip (gerenciador de pacotes Python)

### 1. Clone o repositório
```bash
git clone <url-do-repositorio-frontend>
cd flix-app-streamlit
```

### 2. Configurar ambiente virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

Ou instalar manualmente:
```bash
pip install streamlit
pip install pandas
pip install streamlit-aggrid
pip install requests
```

### 4. Configurar conexão com API
No arquivo `repository.py` de cada módulo, configure a URL do backend:

```python
# Para desenvolvimento local
self.__base_url = "http://localhost:8000/api/v1"

# Para produção
self.__base_url = "https://sua-api.herokuapp.com/api/v1"
```

### 5. Executar aplicação
```bash
streamlit run app.py
```

A aplicação estará disponível em: `http://localhost:8501`

## 🎯 Como Usar

### 1. Autenticação
1. Acesse a página de login
2. Digite suas credenciais(cadastradas no backend, cadastre através da Interface de Admin)
3. O sistema armazenará o token JWT automaticamente

### 2. Navegação
Use o menu lateral para acessar as diferentes seções:
- **Início**: Dashboard principal
- **Gêneros**: Gerenciar categorias de filmes
- **Atores/Atrizes**: Cadastro e edição de atores
- **Filmes**: Catálogo completo de filmes
- **Avaliações**: Sistema de reviews

### 3. Funcionalidades por Módulo

#### 🎭 Atores
- **Listar**: Tabela interativa com todos os atores
- **Adicionar**: Formulário com nome, data de nascimento e nacionalidade
- **Editar**: Seleção e atualização de dados existentes
- **Nacionalidades**: Carregamento dinâmico do backend

#### 🏷️ Gêneros
- **CRUD Completo**: Criar, listar, editar e excluir gêneros
- **Interface Intuitiva**: Formulários simples e diretos

#### 🎥 Filmes
- **Catálogo**: Visualização completa dos filmes
- **Filtros**: Busca por gênero, ator, etc.
- **Detalhes**: Informações completas de cada filme

#### 🌟 Avaliações
- **Sistema de Estrelas**: Avaliação de 0 a 5 estrelas
- **Comentários**: Reviews detalhadas dos filmes
- **Listagem**: Todas as avaliações em formato tabular

## 🔧 Arquitetura e Padrões

### Padrão Repository-Service
```
Page (UI) → Service (Business Logic) → Repository (API Communication)
```

### Gerenciamento de Estado
- **Session State**: Cache de dados para performance
- **Token Management**: Armazenamento seguro do JWT
- **Auto-refresh**: Atualização automática após operações

### Tratamento de Erros
- **API Errors**: Tratamento de erros HTTP
- **User Feedback**: Mensagens claras para o usuário
- **Fallbacks**: Comportamento gracioso em falhas

## 📊 Funcionalidades Técnicas

### Cache Inteligente
```python
# Exemplo de cache no service
def get_actors(self):
    if 'actors' in st.session_state:
        return st.session_state.actors
    actors = self.actors_repository.get_actors()
    st.session_state.actors = actors
    return actors
```

### Componentes Reutilizáveis
- Tabelas AG-Grid configuráveis
- Formulários padronizados
- Sistema de notificações
- Validações consistentes

### Otimizações
- **Lazy Loading**: Carregamento sob demanda
- **Caching**: Redução de chamadas à API
- **Componente Keys**: Evita conflitos de elementos

## 🔐 Segurança

### Autenticação JWT
- Token armazenado no session_state
- Auto-logout em caso de token expirado
- Headers de autorização automáticos

### Validações
- Validação de campos obrigatórios
- Formatação de datas
- Sanitização de inputs

## 🚀 Deploy

### Streamlit Cloud
1. Push do código para GitHub
2. Conectar repositório no [Streamlit Cloud](https://streamlit.io/cloud)
3. Configurar variáveis de ambiente
4. Deploy automático

### Heroku
```bash
# Criar Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Deploy
git push heroku main
```

### Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

## 🐛 Resolução de Problemas

### Erro: "Connection Error"
```bash
# Verificar se o backend está rodando
curl http://localhost:8000/api/v1/

# Verificar URL no repository.py
```

### Erro: "Duplicate Element ID"
```python
# Adicionar keys únicos
st.selectbox("Label", options, key="unique_key_name")
```

### Erro: "401 Unauthorized"
```python
# Limpar session e fazer login novamente
st.session_state.clear()
st.rerun()
```

### Performance Lenta
- Verificar cache do session_state
- Reduzir chamadas desnecessárias à API
- Otimizar queries no backend

## 📋 Requirements.txt
```txt
streamlit>=1.28.0
pandas>=1.5.0
streamlit-aggrid>=0.3.4
requests>=2.28.0
```

## 🤝 Integração com Backend

### Endpoints Utilizados
```
GET  /api/v1/actors/              # Listar atores
POST /api/v1/actors/              # Criar ator
PUT  /api/v1/actors/{id}/         # Atualizar ator
GET  /api/v1/nationalities/       # Listar nacionalidades
GET  /api/v1/genres/              # Listar gêneros
POST /api/v1/authentication/          # Autenticação
```

### Formato de Dados
```json
{
  "actors": [
    {
      "id": 1,
      "name": "Nome do Ator",
      "birthday": "1990-01-01",
      "nationality": "Brasil"
    }
  ]
}
```

## 📝 Contribuição

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nova-feature`
3. Desenvolva a funcionalidade
4. Teste localmente
5. Commit: `git commit -m 'Add: nova feature'`
6. Push: `git push origin feature/nova-feature`
7. Abra um Pull Request

### Padrões de Commit
- `Add:` - Nova funcionalidade
- `Fix:` - Correção de bug
- `Update:` - Atualização de funcionalidade
- `Remove:` - Remoção de código

## 👨‍💻 Autor

**Gustavo Cassiano**
- Email: [gucpinto26@gmail.com]
- LinkedIn: https://linkedin.com/in/gustavocassiano-dev
- GitHub: https://github.com/guscassiano

---

## 🔗 Repositórios Relacionados

- **Backend (Flix API)**: https://github.com/guscassiano/flix_api

---

⭐ Se este projeto te ajudou, deixe uma estrela no repositório!