from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Configurações
    if config_name == 'testing':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
        app.config['TESTING'] = False
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    
    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registrar blueprints
    from app.routes import tasks_bp
    app.register_blueprint(tasks_bp)
    
    # Criar tabelas
    with app.app_context():
        db.create_all()
    
    return app
