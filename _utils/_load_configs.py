import yaml


def _load_config(cfg_path: str):
    if not isinstance(cfg_path, str):
        raise TypeError(
            f"Expected type of argument cfg_path is str, got {type(cfg_path)}"
        )
    try:
        with open(cfg_path, "r") as file:
            data = yaml.safe_load(file)
            if not isinstance(data, dict):
                raise ValueError(
                    f"Config file {cfg_path} must define a mapping, got {type(data)}"
                )
            return data
    except Exception as e:
        raise RuntimeError(f"Failed loading config from {cfg_path}") from e
