import requests
import os
os.environ["CDF_LIB"] = "~/CDF/lib"
from spacepy import pycdf
from shutil import copyfileobj, copy
from tempfile import NamedTemporaryFile

head = {}
url =  "https://spdf.gsfc.nasa.gov/pub/data/psp/isois/merged/l2/summary/2022/psp_isois_l2-summary_20220101_v13.cdf"
session = requests.Session()

fsvr = session.get(url, stream=True, verify=False, headers = head)

ftmp = NamedTemporaryFile(delete=False)

with open(ftmp.name, 'wb') as f:
    copyfileobj(fsvr.raw, f)

copy(ftmp.name, "testData.cdf")

fsvr.close()
ftmp.close()
os.unlink(ftmp.name)

cdf = pycdf.CDF('testData.cdf')
print(cdf)