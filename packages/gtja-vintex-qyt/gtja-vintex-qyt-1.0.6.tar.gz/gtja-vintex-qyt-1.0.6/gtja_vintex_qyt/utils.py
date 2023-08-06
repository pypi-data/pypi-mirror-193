import base64
import pathlib
import platform
import subprocess

from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad

from .constants import Constants


class Utils:
    SESSION_ID = 'pc'
    VINTEX_AES_KEY = "la3uaerpbww680d5h51tvug1csbw6o6i"
    VINTEX_AES_IV = "s1pspww1w10chj73"

    @staticmethod
    def get_device_id() -> str:
        if Constants.os == "Windows":
            return subprocess.check_output("wmic csproduct get uuid").decode("utf-8").split('\n')[1].strip()
        elif Constants.os == "Linux":
            with open('/etc/machine-id') as f:
                return f.readline().strip()
        else:
            raise Exception("Unsupported Os.")

    @staticmethod
    def get_system_version() -> str:
        return platform.uname().version

    @staticmethod
    def encrypt_with_vintex_rsa(data: str) -> str:
        with open(pathlib.Path(__file__).parent.resolve() / 'lib' / 'vintex.pub') as public_key_file:
            # Vintex Mobile team use this deprecated rsa method so we have to use PKCS1_v1_5.
            cipher_rsa = PKCS1_v1_5.new(RSA.import_key(public_key_file.read()))
            return base64.b64encode(cipher_rsa.encrypt(str.encode(data))).decode("utf-8")

    @staticmethod
    def encrypt_with_vintex_aes(data: str) -> str:
        cipher = AES.new(Utils.VINTEX_AES_KEY.encode("utf-8"),
                         AES.MODE_CBC,
                         iv=Utils.VINTEX_AES_IV.encode("utf-8"))
        return base64.b64encode(cipher.encrypt(pad(data.encode("utf-8"), AES.block_size))).decode("utf-8")
