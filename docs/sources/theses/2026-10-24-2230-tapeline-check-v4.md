# Tapeline Check v4: an automatic "first reported" stamp under X market headlines, and nothing else

*Idea bot thesis, Sat 24 Oct 2026, 10:30pm AWST (Perth). Path: /workspace/idea-bot/theses/2026-10-24-2230-tapeline-check-v4.md. **Version 4 of Tapeline Check** (id idea-bot:thesis:tapeline-check). v3 scored 5.5/10, token 6/10, best version (Project Bot, reviews/2026-10-24-0915-tapeline-check-v3.md); its blind holdout landed in the iterate zone (5 of 7 stale caught, 0 of 16 false flags). Marshal ($MRSHL) is at 7.0 with a frozen build spec, so this run rotates to the best other rule-passing thesis, as the 20:30 lesson said. Built from Project Bot's six v4 asks, X bot's 22:00 digest (Larpcheck's new NARRATIVE stamp), Trench Bot run 17, and one free check this run (data/pubtime-check/2026-10-24-2235.md).*

## What changed in v4
Each line answers a weakness Project Bot's v3 review named, or new teammate evidence.

1. **Uniqueness (X bot: "lead only with the first-reported stamp, drop the verdict").** Larpcheck now gives a NARRATIVE score on any tagged post. I pulled its last 25 replies (21:45–22:25 AWST): **25 of 25 carry a NARRATIVE score, 0 of 25 give a first-reported date or call anything old news**, and 18 of 25 are about small coin or app tickers, not market headlines. So the true/false verdict is now commodity and is **cut entirely**, including the fine-print "wrong actor" flag. The product is only the date stamp, plus a figure check where a number can be read straight from the source (kept because it's the same retrieval). Fixed by narrowing.
2. **Retrieval missed a hype-worded post (ask 1).** Queries are now built from a structured claim, `{actor, action, object, figure, named_report}`, not from the headline's words. A post saying "COINBASE JUST DID IT" about a Block report becomes `{actor: Coinbase, action: report/launch, named_report: The Block}`. Rule and pseudocode in the build brief. Fixed in design, to be checked in the light feasibility check.
3. **Publish time (ask 2): free check done.** On 11 fresh articles from CoinDesk, The Block, Decrypt and Cointelegraph, the RSS `pubDate` was present on **11 of 11** and matched the page's `datePublished` to the second on **all 8** pages that exposed one (The Block's pages returned a bot wall to curl, 0 of 3). So exact times are keyless and cheap, with RSS as the primary and the page as the cross-check. The same check found single outlets lagging the first report by **96 minutes to 3 hours** (Initia halt, Blumenthal/Tether, Netanyahu plan), so the stamp always takes the earliest time across an event cluster and never trusts feed-ingest time, which ran up to 31h early in the v3 holdout. Fixed; target ≥80% of stamps within ±6h stays as an acceptance test.
4. **Entity swaps in recycled claims (ask 3).** An alias table (`entities.json`: Ripple ↔ XRP ↔ Garlinghouse, Strategy ↔ MicroStrategy ↔ Saylor, BlackRock ↔ IBIT, etc.) expands every claim before matching, and the recycled-claim library stores claims as `{speaker, claim_core, first_date, source}`. Fixes the Garlinghouse miss in design.
5. **Stage 2 on a real small LLM with logged cost (ask 4).** The build brief now names the call, its prompt contract, a hard per-check cost log and a budget cap (US$0.002 per check target, abstain if over). Still untested; it's the first acceptance test.
6. **Light feasibility check (replaces the blind holdout, per Ethan's 11:28 rule: bots only do light checks; Claude Code builds).** About 10 fresh market headlines from X bot's 8:30am AWST 25 Oct pull; each stamp's earliest outlet and time hand-checked against the outlets. Pass: at least 7 of 10 right. No frozen labels or separate judge.
   **The score now hinges on demand:** a repeated "is this news old?" complaint or tip signal from traders, which X bot is searching for.
7. **Newsflash dependency removed (ask 6).** Since RSS plus page times work keyless, the core retrieval is our own archive of ~25 outlet and exchange feeds. Newsflash becomes an optional supplier only, so the "needs a sign-up" blocker no longer gates the build. The "Newsflash MCP + LLM" substitute benchmark stays as a risk test.
8. **Demand evidence: one small new signal, still no payer.** The free "Custom Timestamps for X" extension (77 users per ExtScope) has a review saying it "has a lot of use cases in the crypto niche where you have to determine if news are old or not". That's one person and a free tool. Nobody is shown paying for accuracy, and that still caps the score.
9. **Budget summary fixed.** The running cost reads A$61 a month, not A$75. The totals are re-costed below, with the Newsflash line gone.
10. **Meta check (Ethan's abandon rule).** Not abandoned: no rival stamps a first-reported date under X posts automatically, and Larpcheck's growth went into coin and app verdicts, not dates. If Larpcheck or Grok adds a date line, this thesis should be dropped, not refined again.

## Executive summary
- **Problem.** In Project Bot's 100 labelled market headlines, **11 were stale**: real events reposted as new (7 late reposts of 2–14 days, 4 recycled claims of 6–15 months). Free checkers replied under none of them. Traders read the post on x.com and act in seconds.
- **Product.** A Chrome extension for x.com that puts one neutral grey line under market headlines: `first reported 23 Oct 17:03 UTC · The Block · 29h ago`, tagged **LATE** only at 48h+ with nothing materially new. If the post's number differs from the source's, it adds `source says 22.46, post says 23.64`. Silent when unsure. Free on click; **Pro US$29/month** for automatic stamps across the feed; **Desk/API US$99/month**; x402 US$0.01 a check plus MCP.
- **Who pays and the token's job.** Crypto-native headline traders who already pay for speed (Tree News US$61.3k of burns in 30 days per [DefiLlama](https://api.llama.fi/summary/fees/tree-news); 247 Terminal has 181 members at US$99 per [WhopScope](https://whopscope.com/w/247terminal)). **$TPLN on pump.fun:** hold to set how many accounts get auto-stamped (25/100/300); burn your own $TPLN for deep checks and API credits. No payouts, no fee-funded buybacks.
- **Cost against A$1,000.** **A$106 to day 30 and A$694 over 4 months** (A$300 legal consult and A$83 token launch included), leaving A$306 of headroom. Running cost about A$57 a month.
- **Path to US$10k/month.** About 345 Pro subscribers. The base case is US$3–6k MRR at month 12 (estimate).
- **Why now and edge.** Verdict bots are now everywhere on crypto X (Larpcheck answers on every tagged post), which makes "is it true" free and leaves "**when** did this first happen" unowned on the post. The edge is placement plus a judge measured on labelled data. It's a channel edge, not a data edge: Kronical and Newsflash cluster events off X.
- **Main risk and first move.** Nobody is shown paying for accuracy, and the judge is only light-checked. First move (free, private): the light feasibility check below (~10 headlines, ≥7 of 10 right), plus X bot's demand search.
- **Verdict: test, about 35% (unchanged).** Cleaner and more unique than v3, and the time layer is now proven cheap, but the score can't pass 6.0 without a demand signal, and 7 needs a payer.

## Problem and user
- **User:** crypto-native traders who trade headlines on Hyperliquid (including HIP-3 stock and pre-IPO perps), Solana terminals and CEX perps, plus small desks and callers who repost news.
- **What goes wrong (private labelled set; never publish per-account results):** 100 headlines from 40 high-volume accounts (X bot backfill, 4,134 posts, 22 Sep–22 Oct; label agreement 90%, kappa 0.79). 11 stale, 4 wrong figure, 4 overstated, 3 wrong actor, 1 early. v4 serves the 11 stale plus the 4 wrong figures; the overstated and wrong-actor cases go to verdict bots.
- **Live example of a figure gap (Trench Bot run 17):** a 20:30 AWST post said "$KIMCHI crashes 99%"; Trench Bot's pool data showed −52% in 24h. A figure check on a coin post can read the pool directly.
- **Today's workaround:** "@grok is this true" (replied under 14 of 100 labelled posts) or Larpcheck (tag-only, verdict not date).
- **Academic backing:** Fedyk and Hodson, ["When Can the Market Identify Old News?"](https://ai.updf.com/paper-detail/when-can-the-market-identify-old-news-fedyk-hodson-b7a99832989a09cd8f98c11759ab401a366031e6): recombined stale stories still move prices and later reverse.

## Evidence of money
- **Tree News:** US$61,347 in 30 days, US$1.05M in a year in TREE burns ([DefiLlama](https://api.llama.fi/summary/fees/tree-news)); part is USDC buy-and-burn. People pay for headline speed.
- **247 Terminal:** 181 members at US$99 ([WhopScope](https://whopscope.com/w/247terminal)), about US$18k/month (estimate).
- **Old-news flags inside paid terminals:** [ArcaneNews](https://arcane.news/) ("Automatic detection to flag potential old news and option to remove it from your feed") and [PVP Terminal's Old News Threshold](https://docs.pvpterminal.com/desktop/desktop/settings/news). Terminals build the label for paying users; nobody sells it alone.
- **Free-tool signal:** [Custom Timestamps for X](https://chromewebstore.google.com/detail/custom-timestamps-for-x/ajdpfnakibpakgacmijifjndjojcejpj) (77 users per [ExtScope](https://extscope.org/extension/ajdpfnakibpakgacmijifjndjojcejpj), no paid features) has a review: "has a lot of use cases in the crypto niche where you have to determine if news are old or not." It colours the post's age, not the event's.
- **Kronical** sells first-report-vs-repeat detection to finance and PR teams ([kronical.ai](https://kronical.ai), no public price).
- **Missing:** no product shows revenue from a stand-alone headline-age label for crypto traders.

## Bottom-up market sizing (assumptions labelled)
- Spend pool (sourced plus estimate): Tree about US$61k/month plus 247 about US$18k/month, roughly US$80k/month already going to headline tools.
- Reachable traders (sourced, v1): Hyperliquid frontends had 125.4K users in 30 days (OpenChainBench, 22 Oct).
- Assumption A: 0.25–0.5% pay US$29 → 310–630 payers → US$9.0–18.3k MRR.
- Assumption B: 10–20 desks at US$99 add US$1–2k; 1,000 x402 calls a day add about US$0.3k.
- **Base case US$3–6k MRR at month 12 (estimate)**, held back by unproven willingness to pay.

## Competitive teardown
| Competitor | What it does | Pricing | Revenue / traction | Gap left | Why they won't build our slice soon |
|---|---|---|---|---|---|
| [Larpcheck](https://larpcheck.app/how) | Tag a post: NARRATIVE + COIN scores | Free; Pro by holding $LARPCHECK | ~90–114 mentions/hour (X bot); 0 of 25 latest replies give a date | Tag-only; verdict, not event date; coin/app focus | Could add a date line fast. **Biggest copy risk; drop the thesis if it does** |
| Grok ("is this true") | On-demand answer | Free | 14 of 100 labelled posts | Manual; no date stamp | X won't stamp its big accounts stale at scale |
| [FactCheckRadar](https://chromewebstore.google.com/detail/factcheckradar/obepkghlneckiemaclcigahjnbkonhnf) | X fact-check button, image "first surfaced" | In-app, prices not public | v1.0.13 (22 Oct) | Click-only, general audience | Misinformation, not trading |
| [Basis Desk Verify](https://basisdesk.news/news/basis-desk-verify-fact-check-crypto-news-chrome-extension) | Side panel, claims vs primary docs | Free | Launched 7 Oct | Click-to-run, articles first | Media brand won't label others' posts |
| [Custom Timestamps for X](https://chromewebstore.google.com/detail/custom-timestamps-for-x/ajdpfnakibpakgacmijifjndjojcejpj) | Colours the post's own age | Free | 77 users | Post age, not event age | Hobby tool |
| [Kronical](https://kronical.ai) | First report vs repeats, alerts to agents/email | Not public | Enterprise | Not on the post; not self-serve | Enterprise sales motion |
| [Newsflash](https://newsflash.sh/docs) | News API, event clusters, MCP | Free 1,000/day; US$29/month | Unknown | Supplier and substitute | Sells data, not an overlay |
| [ArcaneNews](https://arcane.news/), Tree / [PVP](https://docs.pvpterminal.com/desktop/desktop/settings/news) | Paid terminals with old-news flags | Plans / TREE credits | Tree US$61k/30d | Separate app; PVP measures feed lag | Want users in their terminal |
| Mycroft Narrative Tracker, SpyGlass, Tweet Fact Checker, Stale News Warning (2016) | Prior art and demos | Free | None | Not products | Not businesses |

**Gate c on v4's core job** (an automatic event-date stamp under X market posts): 0 working tools do it on the post. Passes.

## Product and UX
**First minute.** Install, open x.com. Under "🚨 JUST IN: Initia halts network after exploit" posted the next evening, a grey line appears: `first reported 23 Oct 17:03 UTC · The Block · 29h ago`. At 48h+ with nothing new it adds `LATE`. A fresh BLS print shows `new · BLS 2 min ago`. A post claiming a number the source contradicts adds `source says 23.64, post says 22.46`. When the judge isn't sure, nothing shows. No sign-up for on-click stamps; wallet signature or email for Pro.

**Advanced under the hood:** structured claim extraction, an alias-expanded event index over our own feed archive, earliest-time clustering across outlets, a two-stage same-event judge that abstains, and a recycled-claim library seeded from ClaimReview. **What's hard:** "same event vs later development" on recurring topics (ETF flows, CPI, funding rounds) and recycled claims whose wording drifts. **What a copycat could clone:** the UI in a weekend; "Newsflash MCP + an LLM" in days. Harder: the measured judge on a growing labelled set and the dispute loop.

**Scores (my estimate):** Innovation 6.5 (event age on the post is new; clustering isn't), Usability 8.5 (one grey line, no click, silent when unsure), Uniqueness 6 (up from 5.5 now verdicts are cut and Larpcheck shows no dates).

## Agent distribution
- MCP `first_reported(text|post_url)`, free for 50 checks a day.
- x402 on Solana, US$0.01 per check in USDC, or burned $TPLN credits.
- A Grok Bot template and paste-in prompt (pumpdata.fun template model).
- Honest limit: earns its place only if the benchmark beats "Newsflash MCP + any LLM".

## Token design (pump.fun)
- **Jobs:** (1) **hold** $TPLN to set the auto-stamp watchlist size (25 / 100 / 300 accounts), checked by wallet signature; (2) **burn your own** $TPLN for deep checks (recycled-claim search beyond 30 days, about US$0.25 equivalent) or a Pro month; (3) **agents prepay API credits** by burning their own $TPLN (SPL burn with a memo carrying the credit ID). Card and USDC are never converted into token buys.
- **Launch:** pump.fun only (X bot 22:00: no meta shift; rival pads 22–32 posts/hour vs pump.fun 916–1,065; StonkFun is a second pad builders add, not a move). Launch after 25 paying users and the legal consult. Mint and freeze authority off and confirmed on-chain; a small labelled dev buy (≤0.5 SOL, wallet published); no bundles, no paid callers, no boosts.
- **Holder Rewards off. Tokenized Agent buybacks off.**
- **Pin one official CA** on the site, the extension's About page and the official X account from day one; copycat mints appear within hours (X bot counted 19 Pump Baby copies in ~2h tonight). Never launch through a QR code or another account's post, and never claim an "official" tie to any brand (Trench Bot's REMUS lesson).
- **Fee flow and verification:** every burn is the user's own SPL burn, listed with Solscan links on a public page. Creator fees go to a published wallet as a bonus only, never to buybacks or burns. Public repo for the extension, judge rules and burn verifier.
- **Comparables:** Tree TREE (verified burns, partly USDC buy-and-burn, organic usage), Larpcheck (hold-to-access Pro), KOLscan $KOLS (hold-to-access). Shilled examples to avoid: tonight's brand name-bait family (~391 of 706 rugs in Trench Bot's log). Don't project token income.
- **Legal line:** usage credit only; no profit wording. Stamps are factual ("first reported 23 Oct at The Block"), inside ASIC's factual-information line ([RG 244](https://download.asic.gov.au/media/tkqi11il/rg244-published-13-december-2012-20211208.pdf)). My reading, not legal advice; the A$300 consult checks it.
- **Token fit about 6**, the Larpcheck hold-to-access pattern plus a real burn-for-credits job.

## Budget and founder load (A$; US$1 ≈ A$1.43; estimates unless sourced)
| Item | One-off | Monthly | 4-month total |
|---|---|---|---|
| Domain plus Chrome Web Store fee | 33 | | 33 |
| VPS (API, feed poller, Postgres) | | 10 | 40 |
| LLM: claim extractor + stage-2 judge (~300 unique checks/day, capped) | | 26 | 104 |
| X API reads for Pro auto-stamps (US$0.005/post) | | 21 | 84 |
| News: own RSS + page reads (keyless); Brave beyond free credit transient only | | 0 | 0 |
| Google Fact Check API key (free) | | 0 | 0 |
| Legal consult | 300 | | 300 |
| Token launch (rent plus ≤0.5 SOL labelled dev buy) | 83 | | 83 |
| Contingency | 50 | | 50 |
| **Total** | | **~A$57** | **A$694** |

**To day 30: A$106** (33 + 10 + 26 + 21 + 16 of contingency). Headroom A$306. Newsflash (about A$41/month) only from revenue, if ever. **Founder load:** Claude Code builds; Ethan reviews about 5–8 h/week for 4 weeks, then about 3 h/week for disputes and feed upkeep.

## Business model and unit economics (estimates)
- Free: 20 on-click stamps a day. Pro US$29/month (automatic stamps, 25-account watchlist, deep checks). Desk/API US$99/month. x402 US$0.01 per call.
- A stamp is computed once per post and shared across users, so cost to serve is about US$0.30–0.80 per Pro user a month, roughly 90% gross margin. Card fees about 5% + US$0.50.

## Go-to-market for a solo founder
1. Private benchmark first; the pitch line is the measured catch rate, no account names.
2. First 10 users (needs Ethan's OK for any outreach): traders who reply "old news" or "@grok is this true" under market headlines; Hyperliquid and Solana trader groups.
3. A free "late repost" Telegram channel naming the event and its first date, never the poster.
4. Agent channels (MCP, x402, Grok Bot template) and directories (Smithery).
5. A 25% cash referral share (card revenue only; never tokens).

## 12-month financial snapshot (estimates)
| Month | Pro | Desk | MRR (US$) | Cumulative cost (A$) |
|---|---|---|---|---|
| 1 | 0 (test) | 0 | 0 | ~106 |
| 3 | 40 | 2 | ~1.4k | ~550 |
| 6 | 90 | 5 | ~3.1k | revenue covers running costs from about month 4 |
| 12 | 150–250 | 10–15 | ~5.3–8.7k | out-of-pocket stays under A$1,000 |

## Defensibility
A labelled benchmark that grows from disputes; published judge accuracy; placement on the post plus agent channels. Weak against Larpcheck or Grok adding a date line and against "Newsflash MCP + LLM". Speed and measured accuracy are the only moat.

## Risks (mitigation, cheap test)
| Risk | Mitigation | Cheap test |
|---|---|---|
| Judge too noisy | Structured claim queries, earliest-time clustering, 48h LATE line, abstain | Light feasibility check (step 1) |
| Wrong times | RSS pubDate + page `datePublished`, never ingest time | AT-T3 (±6h on ≥80%) |
| Recycled claims missed | Alias table + ClaimReview library | Step 2 |
| Substitute: Newsflash MCP + LLM | Publish a benchmark that beats it | Step 3 |
| Larpcheck/Grok add a date line | Ship automatic and fast; **abandon if it happens** | X bot weekly watch |
| Nobody pays for accuracy | Sell automation and watchlists (speed-adjacent) | Founding pass once Ethan picks it |
| X Developer Policy | Event facts only, no per-account scores | Written OK before any poster record |
| Licensing | Store derived records only (post → event, time, source URL); no Google News RSS in production; outlet RSS used under its feed terms | Check each feed's terms before launch |
| Defamation; token seen as investment | Factual wording; usage-credit token | Legal consult |

## Kill or confirm
**Free private steps first (claim each in claims.md):**
1. **Light feasibility check (Ethan's 11:28 rule: bots only do light checks; Claude Code builds).** Take about 10 fresh market headlines from X bot's 8:30am AWST 25 Oct pull, run the stamp, and hand-check each stamp's earliest outlet and time against the outlets. **Pass: at least 7 of 10 right.** Accuracy at scale is left to Claude Code's acceptance tests. The score now hinges on demand: a repeated "is this news old?" complaint or tip signal from traders, which X bot is searching for. **Kill line kept:** drop if Larpcheck or Grok adds a date line; park if it doesn't beat 5.5 without a payer signal.
2. **Recycled-claim match:** the 4 old stale rows plus the Garlinghouse row plus 6 known crypto hoaxes, against Google Fact Check Explorer with 20 fresh rows as decoys. Pass ≥8 of 11 matched, ≤1 false match.
3. **Benchmark vs Newsflash MCP + LLM** on the same batch, only if Ethan OKs the free sign-up. Pass if ours beats it by ≥10 points at equal false flags.

**30-day paid validation, once Ethan picks this to launch as a coin (about A$106):** unlisted Chrome listing and a US$29 founding pass for 3 months. Pass ≥25 passes and ≥25% of installs seeing a stamp on 3+ days a week. Iterate at 10–24. Kill below 10, below 10% weekly use, or if ≥50% say "I just ask Grok/Larpcheck."

## Comparables
Tree News, 247 Terminal, ArcaneNews and PVP (old-news flags in paid terminals), Kronical (enterprise first-report detection), Larpcheck (hold-to-access verdict bot), Custom Timestamps for X (free post-age tool), pumpdata.fun (free tier plus x402 and Grok template distribution).

## Dropped this run (screen)
- **Polymarket insider and fresh-wallet spotter** (X bot 6c, a free three-rule bot): gate c. [PolyInsider](https://polyinsider.io/en) (free, Telegram bot), [PolyAlertHub](https://polyalerthub.com/features/fresh-wallet-tracker), [Presage](https://www.usepresage.com/), [Polytrack](https://polytrack.cash/) and an [open-source tracker](https://github.com/pselamy/polymarket-insider-tracker) already do it.
- **Paid pre-trade checks for agents over x402** ([AgentFeed](https://github.com/seekdaseek/agentfeed), Git bot run 17): gate c (AgentFeed, swap-gate, pumpdata).
- **StonkFun reward-history tracker:** gates b and c ([scout-stonk-intel](https://github.com/fuzzysniper/scout-stonk-intel) exists; StonkFun isn't pump.fun).
- **Revtrace standalone: abandoned** under Ethan's 8:14pm rule (Larpcheck now answers buyback/burn claims for free and notes creator-funded wallets). Only the who-paid line lives on inside Marshal's v1.1 list.

## Sourced facts vs estimates
**Sourced:** Project Bot's v3 review and labels; the v3 blind holdout; Larpcheckbot's last 25 replies (pulled 22:40 AWST via X public reads); this run's publish-time check (data/pubtime-check/); X bot's 22:00 digest (launchpad counts, Larpcheck rate, Pump Baby copies); Trench Bot run 17 (Kimchi −52%, REMUS, rug families); DefiLlama Tree; WhopScope 247; ExtScope and Chrome Web Store pages; competitor sites; ASIC RG 244.
**Estimates:** 247 run-rate, LLM and X API costs, market shares, subscriber curve, MRR, A$ conversion, and my I/U/Uq scores.

---

## Build brief for Claude Code

### Scope of the MVP (4 weeks)
A Chrome MV3 extension for x.com plus a small API that stamps market headlines with the earliest first-reported time of the event they describe, a LATE tag at 48h+, and a figure mismatch line when the source gives a different number. Out of scope for MVP: any true/false verdict, poster track records, account scores, perps trading, Telegram watchlists, coin dev checks.

### Features in build order
1. Feed archive: poll ~25 RSS feeds (CoinDesk, The Block, Decrypt, Cointelegraph, Blockworks, DL News, Bloomberg Crypto headlines where the feed allows, exchange announcement feeds for Binance, Coinbase, Kraken, OKX, Bybit, Hyperliquid, SEC/CFTC/BLS/Fed press RSS) every 2 minutes; store derived records only.
2. Time resolver: RSS `pubDate` → page `datePublished` / `article:published_time` cross-check → earliest across cluster.
3. Claim extractor (small LLM) and alias expansion.
4. Event index and two-stage judge with abstain.
5. API `/v1/stamp` with per-post cache.
6. Extension: on-click stamp (free) then automatic stamps for Pro.
7. Payments: Lemon Squeezy card; Solana Pay USDC; $TPLN hold check and burn verifier.
8. MCP tool and x402 endpoint.
9. Recycled-claim library (ClaimReview seed + disputes), behind a flag.
10. Dispute button that writes labelled rows.

### Architecture and stack
- Extension: TypeScript, MV3, content script reads only the visible post text, post ID and created time; sends them to the API; renders one line. No remote code, permissions limited to x.com and the API host.
- API: Node + Hono on a A$10/month VPS; Postgres (or Supabase free) with `pg_trgm` and `pgvector`; a worker for feed polling.
- LLM: one small, cheap model for extraction and stage 2 (JSON mode); log tokens and cost per call.
- Payments: Lemon Squeezy webhooks; Solana RPC (free tier) for USDC receipts, token balances and burn memos.

### Data sources, costs and terms
| Source | Use | Cost | Limits / terms |
|---|---|---|---|
| Outlet and exchange RSS | Event archive, times | Free | Store derived records (title, lede ≤300 chars, time, URL), link back; respect each feed's terms and robots |
| Article pages | Time cross-check | Free | One fetch per new article; some sites (The Block) block plain fetches, so RSS time is primary |
| X API reads | Pro auto-stamps of watchlist accounts | US$0.005/post (est. A$21/month) | X Developer Policy: event facts only, no per-account measurement or scores |
| Brave Search News | Lookups older than the archive | Free credit then paid | Transient use only, no storing result bodies |
| Google Fact Check Claim Search API | Recycled-claim seed | Free key | Check commercial-use terms before production |
| Hyperliquid info API, GeckoTerminal | Figure check for prices and pool moves | Free | Rate limits; cache 30s |
| Newsflash (optional) | Extra clustering | Free 1,000/day | Only with Ethan's OK for sign-up |

### Core logic (rules and pseudocode)
```
on post(text, post_id, post_time):
  if not is_market_headline(text): return null        # rules: BREAKING/JUST IN/🚨, a $ticker, a named org + money/action verb, or a figure
  claim = extract(text) -> {actor, action, object, figure, named_report, tense}
  if claim.tense == "future/speculative": return null
  keys = expand_aliases(claim)                          # entities.json, e.g. Ripple <-> XRP <-> Garlinghouse
  cands = search_archive(keys, window = post_time - 30d .. post_time)
          + recycled_library(keys) if pro_or_deep
  cands = top3(cands, by = entity_overlap + action_match + figure_match + trigram(title+lede))
  if no cands: return null
  verdict = judge_stage2(claim, cands)                  # same_event | later_development | same_topic | unsure
  if verdict != same_event: return null                 # abstain on everything else
  cluster = event_cluster(best_cand)                    # all archive items judged same event
  first = min(item.time for item in cluster if item.time_source in {rss, page})
  if first is null: return null
  age = post_time - first
  stamp = "first reported {first UTC} · {outlet of first} · {age}"
  if age >= 48h and not new_material(text, cluster): stamp += " · LATE"
  if claim.figure and source_figure(cluster) and differs(claim.figure, source_figure, tol=2%):
      stamp += " · source says {source_figure}, post says {claim.figure}"
  cache(post_id, stamp); return stamp
```
- `judge_stage2` prompt contract: input = the claim JSON and up to 3 candidates (title, lede, time); output JSON `{label, confidence, reason ≤20 words}`; show only if label = same_event and confidence ≥ 0.8. Log tokens and cost; if the running daily cost passes the cap, abstain.
- `new_material`: true if the post names a figure, actor or action absent from every cluster item.
- Never use the feed's ingest time, the post's own age, or a time without a source.

### UI and first-minute flow
Install → open x.com → click "stamp" on any market post (free) → one grey line appears in under 2 seconds, or a quiet "no match" tooltip. Pro: sign with a Solana wallet holding $TPLN or pay by card, pick up to 25 accounts, and stamps appear automatically. LATE is amber text, never red; nothing ever says "fake".

### Token integration steps
1. Before launch: build with $TPLN mint as a config value; test on devnet with a dummy mint.
2. Launch on pump.fun only after 25 paying users and the legal consult; mint and freeze authority off; ≤0.5 SOL labelled dev buy from a published wallet; pin the CA in the extension About page, site and X bio.
3. Hold check: wallet signs a nonce; API reads the SPL balance (RPC); tiers at fixed token amounts set at launch, re-read every 24h.
4. Burn verifier: user burns their own $TPLN with an SPL memo `tpln:<credit_id>`; API confirms the burn tx and credits the account; public page lists every burn with Solscan links.
5. Creator fees to a published wallet, bonus only; no code path converts card or USDC revenue into token buys.

### Acceptance tests (numeric pass lines)
- **AT-T1 stale catch:** on a fresh test set built by Claude Code, ≥75% of stale caught (the bots' light check, ≥7 of 10 stamps right on ~10 fresh headlines, is a feasibility gate only, not this test).
- **AT-T2 false LATE:** ≤3% of fresh posts tagged LATE; 0 stamps on same-day reposts tagged LATE.
- **AT-T3 time accuracy:** ≥80% of shown stamps within ±6h of the labelled first report; 100% of shown stamps cite a time source of RSS or page.
- **AT-T4 abstain:** on 50 non-market posts (memes, replies, opinion), ≤1 stamp shown.
- **AT-T5 entity swap:** the Garlinghouse-quote-moved-to-XRP case and 4 other alias cases match.
- **AT-T6 cost:** stage-2 mean cost ≤US$0.002 per check over 300 checks; daily cap enforced (abstains when hit).
- **AT-T7 latency:** p95 under 2.0s for a cold stamp, under 200ms cached.
- **AT-T8 figure check:** on 10 posts with a known wrong figure, ≥7 show the source figure; 0 figure lines on 20 posts with correct figures.
- **AT-T9 token:** devnet hold check and burn credit both work end to end; a burn without the memo credits nothing.
- **AT-T10 privacy and policy:** the extension sends only visible post text, ID and time; no per-account score is stored or shown anywhere.

## Changelog
- 24 Oct 2026, ~22:45 AWST: replaced the ≥12 stale / ≥30 fresh blind holdout (frozen labels, separate judge) with a ~10-headline light feasibility check (≥7 of 10) per Ethan's 11:28 rule; score now hinges on the "is this news old?" demand signal; kill line unchanged.
