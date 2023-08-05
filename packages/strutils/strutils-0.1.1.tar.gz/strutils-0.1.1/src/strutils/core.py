# src/strutils/core.py
"""
(compound) STRing UTILitieS - A collection of (compound string utilities).

Used to grow on the fly. Aims to provide abstract, general purpose
functionalities.


.. autosummary::
   :nosignatures:

   sos_on
   permute_splits
   variate_compounds
"""
import collections
import itertools as it

import ittools

patterns = [
    "{}{: .0}{: .0}",  # first
    "{: .0}{: .0}{}",  # second
    "{}{}{}",  # first.second
    "{: .1}{}{}",  # f.second
    "{}{}{: .1}",  # first.s
]


def sos_on(compound_string, using=str.capitalize, split_at="_", stitch_with="_"):
    """Split Operate Stitch.

    Split the :paramref:`~sos_on.compound_string` at
    :paramref:`~sos_on.split_at` and operate on it with
    :paramref:`~sos_on.using` on each component to stitch it back
    together into one string using `:paramref:~sos_on.stitch_with`.

    Parameters
    ----------
    compound_string: str
        Compound strings of which the components are to be split, operated and
        stitched.

    using: :class:`~collections.abc.Callable`
        Callable mapped to each component of the string.

    split_at: str, default='_'
        Each component of the inbound compound string  will be identified by
        this.

    stitch_with: str, default='_'
        The outbound compound string will be stitched together using this.

    Yields
    ------
    :class:`~collections.abc.Generator`
        Generator object yielding the splitted, operated and stitched compound
        strings.

    Examples
    --------
    >>> import pprint
    >>> capitilzed = sos_on('variable_cost', using=str.capitalize)
    >>> print(type(capitilzed))
    <class 'generator'>
    >>> pprint.pprint(list(capitilzed))
    ['variable_cost', 'variable_Cost', 'Variable_cost', 'Variable_Cost']
    """
    splitted = compound_string.split(split_at)

    operated = map(using, splitted)
    recombined = it.product(*zip(splitted, operated))

    for combination in recombined:
        stitched = stitch_with.join(combination)
        yield stitched


def permute_splits(strings, stitch_with="_", split_at="_"):
    """Split compound strings and permute its components.

    Split each compund string in
    :paramref:`~permute_splits.strings` at :paramref:`~permute_splits.split_at`
    into its components. Create all possible permutations and stitch them
    back together into compound strings using
    `:paramref:~permute_splits.stitch_with`.

    Parameters
    ----------
    strings: :class:`~collections.abc.Iterable`, str
        String or iterable of compound strings of which the components are to
        be permutated. Must be of depth <= 1. i.e.:
        ``"My_String" or ["My-String1", "My-String2"]``

    split_at: str, default='_'
        Each component of the inbound compound string  will be identified by
        this.

    stitch_with: str, default='_'
        The outbound compound string will be stitched together using this.

    Yields
    ------
    :class:`~collections.abc.Generator`
        Generator object yielding the permmuted compound strings.

    Examples
    --------
    >>> import pprint
    >>> capitilzed = sos_on('variable_cost', using=str.capitalize)
    >>> permuted = permute_splits(strings=capitilzed)
    >>> print(type(permuted))
    <class 'generator'>
    >>> pprint.pprint(list(permuted))
    ['variable_cost',
     'cost_variable',
     'variable_Cost',
     'Cost_variable',
     'Variable_cost',
     'cost_Variable',
     'Variable_Cost',
     'Cost_Variable']
    """
    # 'enforce' container of depth one (DOES NOT FLATTEN)
    if not isinstance(strings, collections.abc.Generator):
        strings = ittools.nestify(strings, target_depth=1)

    for string in strings:
        splitted = string.split(split_at)
        if len(splitted) > 1:
            permutated = it.permutations(splitted)  # , len(splitted))
            for permute in permutated:
                yield stitch_with.join(permute)

        else:
            # non compound strings
            yield splitted[0]


def variate_compounds(
    compound_string,
    using=str.capitalize,
    permutate="True",
    split_at="_",
    stitch_with="_",
):
    """Split, variate and stitch compound strings.

    Convenience wrapper for :func:`sos_on` and :func:`permute_splits`.

    Designed to quickly generate variations of a compound string.

    Parameters
    ----------
    compound_string: str
        Compound string of which the components are to be split, operated and
        stitched.

    using: :class:`~collections.abc.Callable`
        Callable mapped to each compound of the string. Used for creating
        variations. See :func:`sos_on` for details on the mutations.

    permutate: bool, default=True
        If true, all possible permations of the variated compound strings
        will be generated. See :func:`permute_splits` for details on
        the permutation process.

    split_at: str, default='_'
        Each component of the inbound compound string  will be identified by
        this.

    stitch_with: str, default='_'
        The outbound compound string will be stitched together using this.

    Returns
    -------
    variated: :class:`~collections.abc.Generator`
        Generator object yielding the variated compound strings.

    Examples
    --------
    Note how getting a list of generator can be a little inconvenient:

    >>> import pprint
    >>> variated = variate_compounds('variable_cost')
    >>> pprint.pprint(list(variated))
    ['variable_cost',
     'cost_variable',
     'variable_Cost',
     'Cost_variable',
     'Variable_cost',
     'cost_Variable',
     'Variable_Cost',
     'Cost_Variable']

    Use nested for loops and :func:`itertools.chain` to create complex mappings
    of variated compound strings:

    >>> import pprint
    >>> import collections
    >>> import itertools
    >>> import pandas
    >>> stitchers = ['_', ' ']
    >>> compounds = ['variable_cost', 'flow_costs']
    >>> variations = collections.defaultdict(list)
    >>> for string in compounds:
    ...     for stitcher in stitchers:
    ...         variations[string] = list(itertools.chain(
    ...             variations[string],
    ...             variate_compounds(string, stitch_with=stitcher)))
    >>> print(pandas.DataFrame(variations))
        variable_cost  flow_costs
    0   variable_cost  flow_costs
    1   cost_variable  costs_flow
    2   variable_Cost  flow_Costs
    3   Cost_variable  Costs_flow
    4   Variable_cost  Flow_costs
    5   cost_Variable  costs_Flow
    6   Variable_Cost  Flow_Costs
    7   Cost_Variable  Costs_Flow
    8   variable cost  flow costs
    9   cost variable  costs flow
    10  variable Cost  flow Costs
    11  Cost variable  Costs flow
    12  Variable cost  Flow costs
    13  cost Variable  costs Flow
    14  Variable Cost  Flow Costs
    15  Cost Variable  Costs Flow
    """
    if permutate:
        sorred = sos_on(
            compound_string, using=using, split_at=split_at, stitch_with=split_at
        )

        variated = permute_splits(
            strings=sorred, split_at=split_at, stitch_with=stitch_with
        )

        return variated

    # no permutation requested
    sorred = sos_on(
        compound_string, using=using, split_at=split_at, stitch_with=stitch_with
    )

    return sorred
