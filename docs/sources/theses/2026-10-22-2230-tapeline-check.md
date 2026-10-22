# Tapeline Check: is this market headline real, who posted it first and right, and what is it moving?

*Idea bot thesis, Thu 22 Oct 2026, 22:30 AWST (Perth). Path: /workspace/idea-bot/theses/2026-10-22-2230-tapeline-check.md. **An evolution of Tapeline** (theses/2026-10-22-1630-tapeline.md, Project Bot 6/10, token fit 6/10), rebuilt as the read-only product Project Bot recommended. Every new gap this run failed the screen (see "Dropped this run"). This is the best-scored earlier thesis that passes Ethan's audience and token gates.*

## Executive summary
- **Problem.** "BREAKING" and "JUST IN" posts move crypto, AI-stock and pre-IPO perps within minutes, and many turn out to be unconfirmed or wrong. On X, 1,300 to 2,850 posts a day pair "BREAKING"/"JUST IN" with market words (X counts, 15–22 Oct). Traders say they got liquidated on fake headlines ([Benne1818_](https://x.com/Benne1818_/status/2103475842009440627): "Got liquidated on my AMD because of … fake news about Hormuz opening"; [student_charts](https://x.com/student_charts/status/2108538716100972788): "fake news … caused havoc in #AI trade"). Their checking tool today is typing "@grok is this true" under the post.
- **Product.** A Chrome extension that adds one line under any market-moving post on x.com: **confirmed / single-source / contradicted** (with primary-source links), the **poster's record on headlines** (for example "first and right on 31 of 40, later contradicted on 6", with links), and **live prices of what it moves** (Hyperliquid incl. trade.xyz pre-IPO and stock perps, Phoenix, Solana tokens). There's also a Telegram alert bot and a public headline scorecard. It's read-only: no trade buttons and no builder codes.
- **Who pays and how much.** Crypto-native traders who already pay for news speed. Free gets a 60-second delay and 5 deep checks a day. **Pro is US$29/month**: instant verdicts, 300 deep checks, watchlist alerts and full scorecards. **Desk is US$99/month**: verdict webhook or API plus 5 seats. Pay by card, by USDC, or by burning $TPLN.
- **Token's job ($TPLN on pump.fun).** It's the in-app currency for checks and access, and you only ever use your own tokens. You burn $TPLN from your own wallet per deep check or for a month of Pro (the Tree News model), or you **hold** a set amount for Pro limits (the KOLscan model). Mint authority off, Holder Rewards off, Tokenized Agent buybacks off. No payouts and no buybacks from revenue or creator fees. Launch only after 25 paying users.
- **Total cost vs A$1,000.** About **A$691 committed** (build, 4 months of running costs, a A$300 legal reserve, token launch and contingency), so about A$309 is left over. The US$299 DexScreener profile (~A$428) is paid only from revenue.
- **Path to the first US$10k/month.** 345 Pro subscribers, or about 250 Pro plus 15 Desk. **Base case by month 12 (estimate): US$3–6k MRR.** The 2026 money is real: **Tree News users spent US$61,347 in the last 30 days and US$1.05M in the last year on subscriptions, burned on-chain** ([DefiLlama](https://defillama.com/protocol/tree-news)). 247 Terminal shows **181 members at US$99/month on Whop** ([WhopScope](https://whopscope.com/w/247terminal)).
- **Why now, and the edge.** AI and pre-IPO narratives now trade 24/7 as perps (trade.xyz did US$3.39B in 24h on 22 Oct per [OpenChainBench](https://openchainbench.com/hyperliquid)). Pump.fun anger is at a day high, so "verified numbers" is the trench story (X bot). Incumbents sell **speed** (Tree, 247, Proliquid, Reflex) or **coin/KOL trust** (fable, UNMSK, OnlyKOLs). None puts a **headline verdict plus the poster's headline record** on the X post itself. The edge is the scorecard history, which can't be cloned in a weekend.
- **Main risk and first move.** Traders may just ask Grok for free, and they may pay for speed but not for truth. Also, X's Developer Policy bars services that "measure, analyze, or attempt to identify … content which violate X policies" without X's written permission ([policy](https://developer.x.com/en/developer-terms/policy)), so the public scorecard has to stick to off-X facts, and X's OK should be sought before it goes public. **First move this week:** a private 30-day backfill of 40 headline accounts (~US$15 of X API reads), hand-label 100 headlines, and measure how often market headlines are later contradicted and whether markets moved.
- **Verdict: test, about 40% confidence.** The money (Tree News, on-chain) and the audience are proven, and the legal blocker is gone because it's read-only. Grok as a free substitute and willingness to pay for accuracy over speed are unproven.

## Problem and user (sourced)
**User.** A Solana or Hyperliquid trader in Ethan's audience: trades memecoins on Axiom or GMGN, holds USDC, and increasingly trades "the story" through 24/7 perps (pre-IPO ANTHROPIC/OPENAI, NVDA, IREN, oil). They live on X and react to headline accounts within seconds.

**What happens now.**
- **Headline flow is large and noisy.** 17,134 posts in 7 days matched `("BREAKING" OR "JUST IN")` plus a market keyword (bitcoin, crypto, solana, etf, hack, exploit, anthropic, openai, nvidia), excluding replies and reposts. That's 1,303 to 2,846 a day (X recent counts, 15–22 Oct 2026 UTC). This is a phrase count, not unique stories.
- **Examples from the last month of headlines that were unconfirmed or contested at posting:** "Ledger users reportedly hit by $86M wallet-draining attack … a Ledger-wide exploit has not been" confirmed ([AlphaWireHQ](https://x.com/AlphaWireHQ/status/2108564811051102433), 27k followers). "Russia's government just announced it will license its 1st bitcoin and crypto exchanges … could be confirmed within days" (timing unconfirmed in the post itself; [pete_rizzo_](https://x.com/pete_rizzo_/status/2103817108715106340), 222k followers, 938 likes). Kimchi's "$40M on $TRUMP" was cut to about $6M by Bubblemaps (X bot 8pm and 10pm digests). On 18 Oct an unconfirmed "Anthropic deal" post sent the IREN perp from about $26 to $44 and back (Tapeline thesis sources).
- **Traders lose money on them:** "Got liquidated on my AMD because of … fake news about Hormuz opening" ([Benne1818_](https://x.com/Benne1818_/status/2103475842009440627)). "Turned out this was fake news or mis-reported … Stocks were dumped like no tomorrow" ([student_charts](https://x.com/student_charts/status/2108538716100972788)). "Crazy that fake news moves oil 4%" ([kahahj9w422](https://x.com/kahahj9w422/status/2112568690965406116)).
- **Their check today is Grok.** 61 posts in 7 days contain the exact phrase "@grok is this true" plus a crypto or market word (X counts, 15–22 Oct). That's a narrow, unambiguous phrase, so it undercounts the habit. It does show the behaviour exists, and that the answer arrives late and isn't attached to a track record.

**Why it's painful for this audience.** They size big and fast. A single fake headline that triggers a 2–10% wick can liquidate a 10x position. A US$29/month check is small next to one avoided liquidation, but that's an argument, not evidence (see Kill or confirm).

## Evidence of money
**Verified comps (on-chain or platform-reported):**
- **Tree News (Tree of Alpha's news service) on DefiLlama:** US$61,347 of subscription spend in the last 30 days, US$14,324 in 7 days, US$1,050,115 in 1 year and US$3,542,639 all-time. Subscribers pay by burning TREE, or with USDC that is used to buy and burn ([DefiLlama API, fetched 22 Oct 22:20 AWST](https://defillama.com/protocol/tree-news); methodology: "All tokens burned by users for subscriptions"). Plans are Sprout at 500 credits/month and Sapling at 2,500 ([Tree docs](https://docs.treeofalpha.com/welcome/how-to-subscribe)). This is the closest verified comp: crypto traders paying for headlines, **through a token, on-chain**. Note that only the "users burn their own TREE" half is copyable. The USDC buy-and-burn half is a revenue buyback, which is over Ethan's ASIC line.
- **247 Terminal:** 181 members at US$99/month on Whop, 4.93 stars from 14 reviews ([WhopScope](https://whopscope.com/w/247terminal)). The site lists US$99 then US$199, and a US$499 public-access tier also appears (Project Bot review; [Whop](https://whop.com/247terminal/publicaccess/)). Estimated run-rate is about US$18k/month if all members pay US$99. That's an estimate, since Whop member counts may include trials.
- **Hyperliquid frontends** earn verifiable builder fees: US$3.80M over 30 days across 86 builders and 125.4K users ([OpenChainBench](https://openchainbench.com/hyperliquid), 22 Oct). That's context for audience size only; this product takes no trading fees.

**Competitor pricing (public):** Tree Sprout/Sapling at 500/2,500 credits a month (Project Bot cited US$500/US$2,500). Newsflash corroboration API at US$29/month premium ([docs](https://newsflash.sh/docs)). UNMSK Pro at US$16/month ([unmsk.org](https://www.unmsk.org/)). KOLscan Premium at 0.05 ETH/month, or hold 1M $KOLS ([kolscan.app](https://www.kolscan.app/subscription)). Proliquid is free (Project Bot review).

**Teammate signals that corroborate:**
- **X bot (10pm):** "verified numbers" is the trench story (Kimchi $40M→$6M), with pump.fun anger at a day high. Checker bots (Larpcheckbot, @llama) are now the default reply under product coins, and Larpcheck's own token panel is called out as "lying about the fees… 61% bots", so traders distrust unverified verdicts too.
- **Trench Bot (22:12–22:40 run):** survivors had "an outside trigger with a named human" at minute zero (PHP on the PHP RCE news, CHOO with Business Insider). News is the trigger, so knowing whether it's real is the edge. The brand name-bait template reuses real brand links to look official.
- **Telegram tracker:** the "verifiable claims (PnL, revenue, creator fees)" thread is gaining support across bots; free incumbents are strong for coins. Headlines are the uncovered side.
- **Project Bot (Tapeline review):** "the rumour verdict is the product; trading is a later add-on".

## Market sizing (bottom-up; assumptions labelled)
- **Proven spend pool (sourced plus estimate):** Tree News at about US$61k a month, plus 247 Terminal at about US$18k a month (estimate), is **about US$80k a month** that crypto traders already pay for headline tools in just two products.
- **Reachable traders (sourced):** Hyperliquid frontends reached 125.4K users in 30 days (OpenChainBench). Solana terminal users are far more: Axiom alone took US$202M in fees on 353M swaps from Oct 2025 to Aug 2026 ([Bitquery](https://bitquery.io/investigations/solana-jito-tips-trading-app-fees)).
- **Assumption A:** 0.25%–0.5% of Hyperliquid's 125.4K monthly users pay US$29, which is **310–630 payers, or US$9.1k–18.2k MRR**.
- **Assumption B:** Desk/API at US$99 for 10–20 small funds, callers and bot builders adds **US$1–2k**.
- **Ceiling sense-check:** taking 10–20% of Tree News's monthly spend is US$6–12k MRR. US$10k MRR is plausible but needs top-quartile execution, so the base case is US$3–6k (estimate).

## Competitive teardown
| Competitor | What it does | Pricing | Revenue / traction | Gap it leaves |
|---|---|---|---|---|
| [Tree of Alpha / Tree News](https://www.treeofalpha.com/) | Fastest news aggregator plus terminal, 1,150+ sources | 500 / 2,500 credits a month (TREE burned) | **US$61.3k/30d, US$3.54M all-time (DefiLlama)** | Speed, not truth. A separate app with no verdict or poster record, priced for whales |
| [247 Terminal](https://247terminal.com/) | Sub-500ms headlines, one-click CEX/Hyperliquid trades | US$99–199 (to US$499) | 181 Whop members | Speed plus execution. No source check, no on-X layer |
| [Proliquid](https://www.proliquid.xyz/) | Free terminal, AI importance score, matched markets | Free (DEX fees) | Claims US$1B+ yearly volume | No verdict, no poster record, separate app |
| [Reflex](https://reflex.trade/) | Hyperliquid news feed, AI "Sentinel" scores, Telegram /long /short | Waitlist | Not live | Sentiment and execution, not verification |
| [Newsflash](https://newsflash.sh/docs) | Clusters outlet articles into events with a corroboration count, API/MCP | Free, US$29/mo premium | Unknown | Outlets only (not X posters), no X overlay, no market mapping. It could be a supplier |
| Grok (@grok replies, "breaking news checker" prompts) | Ad-hoc "is this true?" answers | Free | Built into X | Slow (ask per post), no record per poster, can repeat unverified claims (Askwatch review). **The main substitute** |
| [fable](https://fable.market/) | Free X extension: rug/shill labels, call records, launch forensics, live coin charts | Free | Open source | Coins and KOL calls, not news headlines |
| [UNMSK](https://www.unmsk.org/) / [Ethos Everywhere](https://chromewebstore.google.com/detail/ethos-everywhere/jblacjfeljfigeglloiclnoehlhnmgne) / [TruthLayer](https://github.com/miraekims/Truthlayer) | Token risk and KOL wallets on X; credibility scores; holder checks | Free / US$16 | Small | Coin or account trust, not headline truth |
| [OnlyKOLs](https://onlykols.io/), [Mihenk](https://mihenkai.com/), VOXCH, Santiment | Score KOLs' **price calls** | Early access / B2B | Small | Price-call accuracy, not news accuracy |
| Larpcheck ([larpcheck.app](https://larpcheck.app/)) | Reply bot verdicts on coin posts | Free + $LARPCHECK | Default checker under coin posts (X bot) | Coins only, and its own token panel is disputed |

**Why incumbents won't build it soon.** Tree and 247 sell latency to people who trade the first print. Telling those users a headline is single-source slows the click they're paying for. Proliquid and Reflex monetise trade fees, and a "contradicted" label kills trades. fable and UNMSK are coin-risk tools whose data model is wallets, not newswires. Grok could do it, but X has no incentive to publish "this poster is often wrong" scores about its own high-engagement accounts. **Honest caveat:** any of them could ship a verdict badge in weeks. The moat is the scorecard history and being on the post, not the model.

## Product and UX
**First minute.** Install the extension and open x.com. Under a "🚨 BREAKING: [exchange] confirms $XXM hack" post a grey line appears (illustrative mock-up, not real data): `SINGLE-SOURCE · no official exchange post or blog yet · poster: first-and-right 9/31, contradicted 7/31 · [exchange token] −4.1% 5m · BTC −0.3%`. Tap it for the Backstory card: the primary-source search done (official X accounts, company blog/RSS, exchange announcement API, SEC EDGAR, top newswires via RSS), what was found, and the poster's last 10 market headlines with outcomes. When the official account confirms, the line turns green and a Telegram ping fires for watchlisted markets.

**MVP stack (all free tiers where possible).**
- Chrome MV3 extension in TypeScript. It reads only the post the user is viewing (text, ID, handle) and sends a hash and ID to the backend.
- Next.js on Vercel plus Supabase (Postgres) for verdicts, poster records and auth (wallet or email).
- Worker on a A$10/month VPS:
  - (1) a claim extractor (small LLM call, cached per post ID);
  - (2) a primary-source matcher: allow-list of ~300 official X accounts and domains, company and exchange RSS, Binance/Coinbase/OKX/Upbit announcement endpoints, SEC EDGAR full-text search and newswire RSS; optionally Newsflash as a corroboration feed;
  - (3) a market mapper: entity-to-ticker table for Hyperliquid (info API incl. HIP-3 dexes), Phoenix markets and Solana tokens via DexScreener;
  - (4) an outcome job at T+1h and T+24h that sets confirmed, contradicted or still single-source and records the price move.
- Telegram bot (grammY), USDC via Solana Pay to a public wallet, card via Lemon Squeezy, and $TPLN burns verified by reading the user's signed burn transaction.

**Week-by-week (solo, ~20–25 h/week).**
1. Backfill and labelling tool: 40 headline accounts, 30 days, hand-label 100, plus the outcome job. This is also the kill test (below).
2. Primary-source matcher plus entity→market mapper, and the verdict API with cache.
3. Chrome extension strip and Backstory card, free/Pro gating and payments, plus the Telegram bot.
4. Public scorecard pages (built from IDs and embeds), polish and Chrome Web Store submission (unlisted until Ethan OKs public listing).

**Advanced parts.** Claim-to-entity resolution across tickers and pre-IPO names. Point-in-time scoring ("first" means the earliest post among poster accounts before the primary source). An outcome model that separates "contradicted" from "never confirmed". Latency: aim for a verdict within 15s of a new post for watchlisted accounts.

**What's hard.** Getting verdicts right on ambiguous stories (partial confirmations, "sources say"). Avoiding defamatory labels. Coverage of non-English primary sources (Upbit, Korean and Chinese outlets).

**What's clonable in a weekend.** The strip UI plus an LLM "is this true" call, which is basically fable plus a Grok prompt. **Not clonable:** months of time-stamped poster records with outcomes, and the maintained official-source allow-list.

## Token design (pump.fun)
- **Job (product use only).** (1) **Burn per use:** non-Pro users burn a fixed $TPLN amount from their own wallet per deep check, priced at about US$0.25 at launch and re-pegged monthly (The Codex pattern). (2) **Burn for a subscription:** a month of Pro can be paid by burning $TPLN worth US$29 (the Tree News pattern, which is verified at US$61k/30d). (3) **Hold for access:** wallets holding a set amount get Pro limits while they hold, verified by wallet signature (the KOLscan pattern: hold 1M $KOLS). Card and USDC payments stay available and are never converted into token buys.
- **Launch plan.** pump.fun only (Ethan's rule; Trench Bot and X bot: no meta shift, 11 of 13 legit or risky coins with real liquidity launched on pump.fun). Launch after **25 paying users** and the legal consult, at a product-reveal post from the official X account with a working extension link. Plan a second beat 1–3 hours later: publish the first public scorecard (Trench Bot: survivors had a second wave). SOL pair. **Mint and freeze authority confirmed revoked on-chain** before announcing. A **small labelled dev buy** (≤0.5 SOL, wallet published) and **no bundles**, no snipers and no caller packages (Trench Bot: LASTCALL and Codex callers were flagged within 30 minutes). **Holder Rewards off and Tokenized Agent buybacks off.** The CA is posted from the official X account and pinned on the site. Reserve the $TPLN ticker early, because strangers launch coins about products (growth bot lesson, 22 Oct). $TAPE is taken on Solana (TAPE ~US$55k FDV; "Launch Tape"), so the ticker changes to $TPLN, which had no DexScreener match on 22 Oct.
- **On-chain fee flow and verification.** Every in-app burn is the user's own SPL burn transaction carrying a memo with the check ID. A public page lists burns from the indexer and links them to Solscan. Creator fees (0.30% on the curve, 0.30–0.95% on PumpSwap at small caps per [pump.fun fees](https://pump.fun/docs/fees)) go to a published wallet and are treated as **bonus income only**. They're never used for buybacks or burns. The repo is public from day one (extension, verdict rules, burn verifier).
- **Comparable tokenised products (organic vs shilled).**
  - **Tree News (TREE):** the only verified organic spend found (DefiLlama burns).
  - **KOLscan ($KOLS hold-to-access):** live paid tiers.
  - **The Codex ($CODEX):** quota plus burn per question. Self-reported US$970 creator fees in a day. Trench Bot found top-10 holders at ~42%, paid callers pushing it, and no burn visible yet.
  - **Larpcheck ($LARPCHECK):** public "61% bots" allegations (X bot).
  - **CrawlHive:** real use but ~US$20k mcap (Trench Bot), so usage doesn't drive price.
  - **Lesson:** don't project token income. Subscriptions pay the bills.
- **Legal line.** No holder payouts, no revenue- or fee-funded buybacks or burns, and no "profit", "yield" or "number go up" language. The token is a prepaid usage and access credit. ASIC: INFO 225 treats some digital assets as financial products. A token with a pure consumptive use and no profit expectation is lower risk, but this is not legal advice, so it gets covered in the fixed-fee consult. US: avoid marketing to US persons as an investment (Howey turns on expectation of profits from others' efforts). Verdicts are factual (sourced or not sourced), never "long/short" calls, which keeps the product away from "financial product advice" and AFSL triggers.

## Budget and founder load (A$; US$1 ≈ A$1.43; estimates unless sourced)
| Item | One-off | Monthly | 4-month total |
|---|---|---|---|
| Domain | 25 | | 25 |
| Chrome Web Store fee (US$5) | 8 | | 8 |
| VPS for worker and Telegram bot | | 10 | 40 |
| LLM inference (claim extraction and verdicts, cached per post; ~300 unique checks/day at ~US$0.002) | | 20 | 80 |
| X API pay-per-use (US$0.005 per post read, [pricing](https://x-preview.mintlify.app/x-api/getting-started/pricing)): ~3,000-post backfill US$15, then ~100 spot reads/day | 21 | 21 | 105 |
| Vercel, Supabase, Hyperliquid/Phoenix/DexScreener APIs, RSS, EDGAR | 0 | 0 | 0 |
| Fixed-fee legal consult (defamation in scorecards, general-advice line, token as usage credit); get a quote first | 300 | | 300 |
| Token launch: network/rent ~A$5 plus labelled dev buy ≤0.5 SOL (~US$55 at TrenchBay's US$109/SOL reference) | 83 | | 83 |
| Contingency | 50 | | 50 |
| **Committed total** | | | **A$691** |
| DexScreener profile US$299 (~A$428): **only from revenue**, after ≥US$500 collected | | | (0 from budget) |

Runway: about A$51/month of running costs, with ~A$309 unallocated. That's about 6 more months even with zero revenue, or the DexScreener profile if revenue lags. **Founder load:** 20–25 h/week for 4 weeks of build, then ~10 h/week. Support is ~2–3 h/week (verdict disputes, payments). Disputes are the main support cost, so each verdict card has a "dispute with source" button that feeds the labelling queue.

## Business model and unit economics (estimates marked)
- **Pricing benchmarked:** Pro at US$29 sits under 247 (US$99) and far under Tree's paid tiers. It's above UNMSK (US$16) because verdicts cost more to run than holder lookups. Desk at US$99 matches 247's entry price for API and seats.
- **Cost to serve (estimate):** verdicts are computed once per post and shared by every user who sees it, so marginal cost per user is about US$0.30–0.80/month (LLM, X spot reads, DB). Card fees ~5% + US$0.50 per charge; USDC and token payments ~US$0.001.
- **Gross margin:** ~90% on Pro (estimate).
- **Channels (no ads, no sales calls):**
  - Reply under viral wrong headlines with the strip screenshot, from Ethan's account and only with his OK.
  - A public weekly "Headline scorecard" thread (which accounts were first and right).
  - A free Telegram channel of verdict flips (single-source → confirmed or contradicted).
  - A 25% revenue-share referral, as 247 does on Whop.
  - Listing in Hyperliquid and Solana tool directories.
- **Payback:** acquisition cash cost ≈ US$0, so payback happens in month one. Time cost is the constraint.

## Go-to-market for a solo founder
**First 10 users.** (1) People already asking "@grok is this true" under market headlines (61 a week with crypto words; reply with the verdict card, with Ethan's OK). (2) Traders posting about ANTHROPIC/IREN/NVDA perps on Phoenix and trade.xyz (Tapeline thesis handles). (3) Hyperliquid and Solana trader Telegram groups. (4) Small callers and funds who'd use the Desk webhook to avoid reposting fakes.

**60-day plan.**
- Days 1–10: private backfill and kill test.
- Days 11–25: build the extension and Telegram bot.
- Days 26–30: unlisted beta to 30 hand-picked traders.
- Days 31–45: public listing and founding pass (US$29 for 3 months) after Ethan's OK.
- Days 46–60: weekly scorecard threads, referral programme, Desk tier, and a decision on token launch at 25+ payers.

**Path to US$10k/month.** ~100 Pro by month 6 through scorecard virality. Then the Desk API for callers and bots, and then coverage of Korean and Chinese primary sources, where many fake "Upbit listing" style headlines start. Reaching 345 Pro-equivalents by month 12 is the stretch case.

## Financial snapshot (12 months; all estimates)
| Month | Pro subs (base) | Desk | MRR base (US$) | MRR stretch (US$) | Running cost (US$) |
|---|---|---|---|---|---|
| 1–2 | 0 | 0 | 0 | 0 | ~35 |
| 3 | 25 | 0 | 725 | 1,200 | ~40 |
| 6 | 70 | 3 | 2,330 | 4,500 | ~60 |
| 9 | 110 | 6 | 3,780 | 7,000 | ~80 |
| 12 | 150 | 8 | 5,140 | 10,000 | ~100 |
Assumptions: ~8% monthly churn. Stretch assumes one or two scorecard threads go viral and the Desk tier finds 15+ buyers. Token creator fees are excluded (bonus only). Cumulative 12-month revenue in the base case is ~US$30k.

## Defensibility
- **The poster scorecard:** time-stamped, point-in-time records of who was first and right, which can't be backfilled later by a rival once posts are deleted or edited (only IDs and verdicts are kept, per X's display rules).
- **A maintained official-source allow-list** and an entity→market map covering HIP-3 and Phoenix listings.
- **Distribution on the post itself, plus the habit:** the line is there before you think to ask Grok.
- **Weak spots:** the UI and an LLM check are copyable, and X or Grok could add native context.

## Risks (each with mitigation and a cheap test)
- **Market: traders pay for speed, not truth.** Mitigation: a free tier and speed-neutral verdicts (the line never blocks the click). Cheap test: the founding pass (below).
- **Substitute: Grok is free.** Mitigation: be instant, sit on every post, and carry the poster record Grok lacks. Test: ask 30 beta users "would you still ask Grok?"; kill if ≥50% say Grok is enough.
- **Technical: verdict accuracy.** Mitigation: three labels only, sources always shown, a dispute button and conservative defaults ("single-source" until proven). Test: ≥85% agreement with hand labels on 100 headlines.
- **Platform: X policy.** The Developer Policy bars services that "measure, analyze, or attempt to identify behaviors or content which violate X policies without express written permission", and it requires removing displayed content that's no longer available on X ([policy](https://developer.x.com/en/developer-terms/policy)). Mitigation: verdicts come only from off-X primary sources; no "scam/bot/spam" labels; scorecards show post IDs and X embeds only; deleted posts are removed from display. Apply for X's written OK before the public scorecard. The extension reads only the page the user is viewing, which fable, UNMSK and Merit already do (tolerated, not permitted). Test: email X developer support (needs Ethan's OK) before day 30.
- **Regulatory: defamation and advice.** Mitigation: factual counts with links, no adjectives about people, a right of reply, and no buy/sell calls. Test: the fixed-fee legal consult (A$300 reserve).
- **Token: launch looks like a casino coin during peak pump.fun backlash (X bot).** Mitigation: launch only with a working product and paying users, burn-for-use only, dev buy labelled, no callers. Test: post-launch holder spread (Trench Bot's check: largest non-pool wallet under ~5% at 1h; pool share not ≥85% after a few hours).

## Kill or confirm (30 days, about A$150 of spend, well under budget)
- **Phase A, days 1–10, private, about A$60** (X API backfill ~US$15, LLM ~A$15, VPS A$10). Backfill 30 days of "BREAKING"/"JUST IN" posts from 40 high-reach crypto and AI headline accounts (~3,000 posts) and hand-label 100.
  - **Pass**, all three needed:
    - ≥8% of market headlines are later contradicted or still single-source at 24h.
    - ≥10 of those coincide with a ≥2% move in a mapped market within 1h.
    - The auto-verdict agrees with hand labels on ≥85% of the 100.
  - **Kill**, either one: <4% of headlines are contradicted or unconfirmed, or agreement is <75%.
- **Phase B, days 11–30, about A$90.** Needs Ethan's OK for the Chrome Web Store listing, posting and any outreach. Founding pass at US$29 for 3 months of Pro, paid by USDC or card.
  - **Pass:** ≥25 passes (~US$725) and ≥25% of installs viewing a strip on 3+ days a week.
  - **Iterate once (14 days):** 10–24 passes.
  - **Kill:** <10 passes, or <10% weekly use, or ≥50% of beta users saying "I just ask Grok".
- **No token, no DexScreener profile and no legal spend before Phase B passes.**

## Comparables
- **Tree News:** headlines for traders, paid by burning a token. US$61.3k/30d and US$1.05M/1y on-chain (DefiLlama).
- **247 Terminal:** 181 members × US$99 on Whop (WhopScope).
- **KOLscan:** hold 1M $KOLS or pay 0.05 ETH/month for premium.
- **UNMSK:** free X/terminal extension, Pro at US$16/month.
- **fable:** free open-source X overlay. Shows the UX is accepted by crypto X.
- **Newsflash:** US$29/month corroboration API, a possible supplier.
- **The Codex:** burn-per-question pattern. Self-reported, unproven.

## Dropped this run (and why)
- **Woulda (English-sentence strategy backtest over pump.fun launches; tracker idea #51).** Failed gate c, crowded: [PumpPill strategy tester](https://www.pumppill.org/strategy-tester), [Pump Lab](https://pumplab.lol/), [three.ws Strategy Lab](https://three.ws/strategy-lab) and [Launch Tape](https://launchtape.io/test) (US$10/day, US$49/month data). hkuds/vibe-trading (36k stars) covers general markets.
- **Execution-fee audit ("what did my fees buy" on Axiom/Photon).** Failed gates e and f (money and repeat use). [Bitquery's investigation](https://bitquery.io/investigations/solana-jito-tips-trading-app-fees) is free, SolJournal records every fee for free, TrenchBay charges no commission, and X demand is thin (22 posts in 7 days matching fee-audit terms). It's a one-off curiosity, not a subscription.
- **KOL fact-check / paid-promotion detector (Askwatch's suggested evolution).** Failed gate c: [UNMSK](https://www.unmsk.org/) (US$16), [OnlyKOLs](https://onlykols.io/), [Mihenk](https://mihenkai.com/), [KOLscan](https://www.kolscan.app/subscription), [KOLBOT](https://www.kolbot.io/project-intel-service), [fable](https://fable.market/), VOXCH and Santiment. Tapeline Check takes only the uncovered slice: headline accuracy, not price calls.
- **Unclaimed creator-fee alerts for builders whose work gets a stranger coin (K9ENTROPY / Monero Cat pattern).** Failed gate c: [ClaimScan](https://claimscan.tech/) (6 launchpads, X-handle lookup), [Prysm](https://docs.prysmbot.com/alerts/fee-claims-and-burns/) /unclaimed and PumpKit social fees, plus pump.fun's native GitHub claim.
- **Polymarket resolution-risk checker.** Failed gate c: [SignalBoard](https://www.signalboard.live/), [PolymarketScan](https://polymarketscan.org/rules-arb), [SettleRisk](https://settlerisk.com/demo), [Scanverity](https://scanverity.com/en/try) and [Do Not Act](https://donotact.com/).
- **Solana landing-service benchmark** (Bitquery: app users tipped landing services 6.4x what they tipped Jito). Failed gate c: [OpenChainBench tx-landing benchmark](https://openchainbench.com/benchmarks/solana-tx-landing), [Helius benchmarks](https://www.helius.dev/benchmarks/sends), bloXroute tests and Nozomi's dashboard.
- **Brand name-bait coin warning (Trench Bot's 500–1,100 SOL-funded template).** Failed gates c and e: UNMSK, fable, and Axiom/GMGN holder and fresh-wallet flags. Mint Seal's 20-launch test showed public data usually resolves it, and no payer was found.
- **Agent spend caps / per-agent key proxy (X bot's repeated pain).** Failed gate a (buyers are mainly developers, not crypto traders) and gate c (Coldstar, Loyal, Crossmint, Seal, purser; Git bot retired it at 22:05).
- **Creator-reward autopilot (Git bot's gap).** Still dropped: crowded (Latrine, ReFi, FROZEN, fees.u.cash, pump.fun native sharing), and fee-funded buybacks or burns are over the ASIC line.
- **Other theses passing the audience and token gates but scoring lower:** Revtrace (5/10, payer checks exist for x402), Askwatch (5/10, X policy and thin feeds), Mint Seal (killed by its 20-launch test).

## Sourced facts versus estimates
Sourced:
- DefiLlama Tree News figures, WhopScope 247 members, OpenChainBench Hyperliquid figures, the Bitquery fee study and X API pricing.
- X recent counts (15–22 Oct UTC) and quoted X posts.
- Competitor pages and pricing, X Developer Policy text, and pump.fun fee docs.

Estimates:
- 247 run-rate, market shares, subscriber curve, churn, LLM and VPS costs, the A$ conversion (~1.43) and the SOL price reference (TrenchBay's 10 Oct US$109).
- Every MRR figure in the projections.

## Addendum (22:45 AWST, from Trench Bot and X bot)
- Paid coin promotion uses the same "JUST IN" / "BREAKING" format as real news. Example: LASTCALL's 125k-follower "JUST IN" post got 102 reposts, mostly from 0-follower accounts created that week; the same account ran one for $CODEX an hour later.
- Product change: add a fourth label, "paid promo", next to confirmed / single-source / contradicted. Signals: repost burst from fresh 0-follower accounts, identical gain templates across accounts, caller hashtags such as #bbvipks4 (a paid-attention flag, not a rug verdict by itself), and the poster's history of promos.
- Data: Trench Bot's rug and shill-check records (/workspace/shared-data/trench-bot/coins.jsonl, /workspace/shared-data/x-bot/signals.jsonl) give free labelled examples for the poster track record.
- Competitors (from X bot, 22:45): Larpcheckbot and DefiLlama's @llama already post verdicts under crypto posts and are the default check for coin and protocol claims. They don't cover news headlines yet, but they are the closest substitute after Grok and could expand into headlines.
- Backfill: X bot will run the 30-day pull with its built-in X reads at no cost, so the first move drops the ~US$15 of API reads. X bot picks the 40 accounts that post the most "BREAKING"/"JUST IN" headlines with market words, and the posts go to /workspace/shared-data/x-bot/.
