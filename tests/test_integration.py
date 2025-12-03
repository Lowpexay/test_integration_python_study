"""
Testes Integrados para a API de Gerenciamento de Tarefas

INSTRUÇÕES:
-----------
Este arquivo contém um exemplo básico de teste integrado.
Sua missão é expandir estes testes para cobrir todos os cenários!

Para rodar os testes:
    pytest tests/test_integration.py -v

O que você precisa testar está documentado no README.md
"""

import pytest
from app import create_app, db
from app.models import Task


@pytest.fixture
def app():
    """Cria uma instância da aplicação configurada para testes."""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Cria um cliente de teste."""
    return app.test_client()


# ==========================================
# EXEMPLO DE TESTE BÁSICO
# ==========================================

def test_create_task_success(client):
    """
    EXEMPLO: Testa a criação bem-sucedida de uma tarefa.
    
    Este é um exemplo de teste integrado básico.
    Você deve criar testes similares para outros cenários!
    """
    # Arrange (Preparar)
    task_data = {
        'title': 'Minha primeira tarefa',
        'description': 'Aprender testes integrados',
        'priority': 'high'
    }
    
    # Act (Agir)
    response = client.post('/api/tasks/', json=task_data)
    
    # Assert (Verificar)
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == task_data['title']
    assert data['description'] == task_data['description']
    assert data['priority'] == task_data['priority']
    assert data['completed'] is False
    assert 'id' in data
    assert 'created_at' in data


# ==========================================
# AGORA É COM VOCÊ! 
# ==========================================
# 
# Crie testes para validar:
#
# 1. CRIAÇÃO DE TAREFAS:
#    - Criar tarefa sem título (deve falhar)
#    - Criar tarefa com prioridade inválida (deve falhar)
#    - Criar tarefa apenas com título (campos opcionais devem ter valores padrão)
#
# DICA: Em testes INTEGRADOS, você deve testar através da API (usando o client),
#       não acessando o banco de dados diretamente!
#
def test_create_task_without_title(client):
    response = client.post('/api/tasks/', json={})
    assert response.status_code == 400
    assert 'error' in response.get_json()


# 2. LISTAGEM DE TAREFAS:
#    - Listar quando não há tarefas
#    - Listar múltiplas tarefas
#    - Filtrar por completed=true
#    - Filtrar por priority

def test_list_tasks_empty(client):
    response = client.get('/api/tasks/')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 0




#
# 3. BUSCAR TAREFA ESPECÍFICA:
#    - Buscar tarefa existente
#    - Buscar tarefa que não existe (404)
#
def test_get_task_not_found(client):
    response = client.get('/api/tasks/999')
    assert response.status_code == 404
    assert 'error' in response.get_json()


# 4. ATUALIZAR TAREFA:
#    - Atualizar título
#    - Atualizar múltiplos campos
#    - Atualizar tarefa inexistente (404)
#
def test_update_task_not_found(client):
    response = client.put('/api/tasks/999', json={'title': 'Updated Title'})
    assert response.status_code == 404
    assert 'error' in response.get_json()

# 5. MARCAR COMO CONCLUÍDA:
#    - Marcar tarefa como concluída
#    - Verificar que completed=True
#
def test_complete_task(client):
    # Criar uma tarefa primeiro
    response = client.post('/api/tasks/', json={'title': 'Task to complete'})
    assert response.status_code == 201
    task_id = response.get_json()['id']
    
    # Marcar como concluída
    response = client.patch(f'/api/tasks/{task_id}/complete')
    assert response.status_code == 200
    data = response.get_json()
    assert data['completed'] is True



# 6. DELETAR TAREFA:
#    - Deletar tarefa existente
#    - Verificar que foi removida
#    - Deletar tarefa inexistente (404)
#

def test_delete_task_not_found(client):
    response = client.delete('/api/tasks/999')
    assert response.status_code == 404
    assert 'error' in response.get_json()


# 7. ESTATÍSTICAS:
#    - Verificar contadores
#    - Verificar contagem por prioridade
#

def test_task_statistics(client):
    # Criar algumas tarefas
    client.post('/api/tasks/', json={'title': 'Task 1', 'priority': 'low'})
    client.post('/api/tasks/', json={'title': 'Task 2', 'priority': 'high'})
    client.post('/api/tasks/', json={'title': 'Task 3', 'priority': 'medium'})
    
    # Obter estatísticas
    response = client.get('/api/tasks/stats')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total'] == 3
    assert data['by_priority']['low'] == 1
    assert data['by_priority']['medium'] == 1
    assert data['by_priority']['high'] == 1


# 8. CENÁRIOS COMPLEXOS (End-to-End):
#    - Criar → Listar → Atualizar → Completar → Deletar
#    - Criar várias tarefas e filtrar
#
# ==========================================

# TODO: Adicione seus testes aqui!
