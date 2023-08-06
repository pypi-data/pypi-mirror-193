import typer
from . import portals
from . import transformations

app = typer.Typer()
app.add_typer(portals.app, name="portals")
app.add_typer(transformations.app, name="transformations")

@app.callback()
def callback():
    """
    Transform data into hardware-agnostic AI models, using the Edge Impulse API
    """

if __name__ == "__main__":
    app()