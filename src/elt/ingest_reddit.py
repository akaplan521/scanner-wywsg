import os
import json
import pandas
import sys
import requests
from datetime import date 
#add src folder to system path so I can import s3Utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import s3Utils as util 

#use date.today() for day in yyyy-mm-dd

