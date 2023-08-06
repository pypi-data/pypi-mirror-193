from pathlib import Path
from typing import Optional

import typer

from talkkeeper.talkkeeper import Talkkeeper

app = typer.Typer()


@app.command()
def upload(files: Optional[Path] = typer.Option(None)):
    t = Talkkeeper.get(files or Path("."))
    for tk in t:
        tk.upload()
        print(tk)


if __name__ == "__main__":
    app()
