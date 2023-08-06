from pathlib import Path
from typing import Optional

import typer

from talkkeeper.packages.index import Index
from talkkeeper.packages.uploader import Uploader

app = typer.Typer()


@app.command()
def scan(files: Optional[Path] = typer.Option(None)):
    i = Index()
    for tk in Uploader.get(files or Path(".")):
        i.push(tk)
        print(tk)


if __name__ == "__main__":
    app()
