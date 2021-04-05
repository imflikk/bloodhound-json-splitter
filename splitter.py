import json
import codecs
import sys


if len(sys.argv) != 4:
	print("\tUsage: \t\tpython3 splitter.py <input file> <num of objects per file> <data type>")
	print("\n\tExample: \tpython3 splitter.py bloodhound-users.json 10000 users")
	exit()

input_file = sys.argv[1]
obj_size = int(sys.argv[2])
type_of_data = sys.argv[3]
possible_data_types = ["users", "groups", "ous", "computers", "gpos", "domains"]

if type_of_data not in possible_data_types:
	print("Invalid Bloodhound data type.  Please choose one of the following types: ")
	
	for data_type in possible_data_types:
		print("\t-" + data_type)
	
	exit()


count = 1
file_num = 1

with open(input_file, 'r', encoding='utf-8-sig') as f:
	
	data = json.load(f)
	objects_left = True
	num_objects_left = len(data[type_of_data])

	while objects_left:
		print("[+] - " + str(num_objects_left) + " total objects left in the given file.\n")

		if (num_objects_left - obj_size) > 0:
			print("Writing to file #" + str(file_num) + "...\n")

			tmp_data = {type_of_data: []}
	
			tmp_data[type_of_data] = data[type_of_data][obj_size * (count - 1):obj_size * count]
			tmp_data['meta'] = {"count": len(tmp_data[type_of_data]), "type": type_of_data, "version": 3}

			new_json_data = json.dumps(tmp_data)

			with open('./output-'+ str(file_num) +'.json', 'w') as f:
				f.write(new_json_data)
			
			num_objects_left -= obj_size
			count += 1

		else:
			print("Writing to last file, #" + str(file_num) + "...\n")

			tmp_data = {type_of_data: []}
	
			tmp_data[type_of_data] = data[type_of_data][obj_size * (count - 1):]
			tmp_data['meta'] = {"count": len(tmp_data[type_of_data]), "type": type_of_data, "version": 3}

			new_json_data = json.dumps(tmp_data)

			with open('./output-'+ str(file_num) +'.json', 'w') as f:
				f.write(new_json_data)

			objects_left = False

		file_num += 1
	
	print("[+] - Done parsing")
	
