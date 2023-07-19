import argparse
import json
import random
import re

def parser_data():
    parser = argparse.ArgumentParser(description="A game.")
    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-n", "--name", help="文章名字")
    return parser.parse_args()

def read_articles(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def replace(article, substitutions):
    text = article["text"]
    for key in article["hints"].keys():
        text = re.sub("\{\{"+key+"\}\}", substitutions[key], text)
    return text

if __name__ == '__main__':
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]

    if args.name != None:
        name = args.name
    else:
        name = random.choice(list(articles.keys()))
    article = articles[name]
    hints = article["hints"]
    
    print(article["text"])
    print("提示：")
    for key in hints.keys():
        hint = hints[key]
        print("{key} : {hint}".format(key=key,hint=hint))
    
    print("请输入你的答案：")
    answers = {}
    for key in hints.keys():
        answers[key]=input("{key} : ".format(key=key))
    print(answers)

    replaced_text=replace(article, answers)
    print(replaced_text)
    

    
    
