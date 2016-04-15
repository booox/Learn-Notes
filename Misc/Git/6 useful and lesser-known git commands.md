# 6 useful and lesser-known git commands

* [6 useful and lesser-known git commands](http://blog.joncairns.com/2015/05/6-useful-and-lesser-known-git-commands/)

## git log -p <path>

* `git log` 是 *git* 方式来向我们展示我们的代码仓库的历史，并且可以添加一个 *path* 到命令里，从而将日志限制在只针对某个文件的改变。最后， *-p* 标志将包括针对这个文件的每次 *commit* 的不同 ( *diff* )，这样我们就能够清晰看到文件是如何在代码的历史中进行变化的。
    ```
        $ git log -p README.md
        commit 524d044afdbedafd94e81c5a0434150efd3a2860
        Author: Jon Cairns <jon@ggapps.co.uk>
        Date:   Thu Sep 18 15:30:00 2014 +0100

            Update README

        diff --git a/README.md b/README.md
        index 8f73735..082d6fa 100644
        --- a/README.md
        +++ b/README.md
        @@ -4,4 +4,4 @@ It's been created with Jekyll. Feel free to poke around.

         Social images courtesy of http://bostinno.streetwise.co/channels/social-media-share-icons-simple-modern-download/.

        -It builds automatically using a Bitbucket POST hook and a basic sinatra app.
        +It builds automatically using a Bitbucket POST hook and a basic sinatra app, but for security reasons the S3 configuration has been left out.

        commit df259431cbd3e6844a100ca5bc31d7c518595e86
        Author: Jon Cairns <jon@ggapps.co.uk>
        Date:   Fri Jun 20 12:03:41 2014 +0100

            Testing bitbucket web hook

        diff --git a/README.md b/README.md
        index ac10f9e..8f73735 100644
        --- a/README.md
        +++ b/README.md
        @@ -3,3 +3,5 @@
         It's been created with Jekyll. Feel free to poke around.

         Social images courtesy of http://bostinno.streetwise.co/channels/social-media-share-icons-simple-modern-download/.
        +
        +It builds automatically using a Bitbucket POST hook and a basic sinatra app.
        ...    
    ```
    * 对编码掌握不同的
    


## git checkout <commit>
## git checkout <tree-ish> -- <path>
## git stash
## git cherry-pick <commit>
## git annotate <file>
## And so on

* `git help -a`
* `git <command> --help`
    
    
    
    
    
    
    
    