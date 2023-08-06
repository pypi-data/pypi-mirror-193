# github_directory: appointy/jaal, stars: 2000, last_update: 2022-08-19
from graphdna.detectors.checkers import in_response_text
from graphdna.entities.interfaces.heuristics import IGQLQuery


class Caliban(IGQLQuery):

    score_factor = 0.55
    genetics = {
        '''
        query {
            __typename
        }
        
        fragment woof on __Schema {
            directives {
                name
            }
        }''': [in_response_text('Fragment \'woof\' is not used in any spread'), ],
    }
