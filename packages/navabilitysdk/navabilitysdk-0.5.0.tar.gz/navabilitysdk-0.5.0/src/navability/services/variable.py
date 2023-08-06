import logging
from typing import List

from gql import gql

from navability.common.mutations import GQL_ADDVARIABLE
from navability.common.queries import (
    GQL_FRAGMENT_VARIABLES,
    GQL_LISTVARIABLES,
    GQL_GETVARIABLE,
    GQL_GETVARIABLES,
)
from navability.entities.client import Client
from navability.entities.navabilityclient import (
    MutationOptions,
    NavAbilityClient,
    QueryOptions,
)
from navability.entities.querydetail import QueryDetail
from navability.entities.variable.variable import (
    Variable,
    VariableSchema,
    VariableSkeleton,
    VariableSkeletonSchema,
    VariableSummarySchema,
    VariableType,
)

DETAIL_SCHEMA = {
    QueryDetail.LABEL: None,
    QueryDetail.SKELETON: VariableSkeletonSchema(),
    QueryDetail.SUMMARY: VariableSummarySchema(),
    QueryDetail.FULL: VariableSchema(),
}

logger = logging.getLogger(__name__)


async def _addVariable(navAbilityClient: NavAbilityClient, client: Client, v: Variable):
    result = await navAbilityClient.mutate(
        MutationOptions(
            gql(GQL_ADDVARIABLE),
            {"variable": {"client": client.dump(), "packedData": v.dumpsPacked()}},
        )
    )
    return result["addVariable"]


def addVariable(
    client: NavAbilityClient, 
    context: Client, 
    variable_or_label, 
    varType=None
):
    """ Add a variable to the graph.

    Args:
        client (NavAbilityClient): client connection to API server
        context (Client): Unique context with (user, robot, session)
        variable_or_label (Variable or string): The variable to add.
        varType (VariableType, optional): Pose2, Pose3, etc. Defaults to None.

    Raises:
        NotImplementedError: _description_

    Returns:
        _type_: _description_
    """
    if isinstance(variable_or_label, Variable):
        return _addVariable(client, context, variable_or_label)
    # TODO standardise varType to string or VariableType after design discussion
    if isinstance(varType, str):
        v = Variable(variable_or_label, varType)
        return _addVariable(client, context, v)
    elif isinstance(varType, VariableType):
        v = Variable(variable_or_label, varType.value)
        return _addVariable(client, context, v)
    raise NotImplementedError()


async def listVariables(
    client: NavAbilityClient,
    context: Client,
    regexFilter: str = ".*",
    tags: List[str] = None,
    solvable: int = 0,
) -> List[str]:
    """Get a list of Variable labels in the graph.

    Args:
        client (NavAbilityClient): client connection to API server
        context (Client): Unique context with (user, robot, session)
        regexFilter (str, optional): Filter on variable label. Defaults to ".*".
        tags (List[str], optional): Variables can have string tags. Defaults to None.
        solvable (int, optional): Whether this variable can be used in solving yet. Defaults to 0.

    Returns:
        List[str]: Async task returning a list of Variable labels.
    """
    params = {
        "userId": context.userId,
        "robotId": context.robotId,
        "sessionId": context.sessionId,
    }
    logger.debug(f"Query params: {params}")
    res = await client.query(
        QueryOptions(gql(GQL_LISTVARIABLES), params)
    )
    if (
        "users" not in res
        or len(res["users"]) != 1
        or len(res["users"][0]["robots"]) != 1
        or len(res["users"][0]["robots"][0]["sessions"]) != 1
        or "variables" not in res["users"][0]["robots"][0]["sessions"][0]
    ):
        # Debugging information
        if len(res["users"]) != 1:
            logger.warn("User not found in result, returning empty list")
        if len(res["users"][0]["robots"]) != 1:
            logger.warn("Robot not found in result, returning empty list")
        if len(res["users"][0]["robots"][0]["sessions"]) != 1:
            logger.warn("Robot not found in result, returning empty list")
        return []
    vl = []
    _lb = lambda s: s['label']
    resvar = res['users'][0]['robots'][0]['sessions'][0]['variables']
    [vl.append(_lb(v)) for v in resvar]
    return vl
    # # LEGACY
    # variables = await getVariables(
    #     client,
    #     context,
    #     detail=QueryDetail.SKELETON,
    #     regexFilter=regexFilter,
    #     tags=tags,
    #     solvable=solvable,
    # )
    # result = [v.label for v in variables]
    # return result



# Alias
ls = listVariables


async def getVariables(
    client: NavAbilityClient,
    context: Client,
    detail: QueryDetail = QueryDetail.SKELETON,
    regexFilter: str = ".*",
    tags: List[str] = None,
    solvable: int = 0,
) -> List[VariableSkeleton]:
    """Get a list of Variable from a graph using various filters.

    Args:
        client (NavAbilityClient): client connection to API server
        context (Client): Unique context with (user, robot, session)
        detail (QueryDetail, optional): Defaults to QueryDetail.SKELETON.
        regexFilter (str, optional): Filter on variable label. Defaults to ".*".
        tags (List[str], optional): Variables can have string tags. Defaults to None.
        solvable (int, optional): Whether this variable can be used in solving yet. Defaults to 0.

    Returns:
        List[VariableSkeleton]: Async task returning a list of VariableSkeleton
    """
    params = {
        "userId": context.userId,
        "robotIds": [context.robotId],
        "sessionIds": [context.sessionId],
        "variable_label_regexp": regexFilter,
        "variable_tags": tags if tags is not None else ["VARIABLE"],
        "solvable": solvable,
        "fields_summary": detail in [QueryDetail.SUMMARY, QueryDetail.FULL],
        "fields_full": detail == QueryDetail.FULL,
    }
    logger.debug(f"Query params: {params}")
    res = await client.query(
        QueryOptions(gql(GQL_FRAGMENT_VARIABLES + GQL_GETVARIABLES), params)
    )
    logger.debug(f"Query result: {res}")
    # TODO: Check for errors
    schema = DETAIL_SCHEMA[detail]
    # Using the hierarchy approach, we need to check that we have
    # exactly one user/robot/session in it, otherwise error.
    if (
        "users" not in res
        or len(res["users"]) != 1
        or len(res["users"][0]["robots"]) != 1
        or len(res["users"][0]["robots"][0]["sessions"]) != 1
        or "variables" not in res["users"][0]["robots"][0]["sessions"][0]
    ):
        # Debugging information
        if len(res["users"]) != 1:
            logger.warn("User not found in result, returning empty list")
        if len(res["users"][0]["robots"]) != 1:
            logger.warn("Robot not found in result, returning empty list")
        if len(res["users"][0]["robots"][0]["sessions"]) != 1:
            logger.warn("Robot not found in result, returning empty list")
        return []
    if schema is None:
        return res["users"][0]["robots"][0]["sessions"][0]["variables"]
    return [
        schema.load(l) for l in res["users"][0]["robots"][0]["sessions"][0]["variables"]
    ]


async def getVariable(
    client: NavAbilityClient, 
    context: Client, 
    label: str
):
    params = context.dump()
    params["label"] = label
    logger.debug(f"Query params: {params}")
    res = await client.query(
        QueryOptions(gql(GQL_FRAGMENT_VARIABLES + GQL_GETVARIABLE), params)
    )
    logger.debug(f"Query result: {res}")
    # TODO: Check for errors
    # Using the hierarchy approach, we need to check that we have
    # exactly one user/robot/session in it, otherwise error.
    if (
        "users" not in res
        or len(res["users"][0]["robots"]) != 1
        or len(res["users"][0]["robots"][0]["sessions"]) != 1
        or "variables" not in res["users"][0]["robots"][0]["sessions"][0]
    ):
        raise Exception(
            "Received an empty data structure, set logger to debug for the payload"
        )
    vs = res["users"][0]["robots"][0]["sessions"][0]["variables"]
    # TODO: Check for errors
    if len(vs) == 0:
        return None
    if len(vs) > 1:
        raise Exception(f"More than one variable named {label} returned")
    return Variable.load(vs[0])
