# CentOS 7 : Install Ftp Server


## Install vsftpd
    `$ sudo yum -y install vsftpd ftp`
    
    
## Configure vsftpd
    
* */etc/vsftpd/vsftpd.conf* 
    `$ sudo vi /etc/vsftpd/vsftpd.conf`
    * Make some changes as shown below:
    ```
         [...]
        ## Disable anonymous login ##
        anonymous_enable=NO
        ## Uncomment ##
        ascii_upload_enable=YES
        ascii_download_enable=YES
        ## Uncomment - Enter your Welcome message - This is optional ##
        ftpd_banner=Welcome to UNIXMEN FTP service.
        ## Add at the end of this  file ##
        use_localtime=YES
    
    ```