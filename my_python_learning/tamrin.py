import re


def res(lis):
    # Removing newline character from string
    # Using regex
    res = []
    for sub in lis:
        res.append(re.sub('\n', '', sub))
    return res



# count = dict()
#
# with open('groh_B') as file:
#     deta = file.readlines()
#     clean = res(deta)
#     clean_ = clean[0].split('-')[1]
    # for item in deta:
    #     clean_item = item.split('-')
    #     clean = res(clean_item)

# with open('Score') as file_:
#     data = file_.readlines()
#         for dt in data:
#             clean_dt = dt.split('-')
#             clean_dt = res(clean_dt)
#             if clean_dt[0] == clean_dt[1]:
#                 count[clean[0]] = count.get(clean[0], 0) +1
#                 count[clean[1]] = count.get(clean[1], 0) +1
#                 break
#             if clean_dt[0] > clean_dt[1]:
#                 count[clean[0]] = count.get(clean[0], 0) +3
#                 break
#             if clean_dt[0] < clean_dt[1]:
#                 count[clean[1]] = count.get(clean[1], 0) +3
#                 break
count = dict()
i = 0

with open('groh_B') as file:
    deta = file.readlines()
    for item in deta:
        clean_item = item.split('-')
        clean = res(clean_item)
        with open('Score') as file_:
            data = file_.readlines()
            clean_ = res(data)
            clean_dt = clean_[i].split('-')
            if clean_dt[0] == clean_dt[1]:
                count[clean[0]] = count.get(clean[0], 0) +1
                count[clean[1]] = count.get(clean[1], 0) +1
                i += 1
            elif clean_dt[0] > clean_dt[1]:
                count[clean[0]] = count.get(clean[0], 0) +3
                i += 1
            elif clean_dt[0] < clean_dt[1]:
                count[clean[1]] = count.get(clean[1], 0) +3
                i += 1
