# github_directory: mercurius-js/mercurius, stars: 2000, last_update: 2022-08-19
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Mercurius(IGQLQuery):

    score_factor = 0.55
    genetics = {
        '': [in_response_text('Unknown query')],
    }
