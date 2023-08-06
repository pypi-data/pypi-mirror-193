"""Manage engines entities."""

from enum import Enum, unique


@unique
class GraphQLEngine(Enum):

    """Represent GraphQL Engines."""

    AGOO = 'Agoo'
    APOLLO = 'Apollo'
    ARIADNE = 'Ariadne'
    AWSAPPSYNC = 'AWSAppSync'
    CALIBAN = 'Caliban'
    DGRAPH = 'DGraph'
    DIANAJL = 'DianaJl'
    DIRECTUS = 'Directus'
    FLUTTER = 'Flutter'
    GRAPHENE = 'Graphene'
    GRAPHQLAPIFORWP = 'GraphQLAPIForWP'
    GRAPHQLGO = 'GraphQLGo'
    GRAPHQLGOGOPHERGO = 'GraphQLGopherGo'
    GRAPHQLJAVA = 'GraphQLJava'
    GRAPHQLPHP = 'GraphQLPHP'
    GRAPHQLYOGA = 'GraphQLYoga'
    HASURA = 'Hasura'
    HYPERGRAPHQL = 'HyperGraphQL'
    JAAL = 'Jaal'
    JUNIPER = 'Juniper'
    LACINIA = 'Lacinia'
    LIGHTHOUSE = 'Lighthouse'
    MERCURIUS = 'Mercurius'
    MORPHEUSGRAPHQL = 'MorpheusGraphQL'
    QGLGEN = 'GQLGen'
    RUBY = 'Ruby'
    SANGRIA = 'Sangria'
    SHOPIFY = 'Shopify'
    STEPZEN = 'Stepzen'
    STRAWBERRY = 'Strawberry'
    TARTIFLETTE = 'Tartiflette'
    WPGRAPHQL = 'WPGraphQL'
