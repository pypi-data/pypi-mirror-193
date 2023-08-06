from __future__ import annotations

import base64
import secrets
from pathlib import Path

import _x21


def encrypt_file(path: Path) -> None:
    path = Path(path)
    assert path.suffix == ".py"

    with path.open() as f:
        source = f.read()

    sbytes = encrypt_string(source)

    # write secrets
    spath = path.with_suffix(".dat")
    assert not spath.exists()
    with spath.open("wb") as f:
        f.write(sbytes)

    # override python file
    with path.open("w") as f:
        f.write("import x21\nx21.__dex_23c__(__file__,globals())\n")


def encrypt_string(message: str) -> bytes:
    # TODO move iv generation in C++ so it cannot be turned off by the user?
    return _x21.encrypt_23a(message, secrets.token_bytes(12))


def __dex_22b__(scope: dict, iv: bytes, smessage: bytes) -> None:
    _x21.decrypt_and_exec_22b(smessage, iv, scope)


def __dex_22c__(scope: dict, iv_smessage: str) -> None:
    data = base64.a85decode(iv_smessage)
    _x21.decrypt_and_exec_22c(data, scope)


def __dex_23a__(scope: dict, iv_smessage_tag: str) -> None:
    data = base64.a85decode(iv_smessage_tag)
    _x21.decrypt_and_exec_23a(data, scope)


def __dex_23b__(scope: dict, data: bytes) -> None:
    # 23b is just like 23a encryption except that byte-strings are exchanged
    _x21.decrypt_and_exec_23a(data, scope)


def __dex_23c__(file: str, scope: dict) -> None:
    # 23c is just like 23a encryption except that only __file__ is given
    file = Path(file).with_suffix(".dat")
    with file.open("rb") as f:
        data = f.read()
    _x21.decrypt_and_exec_23a(data, scope)
