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


