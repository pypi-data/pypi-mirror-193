# github_directory: nuwave/lighthouse, stars: 2959, last_update: 2022-08-19
from graphdna.detectors.checkers import in_response_text, in_section
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Lighthouse(IGQLQuery):

    score_factor = 0.55
    genetics = {
        'query {__typename @include(if: falsee)}': [
            in_response_text('Internal server error'),
            in_section('category', 'internal'),
        ],
    }
