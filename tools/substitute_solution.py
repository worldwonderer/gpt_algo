import os
import json
import logging

import html2text
from pymongo import MongoClient
from langchain_openai import ChatOpenAI

# 连接远程 MongoDB
client = MongoClient(os.getenv("MONGODB_HOST"))

# 选择数据库和集合
db = client['rob_b_hood']
collection = db['leetcode']


def read_prompt(name):
    with open('../prompts/' + name + '.md', 'r') as f:
        return f.read()


def parse_response(res):
    clean_json = res.content.split('```json\n')[-1].replace('\n```', '')
    try:
        data = json.loads(clean_json)
    except json.JSONDecodeError as e:
        logging.error(f'parse res json err {clean_json}', e)
        return
    return data


def update_solution(title_slug, code):
    chat = ChatOpenAI(model_name='gpt-4', temperature=0.7)
    doc = collection.find_one({'_id': title_slug})
    # acquire solution explanation first
    desc_text = '\n'.join([html2text.html2text(x) for x in [doc['title_cn'] or '', doc['content_cn'] or '']])[:500]
    explain_template = read_prompt('explain')
    explain_prompt = explain_template.replace('${desc}', desc_text).replace('${code}', code)
    res = chat.invoke(explain_prompt)
    explain = parse_response(res)['solution']
    print('explain', explain)
    collection.update_one({'_id': doc['_id']}, {'$set': {'explain': explain}})
    # acquire solution follow-up
    explain_text = '\n'.join([explain['approach'].strip(), '时间复杂度: ' +
                              explain['timeComplexity']['result'], '空间复杂度: ' +
                              explain['spaceComplexity']['result'], explain['code']])
    question_template = read_prompt('follow_up')
    question_prompt = question_template.replace('${desc}', desc_text).replace('${explain}', explain_text)
    res = chat.invoke(question_prompt)
    questions = parse_response(res)
    print('questions', questions)
    # acquire follow-up answers
    answer_template = read_prompt('follow_up_answer')
    answer_prompt = answer_template.replace('${desc}', desc_text).replace('${explain}', explain_text).replace(
        '${question_list}', json.dumps(questions))
    res = chat.invoke(answer_prompt)
    explore = parse_response(res)['questions']
    print('explore', explore)
    collection.update_one({'_id': doc['_id']}, {'$set': {'explore': explore}})
    collection.update_one({'_id': doc['_id']}, {'$set': {'submission.code': code}})


if __name__ == '__main__':
    example_title_slug = 'longest-common-prefix'
    example_code = '''class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))
    
        if not strs:
            return ""
    
        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1
    
        return strs[0][:low]'''
    update_solution(example_title_slug, example_code)
