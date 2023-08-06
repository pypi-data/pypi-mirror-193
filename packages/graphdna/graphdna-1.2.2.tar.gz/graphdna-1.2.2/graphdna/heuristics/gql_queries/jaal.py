# github_directory: appointy/jaal, stars: 2000, last_update: 2022-08-19
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Jaal(IGQLQuery):

    score_factor = 0.55
    genetics = {
        '{}': [
            in_response_text('must have a single query'),
            in_response_text('offset'),
        ],
    }
