from flask import Flask
from flask_mongoengine import MongoEngine

from .routes import bp
from .filters import difficulty_filter, remove_empty_paragraphs, format_code
from .config import MONGODB_SETTINGS

app = Flask(__name__)

# 配置 MongoDB
app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS

# 配置 jinja2 过滤器
app.jinja_env.filters['difficulty'] = difficulty_filter
app.jinja_env.filters['remove_empty_p'] = remove_empty_paragraphs
app.jinja_env.filters['format_code'] = format_code

# 初始化 MongoEngine
db = MongoEngine(app)

# 注册蓝图
app.register_blueprint(bp)
