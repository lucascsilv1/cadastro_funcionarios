# API de Cadastro e Gestão de Funcionários

Esta é uma API simples desenvolvida em Python utilizando o framework **FastAPI** para o cadastro e gestão de informações básicas sobre funcionários.

## Funcionalidades

A API permite as seguintes operações:

- Cadastrar um novo funcionário.
- Listar todos os funcionários cadastrados.
- Consultar um funcionário específico pelo CPF.
- Atualizar as informações de um funcionário existente.
- Excluir um funcionário pelo CPF.

## Estrutura de Dados

A entidade **Pessoa** possui os seguintes atributos:

- **nome_completo**: Nome completo do funcionário.
- **data_nascimento**: Data de nascimento (formato: YYYY-MM-DD).
- **endereco**: Endereço do funcionário.
- **cpf**: CPF do funcionário (formato: XXX.XXX.XXX-XX).
- **estado_civil**: Estado civil do funcionário.

## Tecnologias Utilizadas

- Python
- FastAPI
- Uvicorn (servidor ASGI)

## Pré-requisitos

Antes de executar a aplicação, é necessário ter o Python instalado em sua máquina. Você também pode criar um ambiente virtual (opcional) para gerenciar as dependências.

## Passos para Instalação e Execução

### 1. Clone este repositório:

```bash
git clone https://github.com/lucascsilv1/cadastro_funcionarios.git
cd cadastro_funcionarios
```

### 2. Crie e ative um ambiente virtual (opcional):

```bash
python -m venv venv
# Ativar no Windows
.\venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências:

```bash
pip install fastapi uvicorn
```

### 4. Execução da Aplicação

Para rodar a aplicação, execute o seguinte comando:

```bash
uvicorn main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

## Documentação da API

A documentação interativa da API pode ser acessada em:

```
http://127.0.0.1:8000/docs
```

## Testando a API

Você pode testar as operações disponíveis na API através da interface Swagger, que permite fazer requisições HTTP diretamente pelo navegador.

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. 

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

