# sast2023 word game

## 基础版本

### 环境配置

目前没有第三方依赖项

### 使用设置

使用恰当的参数运行`main.py`

约定以下参数：

```
--file  -f  接题库的路径
--name  -n  接文章的名字
...

```

文章使用 JSON 存储的格式如下：

```json
{
    "articles" : {
        "sample" : {
            "text" : "我们都爱 {{1}} 这门课程。这门课程是多么的 {{2}}，以至于所有人都在课程上认真地 {{3}}。在设计数字电路时,我们需要运用到逻辑门、半导体存储器等知识。这些内容相互联系,共同构成复杂的数字电路。这门课能启发我们的逻辑思维能力和科学思考能力。通过为难我们的练习和作业,我们的理解能力和解决问题的能力得到了提高。这些将对今后的 {{4}} 和工作有很大益处。",
            "hints" : {
                "1" : "教材名称",
                "2" : "形容词",
                "3" : "动词，与学生相关",
                "4" : "你最喜欢做的事情"
            }
        },
		"sample2_by_yiyan" : {
			"text" : "My {{1}} name is John. I am a student at the University of {{2}} . I am studying {{3}} at the moment. My favorite {{4}} is music, and I often listen to it in my free time. After {{5}} , I like to go for a run to keep healthy. I also like {{6}} , and I often play it with my friends on the weekends. Finally, I love {{7}} , and I often go hiking in the mountains near my home.",
			"hints" : {
				"1" : "adj.",
				"2" : "n.",
				"3" : "n.",
				"4" : "n.",
				"5" : "n.",
				"6" : "n.",
				"7" : "n."
			}
		}
    } 
}
```

### 游戏功能

- 基础功能



## GUI版本

### 环境配置

```python
import streamlit
```

### 使用设置

在终端中运行：

```
streamlit run GUI_main.py
```

### 游戏功能

- 带GUI的基础功能
  - 实现了导入json文件界面，选择文章界面，游戏界面的分离
  - 添加了返回重新选择文章的功能
- 能检测json文件的（部分）错误
  - 并支持重新导入json文件



## 其他

- 