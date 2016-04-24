Here, we coordinate us to download all **non WikiFarms** wikis.

We start with a [list from Andrew Pavlo](http://www.cs.brown.edu/~pavlo/mediawiki/), which is [mirrored here](http://code.google.com/p/wikiteam/source/browse/trunk/listsofwikis/mediawikis_pavlo.csv). After discarding dead wikis, we have about [7,400+ alive wikis](http://code.google.com/p/wikiteam/source/browse/trunk/listsofwikis/mediawikis_pavlo.alive.filtered.txt).

## Requirements ##
You need GNU/Linux, Python and p7zip-full (sudo apt-get install p7zip-full).

## How to join the effort? ##

Download a list (every list has 100 wikis):

  * Choose one from [000 to 073](http://code.google.com/p/wikiteam/source/browse/trunk#trunk%2Fbatchdownload%2Flists)

And use the following scripts to backup the wikis:

  * [launcher.py](http://wikiteam.googlecode.com/svn/trunk/batchdownload/launcher.py)
  * [dumpgenerator.py](http://wikiteam.googlecode.com/svn/trunk/dumpgenerator.py)

After downloading a list and both scripts in the same directory, you can do: **python launcher.py mylist.txt**

It will backup every wiki and generate two 7z files for each one: _domain-date-history.xml.7z_ (just wikitext) and _domain-date-wikidump.7z_ (wikitext and images/ directory).

See also the NewTutorial page for details on how the scripts work.

**Note**: we recommend to split every 100 wikis list into 10 lists of 10. You can do that with the `split` command like this: `split -l10 list000 list000-`

### Volunteers table ###

Lists claimed by users. Notify us when you start downloading a list of wikis. If you can't edit this page, email us in [our mailing list](https://groups.google.com/group/wikiteam-discuss) (you have to join).

| **List** | **Member** | **Status** | **Notes** |
|:---------|:-----------|:-----------|:----------|
| 000      | emijrp     | Downloading | Downloaded: X. Incomplete: X. Errors: X. |
| 001      | ScottDB    | Downloaded |...        |
| 002      | underscor  | Downloading | ...       |
| 003      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?xs2m67fsd6WvOqsgMssN_g). Including citywiki.ugr.es that is [archived](http://archive.org/details/wiki-citywiki.ugr.es). **All wikis done** except [6 wikis which can't finish download](http://p.defau.lt/?YccPGmBR8qh9uf7FAiYnOA) and biosite still being downloaded. **[See logs](https://code.google.com/p/wikiteam/source/browse/trunk/listsofwikis/mediawikis_pavlo_launcherlogs-Nemo.7z)**. |
| 004      | ianmcorvidae | Downloading | Downloaded: 61; variety of errors, mostly index.php missing |
| 005      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?b_5gXJxVTPPzppgd7jxfrg); 1 wiki being redownloaded |
| 006      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?xFZdHVoVpJBhI5fA5icN3g) |
| 007      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?3qpqOZdAwinhcBFqCAg4vg) |
| 008      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?mS38BbpNQteTQZa8AI3mWQ) |
| 009      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?N4iuP5BFsmNjxf1wJ6GLDw) |
| 010      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?cuYNGuhwREQeDJZV0wlu4A) (katlas.math.toronto.edu has 1.6 million pages, finished as well) |
| 011      | mutoso     | _Downloaded_ | [Final check](http://p.defau.lt/?1_xFsDt6XdQMf_b0Ln9Kpg) |
| 012      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?c_BiYqgcaqw3WHpIsYiZYg) |
| 013      | Nemo       | _Downloaded_ | See above. |
| 014      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?_23I5WxxA1Nl420d7e2w6g) |
| 015      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?KwIjaL3YnDFaLZAxguSz5g) |
| 016      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?pivzqD3LC9vLC0v1nIhm9w); 1 wiki being redownloaded |
| 017      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?pacTBWaiBfOGWW00Qdzaew) |
| 018      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?KKDffMa_VX02rRGU91qY5g) |
| 019      | Nemo       | _Downloaded_ | See above. |
| 020      | mutoso     |            | ...       |
| 021      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?nu9Pm6nZ5viT6JXNaHcKBQ) |
| 022      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?_ftjeMHPvKfSLYaq7RbvOQ); 1 wiki being redownloaded |
| 023      | Nemo       | _Downloaded_ | See above. |
| 024      | Nemo       | _Downloaded_ | [Final check](http://p.defau.lt/?_IPvyVEBJa2UuoVzUM2Yag) |
| 025      | Nemo       | _Downloaded_ | See above. |
| 026      | Nemo       | _Downloaded_ | See above. |
| 027      | Nemo       | _Downloaded_ | See above. |
| 028      | Nemo       | _Downloaded_ | See above. |
| 029      | Nemo       | _Downloaded_ | See above. |
| 030      | Nemo       | _Downloaded_ | See above. |
| 031      | Nemo       | _Downloaded_ | See above. |
| 032      | Nemo       | _Downloaded_ | See above. |
| 033      | Nemo       | _Downloaded_ | See above. |
| 034      | Nemo       | _Downloaded_ | See above. |
| 035      | Nemo       | _Downloaded_ | See above. |
| 036      | Nemo       | _Downloaded_ | Except a single wiki still being downloaded |
| 037      | Nemo       | _Downloaded_ | See above. |
| 038      | Nemo       | _Downloaded_ | See above. |
| 039      | Nemo       | _Downloaded_ | See above. |
| 040      | Nemo       | _Downloaded_ | See above. |
| 041      | Nemo       | _Downloaded_ | See above. |
| 042      | Nemo       | _Downloaded_ | See above. |
| 043      | Nemo       | _Downloaded_ | See above. |
| 044      | Nemo       | _Downloaded_ | See above. |
| 045      | Nemo       | _Downloaded_ | See above. |
| 046      | Nemo       | _Downloaded_ | See above. |
| 047      | Nemo       | _Downloaded_ | See above. |
| 048      | Nemo       | _Downloaded_ | See above. |
| 049      | Nemo       | _Downloaded_ | See above. |
| 050      | Nemo       | _Downloaded_ | See above. |
| 051      | Nemo       | _Downloaded_ | See above. |
| 052      | Nemo       | _Downloaded_ | See above. |
| 053      | Nemo       | _Downloaded_ | See above. |
| 054      | Nemo       | _Downloaded_ | See above. |
| 055      | Nemo       | _Downloaded_ | See above. |
| 056      | Nemo       | _Downloaded_ | See above. |
| 057      | Nemo       | _Downloaded_ | See above. |
| 058      | Nemo       | _Downloaded_ | See above. |
| 059      | Nemo       | _Downloaded_ | See above. |
| 060      | Nemo       | _Downloaded_ | See above. |
| 061      | Nemo       | _Downloaded_ | See above. |
| 062      | Nemo       | _Downloaded_ | See above. |
| 063      | Nemo       | _Downloaded_ | See above. |
| 064      | Nemo       | _Downloaded_ | See above. |
| 065      | Nemo       | _Downloaded_ | See above. |
| 066      | underscor  | Downloading | ...       |
| 067      | underscor  | Downloading | ...       |
| 068      | underscor  | Downloading | ...       |
| 069      | underscor  | Downloading | ...       |
| 070      | underscor  | Downloading | ...       |
| 071      | underscor  | Downloading | ...       |
| 072      | underscor  | Downloading | ...       |
| 073      | underscor  | Downloading | ...       |

## Where/How to upload the dumps? ##

We are uploading the dumps to the [WikiTeam Collection](http://archive.org/details/wikiteam) at Internet Archive.

When you have finished a list of wikis and the script 7ziped them, you can proceed to upload the dumps.

You need to download [uploader.py](http://code.google.com/p/wikiteam/source/browse/trunk/uploader.py) in the same directory you have the .7z dumps, dumpgenerator.py and the list.txt.

You will need [Internet Archive S3-keys](http://archive.org/account/s3.php) associated to your user account. Generate and save them both in a file named keys.txt (first line for access key, second line for secret key).

To execute, do this: **python uploader.py mylist.txt**

It generates a log file which you must preserve to avoid reuploading the same dumps if you re-run the upload script.