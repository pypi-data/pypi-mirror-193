# github_directory: walmartlabs/lacinia, stars: 2000, last_update: 2022-08-19
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Lacinia(IGQLQuery):

    score_factor = 0.55
    genetics = {
        'query {graphw00f}': [in_response_text('Cannot query field `graphw00f\' on type `QueryRoot\'.'), ],
    }
