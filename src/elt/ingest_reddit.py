import os
import json
import praw
import pandas
import sys
from datetime import date 
#add src folder to system path so we can import s3Utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import s3Utils as util #figure out how to import in dif folder

#use date.today() for day in yyyy-mm-dd