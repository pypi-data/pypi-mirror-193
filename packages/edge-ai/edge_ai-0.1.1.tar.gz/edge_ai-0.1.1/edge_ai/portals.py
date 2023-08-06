import typer
import pandas as pd
from .common import api
from .common import utils
from .common import opts

app = typer.Typer()

@app.callback()
def callback():
    """
    Work with Edge Impulse Upload Portals
    """

@app.command()
def create(org_id: int = opts.REQUIRED_ORG_ID,
           org_key: str = opts.REQUIRED_ORG_KEY,
           name: str = typer.Option(..., help="the name of the portal to create")):
    """
    Create an organization data upload portal on Edge Impulse
    """
    # print(org_id, name)
    # Use the name as the bucket path (just replace spaces with dashes)
    payload = {
        "name": name,
        "bucketId": 0,
        "bucketPath": name.replace(" ", "-").replace("\\",
                                                     "-").replace("/", "-")
    }
    api.do_org_post(org_id, org_key, "/portals/create", payload, debug=False)

@app.command()
def show(org_id: int = opts.REQUIRED_ORG_ID,
         org_key: str = opts.REQUIRED_ORG_KEY,
         portal_id: int = opts.OPTIONAL_PORTAL_ID,
         contents: bool = typer.Option(False, help="Show the contents of the portal")):
    """
    Show upload portal details of an Edge Impulse organization

    If --portal-id is provided, only the details for that portal will be shown
    """
    if portal_id == None or isinstance(portal_id, typer.models.OptionInfo):
        response = api.do_org_get(org_id, org_key, "/portals")
        portals = response["portals"]
        if len(portals) > 0:
            df = pd.DataFrame(portals)
            # df will have the following columns:
            # print(df.columns.values)
            # [
            #     "id"
            #     "name"
            #     "description"
            #     "url"
            #     "bucketName"  👈🏽 Irrelevant to customers
            #     "bucketPath"  👈🏽 Irrelevant to customers
            #     "bucketUrl"   👈🏽 Irrelevant to customers
            #     "created"
            # ]
            output = []
            for portal in portals:
                del portal["bucketName"]
                del portal["bucketPath"]
                del portal["bucketUrl"]
                output.append(portal)
            print(df[["id", "name", "url"]].to_string(index=False))
            return output
        else:
            print("This organization has no portals")
            return None
    else:
        response = api.do_org_get(org_id, org_key, "/portals/%s" % portal_id)
        portal = response
        del portal["success"]
        if contents:
            portal["files"] = response["files"]
            response = api.do_org_get(org_id, org_key, "/portals/%s/verify" % portal_id)
            print("Listing the contents of portal %s" % portal_id)
            for item in response["files"]:
                print("- %s/%s" % (item["folderName"], item["name"]))
        return portal

@app.command()
def download(org_id: int = opts.REQUIRED_ORG_ID,
             username: str = opts.REQUIRED_EI_USERNAME,
             password: str = opts.REQUIRED_EI_PASSWORD,
             portal_id: int = opts.REQUIRED_PORTAL_ID,
             path: str = typer.Option(..., help="the path where the portal files should be downloaded")):
    """
    Download the contents of an Edge Impulse organization portal
    """
    # Get JWT token
    response = api.get_jwt(username, password)
    jwt = response["token"]
    # Get portal token
    response = api.do_jwt_get(
        jwt, "organizations/%s/portals/%s" % (org_id, portal_id))
    token = response["token"]
    # Download files in base folder
    print("Downloading the contents of portal %s" % portal_id, flush=True)
    utils.download_folder(jwt, portal_id, path, token, folder_path='')

@app.command()
def delete(org_id: int = opts.REQUIRED_ORG_ID,
           org_key: str = opts.REQUIRED_ORG_KEY,
           portal_id: int = opts.REQUIRED_PORTAL_ID):
    """
    Delete an organization portal from Edge Impulse
    """
    response = api.do_org_delete(org_id, org_key,
                                "/portals/%s/delete" % portal_id)
    if response["success"]:
        msg = "Portal %s successfully deleted" % portal_id
    else:
        msg = "Could not delete portal %s" % portal_id
    print(msg)
    response["message"] = msg
    return response

if __name__ == "__main__":
    app()