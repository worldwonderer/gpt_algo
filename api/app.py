from flask import Flask
from flask_mongoengine import MongoEngine

from .algo import bp
from .system_design import sd_bp
from .filters import difficulty_filter, remove_empty_paragraphs, format_code, clean_remote_html
from .config import Config

app = Flask(__name__)

# 配置 MongoDB
app.config.from_object(Config)

# 配置 jinja2 过滤器
app.jinja_env.filters['difficulty'] = difficulty_filter
app.jinja_env.filters['remove_empty_p'] = remove_empty_paragraphs
app.jinja_env.filters['format_code'] = format_code
app.jinja_env.filters['clean_remote_html'] = clean_remote_html

# 初始化 MongoEngine
db = MongoEngine(app)

# 注册蓝图
app.register_blueprint(bp)
app.register_blueprint(sd_bp)
