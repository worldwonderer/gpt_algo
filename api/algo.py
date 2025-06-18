import json
import os
from flask import Blueprint, render_template, request, abort, jsonify, current_app, send_from_directory, redirect, url_for

from .config import tags
from .vote import get_likes_count, get_dislikes_count, incr_likes_count, incr_dislikes_count

from wrap import fuzzy_search


bp = Blueprint('main', __name__)

_all_problems = None


def get_all_problems():
    global _all_problems
    if _all_problems is None:
        file_path = os.path.join(os.path.dirname(__file__), 'static', 'all_problems.json')
        with open(file_path, 'r', encoding='utf-8') as f:
            _all_problems = json.load(f)
    return _all_problems


@bp.route('/')
def index():
    return redirect(url_for('main.problems'))


@bp.route('/problems')
def problems():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '')
    selected_tag = request.args.get('tag', '')

    all_problems_data = get_all_problems()

    # 过滤问题
    filtered_problems = []
    if search_query or selected_tag:
        for problem in all_problems_data:
            match = True
            if selected_tag and selected_tag not in problem.get('tags_q', []):
                match = False
            if search_query and search_query.lower() not in (problem.get('title_cn') or '').lower():
                match = False
            if match:
                filtered_problems.append(problem)
    else:
        filtered_problems = all_problems_data

    # 分页
    per_page = 14
    total_count = len(filtered_problems)
    total_pages = (total_count + per_page - 1) // per_page
    start = (page - 1) * per_page
    end = start + per_page
    paginated_problems = filtered_problems[start:end]

    return render_template('index.html', problems=paginated_problems, tags=tags,
                           search_query=search_query, selected_tag=selected_tag,
                           page=page, total_pages=total_pages, rt=f'{bp.name}.{problems.__name__}')


@bp.route('/problem/<title_slug>')
def problem_detail(title_slug):
    static_file_dir = current_app.config['STATIC_PAGES_DIR']
    static_file_name = f'{title_slug}.html'

    try:
        return send_from_directory(static_file_dir, static_file_name)
    except FileNotFoundError:
        abort(404)


@bp.route('/api/vote_count/<title_slug>')
def vote_count(title_slug):
    # 伪代码：获取问题的点赞和点踩数量
    data = {
        "likes": get_likes_count(title_slug),
        "dislikes": get_dislikes_count(title_slug)
    }
    return jsonify(data)


@bp.route('/api/vote/<title_slug>/<vote_type>', methods=['POST'])
def vote(title_slug, vote_type):
    likes = None
    dislikes = None
    if vote_type == "like":
        likes = incr_likes_count(title_slug)
    elif vote_type == "dislike":
        dislikes = incr_dislikes_count(title_slug)
    return jsonify({"likes": likes, "dislikes": dislikes})
