"""Logic to calculate 3-decimal parameter deltas and change booleans."""

import pandas as pd


def compute_target_deltas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute target delta columns for all controllable parameters.
    
    Deltas are computed as: after_value - before_value
    and rounded to 3 decimal places.
    
    Args:
        df: DataFrame with before_* and after_* parameter columns
        
    Returns:
        DataFrame with added target delta columns
    """
    result = df.copy()
    
    # Compute deltas for each controllable parameter
    result["target_iris_delta"] = (
        result["after_iris_position"] - result["before_iris_position"]
    ).round(3)
    
    result["target_z_delta"] = (
        result["after_z_position"] - result["before_z_position"]
    ).round(3)
    
    result["target_pitch_delta"] = (
        result["after_pitch_position"] - result["before_pitch_position"]
    ).round(3)
    
    result["target_yaw_delta"] = (
        result["after_yaw_position"] - result["before_yaw_position"]
    ).round(3)
    
    return result


def compute_changed_labels(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute binary changed label columns for all controllable parameters.
    
    A parameter is considered "changed" if its delta is non-zero.
    
    Args:
        df: DataFrame with target delta columns
        
    Returns:
        DataFrame with added changed label columns
    """
    result = df.copy()
    
    result["target_iris_changed"] = (
        result["target_iris_delta"] != 0.000
    ).astype(int)
    
    result["target_z_changed"] = (
        result["target_z_delta"] != 0.000
    ).astype(int)
    
    result["target_pitch_changed"] = (
        result["target_pitch_delta"] != 0.000
    ).astype(int)
    
    result["target_yaw_changed"] = (
        result["target_yaw_delta"] != 0.000
    ).astype(int)
    
    return result


def validate_diff_count(df: pd.DataFrame) -> tuple[int, pd.DataFrame]:
    """
    Validate meta_diff_count against synthesized changed labels.
    
    Args:
        df: DataFrame with meta_diff_count and target_*_changed columns
        
    Returns:
        Tuple of (mismatch_count, dataframe_of_mismatches)
    """
    synthesized_changes = (
        df["target_iris_changed"] +
        df["target_z_changed"] +
        df["target_pitch_changed"] +
        df["target_yaw_changed"]
    )
    
    mismatches = df[synthesized_changes != df["meta_diff_count"]]
    
    return len(mismatches), mismatches


def drop_after_controllable_params(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop after-state controllable parameter columns to prevent data leakage.
    
    Args:
        df: DataFrame with after_* controllable parameter columns
        
    Returns:
        DataFrame with leakage columns dropped
    """
    leakage_cols = [
        "after_iris_position",
        "after_z_position",
        "after_pitch_position",
        "after_yaw_position",
    ]
    
    return df.drop(columns=[c for c in leakage_cols if c in df.columns])
