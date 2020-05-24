# import json
# data = '''{
#         "employee": [{
#                 "name": "Sanjit",
#                 "job": "Finastra",
#                 "Active": true,
#                 "extra": null
#             },
#             {
#                 "name": "Sounak",
#                 "job": "VMWare",
#                 "Active": true,
#                 "extra": "yes"
#             }
# 	    ]
# }'''
#
# json_object = json.loads(data)
# print(json_object)
# # pretty_json = json.dumps(json_object, indent=2)
# # print(pretty_json)
# dict1 = dict()
# for e in json_object["employee"]:
#     # print(e["name"], e["job"])
#     dict1[e["name"]]=e["job"]
# print(dict1)
# with open("delete.json", "w") as f:
#     json.dump(json_object, f, indent=2)
#
#
#

def reverse(x: int) -> int:
    rev = 0
    temp = x
    x = abs(x)
    while (x > 0):
        rem = x % 10
        x = x // 10
        rev = rem + (rev * 10)
    if temp<0:
        return 0-rev
    else:
        return rev

print(reverse(0))