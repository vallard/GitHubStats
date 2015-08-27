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
sort -rnk 2 repos.out3 >topranked.out1
```
Will put the top ranked repo first in the new topranked.out1 file. 
