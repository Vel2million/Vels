import requests
import base64

if __name__ == "__main__":
    b64Val = base64.b64encode('__USER__:__PASS__'.encode('utf-8'))
    uriAddAttachment = "https://jira.bnc.ca/rest/api/2/issue/{0}/attachments".format('DHO-2064')
    
    files = {'file': open('{0}'.format('__FILE_LOCATION__'), 'rb')}
    #headers
    headers2 = {
        "Authorization": "Basic {0}".format(b64Val),
        "X-Atlassian-Token": "nocheck"
    }
    
    requests.post(uriAddAttachment, headers=headers2, files=files)
