_Download some wiki backups from AvailableBackups_

<img src='https://upload.wikimedia.org/wikipedia/commons/f/f3/Nuvola_apps_Wild.png' alt='Documentation' width='100px' align='right' title='Documentation' />
This is a tutorial to learn how to backup a wiki using WikiTeam tools. You can **backup your wiki or any public wiki**.

**Table of contents:**


# Generating a wiki backup #
## I have shell access to server ##

If you have shell access on the web server, follow the instructions on this page: http://www.mediawiki.org/wiki/Manual:DumpBackup.php for an XML backup. For an image backup, just copy the image directory (see your LocalSettings.php for details) or use [dumpUploads.php](https://git.wikimedia.org/blob/mediawiki%2Fcore/HEAD/maintenance%2FdumpUploads.php) to make a fancy list that you can use with tar etc.

## I have no shell access to server ##

If you have no shell access, then use the WikiTeam [dumpgenerator.py](http://code.google.com/p/wikiteam/source/browse/trunk/dumpgenerator.py) ([download](http://wikiteam.googlecode.com/svn/trunk/dumpgenerator.py)), available at the [repository](http://code.google.com/p/wikiteam/source/browse/#svn%2Ftrunk).

There are **[thousands wikis you can help archive](https://wikiapiary.com/wiki/Category:Website_not_archived)**, for which our wonderful friends of WikiApiary could not find a dump.

### Requirements ###

You will need **Python**: http://www.python.org/download/
The dump generator will need to be run from a DOS or GNU/Linux command-line.

### Dump types ###
There are two types of backups that can be made: **XML dumps** (current and history) and **image dumps**. (But you can do both in one dump - see below.)

An **XML dump** contains the meta-data of the edits (author, date, comment) and the text (wikitext). An XML dump may be "**current**" or "**history**". A "history" dump contains the complete history of every page, which is better for historical and research purposes and is the default. A "current" dump contains only the last edit for every page.

An **image dump** contains all the images available in a wiki, plus their descriptions.

### Running the script ###

There are two ways to start a backup - **API** (api.php) or **index.php** . API is the better method to use, but index.php can be used when the API is not available. (Not all mediawiki wikis have api.php.)
To find out if the wiki you want to back up has api.php or not, open a browser window and go to the wiki's Main Page.
Click on the "View history" tab. You will see a URL such as this: _http://en.wikipedia.org/w/index.php?title=Main\_Page&action=history_
Now edit the URL: remove everything after _/w/_, and replace it with _api.php_ (In the example, the result would be: _http://en.wikipedia.org/w/api.php_). If you see a webpage with the API documentation, copy the URL to the clipboard. If not,  the API is probably not being used in the wiki or check the URL and try again (or use index.php).

If there is no api.php, then you'll need to use index.php. For the correct URL, in the example above, remove everything after the '_?_' and copy the URL to the clipboard. (In the example above the correct URL would be: _http://en.wikipedia.org/w/index.php_)

Note: **DO NOT** try to dump the Wikipedia site! It would result in a file that would quite likely be in the terabyte range. We are just using the Wikipedia URL as an example.

At a DOS prompt or GNU/Linux command line, type the following:

If the wiki you want to backup has api.php, use this:
  * _python dumpgenerator.py --api=http://en.wikipedia.org/w/api.php --xml_

If you need to use index.php, then use this:
  * _python dumpgenerator.py --index=http://en.wikipedia.org/w/index.php --xml_

For a complete dump with both xml and images, use both '--xml' and '--images' in the same command, like this:
  * _python dumpgenerator.py --api=http://en.wikipedia.org/w/api.php --xml --images_

The _--xml_ option gets the full history of every page. If you only want the last revision for every page, you will need to use _--xml --curonly_

To reduce the demands of downloading wiki pages one after another, it is recommended that you use a delay.
Use _--delay_ to add any length of delay you want. For example, a delay of 5 seconds between each request: _--delay=5_

To resume an interrupted dump, use the parameters _--resume_ and _--path_ to indicate where the incomplete dump is located. The command will look something like this:
  * _python dumpgenerator.py --api=http://en.wikipedia.org/w/index.php --xml --images --resume --path=dumpdirectory_

When you start a new dump, the script will create a directory (or folder) in the form of: domainorg-20110520-wikidump . Sometimes there will be a sub-directory in the name, or "wiki" added in - that's OK.

### Checking dump integrity ###

If you want to check the XML dump integrity (optional), there are two possible methods:

1. You can try to import it into a MediaWiki (using [this method](http://www.mediawiki.org/wiki/Manual:Importing_XML_dumps), which may be slow if wiki is large).

or

2. Type this into your command line (GNU/Linux) to count _`<title>`__`<page>`__`</page>`_ and _`<revision>`__`</revision>`_ XML tags:

  * _grep "`<title>`" `*`.xml -c;grep "`<page>`" `*`.xml -c;grep "`</page>`" `*`.xml -c;grep "`<revision>`" `*`.xml -c;grep "`</revision>`" `*`.xml -c_

You should see something similar to this (not the actual numbers - the first three numbers should be the same and the last two should be the same as each other):
  * 580
  * 580
  * 580
  * 5677
  * 5677

If your first three numbers or your last two numbers are different, then, your XML dump is corrupt (it contains one or more unfinished `</page>` or `</revision>`). This is not common in small wikis, but large or very large wikis may fail at this due to truncated XML pages while exporting and merging. The solution is to remove the XML dump and resume (re-download, a bit boring, and it can fail again...), or if you don't care to lose the corrupt pages, exclude them with this script (TO DO).

### Further steps: compression ###
After the wiki dump is complete, you will need to archive the files in the wikidump directory. The WikiTeam project uses the **7-Zip** file archiver. 7z is a compressed archive file format. We use it because it is free (the GNU LGPL license) and it has a high compression ratio. [Read about it](http://en.wikipedia.org/wiki/7z) in Wikipedia. There is  software for [Windows](http://www.7-zip.org) and [GNU/Linux](http://p7zip.sourceforge.net) (_sudo apt-get install p7zip_). There are also graphical front-ends for archiving programs for both Windows and GNU/Linux.

You can use a graphical front-end to compress and archive the files, or run one of these commands:
  * 7z a  domainorg-20110520-history.xml.7z domainorg-20110520-wikidump/**-- for xml only**

or

  * 7z a  domainorg-20110520-wikidump.7z domainorg-20110520-wikidump/**-- for xml & images**

It is suggested that you use the following file-naming convention: domainorg-20110520-history.xml.7z - where "domainorg" is the domain name, "20110520" is the date the dump was started. (You can use the domain name and date from the directory that was created when the dump was started.)

### Automatic ###

[launcher.py](https://code.google.com/p/wikiteam/source/browse/trunk/batchdownload/launcher.py) does all this automatically for you; especially useful for multiple wikis at once (it takes a text list of wikis as input): see "Download a list of wikis" below.

# Publishing the dump #
And of course, you then have to release your dumps! You can easily do so on the [Internet Archive's wikiteam collection](https://archive.org/details/wikiteam). [Login](http://archive.org/account/login.php) or register first.

## Automatic publishing ##

Normally, you can just use [uploader.py](https://code.google.com/p/wikiteam/source/browse/trunk/uploader.py) (especially if you have multiple wikis): the script takes the filename of a list of wikis as argument and uploads their dumps to archive.org.
If you've used launcher.py or followed the instructions above closely, you only need to:
  1. [take your s3 keys](http://www.archive.org/account/s3.php), save them one per line on a `keys.txt` file;
  1. run the script like `python uploader.py mywikis`, where `mywikis` is a list of the api.php URL(s) of the wiki(s) to upload, one per line.

If this doesn't work for you, check that dumps are in the same directory and follow the -wikidump.7z/-history.xml.7z format as produced by launcher.py (explained in the next section).

## Manual publishing ##

  1. [Create a new item](http://archive.org/create/) for each wiki.
  1. Use wiki-DOMAIN as identifier and "Wiki - NAME" as title.
  1. Add "MediaWiki; wiki; wikiteam" as subject/keywords so that it's possible to find the item.
  1. If possible, enter more info in the relevant fields, like the license of the wiki.
  1. Follow the instructions to upload the archives.
  1. In the last step, put the item in texts/opensource (community texts); it will then moved to the WikiTeam collection (until then, it should be listed with this [search](http://archive.org/search.php?query=subject%3A%22wikiteam%22%20AND%20collection%3Aopensource).

Advanced tips:
  1. For particularly big archives you might want to use [S3](http://archive.org/help/abouts3.txt) (for API keys, see [this page](http://archive.org/account/s3.php)), or [this tool](https://wiki.archive.org/twiki/bin/view/Main/IAS3BulkUploader) if you have many items.
  1. If you use such command line tools, choose "web" as media type: it's more correct, doesn't need authorisation and will make the items appear in the [web crawls collection](http://archive.org/details/web).
  1. To facilitate future dumps and further metadata fixes, please add the api.php URL of the wiki to the `originalurl` field.
  1. Beware that if you specify a non-Creative Commons license in the licenseurl parameter, due to a bug, you won't be able to edit the item metadata via the graphical interface any longer, so put all the details from the start.

# Download a list of wikis #
A script has been created to mass download lists of wikis, initially for the TaskForce: [launcher.py](http://wikiteam.googlecode.com/svn/trunk/batchdownload/launcher.py).

Just place it in the same directory as dumpgenerator.py and run it like this: **python launcher.py mylist.txt**. The list must contain URLs to the [api.php](https://www.mediawiki.org/wiki/API:Main_page#The_endpoint) of each wiki you have to download, one per line.

The script will try to dump both pages and images of all those wikis, to verify the integrity of the XML dump and to create archives ready for upload to the Internet Archive. It doesn't handle upload yet, but it will soon.

Skimming the output of the script is not very handy, but you can just rerun after completion to ensure that it actually did everything and not terminate some download due to an error: the script checks if the XML is complete (closed by `</mediawiki>`) and all images have been downloaded (the last one on the list has been downloaded) and if not resumes the dump; creates the compressed archive if not produced yet; downloads the missing wikis.

# I want to import an XML/image dump, how can I do it? #

Read http://www.mediawiki.org/wiki/Manual:Importing_XML_dumps and http://www.mediawiki.org/wiki/Manual:ImportImages.php.

# Further help #
Remember you always can see the inline help with _--help_ parameter.

If you have further questions, you can send a message to our [mailing list](http://groups.google.com/group/wikiteam-discuss). If you detect any error, [report an issue](http://code.google.com/p/wikiteam/issues/list). **Be bold!**