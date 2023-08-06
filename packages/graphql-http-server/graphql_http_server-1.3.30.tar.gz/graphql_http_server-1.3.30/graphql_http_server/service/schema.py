import inspect
import logging
from typing import TypeVar, Optional, Type

from graphql import print_schema, GraphQLSchema

from schemadiff import diff, format_diff
from schemadiff.changes import CriticalityLevel

from graphql_api.api import GraphQLRootTypeDelegate
from graphql_api import GraphQLAPI
from graphql_api.remote import GraphQLRemoteExecutor, GraphQLRemoteObject

TClient = TypeVar("TClient", bound='Schema')

"""
Schema Provides Utilities to help with a Service

Schema Class Attributes:
    api_version         The version of this schema, this must be defined
                        in the root controller.

    validate_schema     When set to `True` a check will be run on any
                        implementations of this service and check they
                        adhere to the schema

    criticality         If `validate_schema` is True an exception will be
                        raised if any changes meet or exceed this level.
                        If `validate_schema` is True and `criticality` is
                        set to `None` an exception will not be raised but
                        the changes will still be logged.
"""


class APIVersion(type):

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)

    def __new__(metacls, name, bases, namespace, **kwargs):
        return super().__new__(metacls, name, bases, namespace)

    def __init__(cls, name, bases, namespace, api_version=None, **kwargs):
        if api_version:
            cls.api_version = api_version
        super().__init__(name, bases, namespace)


class Schema(GraphQLRootTypeDelegate, metaclass=APIVersion):
    api_version: str = None
    validate_schema: bool = True
    criticality: Optional[CriticalityLevel] = CriticalityLevel.NonBreaking

    @classmethod
    def validate_graphql_schema(cls, schema: GraphQLSchema) -> GraphQLSchema:

        if cls.validate_schema:
            bases = list(inspect.getmro(cls))
            reversed_bases = list(reversed(bases))
            schema_class: Optional[Type[Schema]] = None
            for base in reversed_bases:
                if issubclass(base, Schema) and base != Schema:
                    schema_class = base
                    break
            if schema_class == reversed_bases[-1]:
                # This is a schema - no need to validate
                return schema

            if schema_class:
                validate(schema, schema_class, cls.criticality)

        return schema

    @classmethod
    def client(cls: TClient, url: str) -> TClient:
        # noinspection PyTypeChecker
        return GraphQLRemoteObject(
            executor=GraphQLRemoteExecutor(url),
            api=GraphQLAPI(root=cls)
        )

    @classmethod
    def graphql_schema(cls) -> GraphQLSchema:
        return GraphQLAPI(root=cls).graphql_schema()[0]


def validate(
        graphql_schema: GraphQLSchema,
        service_schema: Type[Schema],
        criticality: CriticalityLevel
):
    generated_service_schema = \
        GraphQLAPI(root=service_schema).graphql_schema()[0]

    if not generated_service_schema:
        raise ValueError(
            f"Could not generate service schema for {service_schema}"
        )
    query_a = generated_service_schema.query_type
    query_b = graphql_schema.query_type

    if query_a and query_b and query_a.name != query_b.name:
        query_a.name = query_b.name

    mutation_a = generated_service_schema.query_type
    mutation_b = graphql_schema.query_type

    if mutation_a and mutation_b and mutation_a.name != mutation_b.name:
        mutation_a.name = mutation_b.name

    generated_service_schema_language = print_schema(
        generated_service_schema
    )

    schema_language = print_schema(graphql_schema)

    # There should be no changes for a perfect implementation
    changes = diff(generated_service_schema_language, schema_language)

    if changes:
        raise_error_map = {
            None: [],
            CriticalityLevel.NonBreaking: [
                CriticalityLevel.NonBreaking,
                CriticalityLevel.Dangerous,
                CriticalityLevel.Breaking
            ],
            CriticalityLevel.Dangerous: [
                CriticalityLevel.Dangerous,
                CriticalityLevel.Breaking
            ],
            CriticalityLevel.Breaking: [
                CriticalityLevel.Breaking
            ]
        }

        raise_err = any(
            change.criticality.level in raise_error_map[criticality] and
            "DescriptionChanged" not in type(change).__name__
            for change in changes
        )

        format_changes = format_diff(changes)

        if raise_err:
            raise TypeError(
                f"Validation Error\n The service "
                f"`{graphql_schema.query_type.name}` does not adhere to "
                f"`{service_schema.__name__}` version "
                f"'{service_schema.api_version}', here are the changes:\n"
                f"{format_changes}\n You may be able to suppress this error by"
                f" setting the class attribute "
                f"`{graphql_schema.query_type.name}.validate_schema` to False,"
                f" or by lowering the "
                f"`{graphql_schema.query_type.name}.criticality`."
            )
        else:
            logging.warning(
                f"Validation Error\n"
                f"The service `{graphql_schema.query_type.name}` does not "
                f"adhere to `{service_schema.__name__}` version "
                f"'{service_schema.api_version}', here are the "
                f"changes:\n {format_changes}\n"
            )
