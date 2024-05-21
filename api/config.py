import os


class Config:
    STATIC_PAGES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/pages')
    MONGODB_SETTINGS = {
        'db': 'rob_b_hood',
        'host': os.getenv("MONGODB_HOST")
    }


REDIS_SETTINGS = {
    'host': os.getenv("REDIS_HOST"),
    'port': os.getenv("REDIS_PORT"),
    'db': os.getenv("REDIS_DB"),
    'password': os.getenv("REDIS_PASS")
}


tags = {'array': '数组', 'hash-table': '哈希表', 'recursion': '递归', 'linked-list': '链表', 'math': '数学', 'string': '字符串', 'sliding-window': '滑动窗口', 'binary-search': '二分查找', 'divide-and-conquer': '分治', 'dynamic-programming': '动态规划', 'greedy': '贪心', 'two-pointers': '双指针', 'trie': '字典树', 'sorting': '排序', 'backtracking': '回溯', 'stack': '栈', 'heap-priority-queue': '堆（优先队列）', 'merge-sort': '归并排序', 'string-matching': '字符串匹配', 'bit-manipulation': '位运算', 'matrix': '矩阵', 'monotonic-stack': '单调栈', 'simulation': '模拟', 'combinatorics': '组合数学', 'memoization': '记忆化搜索', 'tree': '树', 'depth-first-search': '深度优先搜索', 'binary-tree': '二叉树', 'binary-search-tree': '二叉搜索树', 'breadth-first-search': '广度优先搜索', 'union-find': '并查集', 'graph': '图', 'design': '设计', 'doubly-linked-list': '双向链表', 'geometry': '几何', 'interactive': '交互', 'bucket-sort': '桶排序', 'radix-sort': '基数排序', 'counting': '计数', 'iterator': '迭代器', 'hash-function': '哈希函数', 'rolling-hash': '滚动哈希', 'enumeration': '枚举', 'number-theory': '数论', 'topological-sort': '拓扑排序', 'prefix-sum': '前缀和', 'quickselect': '快速选择', 'binary-indexed-tree': '树状数组', 'segment-tree': '线段树', 'ordered-set': '有序集合', 'line-sweep': '扫描线', 'queue': '队列', 'monotonic-queue': '单调队列', 'counting-sort': '计数排序', 'brainteaser': '脑筋急转弯', 'game-theory': '博弈', 'data-stream': '数据流', 'eulerian-circuit': '欧拉回路', 'randomized': '随机化', 'reservoir-sampling': '水塘抽样', 'shortest-path': '最短路', 'bitmask': '状态压缩', 'probability-and-statistics': '概率与统计', 'rejection-sampling': '拒绝采样', 'suffix-array': '后缀数组', 'minimum-spanning-tree': '最小生成树', 'concurrency': '多线程', 'biconnected-component': '双连通分量', 'strongly-connected-component': '强连通分量'}
