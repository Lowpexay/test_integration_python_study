# 📝 Task Manager API - Playground para Testes Integrados

Este é um projeto de API REST simples para gerenciamento de tarefas, criado especificamente para **prática de testes integrados**.

## 🎯 Objetivo

Este projeto serve como **playground** para você praticar a criação de testes integrados em Python. A aplicação já está funcional - seu trabalho é criar os testes!

## 🚀 Como Rodar

1. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

2. **Rodar a aplicação:**
```bash
python run.py
```

A API estará disponível em `http://localhost:5000`

## 📚 Endpoints Disponíveis

### 1. **Listar todas as tarefas**
```
GET /api/tasks/
```
Query params opcionais:
- `completed=true/false` - Filtrar por status
- `priority=low/medium/high` - Filtrar por prioridade

### 2. **Buscar tarefa específica**
```
GET /api/tasks/<id>
```

### 3. **Criar nova tarefa**
```
POST /api/tasks/
Content-Type: application/json

{
  "title": "Minha tarefa",
  "description": "Descrição opcional",
  "priority": "high",
  "completed": false
}
```

### 4. **Atualizar tarefa**
```
PUT /api/tasks/<id>
Content-Type: application/json

{
  "title": "Título atualizado",
  "description": "Nova descrição",
  "priority": "low",
  "completed": true
}
```

### 5. **Marcar como concluída**
```
PATCH /api/tasks/<id>/complete
```

### 6. **Deletar tarefa**
```
DELETE /api/tasks/<id>
```

### 7. **Estatísticas**
```
GET /api/tasks/stats
```

## 🧪 Estrutura do Projeto

```
python_integrated_tests/
├── app/
│   ├── __init__.py      # Configuração da aplicação Flask
│   ├── models.py        # Modelo de dados (Task)
│   └── routes.py        # Endpoints da API
├── tests/
│   └── test_integration.py  # AQUI VÃO SEUS TESTES!
├── run.py               # Arquivo para rodar a aplicação
├── requirements.txt     # Dependências
└── README.md           # Este arquivo
```

## ✅ O Que Seus Testes Integrados Devem Validar

Crie testes integrados no arquivo `tests/test_integration.py` para validar:

1. **Criação de tarefas**
   - Criar uma tarefa com sucesso
   - Validar que título é obrigatório
   - Validar prioridades válidas (low, medium, high)
   - Validar valores padrão (completed=False, priority=medium)

2. **Listagem de tarefas**
   - Listar todas as tarefas
   - Filtrar por status (completed)
   - Filtrar por prioridade
   - Verificar ordenação (mais recentes primeiro)

3. **Busca de tarefa específica**
   - Buscar tarefa existente
   - Buscar tarefa inexistente (erro 404)

4. **Atualização de tarefas**
   - Atualizar título, descrição, prioridade
   - Atualizar tarefa inexistente (erro 404)
   - Validar campos opcionais

5. **Marcar como concluída**
   - Marcar tarefa como concluída
   - Verificar que o status foi alterado

6. **Deleção de tarefas**
   - Deletar tarefa existente
   - Deletar tarefa inexistente (erro 404)
   - Verificar que foi removida do banco

7. **Estatísticas**
   - Contar total de tarefas
   - Contar tarefas completadas/pendentes
   - Contar por prioridade

8. **Fluxos completos (cenários end-to-end)**
   - Criar → Listar → Atualizar → Completar → Deletar
   - Criar múltiplas tarefas e filtrar
   - Validar persistência entre requisições

## 🔧 Dicas para os Testes

- Use `pytest` como framework de testes
- Use `pytest-flask` para facilitar os testes
- Use fixtures para criar um cliente de teste limpo
- Use banco de dados em memória (SQLite) para testes
- Teste tanto casos de sucesso quanto de erro
- Valide códigos HTTP (200, 201, 404, 400)
- Valide estrutura JSON das respostas
- Teste edge cases (strings vazias, IDs inválidos, etc.)

## 🎓 Para Validar no GitHub

1. **Inicialize o repositório:**
```bash
git init
git add .
git commit -m "Initial commit: Task Manager API"
```

2. **Crie um repositório no GitHub**

3. **Push para o GitHub:**
```bash
git remote add origin <sua-url-do-github>
git branch -M main
git push -u origin main
```

4. **Configure GitHub Actions** (opcional - para rodar testes automaticamente)

---

**Boa sorte com seus testes integrados! 🚀**
