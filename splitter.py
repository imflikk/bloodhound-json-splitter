import json
import codecs
import sys

input_file = sys.argv[1]
obj_size = int(sys.argv[2])
count = 1
file_num = 1

with open(input_file, 'r', encoding='utf-8-sig') as f:
	
	data = json.load(f)
	objects_left = True
	num_objects_left = len(data['users']) # change this if parsing another piece of data

	while objects_left:
		print("[+] - " + str(num_objects_left) + " total objects left in the given file.\n")

		if (num_objects_left - obj_size) > 0:
			print("Writing to file #" + str(file_num) + "...\n")

			tmp_data = {'users': []}
	
			tmp_data['users'] = data['users'][:obj_size * count]
			tmp_data['meta'] = {"count": len(tmp_data['users']), "type": "users", "version": 3}

			new_json_data = json.dumps(tmp_data)

			with open('./output'+ str(file_num) +'.json', 'w') as f:
				f.write(new_json_data)
			
			num_objects_left -= obj_size
			count += 1

		else:
			print("Writing to last file, #" + str(file_num) + "...\n")

			tmp_data = {'users': []}
	
			tmp_data['users'] = data['users'][obj_size * (count - 1):]
			tmp_data['meta'] = {"count": len(tmp_data['users']), "type": "users", "version": 3}

			new_json_data = json.dumps(tmp_data)

			with open('./output'+ str(file_num) +'.json', 'w') as f:
				f.write(new_json_data)

			objects_left = False

		file_num += 1
	
	print("[+] - Done parsing")
	