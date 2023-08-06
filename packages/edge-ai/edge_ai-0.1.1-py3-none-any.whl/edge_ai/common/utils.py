import requests
from ..common import api

def download_folder(jwt, portal_id, path, token, folder_path=''):
    # Get list of files portals/{portalId}/files
    # prefix gives the folder path to download from
    response = api.do_jwt_post(jwt,
                              "portals/%s/files" % portal_id,
                              {"prefix": folder_path + "/"},
                              portal_token=token)
    for item in response["files"]:
        # If a folder (size == 0) then recurse down into next subfolder and download
        if item['size'] == 0:
            # print("\tSubfolder '%s' found, starting recursion..." %
            #       item['name'])
            download_folder(jwt, portal_id, path, token, item['path'] + item['name'])
            continue
        # Get the download URL per file
        filepath = os.path.join(item["path"], item["name"])
        print("- %s..." % filepath, end="", flush=True)
        response = api.do_jwt_post(jwt,
                                  "portals/%s/files/download" % portal_id,
                                  {"path": filepath},
                                  portal_token=token)
        response = requests.get(response["url"])
        # Make sure os.path.join doesn't think filepath is a root path
        if filepath.startswith("/"):
            filepath = filepath.strip("/")
        dest = os.path.join(path, filepath)
        # Make sure the directory we are saving to exists
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "wb").write(response.content)
        print(" downloaded to %s" % dest, flush=True)
    return

