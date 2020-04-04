from access.homepage import homepage_access
from access.approval import approval_access
from access.project import project_access
from access.project_detail import project_detail_access
from access.backstage import backstage_access
from flask import Flask
from flask_cors import *

app = Flask(__name__)
app.register_blueprint(homepage_access, url_prefix='/api/homepage')
app.register_blueprint(approval_access, url_prefix='/api/approval')
app.register_blueprint(project_access, url_prefix='/api/project')
app.register_blueprint(project_detail_access, url_prefix='/api/project_detail')
app.register_blueprint(backstage_access, url_prefix='/api/back')

CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run(port=7777, debug=True, host='127.0.0.1')
