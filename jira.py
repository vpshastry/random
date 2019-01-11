# Copyright: Bitti

from jira.client import JIRA
import requests
from pprint import pprint
import sys

auth=("", "")
query='fixVersion in (versionMatch(5.5),versionMatch(5.8),versionMatch(5.9),versionMatch(5.10)) and status = Resolved and "Assignee Manager" in (<assignee manager>) and project = ENG and issueType not in (Epic, Test, Bug, Improvement) and assignee = currentUser()'
jira_options={"server": url, "verify": False}
integrated_version_field='customfield_11360'
verified_version_field='customfield_11361' #verify

jira_client = JIRA(options=jira_options, basic_auth=auth)
if not jira_client:
  print "Failed"
  sys.exit()

def get_field_list(issue_id, field):
  url="https://"+url+"/rest/api/2/issue/"+issue_id
  headers = {"Accept": "application/json", "Content-Type": "application/json"}
  response = requests.get(url, auth=auth, headers=headers)
  data = response.json()
  if (data and "fields" in data and field in data["fields"]):
    return data["fields"][field]

ret = jira_client.search_issues(query)

result = {}
for each in ret:
  integrated_version_list = get_field_list(each.key, integrated_version_field)
  fix_version_list = get_field_list(each.key, 'fixVersions')
  verified_version_list = get_field(each.key, verified_version_field)
  issue = jira_client.issue(each.key)
  result[each.key] = {}

  verified_version_name_list = [fix_version['name'] for fix_version in verified_version_list]
  integrated_version_name_list = [fix_version['name'] for fix_version in integrated_version_list]
  fix_version_name_list = [verified_version['name'] for verified_version in fix_version_list]
  to_be_updated_verified_name_list = list(set(fix_version_name_list) - set(verified_version_name_list))
  to_be_updated_integrate_name_list = list(set(fix_version_name_list) - set(integrated_version_name_list))

  for fix_version in fix_version_list:
    name = fix_version["name"]
    if name in to_be_updated_integrate_name_list:
      if "verified_version" not in result[each.key]:
        result[each.key]["integrated_version"] = []
      result[each.key]["integrated_version"].append(name)
      print "Updating {2}: {0} to {1}".format(integrated_version_field, name, each.key)
      issue.add_field_value(integrated_version_field, fix_version)

    if name in to_be_updated_verified_name_list:
      if "verified_version" not in result[each.key]:
        result[each.key]["verified_version"] = []
      result[each.key]["verified_version"].append(name)
      print "Updating {2}: {0} to {1}".format(verified_version_field, name, each.key)
      issue.add_field_value(verified_version_field, fix_version)

pprint(result)
