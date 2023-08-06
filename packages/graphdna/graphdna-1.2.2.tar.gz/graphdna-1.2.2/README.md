# GraphDNA ![PyPI](https://img.shields.io/pypi/v/GraphDNA) [![CI](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/ci.yaml/badge.svg)](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/ci.yaml) [![CD](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/cd.yaml/badge.svg)](https://github.com/Escape-Technologies/GraphDNA/actions/workflows/cd.yaml)

GraphDNA is a tool that uses multiple heuristics to fingerprint GraphQL endpoints.

![Banner](docs/banner.png)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/GraphDNA)
![PyPI - Downloads](https://img.shields.io/pypi/dm/GraphDNA)

## Getting Started

It takes only two simple steps to fingerprint an endpoint using GraphDNA.

```bash
pip install graphdna
graphdna -u https://example.com/graphql
```

![Banner](docs/hackerone.png)

## Options

GraphDNA supports the following options:

```bash
graphdna \ 
# Url to fingerprint
--url/-u https://example.com/graphql \
# Header (chainable)
--header/-H "Authorization: Bearer token"
```

## Supported engines

| Name | Supported |   | Name | Supported |   | Name | Supported |
|------|:---------:|---|------|:---------:|---|------|:---------:|
| Agoo | ✅ | | Apollo | ✅ | | Ariadne | ✅ |
| AWS AppSync | ✅ | | Caliban | ✅ | | DGraph | ✅ |
| Dianajl | ✅ | | Directus | ✅ | | Flutter | ✅ |
| GQLGen | ✅ | | Graphene | ✅ | | GraphQLApiForWp | ✅ |
| GraphQL-Go | ✅ | | gopher/GraphQL-Go | ✅ | | GraphQL-Java | ✅ |
| GraphQL-PHP | ✅ | | GraphQL Yoga | ✅ | | Hasura | ✅ |
| HyperGraphQL | ✅ | | Jaal | ✅ | | Juniper | ✅ |
| Lacinia | ✅ | | Lighthouse | ✅ | | Mercurius | ✅ |
| MorpheusGraphQL | ✅ | | GraphQL Ruby | ✅ | | Sangria | ✅ |
| Shopify | ✅ | | Stepzen | ✅ | | Strawberry | ✅ |
| Tartiflette | ✅ | | WPGraphQL | ✅ |


## Environment Variables

**Logger** - *No effect if you pass your own logger*
| Name | Values  | Default| Behavior|
|------|--------|--------|--------|
| `LOG_FORMAT` | `console`, `json` | `console` | Change the log format accordingly |
| `DEBUG` | `True`, `False` | `False` | Enable debug logging |

## Integration

```python
import logging
from typing import Dict, Optional

from graphdna import detect_engine, detect_engine_async
from graphdna.entities import GraphQLEngine

def detect_engine(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    logger: Optional[logging.Logger] = None,
) -> Optional[GraphQLEngine]:
    ...


async def detect_engine_async(
    url: str,
    headers: Optional[Dict[str, str]] = None,
    logger: Optional[logging.Logger] = None,
) -> Optional[GraphQLEngine]:
    ...
```
## Local installation

```bash
git clone git@github.com:Escape-Technologies/graphdna.git
cd graphdna
chmod +x ./install-dev.sh
./install-dev.sh
```

## Credits

* [Graphw00f](https://github.com/dolevf/graphw00f)
* [Dolev Farhi](https://github.com/dolevf)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License ![PyPI - License](https://img.shields.io/pypi/l/GraphDNA)

[MIT](https://choosealicense.com/licenses/mit/)
