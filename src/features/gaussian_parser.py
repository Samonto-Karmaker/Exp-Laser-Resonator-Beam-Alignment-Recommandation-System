"""Regex logic to extract centers/scales from the equation strings."""

import re
import pandas as pd


def parse_gaussian_equation(equation: str) -> tuple[float | None, float | None]:
    """
    Parse a Gaussian equation string into center and scale parameters.
    
    Expected format: Aexp[-2([x-center]/scale)^2]
    
    Args:
        equation: Gaussian equation string from the dataset
        
    Returns:
        Tuple of (center, scale) as floats, or (None, None) if parsing fails
    """
    if not isinstance(equation, str) or not equation.strip():
        return None, None
    
    # Pattern to match: Aexp[-2([x-center]/scale)^2]
    pattern = r'Aexp\[-2\(\[x-(-?\d+(?:\.\d+)?)\]/(-?\d+(?:\.\d+)?)\)\^2\]'
    match = re.match(pattern, equation.strip())
    
    if not match:
        return None, None
    
    try:
        center = float(match.group(1))
        scale = float(match.group(2))
        return center, scale
    except (ValueError, AttributeError):
        return None, None


def parse_gaussian_dataframe(df: pd.DataFrame, prefix: str = "before") -> pd.DataFrame:
    """
    Parse Gaussian equations for both X and Y axes and add parsed columns to DataFrame.
    
    Args:
        df: DataFrame containing raw Gaussian equation columns
        prefix: Prefix for the columns ('before' or 'after')
        
    Returns:
        DataFrame with added parsed center and scale columns
    """
    result = df.copy()
    
    # Parse X axis
    x_eq_col = f"{prefix}_x_axis_gaussian_equation"
    y_eq_col = f"{prefix}_y_axis_gaussian_equation"
    
    x_center_col = f"{prefix}_x_gaussian_center_parsed"
    x_scale_col = f"{prefix}_x_gaussian_scale_parsed"
    y_center_col = f"{prefix}_y_gaussian_center_parsed"
    y_scale_col = f"{prefix}_y_gaussian_scale_parsed"
    
    # Parse X axis equations
    x_parsed = result[x_eq_col].apply(parse_gaussian_equation)
    result[x_center_col] = x_parsed.apply(lambda x: x[0] if x else None)
    result[x_scale_col] = x_parsed.apply(lambda x: x[1] if x else None)
    
    # Parse Y axis equations
    y_parsed = result[y_eq_col].apply(parse_gaussian_equation)
    result[y_center_col] = y_parsed.apply(lambda x: x[0] if x else None)
    result[y_scale_col] = y_parsed.apply(lambda x: x[1] if x else None)
    
    return result


def count_parse_failures(df: pd.DataFrame, prefix: str = "before") -> dict:
    """
    Count parsing failures for Gaussian equations.
    
    Args:
        df: DataFrame with parsed Gaussian columns
        prefix: Prefix for the columns ('before' or 'after')
        
    Returns:
        Dictionary with null counts for each parsed column
    """
    center_col = f"{prefix}_x_gaussian_center_parsed"
    scale_col = f"{prefix}_x_gaussian_scale_parsed"
    
    return {
        "center_nulls": df[center_col].isna().sum(),
        "scale_nulls": df[scale_col].isna().sum(),
    }
