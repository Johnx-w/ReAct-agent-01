from my_llm import HelloAgentsLLM, ToolExecutor, search, ReActAgent

# 1. 初始化 LLM
llm = HelloAgentsLLM()

# 2. 初始化工具并注册
executor = ToolExecutor()
executor.registerTool("Search", "一个网页搜索引擎，用于搜索实时信息", search)

# 3. 创建 Agent 并运行
agent = ReActAgent(llm, executor, max_steps=5)
agent.run("2026年的奥运会举办地是哪里")