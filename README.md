s3_downloader
=============

simple python script that downloads all the files from an s3 bucket that are not in 'glacier'

It follows this simple process:

1. Get an iterator for the keys in the bucket
1. Step through each key
 1. If the key has a storage_class of GLACIER, skip it
 1. If the key already exists as a file in the to_download directory, skip it
 1. Print the key name
 1. Download the contents of the object to a file named after the key in the to_download directory


SETUP
============

Using virtualenv is strongly recommended

```
pip install boto
pip install pyyaml
```

Edit config.yml to taste.

MOTIVATION
============

Why?
Well, why not?
No, but seriously, why?

I have a raspberry pi that I use to capture timelapses of things like snow accumulating out of the window.  The pi has a script which uploads the timelapses (and the jpgs that make them up) to an s3 bucket.  After some number of days, the objects are automatically transitioned to GLACIER using a lifecycle rule.

At some point I wanted to download all of the images that were not in glacier yet (say, the timelapses from the last week or so).  This would have been more painful to do manually than to whip up in python.  I mean, why does anyone ever write a script? =p
