"""Data loading utilities."""

from pathlib import Path
import pandas as pd


def load_labels(path: str | Path) -> pd.DataFrame:
    """
    Load the labels.json file containing beam state metadata.
    
    Args:
        path: Path to the labels.json file
        
    Returns:
        DataFrame with beam state metadata
    """
    return pd.read_json(path)


def load_pairs(path: str | Path) -> pd.DataFrame:
    """
    Load the sampled_pairs_500k.json file containing index pairs.
    
    Args:
        path: Path to the sampled_pairs_500k.json file
        
    Returns:
        DataFrame with index1, index2, and diff_count columns
    """
    return pd.read_json(path)


def find_project_root(start: str | Path | None = None) -> Path:
    """
    Find the repository root by walking upward to pyproject.toml.
    
    Args:
        start: Starting directory (defaults to current working directory)
        
    Returns:
        Path to the project root directory
    """
    current = (Path.cwd() if start is None else Path(start)).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "pyproject.toml").exists():
            return candidate
    raise FileNotFoundError("Could not find project root containing pyproject.toml")
