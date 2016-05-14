# firewall

* 在CentOS7中用 *firewalld* 代替 *iptables* ，
    * 最大的好处有两个：一是支持动态更新，不用重启服务
    * 加入了防火墙的区域概念(zone) 。

## Installation

* If you need to manually install it, do this:
    `# yum install -y firewalld firewall-config`
    
* 确认服务已经运行，并能够开机自启动
    `# systemctl start firewalld.service`
    `# systemctl enable firewalld.service`
    
* 查看状态
    `# systemctl status firewalld.service`
    `# firewall-cmd --state`
    
* 关闭防火墙
    `# systemctl stop firewalld.service`
    `# systemctl disable firewalld.service`
    
    
## 常用命令

* 永久打开一个端口： 
    `# firewall-cmd --permanent --add-port=8080/tcp`
    
* 永久关闭一个端口： 
    `# firewall-cmd --permanent --remove-port=8080/tcp`
    
* 永久打开某项服务： 
    `# firewall-cmd --permanent --add-service=http`
    
* 永久关闭某项服务： 
    `# firewall-cmd --permanent --remove-service=http`
    
* 进行端口转发： 
    `# firewall-cmd --permanent --add-forward-port=port=80:proto=tcp:toport=8080:toaddr=192.0.2.55`
    
* 允许转发到其他地址： 
    `# firewall-cmd --permanent --add-masquerade`
    
* 重新加载防火墙： 
    `# firewall-cmd --reload`

    
## firewall-config

* 查看帮助:    `# firewall-cmd --help`
* 查看版本:    `# firewall-cmd --version`
* 查看设置:
    * 显示状态： `# firewall-cmd --state`
    * 查看区域信息： `# firewall-cmd --get-active-zones`
    * 查看指定接口所属区域： `# firewall-cmd --get-zone-of-interface=eth0`
    * 查看当前活动服务： `# firewall-cmd --get-service`
    * 查看在下次重新加载之后会生效的配置： `# firewall-cmd --get-service --permanent `
* 拒绝所有包: `# firewall-cmd --panic-on `    
* 取消拒绝状态: `# firewall-cmd --panic-on-off `    
* 查询拒绝状态: `# firewall-cmd --query-panic `    
    
    
* 从永久配置文件中重新加载已经运行的配置


