from flask import Blueprint, request, jsonify
from app import db
from app.models import Task

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')


@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    """Retorna todas as tarefas."""
    # Filtros opcionais
    completed = request.args.get('completed')
    priority = request.args.get('priority')
    
    query = Task.query
    
    if completed is not None:
        completed_bool = completed.lower() == 'true'
        query = query.filter_by(completed=completed_bool)
    
    if priority:
        query = query.filter_by(priority=priority)
    
    tasks = query.order_by(Task.created_at.desc()).all()
    return jsonify([task.to_dict() for task in tasks]), 200


@tasks_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Retorna uma tarefa específica."""
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    return jsonify(task.to_dict()), 200


@tasks_bp.route('/', methods=['POST'])
def create_task():
    """Cria uma nova tarefa."""
    data = request.get_json()
    
    # Validação básica
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    # Validar prioridade
    valid_priorities = ['low', 'medium', 'high']
    priority = data.get('priority', 'medium')
    if priority not in valid_priorities:
        return jsonify({'error': f'Priority must be one of: {", ".join(valid_priorities)}'}), 400
    
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        priority=priority,
        completed=data.get('completed', False)
    )
    
    db.session.add(task)
    db.session.commit()
    
    return jsonify(task.to_dict()), 201


@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza uma tarefa existente."""
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Validar prioridade se fornecida
    if 'priority' in data:
        valid_priorities = ['low', 'medium', 'high']
        if data['priority'] not in valid_priorities:
            return jsonify({'error': f'Priority must be one of: {", ".join(valid_priorities)}'}), 400
    
    # Atualizar campos
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'completed' in data:
        task.completed = data['completed']
    if 'priority' in data:
        task.priority = data['priority']
    
    db.session.commit()
    
    return jsonify(task.to_dict()), 200


@tasks_bp.route('/<int:task_id>/complete', methods=['PATCH'])
def complete_task(task_id):
    """Marca uma tarefa como concluída."""
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    task.completed = True
    db.session.commit()
    
    return jsonify(task.to_dict()), 200


@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Deleta uma tarefa."""
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'message': 'Task deleted successfully'}), 200


@tasks_bp.route('/stats', methods=['GET'])
def get_stats():
    """Retorna estatísticas sobre as tarefas."""
    total = Task.query.count()
    completed = Task.query.filter_by(completed=True).count()
    pending = total - completed
    
    stats = {
        'total': total,
        'completed': completed,
        'pending': pending,
        'by_priority': {
            'low': Task.query.filter_by(priority='low').count(),
            'medium': Task.query.filter_by(priority='medium').count(),
            'high': Task.query.filter_by(priority='high').count()
        }
    }
    
    return jsonify(stats), 200
