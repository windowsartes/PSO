import json

import click

from src.scene.scene import Scene


@click.command()
@click.argument("path_to_config", type=click.Path(exists=True))
def cli(path_to_config: click.Path(exists=True)) -> None:
    with open(path_to_config, "r") as config_file:
        config = json.load(config_file)
    scene: Scene = Scene(config=config)

    print(scene.solve())


if __name__ == "__main__":
    cli()
