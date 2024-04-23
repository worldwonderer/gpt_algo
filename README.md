# GPT Algo

GPT Algo 利用 GPT-4 的代码理解能力，为 LeetCode 算法题提供高质量的题解和解答说明。

## 在线演示

你可以通过访问以下网址查看 GPT Algo 的在线演示：

[演示站点](https://algo.pitechan.com/problems)

## 快速上手

1. 克隆仓库到本地：

```
git clone https://github.com/worldwonderer/gpt_algo.git
```

2. 进入项目目录：

```
cd gpt_algo
```

3. 安装所需的Python依赖：

```
pip install -r requirements.txt
```

4. 环境变量：

```
# redis 点赞、点踩计数存储
REDIS_HOST=<your_redis_host>
REDIS_PORT=<your_redis_port>
REDIS_DB=<your_redis_db>
REDIS_PASS=<your_redis_password>

# mongodb 题解存储，mongodb://，数据集暂时没找到合适的共享方式，可联系我提供
MONGODB_HOST=<your_mongodb_host>

# （可选）dify 题目模糊搜索，基于 dify 知识库 + GPT-3.5
DIFY_API_KEY=<your_dify_api_key> 
```

5. 运行Flask应用：

```
python debug.py
```

6. 在浏览器中访问 `http://localhost:5000` 即可使用GPT Algo。

## 贡献

欢迎对 GPT Algo 项目做出贡献！如果你发现了任何问题或有改进建议，请在 GitHub 上提交 Issue 或 Pull Request。

目前已发现部分题解不符合题目规范，可参阅 [无效题解列表](https://docs.qq.com/sheet/DUEVMb0x0SGhqZWVn?tab=BB08J2)。

## 许可证

GPT Algo 项目采用 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。

## 联系方式
如果你有任何问题或建议，欢迎通过以下方式联系我：

邮箱: xtchen.pitt@gmail.com