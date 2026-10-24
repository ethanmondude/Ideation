# Tapeline Check v2: when did this headline actually happen, and what does the fine print get wrong?

*Idea bot thesis, Fri 23 Oct 2026, 9:00am AWST (Perth). Path: /workspace/idea-bot/theses/2026-10-23-0900-tapeline-check-v2.md. **Version 2 of Tapeline Check** (v1: theses/2026-10-22-2230-tapeline-check.md, Project Bot 5.5/10, token fit 6/10, 1st of the theses that pass Ethan's rules). Same thesis id: idea-bot:thesis:tapeline-check. Built from Project Bot's v1 review, its 100 hand labels, X bot's backfill and checker-reply pull, Git bot's pumpdata.fun refinement, Growth Bot's refine protocol and a new free private test run this morning (data/stale-check/README.md).*

## What changed in v2
Each line answers a weakness in Project Bot's v1 review (reviews/2026-10-22-2245-tapeline-check.md).

1. **Differentiation (scored 4): pivoted.** v1 sold a true/false verdict under market headlines. Free tools already do that on demand (Larpcheck, Basis Desk Verify, SpyGlass, and FactCheckRadar, found this run). Our own labels show the real gap is elsewhere. 90% of market-moving originals were true; the damage came from **old news posted as new** (11 of 23 misleading headlines) and **fine-print errors** (wrong figure, wrong actor, overstated scope). Not one of the 11 stale or contradicted posts that free checkers could have caught got a Grok or Larpcheck reply (0 of 15 replies landed on them). v2 leads with an automatic **freshness stamp**: "first happened 8 Oct, 14 days ago, at [CoinDesk]", plus a fine-print flag. Partly fixed. The plain verdict stays as a secondary line, because it isn't ours to win.
2. **Missed competitors: swept the channels that missed them, and found more.** Added FactCheckRadar (Chrome Web Store, an X fact-check button that checks dates, updated 19 Oct 2026, in-app purchases), ArcaneNews (a crypto news-trading terminal with "old news detection" and "same news detection"), Tree/PVP Terminal's "Old News Threshold" (which measures delivery lag, not event age), Tweet Fact Checker, Stale News Warning and Custom Timestamps for X. All of them are on-demand, in a separate terminal, or only measure the post's own timestamp. None stamps the event's first date automatically under X posts. The gap narrows but holds.
3. **X Developer Policy risk: cut.** The public scorecard, the "paid promo" label and "who boosted it" detection come out of the public product. The last of those is contested anyway (devs_hunter, bitecong, WhodlBot). The stamp is a fact about the *event*, taken from off-X sources ("this claim first appeared at [outlet] on [date]"). It isn't a measurement of X accounts. Poster records stay private research until X agrees in writing.
4. **Token score (6): small change, honestly still about 6.** Holding now sets watchlist size (how many accounts get stamped automatically), and agents can prepay API credits by burning their own $TPLN. x402 USDC per call is the other agent rail. It's still close to Larpcheck's hold-to-access model, so I don't expect a big jump.
5. **Demand evidence: still the weak spot, not fixed.** Explicit "this is old news" complaints under crypto BREAKING posts are rare: 17 in 7 days (X counts, 16-23 Oct UTC). The evidence is behavioural. 1 in 4 headlines mislead once timing and fine print count, and the free checkers miss those. Only the founding-pass money test can fix this, and it runs once Ethan picks this thesis to launch as a coin.
6. **Budget: re-costed at about A$694 over 4 months.** The extension reads the post the user is already viewing, so X API reads are needed only for watchlist alerts. Google News RSS can't be used in production: its feed licence says "personal, non-commercial use". So production uses our own RSS/announcement archive plus a licensed search API.
7. **New: free private test run this morning.** An automated "posted before?" check, with no LLM and no paid API, found the earlier story for about 6 of 11 stale headlines. But keyword rules can't separate "same event" from "same topic" (38 false flags in 69 fresh posts). So a same-event judge is the core build, and the next free test has a numeric pass line.
8. **Growth Bot's triggers and Project Bot's 8:50am re-score list: added.** Project Bot re-scored v1 at 8:50am and left it at 5.5. It listed what would lift the score, and v2 now covers each item:
   - A coin-post card that first resolves **which exact mint** the post means (the Project Kimchi vs Kimchi mix-up).
   - A **dev-tie flag** when the poster has promoted the same dev's earlier mints. That's the BTC/@slingoorio case. It shows as links to the earlier posts and mints, not as a score.
   - A dev-wallet history from pumpdata.fun's free tier (300 lookups a day).
   - Market cap and liquidity **read from the pool on-chain** (FORK's frozen DexScreener feed).
   - A flat-volume, buy-equals-sell **staircase tell** (MrBeast EsUyx7).
   - A named and costed licensed news source: Newsflash (free key, 1,000 calls a day; US$29/month premium with five-year history) plus Brave News Search (US$5 per 1,000 calls, with US$5 of free credit a month).
   - A new Agent distribution section: an MCP server, an x402 endpoint and a one-tap Grok Bot template (pumpdata.fun's model).
9. **Retention (5): small fix.** Telegram alerts fire when a watched headline turns out to be a stale repost, or gets confirmed or contradicted. That gives people a reason to come back between news bursts.

## Executive summary
- **Problem.** A lot of the crypto and macro "BREAKING" posts that move perps are real events that already happened: a 2025 Trump quote, Warsh's April remarks, an 8 Oct government wallet move reposted on 22 Oct. Others get the fine print wrong (last month's figure shown as the forecast, BlackRock "dumping" when its clients redeemed). In Project Bot's 100 hand-labelled headlines, **about 1 in 4 would mislead a trader** and **11 were stale**. Free checkers replied under only 15 of the 100 posts, and **none of the stale or contradicted ones**.
- **Product.** A Chrome extension on x.com that automatically stamps market headlines: **"first happened 8 Oct (14 days ago) · CoinDesk"**, or "new today · confirmed by BLS 2 min after", plus a fine-print flag ("figure is last month's", "actor is clients, not BlackRock") and live prices of what it names (Hyperliquid incl. HIP-3/trade.xyz, Solana tokens). Coin posts get a factual card showing the pair's age when it was posted and a dev-wallet check. Free for on-click stamps. Pro US$29/month for automatic stamps across the feed, watchlist alerts in Telegram, and long-memory checks. Desk/API US$99/month, with x402 per call for agents.
- **Who pays and the token's job.** Crypto-native perps and memecoin traders who already pay for headline speed (Tree News burned US$61.3k in 30 days, DefiLlama; 247 Terminal has 181 members at US$99, WhopScope). **$TPLN on pump.fun:** hold for Pro and bigger watchlists, burn your own tokens for long-memory deep checks or prepaid API credits. Card and USDC payments are never converted into token buys. No holder payouts, no fee-funded buybacks.
- **Cost against A$1,000.** About **A$104 to day 30** and **A$694 over 4 months**, including a A$300 legal consult and a A$83 token launch, all before revenue. That leaves about A$306 of headroom. Running cost is about A$75 a month.
- **Path to US$10k/month.** 345 Pro subscribers. The base case is US$3-6k MRR at month 12 (estimate), from on-X replies (with Ethan's OK), Telegram trader groups, agent channels and a free "stale repost" alert channel.
- **Why now and the edge.** Verdict bots just became normal on crypto X, but they all work on demand and answer "did it happen?", not "when?". Our labelled set shows the "when" is where traders get hurt. The edge is a long-memory headline archive plus a same-event judge measured on labelled data, and it sits right on the post with no tagging.
- **Main risk and first move.** Free on-demand checkers (FactCheckRadar, Basis Desk, Larpcheck) could add a date line in weeks, and nobody is shown paying for accuracy. First move this week (free, private): run a same-event judge over this morning's 80 candidate lists. **Pass at 8 or more of 11 stale caught with 5 or fewer false flags.**
- **Verdict: test, about 40% (unchanged).** The wedge is sharper and measured, and the public X-policy risk is gone. Demand for accuracy is still unproven.

## Problem and user
- **The user:** crypto-native traders who trade headlines on Hyperliquid (including trade.xyz pre-IPO and stock perps), Solana terminals and CEX perps, plus small callers and desks who repost news. They live on x.com, so the check has to sit on the post.
- **What goes wrong (sourced from our private labelled set; don't publish per-account results):**
  - 100 headlines from 40 high-volume accounts (X bot backfill, 4,134 posts, 22 Sep-22 Oct). Project Bot labelled 71 confirmed, 8 contradicted, 1 single-source and 20 paid promo. idea bot's blind 30 agreed on 90% (kappa 0.79).
  - Misleading types: 11 stale, 4 wrong figure, 4 overstated, 3 wrong actor, 1 early.
  - Examples: the "Warsh just killed the CBDC" post on 14 Oct repeated April remarks. The "2,000 BTC Satoshi-era wallet" post on 17 Oct recycled a January move, and its $180M figure only fits January's price. A 22 Oct "US government wallet just moved $1B from the Bitfinex hack" was an 8 Oct event (CoinDesk, Decrypt and CryptoSlate all ran it on 8 Oct, per the Google News results in data/stale-check/).
- **Today's workaround:** type "@grok is this true". Explicit asks with market words run 15-40 a day (X counts, v1). Under the 100 labelled posts, Grok replied 14 times and Larpcheck once, all under big accounts. Grok caught 2 of 6 true-but-misleading framings (X bot checker-reply pull; 25 of 36 reply matches are inferred).
- **Trader quotes (from v1, not re-checked today):** [Benne1818_](https://x.com/Benne1818_/status/2103475842009440627): "Got liquidated on my AMD because of … fake news about Hormuz opening". [student_charts](https://x.com/student_charts/status/2108538716100972788): "fake news … caused havoc in #AI trade".
- **Academic backing that stale news moves prices:** Fedyk and Hodson, ["When Can the Market Identify Old News?"](https://ai.updf.com/paper-detail/when-can-the-market-identify-old-news-fedyk-hodson-b7a99832989a09cd8f98c11759ab401a366031e6), Bloomberg terminal data. Recombined stale stories still move prices and later reverse.

## Evidence of money
- **Tree News:** US$61,347 in 30 days, US$1.05M in a year, US$3.54M all-time in TREE burns ([DefiLlama](https://api.llama.fi/summary/fees/tree-news)). Caveat from Project Bot: the adapter also counts USDC buy-and-burns, so only part of that is the copyable "users burn their own tokens" pattern. Traders pay for **speed** here.
- **247 Terminal:** 181 members at US$99/month, 4.93 stars from 14 reviews ([WhopScope](https://whopscope.com/w/247terminal)). That's about US$18k/month (estimate).
- **ArcaneNews and Tree/PVP Terminal** ship "old news" flags inside paid terminals ([ArcaneNews](https://arcane.news/): "Automatic detection to flag potential old news and option to remove it from your feed". [PVP Terminal docs](https://docs.pvpterminal.com/desktop/desktop/settings/news): "Old News Threshold … to be labeled 'OLD NEWS' (and possibly more risky to trade)"). **This is the best new money signal.** Paying news traders already value an "old news" label enough that terminals build it. Theirs measures delivery lag or duplicates inside their own feed, not when the event first happened, and only inside their app.
- **FactCheckRadar** sells in-app purchases on an X fact-check button ([Chrome Web Store](https://chromewebstore.google.com/detail/factcheckradar/obepkghlneckiemaclcigahjnbkonhnf)). It's general-purpose, its prices aren't public and its revenue is unknown.
- **What's missing:** no product is shown earning money from headline *accuracy* for crypto traders. Larpcheck and Basis Desk give it away.

## Bottom-up market sizing (assumptions labelled)
- **Spend pool (sourced plus estimate):** Tree (US$61k/month) plus 247 (about US$18k/month, estimate) is about US$80k/month that crypto traders already pay for headline tools.
- **Reachable traders (sourced, v1):** Hyperliquid frontends reached 125.4K users in 30 days (OpenChainBench, 22 Oct).
- **Assumption A:** 0.25-0.5% of those pay US$29. That's 310-630 payers, or **US$9.0k-18.3k MRR**.
- **Assumption B:** Desk/API at US$99 for 10-20 desks and bot builders adds **US$1-2k**. Agent x402 calls at US$0.01 add US$0.3k at 1,000 calls a day (estimate).
- **Sense-check:** 10-20% of Tree's monthly spend is US$6-12k. **The base case is US$3-6k MRR at month 12** (estimate), because the free on-demand checkers cap what people will pay.

## Competitive teardown
| Competitor | What it does | Pricing | Revenue / traction | Gap it leaves | Why they won't build our slice soon |
|---|---|---|---|---|---|
| Grok (@grok "is this true") | On-demand answer when tagged | Free | Built into X; 14 of 100 labelled posts got a reply | Manual; caught 2 of 6 misleading framings; no event-date stamp | X won't label its own big accounts' posts as stale at scale |
| [Larpcheck](https://larpcheck.app/how) | Tag under any post: claim checked against sources, 0-100 score | Free replies; Pro by holding $LARPCHECK | Self-reported ~1,000 users/day | Tag-only; 1 of 100 labelled posts got a reply | Could add a date line fast. **Biggest copy risk** |
| [FactCheckRadar](https://chromewebstore.google.com/detail/factcheckradar/obepkghlneckiemaclcigahjnbkonhnf) (new) | Fact-check button inside X posts; checks dates and sources; scheduled re-checks | In-app purchases (prices not public) | Updated 19 Oct 2026 | On click only; general (journalists, students); no market mapping or prices | Built for general misinformation, not trading speed |
| [Basis Desk Verify](https://basisdesk.news/news/basis-desk-verify-fact-check-crypto-news-chrome-extension) | Side panel: claims vs primary docs, live prices, token scam check | Free | Launched 7 Oct 2026 | Click-to-run, articles first, "never calls a page false", no automatic stamp on X | A media brand; automatic labels on others' posts conflict with its editorial stance |
| [SpyGlass](https://devpost.com/software/spyglass) | Inline verdict pill on every tweet (hackathon) | n/a | Demo | Proves the UI is a weekend clone | Not a business |
| [ArcaneNews](https://arcane.news/) (new) | News-trading terminal; old-news and same-news detection; execution | 1/6/12-month plans (price not public) | Unknown | Separate app; old = its own feed lag or duplicates | Sells speed and execution; stamping posts on X would send users away from the terminal |
| Tree News / [PVP Terminal](https://docs.pvpterminal.com/desktop/desktop/settings/news) | Fastest feed; "Old News Threshold" on delivery lag | Credits (TREE) | US$61k/30d | Lag, not event age; not on X | Same as Arcane |
| [Tweet Fact Checker](https://chromewebstore.google.com/detail/tweet-fact-checker/oindinllpggjmeiofcchlpkjpjhhhgko), [Stale News Warning](https://github.com/denny/Stale-News-Warning-chrome), [Custom Timestamps for X](https://chromewebstore.google.com/detail/custom-timestamps-for-x/ajdpfnakibpakgacmijifjndjojcejpj) (new) | OpenAI fact-check button; old-article warning on 13 news sites; colours post age | Free | No ratings / 69 users / 1 rating | Abandoned or post-timestamp only | Hobby projects |
| fable, UNMSK, Ethos, OnlyKOLs | Coin, KOL and account labels on X | Free / US$16 | Small | Coins and accounts, not headlines | Different data model |
| [pumpdata.fun](https://pumpdata.fun) | pump.fun trade history, dev checks, Grok Bot template | 300 free/day, then US$0.005/call | 0-star repo, new | Not headlines. **A supplier for our coin card** | n/a |

**Gate c check on the v2 core job** (automatic event-date stamp under X market posts): none of the working tools above does it. Three or more do on-demand verdicts, so the plain verdict is crowded and is no longer the lead. Sweep channels: Chrome Web Store, Devpost, rivals' own how-it-works pages, Git bot's gaps.jsonl and GitHub, X bot verdicts, missed-competitors.jsonl, X Developer Policy.

## Product and UX
**First minute.** Install the extension and open x.com. Under "🚨 BREAKING: A US government wallet just moved $1B in Bitcoin from the Bitfinex hack" a grey line appears (illustrative, built from this morning's test): `FIRST HAPPENED 8 Oct · 14 days ago · CoinDesk, Decrypt · BTC −0.4% 1h`. Tap it for the Backstory card: the earliest matching sources with dates, the fine-print check, and what the post's figure matches. A new, real headline shows `NEW · confirmed by BLS 2 min after release`. A coin post shows `pair created 3h before this post · dev wallet: 4 prior launches, 3 below $5k (pumpdata)`. No sign-up for the free on-click stamp. Wallet or email login for Pro.

**MVP stack.**
- Chrome MV3 extension (TypeScript). It reads only the visible post (text, ID, timestamp) and sends text plus ID to the API. No remote code. Narrow permissions under Chrome's Limited Use rules.
- API on a A$10/month VPS (Hono/Node) plus Supabase:
  - (1) claim extractor (small LLM, cached per post ID);
  - (2) **retrieval** from our own archive (RSS from about 60 crypto, macro and exchange sources; Binance/Coinbase/OKX/Upbit announcement endpoints; SEC EDGAR; BLS/BEA release calendars), plus [Newsflash](https://newsflash.sh/docs) events (free key 1,000/day with 30 days of history; US$29/month premium with five-year history) and [Brave News Search](https://brave.com/search/api/) (US$5 per 1,000 calls, US$5 free credit a month) for older stories;
  - (3) **same-event judge**: small LLM over the top 15 candidates, checking event, actor and figure, and returning the earliest matching date. Embeddings pre-filter;
  - (4) market mapper (Hyperliquid info API incl. HIP-3, DexScreener, GeckoTerminal candles);
  - (5) coin card: exact-mint resolution (the CA in the post, else ticker plus the pinned official CA, never "first search hit"); dev-wallet history from pumpdata.fun's free tier; pool reserves read on-chain through a free Solana RPC tier; flat-volume and buy/sell-symmetry tell from recent candles; dev-tie links when our archive holds this account's posts about the same dev's earlier mints.
- Telegram bot (grammY) for watchlist alerts. Payments: Solana Pay USDC to a public wallet, Lemon Squeezy card, and $TPLN burn/hold verified on-chain with `@pump-fun/pump-sdk`.

**Week by week (about 20-25 h/week).**
1. Archive ingest plus the same-event judge, scored against the 80 labelled rows (the pass line below).
2. Fine-print checks (figure vs consensus/prior release, actor) and the market mapper. Verdict API with cache.
3. Extension stamp, Backstory card, Pro gating, payments, Telegram alerts.
4. Agent channels (MCP, x402, paste-in prompt), coin card, unlisted Chrome listing.

**Advanced parts.** Event-level dedup across languages (Yonhap-first stories). Figure normalisation ($180M for 2,000 BTC implies a price, which dates the story). A point-in-time archive so "first happened" is reproducible.

**What's hard.** Same-event judging on weekly recurring topics (ETF flows, yields, CPI). Today's keyword rules false-flagged about half of fresh posts. Also coverage of hoaxes older than news search reaches.

**What a copycat could clone.** The stamp UI in a weekend. Not easily: the archive built over months, the labelled benchmark, and judge accuracy shown on it.

## Agent distribution
- **MCP server** (`freshness_check(text|post_url)` returns first-seen date, sources, fine-print flags, mapped markets). About 1 day to build. Free tier 50 checks/day.
- **x402 endpoint on Solana:** US$0.01 per check in USDC, or burned $TPLN credits. About 2 days, using the solana-x402-microtools pattern (Git bot).
- **One-tap Grok Bot template plus a paste-in prompt** for ChatGPT/Claude that calls the public API ("paste a headline or a post link, get when it first happened and what the fine print gets wrong"). That's the model of [pumpdata.fun's template](https://github.com/pumpdatafun/grokbot-pumpfun-template) ("paste it once, send a contract address, get the dev check in seconds. Free, no key"). A Runsheet founder reported 9 of 12 weekly signups coming from AI assistants (self-reported, via X bot). About half a day.
- Build cost: about A$0 beyond the VPS. These channels reach bot builders and desks without ads.

## Token design (pump.fun)
- **Jobs (all product use):**
  - (1) **Hold** a set amount for Pro, and more for bigger watchlists (25 / 100 / 300 auto-stamped accounts). Verified by wallet signature.
  - (2) **Burn your own $TPLN** per long-memory deep check (archive and licensed search beyond 90 days, about US$0.25, re-pegged monthly) or for a Pro month worth US$29.
  - (3) **Agents prepay API credits** by burning their own $TPLN (an x402 alternative).
  - Card and USDC are never used to buy the token.
- **Launch:** pump.fun only. No meta shift: X bot's 4am lesson shows the rival-pad spike was Robinhood Chain DeFi news, and other launchpads ran 0-6 posts an hour. Launch after the first 25 paying users and the legal consult, on a product-reveal day with a live extension link.
  - SOL pair. Mint and freeze authority revoked and confirmed on-chain before announcing.
  - **Small labelled dev buy** (≤0.5 SOL, wallet published). No bundles, snipers or paid callers.
  - **Holder Rewards off. Tokenized Agent buybacks off.**
  - **Pin one official CA** from the official X account and site from day one, and match on contract only (copycat mints happen in the same second, as with $PAPZ).
- **On-chain fee flow and verification:** every burn is the user's own SPL burn with a memo carrying the check ID. A public page lists burns from our indexer with Solscan links. Creator fees (0.30% on the curve, tiered on PumpSwap, [pump.fun fees](https://pump.fun/docs/fees)) go to a published wallet as **bonus income only**, never to buybacks or burns. Public repo for the extension, judge rules and burn verifier.
- **Comparable tokenised products (organic vs shilled):** Tree News TREE (verified burns, part USDC buy-and-burn). Larpcheck $LARPCHECK (hold-to-access; "61% bots" allegations). KOLscan $KOLS (hold-to-access). The Codex (burn per question, no burn seen, paid callers). Paparazzi $PAPA (Robinhood Chain, burns for fact-check credits, but its payouts are revenue-funded, which our rules bar). Lesson: don't project token income.
- **Legal line:** a usage and access credit only. No profit, yield or "number go up" language. Stamps are factual ("first reported 8 Oct at [source]"), which sits inside ASIC's factual-information line ([RG 244.24-25](https://download.asic.gov.au/media/tkqi11il/rg244-published-13-december-2012-20211208.pdf)), with no long/short wording. My reading, not legal advice; the A$300 consult covers it.

## Budget and founder load (A$; US$1 ≈ A$1.43; estimates unless sourced)
| Item | One-off | Monthly | 4-month total |
|---|---|---|---|
| Domain plus Chrome Web Store fee | 33 | | 33 |
| VPS (API, ingest, Telegram) | | 10 | 40 |
| LLM: extractor plus same-event judge (~300 unique checks/day × ~US$0.002) | | 26 | 104 |
| X API pay-per-use for watchlist alerts only (US$0.005/post read) | | 21 | 84 |
| News sources: Newsflash free key (1,000/day) now, premium US$29/month only from revenue; Brave News Search beyond its US$5 free credit (~1,500 deep checks/month ≈ US$2.50) | | ~4 | 16 (from contingency) |
| pumpdata.fun (300 free lookups/day; US$10/month for 20,000/day only if needed) and free Solana RPC tier | | 0 | 0 |
| Legal consult (defamation, factual-info line, token as credit) | 300 | | 300 |
| Token launch (rent plus ≤0.5 SOL labelled dev buy) | 83 | | 83 |
| Contingency | 50 | | 50 |
| **Total** | | **~A$57-72** | **~A$694** |

To day 30: about A$104 (domain, Chrome fee, VPS, LLM, X reads, A$20 contingency). DexScreener profile (~A$428) and Newsflash (US$29/month) only from revenue. **Founder load:** 20-25 h/week for 4 weeks, then about 10 h/week, including 2-3 h of verdict disputes (a "dispute with source" button feeds the labelled set).

## Business model and unit economics (estimates)
- **Price:** Free (on-click stamps, 20/day). Pro US$29/month (automatic stamps, 25-account watchlist, Telegram alerts, deep checks). Desk/API US$99/month (300-account watchlist, webhook, 3 seats). Agents pay US$0.01 per call.
- **Cost to serve:** a stamp is computed once per post and shared, so the cost is about US$0.30-0.80 per Pro user per month. Gross margin about 90% (estimate). Card fees about 5% + US$0.50. USDC and token payments about US$0.001.
- **Cash CAC about US$0.** Time is the constraint.

## Solo GTM
1. **Private benchmark first** (free): publish nothing, but once the judge passes, use the measured catch rate (for example "caught N of 11 stale headlines that Grok and Larpcheck never replied to") as the pitch line, with no account names.
2. **First 10 users** (needs Ethan's OK for any outreach): traders who reply "old news" or "@grok is this true" under market headlines, Hyperliquid and Solana Telegram groups, and small desks that repost news.
3. **Free Telegram channel:** "stale repost" alerts naming the *event and its first date*, not the poster.
4. **Agent channels** (MCP, x402, paste-in prompt) and Hyperliquid/Solana tool directories.
5. A 25% referral share for subscriptions (cash, not token).

## 12-month financial snapshot (estimates)
| Month | Pro | Desk | MRR (US$) | Cumulative cost (A$) |
|---|---|---|---|---|
| 1 | 0 (test) | 0 | 0 | ~104 |
| 3 | 40 | 2 | ~1.4k | ~550 (incl. legal and token) |
| 6 | 90 | 5 | ~3.1k | ~770 |
| 12 | 150-250 | 10-15 | ~5.3-8.7k | ~1,200 gross; out-of-pocket stays under A$1,000 because running costs are covered by revenue from about month 4 |
US$10k MRR needs about 345 Pro, or Pro plus Desk mixes. That's plausible but not the base case.

## Defensibility
- A point-in-time headline archive and a labelled benchmark that grows with every dispute.
- Same-event judge accuracy that we measure and can show.
- Distribution inside X plus agent channels. Weak against Larpcheck adding a date line, so speed of shipping and the archive's depth are the moat.

## Risks (mitigation and cheap test)
| Risk | Mitigation | Cheap test |
|---|---|---|
| Same-event judge too noisy (recurring topics) | Figure-and-actor match; abstain when unsure ("no earlier match found") | Next free step: 8+ of 11 stale, ≤5 false flags on the 80 rows |
| Free checkers add a date line | Ship automatic and fast; the archive is the edge | Watch Larpcheck and FactCheckRadar weekly (X bot) |
| Nobody pays for accuracy | Lead with alerts and watchlists (speed-adjacent) | Founding pass, once Ethan picks this thesis to launch as a coin |
| X Developer Policy | No public account scores, promo labels or aggregate X metrics; event facts only | Ask X for written OK before any public poster record |
| News-source licensing | Own RSS archive plus a licensed search API; no Google News RSS in production | Price two search APIs at build week 1 |
| Defamation | Factual wording with sources; the label is about the event, not the person | Legal consult before public launch |
| Token seen as investment | Usage credit only; Holder Rewards and buybacks off | Legal consult |

## Kill or confirm
**Free private steps first:**
1. **Same-event judge on this morning's 80 candidate lists.** Pass at 8 or more of 11 stale caught with 5 or fewer false flags. Kill the freshness stamp as the lead feature below 6 caught or above 10 false flags. Best run blind by a teammate bot (claim it in claims.md).
2. **Batch 2 backfill** (X bot, free reads): WatcherGuru, Cointelegraph, BitcoinArchive, BSCNews, coinbureau, 30 days. Does the stale rate hold for big outlets? Pass at ≥5% stale or fine-print among market-moving posts.
3. **Fine-print check prototype** on the 16 confirmed-but-misleading rows. Pass at 8 or more flagged correctly.

**Then the 30-day paid validation, once Ethan picks this thesis to launch as a coin (about A$104):** an unlisted Chrome listing and a US$29 founding pass for 3 months. **Pass: ≥25 passes and ≥25% of installs seeing a stamp on 3+ days a week. Iterate once: 10-24 passes. Kill: <10 passes, <10% weekly use, or ≥50% saying "I just ask Grok/Larpcheck".** No token, legal spend or DexScreener profile before it passes.

## Comparables
- Tree News (burn-to-use headlines, US$61k/30d). 247 Terminal (181 × US$99).
- ArcaneNews and PVP Terminal (paid terminals that ship old-news flags).
- FactCheckRadar (X fact-check button with in-app purchases).
- Larpcheck (hold-to-access verdict bot). pumpdata.fun (free tier plus x402 plus a Grok template, the distribution model we copy).

## Dropped this run
- **Wrong-coin creator-reward claims** (helloluis claimed rewards on a same-ticker $LUKE): fails gate c (ClaimScan, Prysm /unclaimed, pump.fun's native claim flow) and gate e (one anecdote, no payer). The evidence goes to Mint Seal (official-CA resolution).
- **Set-and-forget orders (TP/SL, cross-chain limit orders):** fails gate c ([Axiom limit orders with TP/SL/auto-sell](https://docs.axiom.trade/axiom/swap/limit-orders), Jupiter Trigger, Photon, GMGN), and it's execution, not information.
- **Name-bait staircase-wash detector** (Trench Bot's MrBeast EsUyx7 pattern): fails gate c (RugCheck, devs_hunter, WhodlBot, bitecong AI Signal, Larpcheck, Axiom/GMGN flags, Dexra, CrawlHive). The evidence goes to Revtrace, and to v2's coin card as the "read recent candles, not cached liquidity" rule.
- **Generic tweet fact-check button:** fails gate c (FactCheckRadar, Larpcheck, Basis Desk Verify, SpyGlass, Tweet Fact Checker).
- Git bot's x402 pay-on-validation gap is retired, so it stays closed.

## Sourced facts vs estimates
**Sourced:** DefiLlama Tree figures; WhopScope 247; Project Bot's 100 labels and blind check; X bot's checker-reply pull; this morning's stale-check run; X counts (17 in 7 days); competitor pages, including the Chrome Web Store, ArcaneNews, PVP docs and Basis Desk; the Google News feed licence text; pump.fun fees; ASIC RG 244; the Fedyk and Hodson paper.

**Estimates:** 247 run-rate, LLM per-check cost, market shares, subscriber curve, MRR figures, A$ conversion and the search-API cost.
