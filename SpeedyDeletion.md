# Introduction #

Wikipedia articles are constantly deleted, sometimes so quickly that you don't even notice. They are sometimes put in the speedy deletion category http://en.wikipedia.org/wiki/Category:Speedy_deletion and its subcategories so that administrators notice them and delete those pages.

However, these speedily-deleted articles may contain useful information to other wikis, but isn't notable in Wikipedia. We think its a shame for it to be deleted and hidden from public's view, and thus we are doing this project to allow these deleted articles have hopes of coming back to Wikipedia again, once they passed the notability tests.

# Code #

Many thanks to Mike Dupont, he merged the code from the pywikipedia bot framework with some of WikiTeam's tools, and it is located here:

https://github.com/h4ck3rm1k3/wikiteam

## S3 buckets ##
It uses boto/s3 to upload the buckets, they are currently created by hand, but use the month name.

For May 2012 :
http://archive.org/details/wikipedia-delete-2012-05

For June 2012 :
http://archive.org/details/wikipedia-delete-2012-06
http://archive.org/details/wikipedia-delete-v2-2012-06

July 2012:
http://archive.org/details/wikipedia-delete-2012-07
http://archive.org/details/wikipedia-delete-v2-2012-07
http://archive.org/details/wikipedia-delete-v3-2012-07


August 2012:
http://archive.org/details/wikipedia-delete-v2-2012-08


## crontab ##
This script can be run from crontab at 30 minute intervals. Here is a snippet of what you should add:
```
1,30 * * * * bash /path/to/runexport.sh
```

## runexport.sh ##
The runexport.sh script is this:
```
export PYTHONPATH=/home/mdupont/experiments/wikipedia/wikiteamgit/
cd /home/mdupont/experiments/wikipedia/wikiteamgit/data
python /home/mdupont/experiments/wikipedia/wikiteamgit/dumpgenerator.py --api=http://en.wikipedia.org/w/api.php --xml
```


## Hosting ##

I have started to populate the speedy deletion wikia with speedy delete and contested articles
http://speedydeletion.wikia.com/wiki/Speedy_deletion_Wiki

the updated script to upload is here:
https://github.com/h4ck3rm1k3/pywikipediabot/commit/a2ebb6aa3363ac4cb354147d8d7af5e1199abc43
Posted 2 hours ago by James Michael Dupont

## Blog posts ##

http://undeletewikipedia.blogspot.de/2012/05/export-articles-to-be-deleted.html

## See Also ##

http://deletionpedia.dbatley.com/w/index.php?title=Main_Page

Seems to be down: http://wikiscanner.virgil.gr/
wikipedia stats : http://stats.grok.se/?pos=7&s=10
http://lexisum.com/