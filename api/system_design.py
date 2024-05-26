from flask import Blueprint, render_template, request, abort

from .models import SystemDesign, SystemDesignSolution


sd_bp = Blueprint('sd', __name__, url_prefix='/sd')


@sd_bp.route('/problems')
def problems():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '')

    # 构建查询条件
    query = {}
    if search_query:
        query['title_zh__icontains'] = search_query

    # 分页和查询问题列表
    # 计算跳过的文档数量
    per_page = 12
    skip = (page - 1) * per_page

    # 查询并分页问题列表
    problem_list = SystemDesign.objects(**query).skip(skip).limit(per_page)
    total_count = problem_list.count()

    # 计算总页数
    total_pages = (total_count + per_page - 1) // per_page

    return render_template('sd_index.html', problems=problem_list,
                           search_query=search_query, page=page,
                           total_pages=total_pages, rt=f'{sd_bp.name}.{problems.__name__}')


@sd_bp.route('/problem/<path:path_name>')
def problem_detail(path_name):
    problem = SystemDesign.objects(problem_path_name=path_name).first()
    if problem is None:
        abort(404)
    problem.description_zh = problem.description_zh.split('**')[-1].strip()
    solution = SystemDesignSolution.objects(problem_path_name=path_name).order_by('-score').first()
    return render_template('sd_detail.html', problem=problem, solution=solution)
