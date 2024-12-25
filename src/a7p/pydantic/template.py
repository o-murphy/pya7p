from a7p import A7PFactory

PAYLOAD_RECOVERY_SCHEMA = {
    "profile": {
        "profile_name": "nil",
        "cartridge_name": "nil",
        "bullet_name": "nil",
        "short_name_top": "nil",
        "short_name_bot": "nil",
        "user_note": "\n",
        "zero_x": 0,
        "zero_y": 0,
        "sc_height": 90,
        "r_twist": 900,
        "c_muzzle_velocity": 8000,
        "c_zero_temperature": 15,
        "c_t_coeff": 1000,
        "c_zero_air_temperature": 15,
        "c_zero_air_pressure": 10000,
        "c_zero_air_humidity": 0,
        "c_zero_p_temperature": 15,
        "b_diameter": 338,
        "b_weight": 3000,
        "b_length": 1800,
        "bc_type": "G7",
        "switches": [
            {
                "c_idx": 255,
                "zoom": 1,
                "distance": 10000,
                "reticle_idx": 0,
                "distance_from": "VALUE"
            },
            {
                "c_idx": 255,
                "zoom": 2,
                "distance": 20000,
                "reticle_idx": 0,
                "distance_from": "VALUE"
            },
            {
                "c_idx": 255,
                "zoom": 3,
                "distance": 30000,
                "reticle_idx": 0,
                "distance_from": "VALUE"
            },
            {
                "c_idx": 255,
                "zoom": 4,
                "distance": 100000,
                "reticle_idx": 0,
                "distance_from": "VALUE"
            }
        ],
        "distances": [
            10000,
            20000,
            25000,
            30000,
            35000,
            40000,
            42000,
            44000,
            46000,
            48000,
            50000,
            52000,
            54000,
            56000,
            58000,
            60000,
            61000,
            62000,
            63000,
            64000,
            65000,
            66000,
            67000,
            68000,
            69000,
            70000,
            71000,
            72000,
            73000,
            74000,
            75000,
            76000,
            77000,
            78000,
            79000,
            80000,
            81000,
            82000,
            83000,
            84000,
            85000,
            86000,
            87000,
            88000,
            89000,
            90000,
            91000,
            92000,
            93000,
            94000,
            95000,
            96000,
            97000,
            98000,
            99000,
            100000,
            100500,
            101000,
            101500,
            102000,
            102500,
            103000,
            103500,
            104000,
            104500,
            105000,
            105500,
            106000,
            106500,
            107000,
            107500,
            108000,
            108500,
            109000,
            109500,
            110000,
            110500,
            111000,
            111500,
            112000,
            112500,
            113000,
            113500,
            114000,
            114500,
            115000,
            115500,
            116000,
            116500,
            117000,
            117500,
            118000,
            118500,
            119000,
            119500,
            120000,
            120500,
            121000,
            121500,
            122000,
            122500,
            123000,
            123500,
            124000,
            124500,
            125000,
            125500,
            126000,
            126500,
            127000,
            127500,
            128000,
            128500,
            129000,
            129500,
            130000,
            130500,
            131000,
            131500,
            132000,
            132500,
            133000,
            133500,
            134000,
            134500,
            135000,
            135500,
            136000,
            136500,
            137000,
            137500,
            138000,
            138500,
            139000,
            139500,
            140000,
            140500,
            141000,
            141500,
            142000,
            142500,
            143000,
            143500,
            144000,
            144500,
            145000,
            145500,
            146000,
            146500,
            147000,
            147500,
            148000,
            148500,
            149000,
            149500,
            150000,
            150500,
            151000,
            151500,
            152000,
            152500,
            153000,
            153500,
            154000,
            154500,
            155000,
            155500,
            156000,
            156500,
            157000,
            157500,
            158000,
            158500,
            159000,
            159500,
            160000,
            160500,
            161000,
            161500,
            162000,
            162500,
            163000,
            163500,
            164000,
            164500,
            165000,
            165500,
            166000,
            166500,
            167000,
            167500,
            168000,
            168500,
            169000,
            169500,
            170000
        ],
        "coef_rows": [
            {
                "bc_cd": 3820,
                "mv": 0
            },
        ],
        "caliber": "nil",
        "c_zero_distance_idx": 0,
        "c_zero_w_pitch": 0,
        "twist_dir": "RIGHT",
        "device_uuid": ""
    }
}


def _fix_str_len_type(string: str, expected_len: int, default: str = "nil"):
    if isinstance(string, str):
        return string[:expected_len]
    return default[:expected_len]


# PAYLOAD_RECOVERY_SCHEMA['profile']['profile_name'] = lambda value: _fix_str_len_type(value, 50)
# PAYLOAD_RECOVERY_SCHEMA['profile']['bullet_name'] = lambda value: _fix_str_len_type(value, 50)
# PAYLOAD_RECOVERY_SCHEMA['profile']['cartridge_name'] = lambda value: _fix_str_len_type(value, 50)
# PAYLOAD_RECOVERY_SCHEMA['profile']['caliber'] = lambda value: _fix_str_len_type(value, 50)
# PAYLOAD_RECOVERY_SCHEMA['profile']['device_uuid'] = lambda value: _fix_str_len_type(value, 50,
#                                                                                    "Warning: Restored profile")
# PAYLOAD_RECOVERY_SCHEMA['profile']['short_name_top'] = lambda value: _fix_str_len_type(value, 8)
# PAYLOAD_RECOVERY_SCHEMA['profile']['short_name_bot'] = lambda value: _fix_str_len_type(value, 8)
# PAYLOAD_RECOVERY_SCHEMA['profile']['user_note'] = lambda value: _fix_str_len_type(value, 1024)
# PAYLOAD_RECOVERY_SCHEMA['profile']['distances'] = [int(d * 100) for d in A7PFactory.DistanceTable.LONG_RANGE.value]

__all__ = (
    'PAYLOAD_RECOVERY_SCHEMA',
)
