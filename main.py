import typer

app = typer.Typer()

def main() -> int:
    app()
    return 0

@app.command()
def hello(name: str = typer.Argument(..., help="Name to greet")):
    typer.echo(f"Hello, {name}!")


if __name__ == '__main__':
    exit(main())