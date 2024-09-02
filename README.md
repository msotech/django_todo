# To Do List API

Esta é uma API simples para gerenciar tarefas de uma lista de afazeres (To Do) construída com Django Rest Framework.

## Funcionalidades

A API permite as seguintes operações:

- **Criar Tarefas:** Adicionar novas tarefas à lista.
- **Listar Tarefas:** Exibir todas as tarefas existentes.
- **Detalhar Tarefa:** Exibir detalhes específicos de uma tarefa.
- **Atualizar Tarefa:** Modificar uma tarefa existente.
- **Completar Tarefa:** Marcar uma tarefa como concluída.
- **Deletar Tarefa:** Remover uma tarefa da lista.

## Endpoints

### Criar Tarefa

- **Método:** `POST`
- **Endpoint:** `/api/todos/`
- **Descrição:** Cria uma nova tarefa.

### Listar Tarefas

- **Método:** `GET`
- **Endpoint:** `/api/todos/`
- **Descrição:** Retorna todas as tarefas da lista.

### Detalhar Tarefa

- **Método:** `GET`
- **Endpoint:** `/api/todos/{id}/`
- **Descrição:** Retorna detalhes de uma tarefa específica.

### Atualizar Tarefa

- **Método:** `PUT`
- **Endpoint:** `/api/todos/{id}/`
- **Descrição:** Atualiza uma tarefa existente.

### Completar Tarefa

- **Método:** `PATCH`
- **Endpoint:** `/api/todos/{id}/`
- **Descrição:** Marca uma tarefa como concluída.

### Deletar Tarefa

- **Método:** `DELETE`
- **Endpoint:** `/api/todos/{id}/`
- **Descrição:** Remove uma tarefa da lista.

## Funcionamento

Este aplicativo é baseado no Django e utiliza o Django Rest Framework (DRF) para construir uma API RESTful. As tarefas são armazenadas em um banco de dados SQLite por padrão, mas você pode configurar o banco de dados de sua escolha.

### Estrutura do Projeto

- **Models:** O modelo `todo` define a estrutura de uma tarefa, incluindo campos para título, descrição, status de conclusão, data de criação e data de atualização.
- **Serializers:** O `serializers` é responsável por converter os objetos todos em JSON e vice-versa.
- **Views:** As views da API são baseadas nas classes genéricas do DRF, como `ToDoCreateListView`, `ToDoView`, e são personalizadas conforme necessário.
- **URLs:** O arquivo de URLs mapeia os endpoints para as views correspondentes.

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/msotech/django_todo.git
