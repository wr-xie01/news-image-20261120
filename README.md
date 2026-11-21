# The World in One Day — 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/wr-xie01/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/wr-xie01/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for the make.fun bounty [Sum up 20 November's world news in one image](https://make.fun/bounty/news-image-20261120): a one-page newspaper front page summing up Friday 20 November 2026.

## The six stories

1. **Ukraine** — Russian missiles hit three Kyiv bridges; three killed and 15 hurt in overnight strikes on the Dnipro crossings.
2. **Poland** — Russian missiles and a jet drone cross into Polish airspace; NATO jets scramble and PM Tusk calls it a provocation.
3. **Summit** — The EU and UK strike a post-Brexit deal in Brussels: food trade, carbon markets and a youth scheme for 100,000.
4. **Markets** — Bitcoin sinks below $60,000 for the first time since July as AI stocks slide and the S&P 500 nears correction.
5. **Cyclone** — Cyclone Akvan makes landfall on India's east coast, the third storm in under a month.
6. **Estonia** — Estonia will shut its road border with Russia from 1 December for at least six months after an alleged sabotage plot.

All six happened or were first reported on 20 November 2026.

## How it runs

`main.py` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output`), refusing if the image is over the 1 MiB limit. `generate_image.py` draws the front page from scratch with PIL (1024×1024, masthead, date band, six story cards with simple icons).
