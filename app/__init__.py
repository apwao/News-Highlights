from flask import Flask
from config import config_options





def create_app(config_name):
    """
    function create_app to help load configurations dynamically
    """
    
    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])


    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Setting config
    from .requests import configure_request
    configure_request(app)


    return app
