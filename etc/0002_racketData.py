# import requests
# from django.db import migrations
#
# from racket.models import Racket
#
#
# def gen_master(apps, schema_editor):
#     r = requests.get('https://api.racketlogger.com/rackets')
#     data = r.json()
#     checkbrand = 0
#     for element in data:
#         if element['brand'] == 'HEAD':
#             checkbrand = 1
#         elif element['brand'] == 'Wilson':
#             checkbrand = 2
#         elif element['brand'] == 'Yonex':
#             checkbrand = 3
#         elif element['brand'] == 'Babolat':
#             checkbrand = 4
#         elif element['brand'] == 'Volkl':
#             checkbrand = 5
#         elif element['brand'] == 'ProKennex':
#             checkbrand = 6
#         elif element['brand'] == 'Prince':
#             checkbrand = 7
#         elif element['brand'] == 'Dunlop':
#             checkbrand = 8
#         elif element['brand'] == 'Tecnifibre':
#             checkbrand = 9
#         elif element['brand'] == 'Pacific':
#             checkbrand = 10
#         elif element['brand'] == 'Gamma':
#             checkbrand = 11
#         elif element['brand'] == 'Donnay':
#             checkbrand = 12
#         elif element['brand'] == 'Solinco':
#             checkbrand = 13
#         elif element['brand'] == 'Asics':
#             checkbrand = 14
#         elif element['brand'] == 'Snauwaert':
#             checkbrand = 15
#         elif element['brand'] == 'PowerAngle':
#             checkbrand = 16
#
#         Racket(name=element['model'], weight=element['weight'] * 28.35, pattern=element['pattern'],
#                headsize=element['head_size'],
#                stiffness=element['stiffness'], length=27, balance=element['balance'],
#                visitorAvgScore=0, countLike=0,
#                brand_id=checkbrand).save()
#
#
# class Migration(migrations.Migration):
#     initial = True
#
#     dependencies = [
#         ('racket', '0001_initial'),
#     ]
#
#     operations = [
#         migrations.RunPython(gen_master)
#     ]

# 라켓 데이터 가져오기
# r = requests.get('https://api.racketlogger.com/rackets')
# data = r.json()
# for ele in data:
#     print(ele['brand'])