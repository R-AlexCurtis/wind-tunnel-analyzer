"""
analysis.py

Aerodynamic analysis utilities for the Wind Tunnel Analyzer project.

This module currently supports simple calculations based on a linear
lift-curve model. Numerical solver support for finding angle of attack
from a target lift coefficient is planned but not yet implemented.
"""

from scipy.optimize import fsolve


def compute_cl(alpha, cl0=0.10, lift_slope=0.11):
    """
    Compute lift coefficient using a linear lift model.

    Parameters
    ----------
    alpha : float
        Angle of attack in degrees.
    cl0 : float, optional
        Lift coefficient at zero angle of attack.
    lift_slope : float, optional
        Lift curve slope in units of 1/degree.

    Returns
    -------
    float
        Lift coefficient.
    """
    return cl0 + lift_slope * alpha


def print_lift_summary(alpha, cl0=0.10, lift_slope=0.11):
    """
    Print a simple summary of the lift coefficient for a given angle of attack.

    Parameters
    ----------
    alpha : float
        Angle of attack in degrees.
    cl0 : float, optional
        Lift coefficient at zero angle of attack.
    lift_slope : float, optional
        Lift curve slope in units of 1/degree.
    """
    cl = compute_cl(alpha, cl0=cl0, lift_slope=lift_slope)

    print("Wind Tunnel Analyzer")
    print("--------------------")
    print(f"Angle of attack : {alpha:.2f} deg")
    print(f"Lift coefficient: {cl:.3f}")


def alpha_residual(alpha, target_cl, cl0=0.10, lift_slope=0.11):
    """
    Residual function for the linear lift model.

    Returns zero when alpha produces the target lift coefficient:
        f(alpha) = cl0 + lift_slope * alpha - target_cl

    Parameters
    ----------
    alpha : float
        Angle of attack in degrees.
    target_cl : float
        Desired lift coefficient.
    cl0 : float, optional
        Lift coefficient at zero angle of attack.
    lift_slope : float, optional
        Lift curve slope in units of 1/degree.

    Returns
    -------
    float
        Difference between the model CL and the target CL.
    """
    return compute_cl(alpha, cl0=cl0, lift_slope=lift_slope) - target_cl


def solve_alpha(target_cl, cl0=0.10, lift_slope=0.11, alpha_guess=0.0):
    """
    Find the angle of attack that produces a target lift coefficient.

    Parameters
    ----------
    target_cl : float
        Desired lift coefficient.
    cl0 : float, optional
        Lift coefficient at zero angle of attack.
    lift_slope : float, optional
        Lift curve slope in units of 1/degree.
    alpha_guess : float, optional
        Initial guess for the angle of attack in degrees.

    Returns
    -------
    float
        Angle of attack in degrees.
    """
    solution = fsolve(
        alpha_residual,
        alpha_guess,
        args=(target_cl, cl0, lift_slope),
    )
    return float(solution[0])