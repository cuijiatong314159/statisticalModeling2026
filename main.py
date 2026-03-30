import random
import string


def generate_password(length=12):
    """
    生成一个随机密码
    :param length: 密码长度，默认12位
    :return: 随机密码字符串
    """
    # 密码可用字符：大小写字母 + 数字 + 符号
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"

    # 随机选择字符生成密码
    password = "".join(random.choice(characters) for _ in range(length))

    return password


# 主程序
if __name__ == "__main__":
    print("🔐 随机密码生成器")

    # 生成一个12位密码
    pwd = generate_password(12)
    print(f"你的随机密码：{pwd}")