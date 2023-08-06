import typer

HELP_PORTAL_ID = "the ID of the portal to download files from"
REQUIRED_ORG_ID = typer.Option(..., help="the ID of the Edge Impulse organization that the portal belongs to", envvar="EI_ORG_ID")
REQUIRED_ORG_KEY = typer.Option(..., help="an Edge Impulse Organization API key", envvar="EI_ORG_KEY")
REQUIRED_EI_USERNAME = typer.Option(..., help="the Edge Impulse username to login with", envvar="EI_USERNAME")
REQUIRED_EI_PASSWORD = typer.Option(..., help="the Edge Impulse user password", envvar="EI_PASSWORD")
REQUIRED_PORTAL_ID = typer.Option(..., help=HELP_PORTAL_ID)
OPTIONAL_PORTAL_ID = typer.Option(None, help=HELP_PORTAL_ID)
