dict = {0:'###',
        1:'UNIT_FLAG_SERVER_CONTROLLED',
        2:'UNIT_FLAG_NON_ATTACKABLE',
        4:'UNIT_FLAG_REMOVE_CLIENT_CONTROL',
        8:'UNIT_FLAG_PVP_ATTACKABLE',
        16:'UNIT_FLAG_RENAME',
        32:'UNIT_FLAG_PREPARATION',
        64:'UNIT_FLAG_UNK_6',
        128:'UNIT_FLAG_NOT_ATTACKABLE_1',
        256:'UNIT_FLAG_IMMUNE_TO_PC',
        512:'UNIT_FLAG_IMMUNE_TO_NPC',
        1024:'UNIT_FLAG_LOOTING',
        2048:'UNIT_FLAG_PET_IN_COMBAT',
        4096:'UNIT_FLAG_PVP',
        8192:'UNIT_FLAG_SILENCED',
        16384:'UNIT_FLAG_CANNOT_SWIM',
        32768:'UNIT_FLAG_ONLY_SWIM',
        65536:'UNIT_FLAG_NO_ATTACK2',
        131072:'UNIT_FLAG_PACIFIED',
        262144:'UNIT_FLAG_STUNNED',
        524288:'UNIT_FLAG_IN_COMBAT',
        1048576:'UNIT_FLAG_TAXI_FLIGHT',
        2097152:'UNIT_FLAG_MH_DISARMED',
        4194304:'UNIT_FLAG_CONFUSED',
        8388608:'UNIT_FLAG_FEARED',
        16777216:'UNIT_FLAG_PLAYER_CONTROLLED',
        33554432:'UNIT_FLAG_NOT_SELECTABLE',
        67108864:'UNIT_FLAG_SKINNABLE',
        134217728:'UNIT_FLAG_MOUNT',
        268435456:'UNIT_FLAG_PREVENT_KNEELING_WHEN_LOOTING',
        536870912:'UNIT_FLAG_PREVENT_EMOTES',
        1073741824:'UNIT_FLAG_SHEATHE',
        2147483648:'UNIT_FLAG_UNK_31'}

a = int(input('Emter a unit flag here:'))
bits = list(map(int, reversed(bin(a)[2:])))
print(bits)
for i, b in enumerate(bits):
    if (2 ** i) * b == 0:
        continue
    print((2 ** i) * b, dict[(2 ** i) * b])
