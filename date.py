# http://alfredworkflow.readthedocs.org/en/latest/xml_format.html
import datetime
import sys
from workflow import Workflow
wf = Workflow()

try:
    t = datetime.datetime.now()
    for fmt in ["%Y-%m-%d", "%Y%m%d"]:
        time_str = t.strftime(fmt)
        subtitle = "Press 'Enter' to copy '{}' to clipboard.".format(time_str)
        #wf.add_item(time_str,subtitle,arg=time_str,uid=fmt,valid=True)
        wf.add_item(time_str,subtitle,arg=time_str,valid=True)
except Exception as ex:
    msg = ex.message
    wf.add_item(msg)

# Print XML to STDOUT
wf.send_feedback()
