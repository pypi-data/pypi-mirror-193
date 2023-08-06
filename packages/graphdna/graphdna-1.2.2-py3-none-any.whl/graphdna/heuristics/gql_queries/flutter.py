# github_directory: zino-hofmann/graphql-flutter, stars: 3002, last_update: 2022-08-19
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Flutter(IGQLQuery):

    score_factor = 0.55
    genetics = {
        'query { __typename @deprecated }': in_response_text('Directive \\"deprecated\\" may not be used on FIELD.'),
    }
