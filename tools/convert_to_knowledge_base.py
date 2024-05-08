import os

from pymongo import MongoClient
from bs4 import BeautifulSoup

# 连接远程 MongoDB
client = MongoClient(os.getenv("MONGODB_HOST"))

# 选择数据库和集合
db = client['rob_b_hood']
collection = db['leetcode']

mapping = {1: '简单', 2: '中等', 3: '困难'}


def convert_cn():
    with open('leetcode_solutions_cn.txt', 'w', encoding='utf-8') as file:
        # 查询所有题解
        solutions = collection.find()

        for solution in solutions:
            # 提取需要的字段
            title_cn = solution['title_cn']
            difficulty = mapping[solution['difficulty']]
            tags = ', '.join(solution['tags'].values())
            similar_questions = ', '.join(solution['similar_questions'].values())

            # 解析 HTML 内容
            content_cn = BeautifulSoup(solution['content_cn'] or '', 'html.parser').get_text()

            # 获取解题方法和复杂度分析
            approach = solution['explain']['approach']
            time_complexity = solution['explain']['timeComplexity']['result']
            space_complexity = solution['explain']['spaceComplexity']['result']
            code = solution['explain']['code']

            # 获取 follow up 部分
            explore = solution['explore']

            # 将信息写入 txt 文件
            file.write(f"题目：{title_cn}\n\n")
            file.write(f"难度：{difficulty}\n\n")
            file.write(f"标签：{tags}\n\n")
            file.write(f"题目描述：\n{content_cn}\n\n")
            file.write(f"解题方法：\n{approach}\n\n")
            file.write(f"时间复杂度：{time_complexity}\n\n")
            file.write(f"空间复杂度：{space_complexity}\n\n")
            file.write(f"代码：\n{code}\n\n")
            file.write("常见问题：\n")
            for item in explore:
                file.write(f"\t问题：{item['content']}\n")
                file.write(f"\t解释：{item['explanation']}\n")
            file.write("\n")
            file.write(f"相似题目：{similar_questions}\n")
            file.write("==========\n\n")
    print("中文版知识库 txt 文件转换完成")


if __name__ == '__main__':
    convert_cn()
