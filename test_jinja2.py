from jinja2 import Environment, FileSystemLoader

# 打开配置的jinja2模板
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template_1.txt')


# 数据文件结构
interface = {
    'hostname':'SW1',
    'interface':'e0/0',
    'vlan_id':'10',
    'link_type':'trunk'
}
print(template.render(interface))


# import csv
# # 打开配置数据文件，编码 utf-8-sig,带标记的utf-8编码
# with open("interface.csv", encoding='utf-8-sig') as f:
#     csv_f = csv.DictReader(f)
#     for i in csv_f:
#         print(template.render(i))
