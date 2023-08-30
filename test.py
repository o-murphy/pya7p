data = b'73e771793eefa7138da2ad842f97ffb5\n\xe2\x02\n\x0212\x12\x011\x1a\x011"\x011*\x0118\xe8\x07@' \
       b'\xe8\x07H\x01PdXn`\x01h\xe8\x07x\x0f\x80\x01\x90N\x88\x01(\x98\x01\x0f\xa0\x01\xe0+\xa8\x01' \
       b'\n\xb0\x01\xe8\x07\xca\x01\x08\x08\xff\x01\x18\x01 \x90N\xca\x01\t\x08\xff\x01\x18\x02 \xa0' \
       b'\x9c\x01\xca\x01\t\x08\xff\x01\x18\x03 \xb0\xea\x01\xca\x01\t\x08\xff\x01\x18\x04 \xa0\x8d' \
       b'\x06\xd2\x01\xe9\x01\x90N\xa0\x9c\x01\xa8\xc3\x01\xb0\xea\x01\xf4\xfd\x01\xb8\x91\x02\xfc\xa4' \
       b'\x02\xc0\xb8\x02\x90\xc8\x02\xe0\xd7\x02\xb0\xe7\x02\x80\xf7\x02\xd0\x86\x03\xa0\x96\x03\xf0' \
       b'\xa5\x03\xc0\xb5\x03\x90\xc5\x03\xe0\xd4\x03\xc8\xdc\x03\xb0\xe4\x03\x98\xec\x03\x80\xf4\x03' \
       b'\xe8\xfb\x03\xd0\x83\x04\xb8\x8b\x04\xa0\x93\x04\x88\x9b\x04\xf0\xa2\x04\xd8\xaa\x04\xc0\xb2' \
       b'\x04\xa8\xba\x04\x90\xc2\x04\xf8\xc9\x04\xe0\xd1\x04\xc8\xd9\x04\xb0\xe1\x04\x98\xe9\x04\x80' \
       b'\xf1\x04\xf4\xf4\x04\xe8\xf8\x04\xdc\xfc\x04\xd0\x80\x05\xc4\x84\x05\xb8\x88\x05\xac\x8c\x05' \
       b'\xa0\x90\x05\x94\x94\x05\x88\x98\x05\xfc\x9b\x05\xf0\x9f\x05\xe4\xa3\x05\xd8\xa7\x05\xcc\xab' \
       b'\x05\xc0\xaf\x05\xb4\xb3\x05\xa8\xb7\x05\x9c\xbb\x05\x90\xbf\x05\x84\xc3\x05\xf8\xc6\x05\xec' \
       b'\xca\x05\xe0\xce\x05\xd4\xd2\x05\xc8\xd6\x05\xbc\xda\x05\xb0\xde\x05\xa4\xe2\x05\x98\xe6\x05' \
       b'\x8c\xea\x05\x80\xee\x05\xf4\xf1\x05\xe8\xf5\x05\xdc\xf9\x05\xd0\xfd\x05\xc4\x81\x06\xb8\x85' \
       b'\x06\xac\x89\x06\xa0\x8d\x06\xda\x01\x03\x08\x90N\xe2\x01\x0522 LR'

from a7p import A7PFile
from a7p.profedit_pb2 import Payload, Profile, DType, GType, TwistDir, SwPos, CoefRow

with open('test2.a7p', 'rb') as fp:
    print(A7PFile.load(fp))

payload = Payload(profile=Profile(
    profile_name="swiss p ap 260gr",
    cartridge_name="swiss p ap 260gr",
    bullet_name="swiss p ap 260gr",
    short_name_top="338LM",
    short_name_bot="260gr",
    user_note='Note text',

    zero_x=2000,  # click_x * -1000
    zero_y=-20000,  # click_y * 1000
    sc_height=90,  # mm
    r_twist=900,  # Inch * 100

    c_muzzle_velocity=8000,  # MPS * 10
    c_zero_temperature=15,  # C
    c_t_coeff=1500,  # % * 1000
    c_zero_air_temperature=15,
    c_zero_air_pressure=7600,  # hPa * 10
    c_zero_air_humidity=50,  # %
    c_zero_p_temperature=15,  # C
    c_zero_w_pitch=200,  # degree * 10

    b_diameter=308,  # Inch * 1000
    b_weight=2600,  # grain * 10
    b_length=1420,  # Inch * 1000

    twist_dir=TwistDir.RIGHT,
    bc_type=GType.G7,  # G1, G7, CUSTOM

    switches=[
        SwPos(
            c_idx=255,
            # reticle_idx = 1  # undefined
            zoom=1,
            distance=10000,
            # distance_from = 5  # undefined
        ),
        SwPos(c_idx=255, zoom=2, distance=20000),
        SwPos(c_idx=255, zoom=3, distance=30000),
        SwPos(c_idx=255, zoom=4, distance=100000)
    ],

    distances=list(range(10000, 100001, 5000)),  # m * 100
    c_zero_distance_idx=0,  # idx of zero distance in distances

    coef_rows=[
        CoefRow(
            bc_cd=3270,  # bc * 10
            mv=8000  # mps * 10
        )
    ],

    caliber="338LM",
    # device_uuid  # undefined

))

with open('test1.a7p', 'wb') as fp:
    A7PFile.dump(payload, fp)


print()