from flask import Blueprint, render_template, request, abort, jsonify

from .models import Problem
from .config import tags
from .vote import get_likes_count, get_dislikes_count, incr_likes_count, incr_dislikes_count

from wrap import fuzzy_search


bp = Blueprint('main', __name__)


@bp.route('/problems')
def problems():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '')
    selected_tag = request.args.get('tag', '')

    # 构建查询条件
    query = {}
    if search_query:
        query['title_cn__icontains'] = search_query
    if selected_tag:
        query['tags_q__in'] = [selected_tag]

    # 分页和查询问题列表
    # 计算跳过的文档数量
    per_page = 15
    skip = (page - 1) * per_page

    # 查询并分页问题列表
    problem_list = Problem.objects(**query).skip(skip).limit(per_page)
    total_count = problem_list.count()

    if total_count == 0 and len(search_query) > 2:  # 在未命中任何题目，且有足够的信息时，进行模糊搜索
        title_slug = fuzzy_search(search_query)
        problem_list = Problem.objects(_id=title_slug)
        total_count = problem_list.count()

    # 计算总页数
    total_pages = (total_count + per_page - 1) // per_page

    return render_template('index.html', problems=problem_list, tags=tags,
                           search_query=search_query, selected_tag=selected_tag,
                           page=page, total_pages=total_pages)


@bp.route('/problem/<title_slug>')
def problem_detail(title_slug):
    try:
        problem = Problem.objects.get(title_slug=title_slug)
        return render_template('detail.html', problem=problem)
    except Problem.DoesNotExist:
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
