from typing import List, Dict
from concurrent.futures.thread import ThreadPoolExecutor
import click
from rich.console import Console
from rich import print

console = Console()


@click.group()
def av2():
    pass

@av2.command()
@click.option('-i', '--source_video', help='视频在硬盘中的路径')
def view(source_video: str = ...):
    """ view all container """
    import av2
    import json
    import yaml

    with av2.open(source_video) as file:
        print(file.dict())
        print(json.dumps(file.dict(),indent=4))
        print(yaml.dump(file.dict(),indent=4))

@av2.command()
@click.option('-i', '--source_video', help='视频在硬盘中的路径')
def info(source_video: str = ...):
    """ view all container """
    import av2
    import json
    import yaml

    with av2.open(source_video) as file:
        print(file.dict())
        print(json.dumps(file.dict(),indent=4))
        print(yaml.dump(file.dict(),indent=4))
        


cli = click.CommandCollection(sources=[av2])

if __name__ == '__main__':
    cli()
