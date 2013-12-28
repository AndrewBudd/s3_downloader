from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys
import os.path
import yaml

# load settings from a yaml file
config_fp = open('config.yml')
config = yaml.load(config_fp)
config_fp.close()

# decouple config file structure from every place a setting is used
aws_public_key  = config['aws']['public_key']
aws_private_key = config['aws']['private_key']
aws_s3_bucket   = config['aws']['s3_bucket']
download_to     = config['download_to']

conn = S3Connection(aws_public_key,aws_private_key)

mybucket = conn.get_bucket(aws_s3_bucket)

rs = mybucket.list()

for key in rs:
  if(key.storage_class != 'GLACIER' and not os.path.isfile(download_to+key.name)):
    print key.name
    key.get_contents_to_filename(download_to+key.name)

