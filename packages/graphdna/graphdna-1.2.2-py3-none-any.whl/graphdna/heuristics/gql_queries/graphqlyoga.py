# github_directory: dotansimha/graphql-yoga, stars: 7088, last_update: 2022-08-19
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class GraphQLYoga(IGQLQuery):

    score_factor = 0.62
    genetics = {
        'subscription {__typename }': in_response_text([
            'asyncExecutionResult[Symbol.asyncIterator] is not a function',
            'Unexpected error.',
        ])
    }
