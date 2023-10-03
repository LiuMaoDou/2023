import paramiko

def ssh_ping(host, user, password, target_ip, count=10000):
    # 创建SSH客户端对象
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password)
    
    # 执行ping命令
    stdin, stdout, stderr = client.exec_command(f"ping -c {count} {target_ip}")
    result = stdout.read().decode()
    
    # 关闭连接
    client.close()
    
    return result

if __name__ == "__main__":
    # 设备列表，形式为(设备IP, 用户名, 密码, 要ping的目标IP)
    devices = [
        ("192.168.1.1", "username1", "password1", "8.8.8.8"),
        # 添加更多设备信息...
    ]

    for device in devices:
        host, user, password, target_ip = device
        result = ssh_ping(host, user, password, target_ip)
        
        # 保存ping结果
        with open(f"{host}_ping_result.txt", "w") as f:
            f.write(result)
        
        print(f"Ping results for {host} saved!")
