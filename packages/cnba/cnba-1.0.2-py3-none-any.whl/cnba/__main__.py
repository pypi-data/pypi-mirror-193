import click
from .commands import init

@click.group(help="CLI tool for CNBA network analysis")
def main():
    pass


# cnba.add_command(init.create)
main.add_command(init.run)


if __name__=="__main__":
    main()