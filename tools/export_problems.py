import os
import json
from mongoengine import connect

from api.models import Problem
from api.config import Config


def export_problems_to_json():
    """
    连接到 MongoDB，获取所有问题数据，并将其保存为 JSON 文件。
    """
    # 使用 Config 中的设置连接到数据库
    connect(db=Config.MONGODB_SETTINGS['db'], host=Config.MONGODB_SETTINGS['host'])

    # 获取所有问题
    problems = Problem.objects.only('_id', 'title_cn', 'difficulty', 'tags_q', 'paid_only', 'ac_rate', 'frontend_id', 'title_slug')

    problem_list = []
    for problem in problems:
        problem_list.append({
            '_id': problem._id,
            'title_cn': problem.title_cn,
            'difficulty': problem.difficulty,
            'tags_q': problem.tags_q,
            'paid_only': problem.paid_only,
            'ac_rate': problem.ac_rate,
            'frontend_id': problem.frontend_id,
            'title_slug': problem.title_slug
        })

    # 定义输出文件路径
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'api', 'static')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'all_problems.json')

    # 将数据写入 JSON 文件
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(problem_list, f, ensure_ascii=False, indent=4)

    print(f"成功将 {len(problem_list)} 个问题导出到 {output_path}")


if __name__ == '__main__':
    export_problems_to_json()
