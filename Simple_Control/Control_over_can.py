import odrive
import can 
import struct

bus = can.interface.Bus("can0", bustype="socketcan")

#Flush can rx
while not (bus.recv(timeout=0) is None): pass
#Print heartbeats
node_id = 3
cmd_id = 0x01
message_id = (node_id << 3 | cmd_id)
for msg in bus:
    if msg.arbitration_id == message_id:
        error, state, result, traj_done = struct.unpack('<IBBB', bytes(msg.data[:7]))
        break
print(error, state, result, traj_done)


# bus.send(can.Message(
#     arbitration_id = (node_id << 5 | 0x07),
#     data = struct.pack('<I', 8),
#     is_extended_id = False
# ))

