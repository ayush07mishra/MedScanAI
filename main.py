import os
from flask import Flask, render_template, redirect, url_for, send_from_directory
from models.medi_scan.app import medicine_bp
from models.health_qa.app import healthqa_bp
from models.nearby_help.app import nearby_bp
from models.mental_health.app import mental_bp
from models.x_ray.app import xray_bp

app = Flask(__name__)

# Register Blueprints for each module
app.register_blueprint(medicine_bp, url_prefix='/medi_scan')
app.register_blueprint(healthqa_bp, url_prefix='/health_qa')
app.register_blueprint(nearby_bp, url_prefix='/nearby_help')
app.register_blueprint(mental_bp, url_prefix='/mental_health')
app.register_blueprint(xray_bp, url_prefix='/x_ray')

@app.route('/')
def home():
    return render_template('index1.html') # Your main landing page

@app.route('/login')
def login():
    return render_template('login.html')

# Serve assets (images) that currently live under templates/
@app.route('/assets/<path:filename>')
def serve_template_assets(filename: str):
    templates_dir = os.path.join(app.root_path, 'templates')
    return send_from_directory(templates_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)