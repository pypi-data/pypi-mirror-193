import typer
import pandas as pd
from .common import api
from .common import opts

app = typer.Typer()


@app.callback()
def callback():
    """
    Manage organization data transformations on Edge Impulse
    """


@app.command()
def create(org_id: int = opts.REQUIRED_ORG_ID,
           org_key: str = opts.REQUIRED_ORG_KEY,
           container: str = typer.Option(..., help="the URI of the Docker container to run (may include version tag)"),
           name: str = typer.Option(None, help="the name of the transformation block"),
           description: str = typer.Option(None, help="a summary describing the transformation block")):
    """
    Create a data transformation block on Edge Impulse
    
    Organization portals and buckets are mounted as /portals/<id> and /buckets/<id> respectively.
    """
    # Use container as name if name is missing
    if name == None:
        name = container

    # Use name as description if description is missing
    if description == None:
        description = name

    # Define mountpoints
    # Mount portals
    response = api.do_org_get(org_id, org_key, "/portals")
    portals = response["portals"]
    mount_points = []
    for portal in portals:
        # keys: { "id", "name", "description",
        #         "url", "bucketName", "bucketPath",
        #         "bucketUrl", "created" }
        mount_points.append({
            "mountPoint": "/portals/%s" % portal["id"],
            "portalId": int(portal["id"]),
            "type": "portal"
        })
    # Mount buckets
    response = api.do_org_get(org_id, org_key, "/buckets")
    buckets = response["buckets"]
    for bucket in buckets:
        mount_points.append({
            "mountPoint": "/buckets/%s" % bucket["id"],
            "bucketId": int(bucket["id"]),
            "type": "bucket"
        })
    # No metadata, no arguments
    payload = {
        "allowExtraCliArguments": True,
        "cliArguments": "",
        "description": description,
        "dockerContainer": container,
        "indMetadata": False,
        "name": name,
        "operatesOn": "standalone",
        "additionalMountPoints": mount_points
    }
    response = api.do_org_post(org_id, org_key, "/transformation",
                              payload)
    print(response)

@app.command()
def list(org_id: int = opts.REQUIRED_ORG_ID,
         org_key: str = opts.REQUIRED_ORG_KEY):
    """
    List data transformation blocks for an Edge Impulse organization
    """
    response = api.do_org_get(org_id, org_key, "/transformation")
    blocks = response["transformationBlocks"]
    if len(blocks) > 0:
        df = pd.DataFrame(blocks)
        # df will have the following columns:
        # print(df.columns.values)
        # [
        #     'id'
        #     'name'
        #     'dockerContainer'
        #     'dockerContainerManagedByEdgeImpulse'
        #     'created'
        #     'description'
        #     'cliArguments'
        #     'indMetadata'
        #     'additionalMountPoints'
        #     'operatesOn'
        #     'allowExtraCliArguments'
        # ]
        df = df[["id", "name", "dockerContainer", "additionalMountPoints"]]
        print(df.to_string(index=False))
    else:
        print("This organization has no data transformation blocks")

@app.command()
def delete(org_id: int = opts.REQUIRED_ORG_ID,
           org_key: str = opts.REQUIRED_ORG_KEY,
           transformation_id = typer.Option(..., help="the ID of the data transformation to delete")):
    """
    Delete a data transformation block for an Edge Impulse organization
    """
    response = api.do_org_delete(org_id, org_key,
                                "/transformation/%s" % id)
    print(response)
