import struct

with open('seed/crash.log', mode='r') as f:
    lines = f.readlines()
    sended_data = []
    for line in lines:
        sended_data.append(line.strip()[26:])
    sended_data = sorted(list(set(sended_data)))
    i = 1
    for data in sended_data:
        can_id_str = data.split('#')[0]
        can_id = int(can_id_str, 16)
        can_data = data.split('#')[1]
        assert len(can_data) % 2 == 0 and len(can_data) >= 4
        can_dlc = len(can_data) // 2

        can_id_hex_str = '{:08x}'.format(can_id)
        can_dlc_hex_str = '{:02x}'.format(can_dlc)
        can_data_hex_str = can_data + ("0" * (8 * 2 - len(can_data)))

        # print("i={}, id={}, dlc={}, data={}".format(i,can_id_hex_str, can_dlc_hex_str, can_data_hex_str))
        test_case_str = '{}{}{}'.format(can_id_hex_str, can_dlc_hex_str, can_data_hex_str)

        test_case_str_list = [ int(test_case_str[i*2:i*2+2], 16) for i in range(len(test_case_str) // 2) ]
        assert(len(test_case_str_list) == 13)
        test_case_binaries = struct.pack('B'* len(test_case_str_list), *test_case_str_list)
        with open('testcases/{}.bin'.format(i), 'wb+') as fb:
            fb.write(test_case_binaries) 
        i += 1