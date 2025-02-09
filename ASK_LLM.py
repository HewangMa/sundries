import os
from openai import OpenAI
from config import *
import argparse

qwen_client = OpenAI(
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
# 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
qwen_models = ['qwen-max', 'qwen-plus', 'qwen-turbo', 'qwen-long']

deepseek_client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)
# 模型列表：https://api-docs.deepseek.com/zh-cn/quick_start/pricing
deepseek_models = ['deepseek-reasoner', 'deepseek-chat']


def ask_llm(client, model, rule, question):
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {'role': 'system', 'content': rule},
                {'role': 'user', 'content': question}
            ]
        )
        logger.info(
            f"\nfor question: {question}, got answer: {completion.choices[0].message.content}\n")
    except Exception as e:
        logger.warning(f"错误信息：{e}")


def get_embeddings():

    client = OpenAI(
        api_key=os.getenv("QWEN_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 百炼服务的base_url
    )

    completion = client.embeddings.create(
        model="text-embedding-v3",
        input='衣服的质量杠杠的，很漂亮，不枉我等了这么久啊，喜欢，以后还来这里买',
        dimensions=1024,
        encoding_format="float"
    )

    print(completion.model_dump_json())


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="处理多参数示例")
    # parser.add_argument("question", help="输入问题")
    # args = parser.parse_args()
    model1 = deepseek_models[0]
    rule1 = "你是一个中国八字占卜的专家"
    # 请基于以下结构化数据，以[指定流派，如中国八字/西方占星/紫微斗数]理论为基础，遵循传统命理框架进行综合分析：
    question1 = '''请基于以下结构化数据，以中国八字理论为基础，遵循传统命理框架进行综合分析：

        【用户信息】
        1. 出生日期：阳历 1999-10-30/农历九月二十二
        2. 出生时间：05:20
        3. 性别：男
        4. 出生地点：中国安徽省霍山县
        5. 关注领域：[事业/感情/健康/财富等]

        【专业要求】
        1. 信息校验：自动检测历法转换需求（如阳历转干支历）
        2. 术语解释：对专业名词（如"正官格"、"上升星座"）进行括号注释
        3. 三维分析：
        - 先天格局（出生时空能量组合）
        - 大运走势（按年龄阶段划分）
        - 年度建议（结合当前年份）
        4. 呈现形式：
        ① 关键星盘/八字排盘（文字版）
        ② 优势机遇（3点）
        ③ 注意事项（3点）
        ④ 增强建议（穿戴/方位/生活习惯等）'''
    question1_1 = '''请基于以下结构化数据，以中国八字理论为基础，遵循传统命理框架进行综合分析：

        【用户信息】
        1. 出生日期：阳历 2001-05-14
        2. 出生时间：16:30
        3. 性别：女
        4. 出生地点：中国安徽省霍山县
        5. 关注领域：[事业/感情/健康/财富等]

        【专业要求】
        1. 信息校验：自动检测历法转换需求（如阳历转干支历）
        2. 术语解释：对专业名词（如"正官格"、"上升星座"）进行括号注释
        3. 三维分析：
        - 先天格局（出生时空能量组合）
        - 大运走势（按年龄阶段划分）
        - 年度建议（结合当前年份）
        4. 呈现形式：
        ① 关键星盘/八字排盘（文字版）
        ② 优势机遇（3点）
        ③ 注意事项（3点）
        ④ 增强建议（穿戴/方位/生活习惯等）'''

    model2 = qwen_models[0]
    rule2 = '你是一个精通使用阿里云服务和flask开发的专家'
    question2 = '''怎么在服务器中生成ssh密钥并上传到github使用？'''

    model3 = qwen_models[0]
    rule3 = '你是一个图像和视频处理的开发专家'
    question3 = '''
            thumb_path = f"{filename_list[0]}.jpg"
            num_frames = 20
            frames, width, height = capture_frames(vid_path, num_frames)
            if frames:
                thumbnail = create_thumbnail(frames, width, height, columns=5)
                cv2.imwrite(thumb_path, thumbnail)
                print(f"Thumbnail saved to {thumb_path}")
            这段代码用来从vid生成thumb，如何支持thumb的名称中含有中文？
    '''

    rule4='你是一个windows开发专家'
    question4='''
        我的windows11的shift切换中英文输入法关闭了，如何打开？
    '''
    ask_llm(qwen_client, model3, rule2, question2)
