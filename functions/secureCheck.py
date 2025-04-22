
# 执行密码验证的功能
import os
import hashlib
from config import securityCode

def loginEncryption(password):
    # 生成一个随机盐值（salt）
    salt = os.urandom(16)  # 16 字节的随机盐值
    combined = password.encode('utf-8') + salt + securityCode.encode('utf-8')
    # 使用 SHA-256 进行加密
    sha256_hash = hashlib.sha256(combined).hexdigest()
    # 返回盐值和加密后的密码。盐值需要存储，才能用于验证
    return sha256_hash, salt
def verifyPassword(input_password, stored_encrypted_password, stored_salt):
    combined = input_password.encode('utf-8') + stored_salt + securityCode.encode('utf-8')
    sha256_hash = hashlib.sha256(combined).hexdigest()
    return sha256_hash == stored_encrypted_password

if __name__ == '__main__':
    # 示例使用
    user_password = "mypassword"
    encrypted_password, salt = loginEncryption(user_password)

    print("加密后的密码：", encrypted_password)
    print("盐值：", salt.hex())  # 打
