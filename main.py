# import the library
import can
import time
from bitstring import BitArray
# create a bus instance using 'with' statement,
# this will cause bus.shutdown() to be called on the block exit;
# many other interfaces are supported as well (see documentation)



def read():
    filters = []

    with can.Bus(interface='socketcan',
                channel='can0',
                filter=filters) as bus:

        for msg in bus:
            mentahan = ' '.join(format(byte, '08b') for byte in msg.data)
            data = "".join(mentahan.split(" ")[::-1])

            id = data[:8]
            is_req = data[8:9]
            mode = data[9:10]
            motor_1 = data[10:10+16]
            motor_2 = data[26:26+16]
            int_a = data[42:42+16]
            lim_sw_1 = data[58:58+1]
            lim_sw_2 = data[59:59+1]
            lim_sw_3 = data[60:60+1]
            lim_sw_4 = data[61:61+1]
            lim_sw_5 = data[62:62+1]
            lim_sw_6 = data[63:63+1]    

            # DATA
            print(f"[{msg.arbitration_id}] {time.time()}")
            print(f"s_id    : {BitArray(bin=id).int} -> {id}")
            print(f"is_req  : {BitArray(bin=is_req).int} -> {is_req}")
            print(f"mode    : {BitArray(bin=mode).int} -> {mode}")
            print(f"m1      : {BitArray(bin=motor_1).int} -> {motor_1}")
            print(f"m2      : {BitArray(bin=motor_2).int} -> {motor_2}")
            print(f"int_a   : {BitArray(bin=int_a).int} -> {int_a}")
            print(f"lim_sw_1  : {BitArray(bin=lim_sw_1).int} -> {lim_sw_1}")
            print(f"lim_sw_2  : {BitArray(bin=lim_sw_2).int} -> {lim_sw_2}")
            print(f"lim_sw_3  : {BitArray(bin=lim_sw_3).int} -> {lim_sw_3}")
            print(f"lim_sw_4  : {BitArray(bin=lim_sw_4).int} -> {lim_sw_4}")
            print(f"lim_sw_5  : {BitArray(bin=lim_sw_5).int} -> {lim_sw_5}")
            print(f"lim_sw_6  : {BitArray(bin=lim_sw_6).int} -> {lim_sw_6}\n")

#def send(int target, int8 can_from_id, bool is_req, bool mode, int16 motor_1, int16 motor_2, int16 int_a, int6 lim_sw):
def send(target : int, can_from_id : int, is_req : bool, mode : bool, motor_1 : int, motor_2 : int, int_a : int, lim_sw_1 : bool, lim_sw_2 : bool, lim_sw_3 : bool, lim_sw_4 : bool, lim_sw_5 : bool, lim_sw_6 : bool):
    filters = []
    filters = []

    with can.Bus(interface='socketcan',
                channel='can0',
                filter=filters) as bus:
        
        # Kontruksi data yang akan dikirim berdasarkan input send(), data berupa HEXADECIMAL yang berjumlah 8 byte
        # 8 byte = 64 bit disusun atas semua input send() yang dijadikan satu yaitu data. KOntruksi data dibawah ini
        # sehingga data berupa bit bit berurutan berdasarkan input send() yang dijadikan satu

        # DATA
        # 0-7     : id
        # 8       : is_req
        # 9       : mode
        # 10-25   : motor_1
        # 26-41   : motor_2
        # 42-57   : int_a
        # 58      : lim_sw_1
        # 59      : lim_sw_2
        # 60      : lim_sw_3
        # 61      : lim_sw_4
        # 62      : lim_sw_5
        # 63      : lim_sw_6

        # Kontruksi data dijadikan satu
        data = f"{can_from_id:08b}{is_req:01b}{mode:01b}{motor_1:016b}{motor_2:016b}{int_a:016b}{lim_sw_1:01b}{lim_sw_2:01b}{lim_sw_3:01b}{lim_sw_4:01b}{lim_sw_5:01b}{lim_sw_6:01b}"

        # Konversi target menjadi HEXADECIMAL
        target = hex(target)

        msg = can.Message(arbitration_id=target,
                        data=data,
                        is_extended_id=False)

        bus.send(msg)


if __name__ == "__main__":
    read()
    send(1, 2, 0, 0, 16, 20, 35)