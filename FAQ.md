**Table of contents:**


### What is the purpose of this project? ###

There are [thousands of wikis](http://wikiindex.org) in the Internet. Everyday a few of them are lost, due to lack of backups. People download tons of films and music. Wikis, most of them published under free licenses, disappear from time to time because nobody grabbed a copy of them. That is a shame.

### What do a wiki backup contain? ###

A wiki backup (and those in **AvailableBackups** page) contain the text of the wikis and/or their images. Passwords or user accounts related information are **NOT** included. Read about the license of these materials below.

### What is the license of the texts and the files contained in the backups? ###

Every wiki has its own license.

Usually, wikis use free licenses like [Creative Commons](http://creativecommons.org) or [GFDL](http://en.wikipedia.org/wiki/GNU_Free_Documentation_License), but some wikis may have non-free content. For an exact answer, you must visit the wiki site and check the license (probably, at the bottom of the wiki page).

The licenses of the images are a bit more complex. Every image may have a different license. Again, check the wiki and/or every _.desc_ file inside the '_images_' directory in the backup. If the uploader did it correctly, the '_.desc_' file must contain the author, date, and license details of the image.

### I am a wiki administrator with shell access. How can I backup my wiki? ###

You can use [dumpBackup.php](http://www.mediawiki.org/wiki/Manual:DumpBackup.php), a script available in every MediaWiki installation.

### I am a wiki user. How can I backup a single article? ###

You can use [Special:Export](http://meta.wikimedia.org/wiki/Help:Export). There is an [advanced guide](http://www.mediawiki.org/wiki/Manual:Parameters_to_Special:Export) too.

### I am a wiki user. How can I backup the entire wiki? ###

You can use [Special:Export](http://meta.wikimedia.org/wiki/Help:Export) over all the pages. Or use a [WikiTeam](http://code.google.com/p/wikiteam/source/checkout) tool (dumpgenerator.py). **Read the NewTutorial.**

### What is that .7z format? Why do you use it? ###

7z is a compressed archive file format. I use it because it is free (GPL) and it has a high compression ratio. [Read about it](http://en.wikipedia.org/wiki/7z) in Wikipedia. There are software for [Windows](http://www.7-zip.org) and [GNU/Linux](http://p7zip.sourceforge.net) (_sudo apt-get install p7zip_).

### How can I import a XML dump? ###

Use the [importDump.php](http://www.mediawiki.org/wiki/Manual:ImportDump.php). Read [Manual:Importing XML dumps](http://www.mediawiki.org/wiki/Manual:Importing_XML_dumps).

### I would like to help you. How can I do it? ###

You can help [reporting broken links, bugs, new wikis or making suggestions](http://code.google.com/p/wikiteam/adminIssues). Thanks.

### Can I download a Wikipedia/Wikia backup? ###

Yes, you can. Wikimedia Foundation publishes dumps from time to time, so you don't need to use our tools. Follow this link [http://dumps.wikimedia.org](http://dumps.wikimedia.org). Read [this guide](http://en.wikipedia.org/wiki/User:Emijrp/Wikipedia_Archive) too (it includes details about Wikipedia offline readers).

Some other projects publish their backups too (although most of them publish only text, no images): [Citizendium](http://en.citizendium.org/wiki/CZ:Downloads), [Gentoo Linux Wiki](http://en.gentoo-wiki.com/wiki/Gentoo_Linux_Wiki:Backup), [OmegaWiki](http://www.omegawiki.org/Development), [OSDev](http://wiki.osdev.org/OSDev_Wiki:About), [Wikia](http://wiki-stats.wikia.com), [WikiFur](http://dumps.wikifur.com), [Wikivoyage](http://www.wikivoyage.org/general/Wikivoyage_General:XML_dumps).

**If a project publishes dumps, you don't have to use dumpgenerator.py**. Just download the dumps they offer, handy or using our download managers (see below).

**New!** We have developed Wikipedia/Wikia download managers. See [wikipediadownloader.py](http://code.google.com/p/wikiteam/source/browse/trunk/wikipediadownloader.py) and [wikiadownloader.py](http://code.google.com/p/wikiteam/source/browse/trunk/wikiadownloader.py).