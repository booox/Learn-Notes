# Understanding PAM Authentication and Security

* [Understanding PAM Authentication and Security](http://aplawrence.com/Basics/understandingpam.html)

* PAM is the *Pluggable* *Authentication* *Module* , invented by *Sun* .


## Advantage of PAM

1. The security is no longer the application's concern.
    * If PAM says its OK, its OK
    
2. PAM is also extensible
    
## Configuration Files

* */etc/pam.d* : PAM's configuration file
    * One file for each PAM aware app.
* Changes to these files take effect instantly.
    * Test changes before you exit, because you may not be able to log back in.
    
* Example: We'll use *PAM* to add some additional restriction about *SSH* :
    * The time you are allowed to use *ssh* :
        * To do this, we need a *PAM* module called *pam_time.so*
            * Maybe in your */lib/security/* direcotry
        * It uses a configuration file */etc/security/time.conf* 
            * Add this line:
            `sshd;*;*;!Al2200-0400`
            * *sshd* cannot be used between 10:00 PM and 4:00 AM.
            
        * Add the *pam* module to */etc/pam.d/sshd* . A file like this :
        ```
            #%PAM-1.0
            account    required     pam_time.so
            auth       required     pam_stack.so service=system-auth
            auth       required     pam_nologin.so
            account    required     pam_stack.so service=system-auth
            password   required     pam_stack.so service=system-auth
            session    required     pam_stack.so service=system-auth
            session    required     pam_limits.so
            session    optional     pam_console.so
        
        ```
            * The *time.so* module at the first of the file, so that is is the very first thing that is checked.
                * If that module doesn't give *sshd* a green light, that's the end of it: no access.
                * That's the meaning of "required" : the module HAS to say that it is happy.                
            * There are four type of the PAM Modules: 
                * *account* : provide the actual authentication, perhaps asking for and checking a password, and they set "credentials" such as group membership or kerberos "tickets."
                * *auth(entication)* : check to make sure that the authentication is allowed (the account has not expired, the user is allowed to log in at this time of day, and so on).
                * *password* : used to set passwords.
                * *session* : used once a user has been authenticated to allow them to use their account
                    * perhaps mounting the user's home directory or making their mailbox available.
                    
##Stacking

* RedHat has a special module *pam_stack* 
   * It functions much like an "include" statement in any programming language. We saw it in my /etc/pamd/sshd file:
        `auth       required     pam_stack.so service=system-auth`
        * That says to look in */etc/pam.d/system-auth* for other modules to use.
            * Both login and sshd have this line (as does just about every other file in */etc/pam.d/* ) 
* we can look in system-auth to see what gets called by them:
    ```
        #%PAM-1.0
        # This file is auto-generated.
        # User changes will be destroyed the next time authconfig is run.
        auth        required      /lib/security/$ISA/pam_env.so
        auth        sufficient    /lib/security/$ISA/pam_unix.so likeauth nullok
        auth        required      /lib/security/$ISA/pam_deny.so
        auth required /lib/security/$ISA/pam_tally.so no_magic_root onerr=fail
        account     required      /lib/security/$ISA/pam_unix.so
        account    required      /lib/security/$ISA/pam_tally.so onerr=fail file=/var/log/faillog deny=1 no_magic_root even_deny_root_account

        password    required      /lib/security/$ISA/pam_cracklib.so retry=3 type=
        password    sufficient    /lib/security/$ISA/pam_unix.so nullok use_authtok md5 shadow
        password    required      /lib/security/$ISA/pam_deny.so

        session     required      /lib/security/$ISA/pam_limits.so
        session     required      /lib/security/$ISA/pam_unix.so
    
    ```
        