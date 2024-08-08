# #!/bin/bash

# REPO_OWNER="king-technologies"
# REPO_NAME="kaushal"
# TOKEN=""

# releases=$(curl -s -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github.v3+json" "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/releases")

# for release in $(echo "$releases" | jq -r '.[] | @base64'); do
#     id=$(echo "$release" | base64 --decode | jq -r '.id')
#     curl -X DELETE -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github.v3+json" "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/releases/$id"
# done

import requests
import json


def remove_release(owner, repo, token, release_id):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/{release_id}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Release {release_id} deleted successfully")
    else:
        print(f"Error deleting release {release_id}: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    owner = "king-technologies"
    repo = "kaushal"
    token = ""
    release_id = "1"
    # https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/releases
    # get all releases
    # releases = requests.get(f"https://api.github.com/repos/{owner}/{repo}/releases", headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}).json()
    releases = requests.get(f"https://api.github.com/repos/{owner}/{repo}/tags", headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}).json()
    # print(releases)
    for release in releases:
        # id = release["id"]
        print(release)
        # delete release
        # remove_release(owner, repo, token, id)
    # remove_release(owner, repo, token, release_id)