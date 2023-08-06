# github_directory: morpheusgraphql/morpheus-graphql, stars: 2000, last_update: 2022-08-19
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class MorpheusGraphQL(IGQLQuery):

    score_factor = 0.55
    genetics = {
        'queryy {__typename}': [
            in_response_text('expecting white space'),
            in_response_text('offset'),
        ],
    }
