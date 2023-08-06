import functools as ft
import operator

import diffrax
import equinox as eqx
import jax.numpy as jnp
import jax.random as jrandom
import jax.tree_util as jtu


all_ode_solvers = (
    diffrax.Bosh3(scan_stages=False),
    diffrax.Bosh3(scan_stages=True),
    diffrax.Dopri5(scan_stages=False),
    diffrax.Dopri5(scan_stages=True),
    diffrax.Dopri8(scan_stages=False),
    diffrax.Dopri8(scan_stages=True),
    diffrax.Euler(),
    diffrax.Ralston(scan_stages=False),
    diffrax.Ralston(scan_stages=True),
    diffrax.Midpoint(scan_stages=False),
    diffrax.Midpoint(scan_stages=True),
    diffrax.Heun(scan_stages=False),
    diffrax.Heun(scan_stages=True),
    diffrax.LeapfrogMidpoint(),
    diffrax.ReversibleHeun(),
    diffrax.Tsit5(scan_stages=False),
    diffrax.Tsit5(scan_stages=True),
    diffrax.ImplicitEuler(),
    diffrax.Kvaerno3(scan_stages=False),
    diffrax.Kvaerno3(scan_stages=True),
    diffrax.Kvaerno4(scan_stages=False),
    diffrax.Kvaerno4(scan_stages=True),
    diffrax.Kvaerno5(scan_stages=False),
    diffrax.Kvaerno5(scan_stages=True),
)


def implicit_tol(solver):
    if isinstance(solver, diffrax.AbstractImplicitSolver):
        return eqx.tree_at(
            lambda s: (s.nonlinear_solver.rtol, s.nonlinear_solver.atol),
            solver,
            (1e-3, 1e-6),
            is_leaf=lambda x: x is None,
        )
    return solver


def random_pytree(key, treedef):
    keys = jrandom.split(key, treedef.num_leaves)
    leaves = []
    for key in keys:
        dimkey, sizekey, valuekey = jrandom.split(key, 3)
        num_dims = jrandom.randint(dimkey, (), 0, 5)
        dim_sizes = jrandom.randint(sizekey, (num_dims,), 0, 5)
        value = jrandom.normal(valuekey, dim_sizes)
        leaves.append(value)
    return jtu.tree_unflatten(treedef, leaves)


treedefs = [
    jtu.tree_structure(x)
    for x in (
        0,
        None,
        {"a": [0, 0], "b": 0},
    )
]


def _shaped_allclose(x, y, **kwargs):
    return jnp.shape(x) == jnp.shape(y) and jnp.allclose(x, y, **kwargs)


def shaped_allclose(x, y, **kwargs):
    """As `jnp.allclose`, except:
    - It also supports PyTree arguments.
    - It mandates that shapes match as well (no broadcasting)
    """
    same_structure = jtu.tree_structure(x) == jtu.tree_structure(y)
    allclose = ft.partial(_shaped_allclose, **kwargs)
    return same_structure and jtu.tree_reduce(
        operator.and_, jtu.tree_map(allclose, x, y), True
    )
