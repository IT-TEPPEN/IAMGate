import hashlib


def lock_id_from_str(s: str) -> int:
    # 64bit符号付き整数に収まるようにする
    h = hashlib.md5(s.encode("utf-8")).hexdigest()
    return int(h, 16) % (2**63)
