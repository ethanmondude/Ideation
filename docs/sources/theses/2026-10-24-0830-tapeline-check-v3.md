# Tapeline Check v3: a "first reported" stamp under X market headlines that stays quiet unless it's sure

*Idea bot thesis, Sat 24 Oct 2026, 8:30am AWST (Perth). Path: /workspace/idea-bot/theses/2026-10-24-0830-tapeline-check-v3.md. **Version 3 of Tapeline Check** (same id: idea-bot:thesis:tapeline-check). v1: 5.5/10, token 6/10. v2 (theses/2026-10-23-0900-tapeline-check-v2.md): Project Bot's draft re-score set 5.0 if Trench Bot's blind same-event run hit the kill line, which it did (5 of 11 stale caught, 7 false flags in 69; trench-bot/blind-same-event/RESULT.md). v1 at 5.5 is still the best scored version. Built from that blind result, Project Bot's draft re-score (reviews/draft-rescore-tapeline-check-v2.md) and its 7 asks, and a new free private step this run (data/stale-check/window-split.md).*

## What changed in v3
Each line answers a weakness or ask in Project Bot's v2 draft re-score.

1. **Core judge failed its blind test: split into two engines, and the failure stays on the record.** The blind run missed both pass lines (5/11, 7 false flags). This run's free step split the 11 stale headlines by age. **4 of 11 recycle events older than 30 days** (a 2025 Trump quote, a 2025 XRP/China hoax, Warsh's April hearing, a January Satoshi-era wallet move), and the judge caught **0 of 4**. **Inside 30 days it caught 5 of 7.** So "stale" is two jobs. (a) A **late-repost stamp** for events under 30 days old, which event clustering is built for. (b) A **recycled-claim match** for months-old quotes and hoaxes, which needs a claim library, not headline search. v3 builds (a) first and treats (b) as an untested add-on. Partly fixed. The judge is still unproven on unseen data.
2. **False flags (7 of 69): the product now stamps, it doesn't accuse.** 6 of 7 false flags were reposts 1 to 2.5 days after a fresh event, which the labels don't count as misleading. v3 always shows a neutral line, "first reported 14 Oct · CoinDesk", and only adds a "LATE" tag at 48 hours or more with nothing materially new. On the frozen output, a 48-hour line gives 4 of 11 caught with 2 false flags (2.9% of fresh posts; Trench Bot's post-hoc table, not official). When it's unsure it shows nothing. Fixed in design, not yet tested blind.
3. **Retrieval rebuilt on Newsflash events (ask 2).** The `first_seen_at` event clusters and `semantic=1` matching from [Newsflash](https://newsflash.sh/docs) are the retrieval layer. Its free key's 30-day history covers 7 of the 11 stale rows. The other 4 sit outside it, which is now the job of engine (b). The full lede and exact publish time are stored as our own derived record, because most of the misses came from matching on titles alone. A small LLM stage asks "same event, later development, or same topic?" on the top 3 candidates. That handles "in talks" turning into "raised" and the Kraken paraphrase.
4. **Brave storage limit (ask 3): fixed by storing only derived records.** Brave results are used transiently for anything older than 30 days. We keep only post ID → event, first date and source URL, never Brave result bodies. Storage rights get priced only if revenue needs them.
5. **Missed rivals (ask 1): added Kronical and Mycroft.** [Kronical](https://kronical.ai) "separate[s] the first report of a story from the repeat coverage" for finance, PR and publisher teams, delivered to their agents and email, with no public price. That's the same core skill, sold to enterprises. Why an on-X stamp still has room: Kronical decides what to alert *you* about, while Tapeline stamps the post a trader is already reading, from someone else, on x.com, in the second they decide. It sells to a different buyer through a different channel. The Mycroft Media Narrative Tracker is open-source prior art for the judge (an "information age" score from 0 to 100, no ground truth), not a product. Differentiation is narrower than v2 claimed. I'd now call it a channel-and-audience edge, not a technology edge.
6. **Scope trimmed (ask 6).** The 4-week build keeps the stamp, the fine-print flag, live prices, and a coin card with only exact-mint resolution plus pumpdata.fun's dev check. On-chain pool reads, the staircase tell, dev-tie links and Telegram watchlists move to after the money test.
7. **Budget fixed (ask 4).** Day 30 is **A$110** (33 + 10 + 26 + 21 + 20), not A$104. The 4-month total is **A$710**, with the A$16 news line shown as its own item rather than hidden in contingency. Headroom is A$290.
8. **FactCheckRadar fact fixed (ask 5).** It was updated on 22 Oct 2026 (v1.0.13), not 19 Oct, and it also dates images ("first surfaced"). It still works on click only.
9. **Benchmark vs "Newsflash MCP + an LLM" (ask 7): not run, and said plainly.** It needs a free Newsflash API key, which means registering an account, so I didn't do it in this run. It's the next free step (below). Until it runs, the agent channel has no proven edge over that substitute.
10. **Demand for accuracy: still not fixed.** No new evidence that anyone pays for old-news flags on their own. Teammate digests haven't updated since 23 Oct 8am, so there was no fresh X demand count this run.

## Executive summary
- **Problem.** About 1 in 4 market-moving "BREAKING" posts in Project Bot's 100 hand labels would mislead a trader, and **11 were stale**: real events reposted as new. Free checkers replied under none of them. This run found the stale ones come in two kinds. **7 of 11 are late reposts** (2 to 14 days old) and **4 of 11 are recycled claims** (6 to 15 months old).
- **Product.** A Chrome extension on x.com that puts a neutral grey line under market headlines, "**first reported 8 Oct · CoinDesk · 14 days ago**", tagged LATE only at 48 hours or more with nothing new. It adds a fine-print flag (wrong figure or actor) and live prices of what the post names. Coin posts get the exact mint plus a dev-wallet check. It says nothing when it isn't sure. Free on click. Pro US$29/month for automatic stamps across the feed. Desk/API US$99/month. x402 US$0.01 per call, plus MCP.
- **Who pays and the token's job.** Crypto-native perps and memecoin headline traders who already pay for speed (Tree News US$61.3k of burns in 30 days per [DefiLlama](https://api.llama.fi/summary/fees/tree-news); 247 Terminal has 181 members at US$99 per [WhopScope](https://whopscope.com/w/247terminal)). **$TPLN on pump.fun:** hold it to set how many accounts get auto-stamped. Agents and users burn their own tokens for API credits and deep checks. No holder payouts and no fee-funded buybacks.
- **Cost against A$1,000.** **A$110 to day 30, A$710 over 4 months**, including a A$300 legal consult and an A$83 token launch. That leaves about A$290 of headroom. Running cost is about A$75 a month.
- **Path to US$10k/month.** 345 Pro subscribers. The base case is US$3-6k MRR at month 12 (estimate).
- **Why now and edge.** Verdict bots are now normal on crypto X, but they answer "did it happen?" on demand. The money already spent on headline speed, plus paid terminals adding "old news" flags (ArcaneNews, PVP), shows the "when" matters. The edge is placement on the post traders are reading, plus a judge measured on labelled data. It isn't the data itself, since Newsflash and Kronical have event clusters too.
- **Main risk and first move.** The judge failed its first blind test, and nobody has been shown paying for accuracy. First move (free, private): a fresh blind run of the 48-hour stamp with the LLM stage on a new batch of unseen headlines. Pass when it catches at least 75% of in-window late reposts with at most 3% false flags.
- **Verdict: test, about 35% (down from 40%).** The failed blind run is a real hit. v3 is a narrower, more honest product with a clearer next test, but it hasn't proven anything new yet.

## Problem and user
- **User:** crypto-native traders who trade headlines on Hyperliquid (including HIP-3 pre-IPO and stock perps), Solana terminals and CEX perps, plus small desks and callers who repost news. They decide on x.com, so the stamp has to sit on the post.
- **What goes wrong (private labelled set; don't publish per-account results):** 100 headlines from 40 high-volume accounts (X bot backfill, 4,134 posts, 22 Sep to 22 Oct). Project Bot's labels and idea bot's blind 30 agreed 90% (kappa 0.79). Misleading types: 11 stale, 4 wrong figure, 4 overstated, 3 wrong actor, 1 early.
- **New split this run (data/stale-check/window-split.md):**
  - **Late reposts (7):** Bitfinex-seizure wallet move (8 Oct, posted 22 Oct), Ledger implant confirmation (12-13 Oct, posted 22 Oct), ETF holdings data as of 8 Oct (posted 17 Oct), Ripple Prime (15 Oct, posted 21 Oct), Kraken VARA (6 Oct, posted 12 Oct), Bloomberg story (posted 2.5 days late), Senate amendment vote (posted 2 days late).
  - **Recycled claims (4):** Trump's GENIUS Act remarks (Jul 2025), the XRP/China "$40B" hoax (mid-2025), Warsh's "no CBDC" (Apr 2026 hearing), and the Satoshi-era 2,000 BTC move (Jan 2026).
- **Today's workaround:** type "@grok is this true". Grok replied under 14 of 100 labelled posts and caught 2 of 6 true-but-misleading framings (X bot's checker-reply pull, from v1/v2).
- **Academic backing:** Fedyk and Hodson, ["When Can the Market Identify Old News?"](https://ai.updf.com/paper-detail/when-can-the-market-identify-old-news-fedyk-hodson-b7a99832989a09cd8f98c11759ab401a366031e6). Recombined stale stories still move prices and later reverse.

## Evidence of money
- **Tree News:** US$61,347 in 30 days, US$1.05M in a year in TREE burns ([DefiLlama](https://api.llama.fi/summary/fees/tree-news)). Part of that is USDC buy-and-burn, so only some of it is the "users burn their own tokens" pattern. People pay for speed.
- **247 Terminal:** 181 members at US$99 ([WhopScope](https://whopscope.com/w/247terminal)), about US$18k/month (estimate).
- **Old-news flags inside paid terminals:** [ArcaneNews](https://arcane.news/) ("Automatic detection to flag potential old news") and [PVP Terminal's Old News Threshold](https://docs.pvpterminal.com/desktop/desktop/settings/news), which measures delivery lag. Paying news traders value the label enough that terminals build it. Nobody shows payment for the label on its own.
- **Kronical** sells "first report vs repeat coverage" to finance and PR teams ([kronical.ai](https://kronical.ai), no public price). It's a sign enterprises pay for this skill, but there's no price or revenue to cite.
- **Missing:** no product shows revenue from headline accuracy for crypto traders. This is still the cap on the score.

## Bottom-up market sizing (assumptions labelled)
- Spend pool (sourced plus estimate): Tree (US$61k/month) plus 247 (about US$18k/month) comes to about US$80k/month already going to headline tools.
- Reachable traders (sourced, v1): Hyperliquid frontends had 125.4K users in 30 days (OpenChainBench, 22 Oct).
- Assumption A: 0.25-0.5% pay US$29, which is 310-630 payers, or US$9.0k-18.3k MRR.
- Assumption B: 10-20 desks at US$99 add US$1-2k. Agent x402 calls at 1,000 a day add about US$0.3k.
- **Base case US$3-6k MRR at month 12 (estimate)**, held back by free on-demand checkers and the unproven willingness to pay for accuracy.

## Competitive teardown
| Competitor | What it does | Pricing | Revenue / traction | Gap left | Why they won't build our slice soon |
|---|---|---|---|---|---|
| Grok ("is this true") | On-demand answer when tagged | Free | Built into X; 14 of 100 labelled posts | Manual; no event-date stamp | X won't label its big accounts' posts stale at scale |
| [Larpcheck](https://larpcheck.app/how) | Tag under any post, claim scored 0-100 | Free; Pro by holding $LARPCHECK | Self-reported ~1,000 users/day | Tag-only; 1 of 100 labelled posts | Could add a date line fast. **Biggest copy risk** |
| [FactCheckRadar](https://chromewebstore.google.com/detail/factcheckradar/obepkghlneckiemaclcigahjnbkonhnf) | X fact-check button; dates images ("first surfaced"); scheduled rechecks | In-app purchases, prices not public | v1.0.13, updated 22 Oct 2026; no ratings | On click; general audience; no auto text stamp, no market prices | General misinformation, not trading |
| [Basis Desk Verify](https://basisdesk.news/news/basis-desk-verify-fact-check-crypto-news-chrome-extension) | Side panel, claims vs primary docs, prices | Free | Launched 7 Oct 2026 | Click-to-run, articles first | Media brand avoids labelling others' posts |
| [Kronical](https://kronical.ai) (new) | Reads news, filings, X; separates first report from repeats; alerts agents and email | Not public | Enterprise (finance, PR, publishers) | Not on the post; not crypto-trader self-serve | Enterprise sales motion; a US$29 consumer extension isn't their market |
| [Mycroft Narrative Tracker](https://github.com/Humanitariansai/Mycroft/tree/main/n8n_Workflows/Media_Narrative_Tracker) (new) | Open-source n8n "information age" score | Free | Prior art | No ground truth, no product | Not a business |
| [Newsflash](https://newsflash.sh/docs) | News API with event clusters (`first_seen_at`), semantic match, MCP | Free 1,000/day, 30-day history; US$29/month for 5 years | Unknown | **Supplier and substitute**: any agent can approximate the stamp with it | Sells data, not an X overlay |
| [ArcaneNews](https://arcane.news/), Tree/[PVP](https://docs.pvpterminal.com/desktop/desktop/settings/news) | Paid terminals with old-news flags | Plans / TREE credits | Tree US$61k/30d | Separate app; feed lag, not event age | Want users in their terminal, not on X |
| [SpyGlass](https://devpost.com/software/spyglass), Tweet Fact Checker, Stale News Warning, Custom Timestamps for X | Inline pills, OpenAI button, old-article warning, post-age colours | Free | Demos and hobby projects | Post timestamp only or demo | Not businesses |
| [pumpdata.fun](https://pumpdata.fun) | pump.fun dev checks, x402/MCP, Grok Bot template | 300 free/day | New | Not headlines. Supplier for the coin card | n/a |

**Gate c on v3's core job** (an automatic late-repost stamp under X market posts for crypto traders): no working tool does it on the post. Kronical and Newsflash do the underlying job off X, so the gap is the channel and the buyer, not the technology. The plain verdict and the generic button stay crowded and aren't the lead.

## Product and UX
**First minute.** Install the extension and open x.com. Under "🚨 JUST IN: US government wallet just moved $1B from the Bitfinex hack" a grey line appears (illustrative, built from the labelled case): `first reported 8 Oct · CoinDesk, Decrypt · LATE 14 days · BTC −0.4% 1h`. A next-day repost shows only `first reported yesterday 21:10 · The Block`, with no tag. A brand-new release shows `new · BLS release 2 min before`. A coin post shows `mint 7xKX…pump (exact) · dev: 4 prior launches, 3 under $5k (pumpdata)`. When the judge isn't confident, there's no line at all. No sign-up for on-click stamps. Wallet or email login for Pro.

**MVP stack.**
- Chrome MV3 extension (TypeScript). It reads only the visible post and sends text plus post ID. Narrow permissions, no remote code.
- API on a A$10/month VPS (Hono/Node) plus Supabase:
  - (1) a claim extractor (small LLM, cached per post);
  - (2) **retrieval**: Newsflash event clusters (free key, then US$29/month from revenue), our own RSS and exchange-announcement archive (storing derived records with lede and exact time), and transient Brave News for anything older than 30 days;
  - (3) **two-stage judge**: Trench Bot's rules layer (figures, names, action, tense, explainer veto) as a cheap filter, then a small LLM over the top 3 candidates answering "same event, later development, or same topic". It abstains below a confidence bar;
  - (4) a market mapper (Hyperliquid info API including HIP-3, GeckoTerminal);
  - (5) coin card: exact-mint resolution plus pumpdata.fun's free dev check.
- **Engine (b), recycled-claim match, add-on and untested:** a library of known recycled claims, seeded from the [Google Fact Check Claim Search API](https://developers.google.com/fact-check/tools/api) (needs an API key; under Google's API terms, to be checked for commercial use) plus every dispute users file. Matched by embedding and an LLM check.
- Payments: Lemon Squeezy card, Solana Pay USDC to a public wallet, and $TPLN hold or burn verified on-chain.

**Week by week (20-25 h/week).**
1. Newsflash plus archive ingest, two-stage judge, and a new blind benchmark batch (pass line below).
2. Fine-print flag and market mapper, with the API and cache.
3. Extension line, Backstory card, Pro gating and payments.
4. MCP, x402 and the Grok Bot template, the coin card (mint and dev only), and an unlisted Chrome listing.

**What's hard.** Getting "same event vs later development" right on recurring topics (ETF flows, CPI, funding rounds), and recycled claims whose wording and amounts change.

**What a copycat could clone.** The UI in a weekend, and "Newsflash MCP + an LLM" in a few days. What's harder to copy: the measured judge on a growing labelled set, and the dispute loop that feeds it.

## Agent distribution
- **MCP** `freshness_check(text|post_url)`, free for 50 checks a day. About 1 day to build.
- **x402 on Solana**, US$0.01 per check in USDC or burned $TPLN credits. About 2 days.
- **A one-tap Grok Bot template plus a paste-in prompt**, on the [pumpdata.fun template](https://github.com/pumpdatafun/grokbot-pumpfun-template) model. About half a day.
- **Honest limit:** "Newsflash MCP + any LLM" is a substitute. This channel only earns its place if the published benchmark (no account names) beats that baseline on market headlines.

## Token design (pump.fun)
- **Jobs:**
  - (1) **Hold** to set the auto-stamp watchlist (25 / 100 / 300 accounts), verified by wallet signature.
  - (2) **Burn your own $TPLN** for deep checks (recycled-claim search beyond 30 days, about US$0.25 each) or a Pro month (US$29 equivalent).
  - (3) **Agents prepay API credits** by burning their own $TPLN, with an SPL burn and a memo carrying the check ID.
- Card and USDC are never converted into token buys.
- **Launch:** pump.fun only (X bot shows no meta shift: rival pads ran 7-21 posts an hour against pump.fun's 1,065-1,339 on 23 Oct). Launch after 25 paying users and the legal consult. SOL pair, mint and freeze authority revoked and confirmed on-chain, a **small labelled dev buy** (≤0.5 SOL, wallet published), no bundles or paid callers.
- **Holder Rewards off. Tokenized Agent buybacks off.**
- **Pin one official CA** on the site and official X account from day one, and never launch through a QR code or a third party's post (lesson from Kimchi, 23 Oct).
- **Fee flow:** every burn is the user's own SPL burn, listed with Solscan links. Creator fees go to a published wallet as **bonus only**, never to buybacks or burns. Public repo for the extension, judge rules and burn verifier.
- **Comparables:** Tree TREE (verified burns, part USDC buy-and-burn), Larpcheck (hold-to-access), KOLscan $KOLS (hold-to-access), Paparazzi $PAPA (Robinhood Chain, burns for credits, but revenue-funded payouts that our rules bar). Don't project token income.
- **Legal line:** usage credit only, with no profit or "number go up" wording. Stamps are factual ("first reported 8 Oct at [source]"), inside ASIC's factual-information line ([RG 244](https://download.asic.gov.au/media/tkqi11il/rg244-published-13-december-2012-20211208.pdf)). This is my reading, not legal advice; the A$300 consult checks it.
- Token fit is honestly still about 6: it's the same hold-to-access pattern as Larpcheck.

## Budget and founder load (A$; US$1 ≈ A$1.43; estimates unless sourced)
| Item | One-off | Monthly | 4-month total |
|---|---|---|---|
| Domain plus Chrome Web Store fee | 33 | | 33 |
| VPS | | 10 | 40 |
| LLM: extractor plus 2nd-stage judge (~300 unique checks/day) | | 26 | 104 |
| X API reads for Pro auto-stamps (US$0.005/post) | | 21 | 84 |
| News: Newsflash free key; Brave beyond its free credit | | 4 | 16 |
| pumpdata.fun free tier; Google Fact Check API key (free) | | 0 | 0 |
| Legal consult | 300 | | 300 |
| Token launch (rent plus ≤0.5 SOL labelled dev buy) | 83 | | 83 |
| Contingency | 50 | | 50 |
| **Total** | | **~A$61** | **A$710** |

**To day 30: A$110** (33 + 10 + 26 + 21 + 20 contingency). Newsflash premium (about A$41/month) only from revenue. That leaves A$290 of headroom. **Founder load:** 20-25 h/week for 4 weeks, then about 10 h/week.

## Business model and unit economics (estimates)
- Free (20 on-click stamps a day). Pro US$29/month (automatic stamps, 25-account watchlist, deep checks). Desk/API US$99/month. x402 US$0.01 per call.
- A stamp is computed once per post and shared, so cost to serve is about US$0.30-0.80 per Pro user per month, with about 90% gross margin. Card fees about 5% + US$0.50.
- Cash CAC about US$0. Time is the constraint.

## Solo GTM
1. A private benchmark first. Once it passes, the pitch line is the measured catch rate with no account names.
2. First 10 users (needs Ethan's OK for outreach): traders who reply "old news" or "@grok is this true" under market headlines, plus Hyperliquid and Solana Telegram groups.
3. A free "late repost" Telegram channel naming the event and its first date, never the poster.
4. Agent channels (MCP, x402, Grok template) and tool directories.
5. A 25% cash referral share.

## 12-month financial snapshot (estimates)
| Month | Pro | Desk | MRR (US$) | Cumulative cost (A$) |
|---|---|---|---|---|
| 1 | 0 (test) | 0 | 0 | ~110 |
| 3 | 40 | 2 | ~1.4k | ~560 |
| 6 | 90 | 5 | ~3.1k | ~790 |
| 12 | 150-250 | 10-15 | ~5.3-8.7k | out-of-pocket stays under A$1,000; revenue covers running costs from about month 4 |

US$10k MRR needs about 345 Pro subscribers. That's plausible, but it isn't the base case.

## Defensibility
- A labelled benchmark that grows from disputes, with the judge accuracy published on it.
- Placement on the post, plus agent channels.
- Weak against Larpcheck or FactCheckRadar adding a date line, and against "Newsflash MCP + LLM". Speed and measured accuracy are the only moat.

## Risks (mitigation, cheap test)
| Risk | Mitigation | Cheap test |
|---|---|---|
| Judge still too noisy | 48-hour LATE line, LLM 2nd stage, abstain | Fresh blind batch (step 1 below) |
| Recycled claims unreachable | Claim library from ClaimReview plus disputes; ship as add-on | Step 2 below |
| Substitute: Newsflash MCP + LLM | Publish a benchmark that beats it | Step 3 below |
| Free checkers add a date line | Ship automatic and fast | X bot weekly watch |
| Nobody pays for accuracy | Lead with automatic stamps and watchlists (speed-adjacent) | Founding pass, once Ethan picks it to launch |
| X Developer Policy | Event facts only, no account scores | Written OK before any poster record |
| Licensing (Brave, Google News) | Derived records only; no Google News RSS in production | Check Google API terms before using ClaimReview data |
| Defamation; token seen as investment | Factual wording; usage-credit token | Legal consult |

## Kill or confirm
**Free private steps first (claim each in claims.md):**
1. **Fresh blind batch.** The 80 rows have now been seen, so re-scoring on them is no longer blind. X bot pulls batch 2 (WatcherGuru, Cointelegraph, BitcoinArchive, BSCNews, coinbureau, 30 days). One bot labels about 100 headlines, and a different bot runs the two-stage, 48-hour judge with predictions frozen first. **Pass: ≥75% of in-window late reposts tagged LATE, ≤3% false flags on fresh posts, and a correct "first reported" date on ≥80% of the stamps it shows. Kill the stamp as the lead below 50% caught or above 8% false flags.**
2. **Recycled-claim match** on the 4 old stale rows plus 6 known crypto hoaxes, against Google Fact Check Explorer or Claim Search, with 20 fresh confirmed rows as decoys. Pass at ≥7 of 10 matched and ≤1 false match. A teammate can run it by hand in Fact Check Explorer with no key.
3. **Benchmark vs Newsflash MCP + LLM** on the same batch. This needs a free Newsflash key, which means registering an account, so a bot should only do it with Ethan's OK. Pass if ours beats it by ≥10 points on catch rate at equal false flags.

**Then the 30-day paid validation, once Ethan picks this thesis to launch as a coin (about A$110):** an unlisted Chrome listing and a US$29 founding pass for 3 months. **Pass: ≥25 passes and ≥25% of installs seeing a stamp on 3+ days a week. Iterate once at 10-24 passes. Kill below 10, below 10% weekly use, or if ≥50% say "I just ask Grok/Larpcheck."**

## Comparables
Tree News, 247 Terminal, ArcaneNews and PVP (old-news flags inside paid terminals), Kronical (enterprise first-report detection), FactCheckRadar, Larpcheck, pumpdata.fun (free tier, x402 and Grok template distribution).

## Dropped this run (screen)
- **0%-fee trading terminal** (repeated "terminal fees" anger in X bot's 23 Oct digest; Nought0Fees pitched in replies): fails gate f (a terminal isn't a solo A$1,000 build, and it's execution, not information) and gate c (Nought0Fees, Axiom, Photon, GMGN).
- **Enterprise "first report vs repeat" alerts for crypto funds** (the Kronical model): fails gate a (enterprise buyers, sales-led) and gate c (Kronical, Newsflash). The evidence goes to this thesis as a rival.

## Sourced facts vs estimates
**Sourced:** the blind result (trench-bot/blind-same-event/RESULT.md), the labels, this run's window split, Project Bot's draft re-score, DefiLlama Tree, WhopScope 247, competitor pages (Kronical, Newsflash docs, Google Fact Check Tools API, FactCheckRadar store page via Project Bot, ArcaneNews, PVP docs), X bot's 23 Oct launchpad counts, and ASIC RG 244.
**Estimates:** the 247 run-rate, LLM cost, market shares, subscriber curve, MRR, the A$ conversion, and the 48-hour figures (post-hoc on frozen output, not an official blind result).
