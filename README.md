#Get stats. 



## Run it

By default it looks for a file called "accounts.txt".  You can use the 
-f flag to specify a different file name: 

```shell
go run main.go -f mypeople.txt | tee run.3
```

Where mypeople.txt is just a file with user names that looks like:

```
vallard
datacenter
kubernetes
ciscocloud
```

You'll need to also define an env variable called GETHUB_TOKEN so you can
actually make more than 5 requests per hour


## Decypher it

This doesn't go in concurancy as to not get you banned from github's api. 
Output is: 

```
project-name watcher-count star-count isfork?
```
to sort by the most stars:

``` 
sort -rnk 3 repos.out3 >topranked.out1
```
Will put the top ranked repo first in the new topranked.out1 file. 

## Languages

To see what languages are the most popular
```
awk '{print $6}' language.out | sort  >l.out
awk '{a[$1]++;b[$1]=b[$1]+$2} END{for (i in a) print i,a[i],b[i]}' l.out
```
Will render output like: 
```
Swift 1 0
Java 26 0
Ruby 53 0
Puppet 32 0
Arduino 3 0
Lua 1 0
XSLT 1 0
Go 67 0
C# 4 0
CoffeeScript 1 0
C++ 13 0
Scala 8 0
PowerShell 1 0
C 39 0
Emacs 1 0
Python 259 0
Shell 71 0
Makefile 6 0
Objective-C 2 0
JavaScript 36 0
R 7 0
Perl 7 0
BitBake 1 0
VimL 7 0
HTML 17 0
Clojure 1 0
OpenSCAD 1 0
PHP 20 0
TeX 1 0
CSS 13 0
HCL 1 0
```
