import requests
import os
os.environ["CDF_LIB"] = "~/CDF/lib"
from spacepy import pycdf
from shutil import copyfileobj, copy
from tempfile import NamedTemporaryFile
from pytplot import tplot, cdf_to_tplot


##Yee haw. No gods no kings no comments

head = {}
suffix=''
varnames=[]
prefix = 'psp_isois_'
url =  "https://spdf.gsfc.nasa.gov/pub/data/psp/isois/merged/l2/summary/2018/psp_isois_l2-summary_20181006_v13.cdf"
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

testVars = cdf_to_tplot("testData.CDF", suffix=suffix, prefix=prefix, get_support_data=False, 
                    varformat=None, varnames=varnames, notplot=False)

print(testVars)

tplot([prefix+"Electron_CountRate_ChanE", prefix+"HET_A_H_Rate_TS", prefix+"HET_A_Electrons_Rate_TS", prefix+"H_CountRate_ChanP_SP"])