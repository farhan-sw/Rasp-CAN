# import the library
import can
import time
from bitstring import BitArray
# create a bus instance using 'with' statement,
# this will cause bus.shutdown() to be called on the block exit;
# many other interfaces are supported as well (see documentation)

filters = []

with can.Bus(interface='socketcan',
              channel='can0',
              filter=filters) as bus:

    for msg in bus:
        mentahan = ' '.join(format(byte, '08b') for byte in msg.data)
        data = "".join(mentahan.split(" ")[::-1])
        data2 = " ".join(mentahan.split(" ")[::-1])

        id = data[:8]
        is_req = data[8:9]
        mode = data[9:10]
        motor_1 = data[10:10+16]
        motor_2 = data[26:26+16]
        int_a = data[42:42+16]
        lim_sw = data[58:58+6]        

        # DATA
        print(f"[{msg.arbitration_id}] {time.time()}")
        print(f"s_id    : {BitArray(bin=id).int} -> {id}")
        print(f"is_req  : {BitArray(bin=is_req).int} -> {is_req}")
        print(f"mode    : {BitArray(bin=mode).int} -> {mode}")
        print(f"m1      : {BitArray(bin=motor_1).int} -> {motor_1}")
        print(f"m2      : {BitArray(bin=motor_2).int} -> {motor_2}")
        print(f"int_a   : {BitArray(bin=int_a).int} -> {int_a}")
        print(f"lim_sw  : {BitArray(bin=lim_sw).int} -> {lim_sw}\n")