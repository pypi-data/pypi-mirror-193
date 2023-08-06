
from cryptography.fernet import Fernet
import base64

# 生成一个随机密钥
key = Fernet.generate_key()


# 创建一个Fernet对象
cipher_suite = Fernet(key)

# 要加密的数据
plaintext = b"Hello, world!"

# 对数据进行加密
ciphertext = cipher_suite.encrypt(plaintext)

# 将密钥和密文转换成base64编码字符串
key_b64 = base64.urlsafe_b64encode(key).decode('utf-8')
ciphertext_b64 = base64.urlsafe_b64encode(ciphertext).decode('utf-8')

# 打印结果
print("密钥：", key_b64)
print("密文：", ciphertext_b64)


# 将base64编码的密钥和密文解码
key = base64.urlsafe_b64decode(key_b64)
ciphertext = base64.urlsafe_b64decode(ciphertext_b64)


# 创建一个Fernet对象，并使用密钥解密密文
cipher_suite = Fernet(key)
plaintext = cipher_suite.decrypt(ciphertext)

# 打印解密后的数据
print("解密后的数据：", plaintext.decode('utf-8'))