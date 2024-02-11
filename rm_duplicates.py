id_codes = [55,3,22,4,9,7,1,2,99,88,2,2,2,25,2,88,7,9,3]

id_codes.sort()


print(id_codes)

uniq_id = []

for item in id_codes:
    if item not in uniq_id:
        uniq_id.append(item)

print (uniq_id)