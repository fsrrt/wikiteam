How to use the dump generator? Here we explain it.

**We use [dumpgenerator.py](http://code.google.com/p/wikiteam/source/browse/trunk/dumpgenerator.py) ([download](http://wikiteam.googlecode.com/svn/trunk/dumpgenerator.py)), available at the [repository](http://code.google.com/p/wikiteam/source/browse/#svn%2Ftrunk).**

Remember you always can see the inline help with _--help_ parameter.

If you have further questions, you can send a message to our [mailing list](http://groups.google.com/group/wikiteam-discuss). If you detect any error, [report an issue](http://code.google.com/p/wikiteam/issues/list). **Be bold!**


---


**What kind of backups exist?**

There are XML dumps (current and history) and image dumps.

**What does a XML dump contain?**

A XML dump contains the metadata of the edits (author, date, comment) and the text (wikitext).

A XML dump may be "current" or "history". First one contains only the last edit for every page. Second one contains the full history (which is better for historical and research purposes).

**What does an image dump contain?**

An image dump contain all the images available in a wiki, plus their descriptions.

**How can I make a XML backup?**

If you have shell access, use this http://www.mediawiki.org/wiki/Manual:DumpBackup.php

If you have no shell access, then use our dump generator. If the wiki you want to backup has API, use this:
  * _python dumpgenerator.py --api=http://wikidomain.com/path/to/api.php --xml_

If API is not available, then use this:
  * _python dumpgenerator.py --index=http://wikidomain.com/path/to/index.php --xml_

**What if I only want the last version of every page, not the full history?**

_--xml_ option retrieves the full history, if you only want the last revision for every page, you have to use _--xml --curonly_

**How can I make an images backup?**

If you have shell access, copy the image directory (see your LocalSettings.php for details).

If you have no shell access, then use the same method in the question above, but replace _--xml_ with _--images_.

If the wiki you want to backup has API, use this:
  * _python dumpgenerator.py --api=http://wikidomain.com/path/to/api.php --images_

If API is not available, then use this:
  * _python dumpgenerator.py --index=http://wikidomain.com/path/to/index.php --images_

**How can I back up both XML and images?**

Just use _--xml_ and _--images_ at the same time:

  * _python dumpgenerator.py --api=http://wikidomain.com/path/to/api.php --xml --images_

**Which method is better, API or index.php?**

API is better. Use index.php only when API fails or is not available.

**How can I know the path of the API or index.php?**

Go to the wiki Main Page, click on "History" tab. You will see an URL with this format: _http://www.example.com/.../index.php?title=..._

If you want the API URL, remove all from _index.php_, and replace it with _api.php_ (in the example would result: _http://www.example.com/.../api.php_). If you see a webpage with the API documentation, then, you did it fine. Otherwise, API can be located in other path or you did it wrong.

If you want the index.php URL, remove only from the '?' symbol.

**Can I resume a dump?**

Of course, you can. Use the parameters _--resume_ and _--path_ to indicate where the incomplete dump is. The script will resume it.
  * _python dumpgenerator.py --api=http://wikidomain.com/path/to/api.php --xml --images --resume --path=dumpdirectory_

**Can I add a delay between server requests?**

Yes. Use _--delay_ to add any seconds you want. For example, a wait of 5 seconds between every request: _--delay=5_

**I want to import a XML/image dump, how can I do it?**

Read http://www.mediawiki.org/wiki/Manual:Importing_XML_dumps and http://www.mediawiki.org/wiki/Manual:ImportImages.php.

**How can I check the XML dump integrity?**

You can try to import it into a MediaWiki (using the method above, which may be slow if wiki is large), or writing this into your command line (GNU/Linux) to count _`<page>`__`</page>`__`<title>`_ and _`<revision>`__`</revision>`_ XML tags.

  * _grep "`<title>`" `*`.xml -c;grep "`<page>`" `*`.xml -c;grep "`</page>`" `*`.xml -c;grep "`<revision>`" `*`.xml -c;grep "`</revision>`" `*`.xml -c_

You have to see something similar to this (not the numbers but the equality between the first 3 numbers and the 2 last ones):
  * 580
  * 580
  * 580
  * 5677
  * 5677

If your first 3 numbers or your last 2 numbers are different, then, your XML dump is corrupt (it contains one or more unfinished `</page>` or `</revision>`). This is not common in small wikis, but large or very large wikis may fail at this due to truncated XML pages while exporting and merging. The solution is to remove the XML dump and resume (re-download, a bit boring, and it can fail again...), or if you don't care to lose the corrupt pages, exclude them with this script (TO DO).