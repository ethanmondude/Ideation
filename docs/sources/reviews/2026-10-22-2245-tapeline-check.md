# Review: Tapeline Check (is this market headline real, who posted it first and right, and what is it moving?)

*Project Bot review · 22 Oct 2026, 10:45pm AWST (Perth time) · thesis: /workspace/idea-bot/theses/2026-10-22-2230-tapeline-check.md (idea bot, 10:30pm AWST, including its 10:45pm addendum) · compared with: 2026-10-22-1645-tapeline.md · lens: solo, bootstrapped, ~A$1,000 total, Ethan builds full-stack web apps, audience = crypto-native tech bros, own token required (pump.fun only) · room notes: inputs-2026-10-22-2230.md (incl. the 10:40pm additions) · read first: /workspace/shared-data/growth-bot/lessons.jsonl*

## Verdict
- **Score: 5.5/10. Thesis (narrow: test before building). Token fit 6/10. Passes Ethan's rules gate** (paying buyer = crypto-native traders; token fit 6 ≥ 5, with a real pump.fun job: users burn or hold their own $TPLN for checks and Pro). Ranked 3rd of 9 overall, level with Mint Seal and Breach Kit (5.5), behind Ledgerport (6.5, outside Ethan's rules) and the original Tapeline (6), which this replaces. **1st of the theses that pass the rules gate** (ahead of Revtrace 5).
- **Biggest correction: the "nobody checks the post itself" gap is smaller than the thesis says.** [Larpcheck](https://larpcheck.app/how) is not coins-only. Tag @Larpcheckbot under any X post and it checks "the claim in that one post, checked against its sources", with a verdict and score. Verdict replies are free, and Pro is unlocked by holding a little $LARPCHECK (the same hold-to-access model as $TPLN). [Basis Desk Verify](https://basisdesk.news/news/basis-desk-verify-fact-check-crypto-news-chrome-extension) (free Chrome extension, 7 Oct 2026) already labels crypto-news claims against primary sources with live prices, and [SpyGlass](https://devpost.com/software/spyglass) (hackathon project) puts an inline verdict on every tweet. What's still open: **automatic** verdicts with no tagging, the **poster's headline record**, and **what the headline moved** (Hyperliquid/trade.xyz perps). That's the product.
- **Biggest money gap:** nobody is shown paying for headline *accuracy*. The money next door (Tree News, 247 Terminal) is for *speed*, and Tree's on-chain figure is partly a USDC buy-and-burn (see fact-check). **New platform risk from tonight's addendum:** the "paid promo" label (0-follower repost bursts, copy-paste gain text, caller hashtags) is exactly what X's Developer Policy bars without written permission: services that "measure, analyze, or attempt to identify behaviors or content which violate X policies", including "spam or security on X" ([policy](https://developer.x.com/en/developer-terms/policy)). Keep "paid promo" out of the public product until X says yes in writing; use it only as a private signal in the backfill.

## What changed since the 4:45pm Tapeline review
| | Tapeline (4:45pm) | Tapeline Check (10:30pm) |
|---|---|---|
| Product | Headline strip + later Phoenix "Trade" button via Flight builder fees | Read-only verdict line, poster headline record, live prices; Telegram bot; public scorecard. No trade buttons |
| Revenue | Builder fees (likely needs an AFSL) + subscription | Subscription only (US$29 Pro, US$99 Desk), card/USDC/own-token burn |
| Legal blocker | Main blocker (ASIC INFO 225: "arranging" derivatives) | **Mostly gone.** Factual information needs no AFSL ([RG 244.24–25](https://download.asic.gov.au/media/tkqi11il/rg244-published-13-december-2012-20211208.pdf)), as long as it doesn't imply a buy/sell call (RG 36.24). A defamation risk remains for poster records and labels |
| Token | $TAPE (taken) | $TPLN: burn own tokens per check or for a month of Pro, or hold for Pro. Holder Rewards and Tokenized Agent off |
| Budget | ~A$560 test incl. A$500 legal | A$691 committed over 4 months; **~A$670 after X bot does the backfill free** |
| Competitors found | Proliquid, 247, Reflex, Tree, Merit | + Larpcheck post checks, Basis Desk Verify, SpyGlass, @llama, Newsflash, fable, UNMSK |
| Score | 6 (capped by legal) | 5.5 (legal cap lifted; differentiation and X-policy risk worse) |

## 1. Fact-check
**Verified (opened or re-run today, 10:35–10:45pm AWST)**
- **Tree News on DefiLlama:** US$61,347 (30d), US$14,324 (7d), US$1,050,115 (1y), US$3,542,639 all-time, US$2,278 (24h). All match the thesis ([DefiLlama API](https://api.llama.fi/summary/fees/tree-news)). **But the "users burn their own tokens" reading is only half right.** DefiLlama's own methodology says fees include "direct token burns, and USDC used to buy and burn", and its [adapter](https://github.com/DefiLlama/dimension-adapters/blob/master/fees/tree-news/index.ts) just sums every TREE transfer to the burn address under 100k tokens (to drop treasury burns). It can't tell a user's own burn from a USDC buy-and-burn. So US$61k a month is real crypto-trader spend on headlines, but only an unknown share of it is the copyable "burn your own tokens" pattern. DefiLlama also books it as "HoldersRevenue … benefitting all holders" — the framing Ethan's ASIC line avoids.
- **247 Terminal:** 181 members, US$99/month, 4.93 stars from 14 reviews, launched ~1 year ago ([WhopScope](https://whopscope.com/w/247terminal)). Correct. The ~US$18k/month run-rate is still an estimate (members may include trials or other tiers).
- **trade.xyz:** US$3.47B 24h volume, 115 markets, US$3.91B open interest at 14:34 UTC (10:34pm AWST) ([OpenChainBench HIP-3 bench](https://openchainbench.com/benchmarks/hyperliquid-hip3-deployers)). The thesis's US$3.39B was an earlier refresh of a rolling 24h number; same order. The frontend cohort page (US$3.80M builder fees, 125.4K users) shows "temporarily unavailable" tonight, so I relied on the 4:45pm check for those.
- **X Developer Policy quote:** correct, word for word. Also relevant and missed: the same "X performance benchmarking" section bars using the X API to "calculate aggregate X Post metrics, such as the total number of Posts posted per day" for commercial purposes. The thesis's 1,300–2,850/day count is fine as private research but shouldn't appear in marketing or on the public scorecard.
- **AFSL:** a read-only verdict is much safer than the trading layer. ASIC says "You do not need to hold an AFS licence to give factual information" (objectively ascertainable, truth can't reasonably be questioned) (RG 244.24–25). "No official post yet" and "price moved 4% in 5 minutes" are factual. "Contradicted" is a judgement, so always show the source. Never pair a verdict with "long/short" wording, and say up front it's factual information, not advice (RG 36.25). My reading, not legal advice.
- **Chrome Web Store:** no rule against overlaying x.com (fable, UNMSK and Ethos already do). Rules that bite ([Program Policies](https://developer.chrome.com/docs/webstore/program-policies/policies)): browsing data only for the disclosed feature (Limited Use), a privacy policy, narrowest permissions, no remote code (MV3), say clearly if basic features need payment, and don't imply X endorses it. **Crypto extensions are not featured**, so the store won't give discovery.
- **$TPLN ticker:** no DexScreener pair with symbol TPLN tonight (search API, 10:40pm AWST). "Tapeline" returned no pairs. Pump.fun tickers aren't unique, so reserve it early and match on contract (x-bot lesson).
- **Budget arithmetic:** 25 + 8 + 40 + 80 + 105 + 300 + 83 + 50 = A$691. Correct. Removing the one-off X backfill (A$21) gives **A$670**. The ~A$51/month running cost stays, because production can't use X bot's reads (see section 6).

**Wrong, unsupported or missing**
- **Larpcheck mis-described** as "coins only" (thesis teardown). It checks single X posts and links too, see Verdict. Its usage figures (~1,000 people a day running a check, ~17,000 checks in week one, 17 Oct) are self-reported by @Larpcheckbot.
- **Basis Desk Verify and SpyGlass missing** from the teardown.
- **"Edge can't be cloned in a weekend"** holds only for the poster record. The verdict line itself is SpyGlass-level hackathon work.
- **Not re-checked tonight:** the 1,300–2,850/day and 61/week "@grok is this true" counts (X counts, idea bot), the quoted liquidation posts, the IREN $26→$44 move, Newsflash pricing, UNMSK US$16, KOLscan 0.05 ETH. Plausible, unchecked.

## 2. Competitor check (incl. open-source clones and platform terms)
| Competitor | What it does | Price | Gap it leaves |
|---|---|---|---|
| Grok (@grok "is this true") | Ad-hoc answer when tagged | Free, built into X | Manual, slow, no poster record. **Main substitute** |
| [Larpcheck](https://larpcheck.app/how) (@Larpcheckbot) | Tag under any post: claim checked against sources, verdict + 0–100 score; coin checks; MCP/API | Free replies; Pro by holding $LARPCHECK | Must be tagged, ~1 minute per check, no poster headline record, no market mapping. **Closest after Grok**; could add headlines in a week |
| DefiLlama @llama | Tag for data-backed answers on fees/revenue/TVL with charts | Free | Protocol data, not news. Could become a supplier-style check |
| [Basis Desk Verify](https://basisdesk.news/news/basis-desk-verify-fact-check-crypto-news-chrome-extension) | Free extension: claim labels vs primary sources, live prices, token scam check | Free | Side panel on articles, on click; not automatic under X posts; no poster record |
| [SpyGlass](https://devpost.com/software/spyglass) | Inline verdict pill on every tweet, Gemini + Google grounding, Supabase cache | Hackathon | Proves the UI is a weekend clone; general, not market-aware |
| [fable](https://fable.market/) (open source), [TruthLayer](https://github.com/miraekims/Truthlayer), UNMSK, Ethos | Rug/shill/KOL labels on X | Free / US$16 | Coins and accounts, not headlines |
| Tree News, 247 Terminal, Proliquid, Reflex | Headline speed (+ trading) | 500–2,500 credits; US$99–199; free; waitlist | Speed, not truth |
| [Newsflash](https://newsflash.sh/docs) | Outlet corroboration API | Free / US$29 | Outlets only; possible supplier |

**Platform terms:** X Developer Policy (spam/abuse analysis and aggregate post metrics need written permission; remove deleted posts), Chrome Web Store (above). **Gap holds narrowly:** an automatic headline verdict plus poster record plus market move, inside x.com. Winnable only if the poster record is built first and kept private until X's OK.

## 3. Money check
- **Money already moving:** Tree News US$61k/30d on-chain (part own-token burns, part USDC buy-and-burn); 247 Terminal 181 × US$99 (estimate ~US$18k/month). That's ~US$80k/month for headline **speed** (estimate). For headline **accuracy**: zero proven payers. Larpcheck gives verdicts away and gates Pro by holding its token (no revenue shown).
- **Unit economics (estimates):** US$29 Pro; cost to serve ~US$0.30–0.80/user/month (verdict cached per post); ~90% gross margin; cash CAC ~US$0. Plausible.
- **Market size (estimate):** the thesis's 0.25–0.5% of 125.4K Hyperliquid users = 310–630 payers (US$9–18k MRR) is reasonable as a ceiling for year one. Base case US$3–6k MRR at month 12 is fair, and maybe optimistic given free Larpcheck/Basis Desk.
- **Route to US$10k/month without ads or sales:** 345 Pro. The best channel is the one only this product has: a weekly "who was first and right" scorecard. That's also the part X's policy puts at risk, so get X's written OK before day 30.
- **The money test that matters:** will 25 people pay US$29 when Grok, Larpcheck and Basis Desk are free? The thesis's Phase B asks exactly that. Keep it.

## 4. Scores
| Criterion | Score | Why |
|---|---|---|
| Problem severity | 6 | Real liquidations on fake headlines, but bursty |
| Timing | 7 | 24/7 AI and pre-IPO perps (trade.xyz US$3.47B/24h); verdict bots just became normal on crypto X |
| Differentiation | 4 | Larpcheck post checks, Basis Desk, SpyGlass; only poster record + market move + automatic are new |
| Usability for tech bros | 8 | Install, see a line under the post |
| Ape appeal | 7 | Traders love "who called it first"; less excited by "this is unconfirmed" |
| Solo buildability | 7 | 4 weeks for the read-only MVP; verdict accuracy is the hard part |
| Self-serve sales | 9 | Card, USDC or token; no calls |
| Distribution | 6 | Lives on X, but Chrome doesn't feature crypto and the scorecard needs X's OK |
| Retention | 5 | News-driven; daily use unproven |
| Money evidence | 6 | Speed is paid for on-chain; accuracy isn't proven |
| Token fit | 6 | Real use (burn own tokens per check, hold for Pro); same model as Larpcheck, so no edge from it |
| **Overall** | **5.5/10** | **Thesis (narrow).** Legal cap lifted, but free verdict bots and X's spam-analysis rule cut the edge |

**Rules gate: PASS** (tech-bro buyer: yes; token fit 6 ≥ 5 with a real pump.fun job). **Rank:** 3rd of 9 overall, level with Mint Seal and Breach Kit (5.5); behind Ledgerport 6.5 (outside rules) and Tapeline 6 (superseded by this); ahead of Second Look, Revtrace, Askwatch (5) and Agent Spend Books (4.5). **1st among rules-passing theses**, ahead of Revtrace (5).

## 5. Token-launch check (pump.fun only)
- **Job:** (1) burn your own $TPLN per deep check (~US$0.25, The Codex pattern, unproven); (2) burn your own $TPLN worth US$29 for a month of Pro (the own-token half of Tree News); (3) hold a set amount for Pro limits (KOLscan and Larpcheck pattern). Card and USDC are never converted into token buys. All three are product use, so they sit inside the ASIC line.
- **Settings:** SOL pair; Holder Rewards **off**; Tokenized Agent buybacks **off**; mint and freeze authority revoked on-chain before announcing; no bundles, snipers or caller packages; small labelled dev buy (≤0.5 SOL). Creator fees (0.30% on curve; tiered on PumpSwap per [pump.fun fees](https://pump.fun/docs/fees)) go to a public wallet as bonus income, never to buybacks or burns. Use `@pump-fun/pump-sdk` 4.3.1 (bonding curve + PumpSwap in one package, Git bot 10pm) for the burn and holder checks.
- **Launch:** only after 25 paying users and the legal consult, on a product-reveal day with a live extension link, CA posted from the official X account and pinned. Second beat 1–3h later: the first public scorecard (Trench Bot: survivors had a real event with a named person and holders still spread an hour later; site + X + paid DexScreener profile alone no longer separates winners, 11 of 12 died). DexScreener profile only from revenue.
- **Evidence:** Tree News is the only verified on-chain spend, and part of it is a revenue buyback we won't copy. The Codex peaked ~US$160k, never crossed $500k, no burn seen (Trench Bot, X bot). Larpcheck's own token panel is disputed ("61% bots", X bot).
- **Token fit: 6/10 (unchanged).** Plan: $TPLN on pump.fun, burned or held by users for checks and Pro, launched after 25 payers and legal OK.

## 6. Build and revenue plan
**What to change from the thesis:**
1. **Backfill: X bot runs it free with its built-in X reads** (40 accounts posting the most "BREAKING"/"JUST IN" market headlines, 30 days, into /workspace/shared-data/x-bot/). That's for private research only. A live product needs its own X API access under X's terms, so keep the A$21/month spot-read line.
2. **Add Trench Bot's and X bot's shill-check records as free labelled data** (/workspace/shared-data/trench-bot/coins.jsonl, /workspace/shared-data/x-bot/signals.jsonl). Use "paid promo" as a **private** feature in poster records and to measure how often "JUST IN" is a coin ad. Don't show it publicly until X's written OK.
3. **Phase A pass line, add one:** the auto-verdict must beat a tagged Larpcheck/Grok answer on the same 100 headlines (more correct or faster). Kill if it isn't better on either.
4. Verdict wording: factual only ("no official post found", "contradicted by [source]"), a "factual information, not advice" note, and no long/short words.

**MVP (4 weeks, ~20–25 h/week):** as the thesis: backfill + labelling tool → source matcher + market mapper (Hyperliquid info API incl. HIP-3, DexScreener) → MV3 extension + Telegram bot + payments (Solana Pay USDC, Lemon Squeezy card, own-token burn verification) → private scorecard, unlisted Chrome listing.

**Cost (A$, estimates):**
| Item | To end of 30-day test | 4-month total |
|---|---|---|
| Domain, Chrome fee | 33 | 33 |
| VPS | 10 | 40 |
| LLM | 20 | 80 |
| X API spot reads (backfill now free via X bot) | 21 | 84 |
| Contingency | 20 | 50 |
| Legal consult (before public scorecard/token) | 0 | 300 |
| Token launch | 0 | 83 |
| **Total** | **~A$104** (high ~A$130) | **~A$670** of A$1,000 |
DexScreener profile (~A$428) only from revenue.

**First 10 users:** people tagging @grok or @Larpcheckbot under market headlines, perps traders posting about ANTHROPIC/IREN/NVDA, Hyperliquid and Solana Telegram groups. All replies and posts from Ethan's account only with his OK.

**30-day test:** Phase A (days 1–10, private): pass if ≥8% of market headlines are contradicted or still single-source at 24h, ≥10 coincide with a ≥2% move within 1h, ≥85% agreement with hand labels, and it beats Larpcheck/Grok on the same set. Kill if <4%, <75% agreement, or no better than the free bots. Phase B (days 11–30, needs Ethan's OK for the unlisted listing and outreach): founding pass US$29 for 3 months. **Pass ≥25 passes (~US$725) and ≥25% of installs using it 3+ days a week. Kill <10 passes, <10% weekly use, or ≥50% saying "I just ask Grok/Larpcheck".** No token, legal spend, public scorecard or DexScreener profile before Phase B passes.

## Validation update, 22 Oct 11:20pm AWST
- 100 headlines hand-labelled (/workspace/shared-data/project-bot/tapeline-labels.jsonl): 71 confirmed, 8 contradicted, 1 single-source, 20 paid_promo; 10% of market-moving originals wrong, ~1 in 4 misleading once stale/early/wrong-figure/wrong-actor framing counts. idea bot's blind 30 matched 27 (90%, kappa 0.79).
- Head-to-head (X bot, /workspace/shared-data/x-bot/tapeline-backfill/checker-replies.jsonl): only 15 of 100 posts got any @grok or @Larpcheckbot reply; none of the 8 contradicted or 7 stale/early posts did; 1 of 20 promos (Larpcheck, correct). Grok never disagreed with a label but caught only 2 of 6 true-but-misleading framings. 25 of 36 reply matches are inferred.
- Result: the data half of the kill test passes. The free checkers' gap is coverage (tag-only) and framing (stale/misleading), which is exactly Tapeline's verdict format. Score stays 5.5 until the money half (US$29 founding passes, kill below 10) is run, which needs Ethan's OK.

## Update, 23 Oct 12:25am AWST: Paparazzi and template rings
- Paparazzi ($PAPA) is on Robinhood Chain, not Solana (X bot). Solana $PAPZ mints are copycats. It self-reports 1,092 readers, 7,065 tips a day and 10.5M burned. It posts its own BREAKING headlines with a 29–50/100 trust score. Its payouts are funded by revenue, which our rules bar. Overlap: headline trust scoring. No overlap: it's not a browser extension inside X, it doesn't search for earlier posts, and it's not on Solana. Score unchanged at 5.5.
- Feature idea from Trench Bot run 5: flag identical lines posted by several accounts within 60s (a template ring). Coins those rings pushed fell 67–75% within an hour. It's cheap to build on the "posted before?" search.
- Caveat (Trench Bot, 12:23am): the 67–75% figure comes from a handful of coins pushed by one ring. Show the ring flag without a number until it covers about 20 coins and more than one ring.
- Competitors the sweep missed: Larpcheck post checks (Larpcheck's own how-it-works page and its X replies), Basis Desk Verify (web search for crypto fact-check Chrome extensions), SpyGlass (Devpost hackathon search). Logged in /workspace/shared-data/project-bot/missed-competitors.jsonl.

## Re-score 23 Oct 2026 8:50am AWST (v1, new evidence)
**Covers:** idea bot's v1 thesis (no v2 file had landed at 8:50am; idea bot claimed a v2 run at 8:31am). New evidence since the 22 Oct 11:20pm validation update: idea bot's automated "posted before?" stale-check prototype (/workspace/idea-bot/data/stale-check/README.md, run against my 100 labels), Git bot's thesis refinement (git-bot:refine, pumpdata.fun as a data source and agent channel), six Trench Bot thesis notes for Tapeline Check (trench-bot/thesis-inputs.jsonl, 8:40am), and Growth Bot's new rule that every version needs an AI-agent distribution path (refine-protocol.md).

**Weak spots from the last review, checked:**
- Differentiation (Larpcheck, Basis Desk, SpyGlass): **still open.** No new rival to the headline check, but nothing yet proves our verdicts beat theirs.
- "Nobody pays for accuracy": **still open.** No money evidence has moved; the US$29 founding-pass test is parked until Ethan picks this thesis to launch as a coin (not waiting on him).
- "Date check is the real edge": **partly tested.** The labels showed stale news is the biggest failure type (11 of 23 misleading headlines) and no free checker replied under any stale post. Idea bot's prototype found the earlier story for 6 of 11 stale posts using a free news search, but keyword matching false-flagged 23 to 38 of 69 fresh posts, so a same-event judge (small LLM or embeddings) is required. Pass line set by idea bot: 8+ of 11 caught with 5 or fewer false flags on the same 80 rows. The Google News RSS feed used is personal, non-commercial only, so production needs another source.
- X policy on "paid promo": **still open** (private only).

**Fact-check of new claims:** pumpdata.fun's own page confirms 300 free lookups a day with no key, then US$0.005 a call for launch and deployer lookups (US$0.01 for a 50-wallet batch) paid in USDC over x402 on Solana, a free key for 2,000 a day, US$10/month for 20,000 a day, an MCP server at pumpdata.fun/mcp, and a Telegram bot (@pumpdatafun_bot) that runs a contract check and can /watch a dev ([pumpdata.fun](https://pumpdata.fun)). That makes it both a near-free data source for dev-wallet checks and a free rival for any "paste a contract, get a dev check" feature. It doesn't check headlines or posters. Trench Bot's coin notes (dev-tied organic poster on BTC, staircase wash on MrBeast, frozen DexScreener feed on FORK, Project Kimchi vs Kimchi mint mix-up) come from its own logs; small samples, medium confidence.

**Competitors the sweep missed:** pumpdata.fun's Telegram contract check (@pumpdatafun_bot), found on pumpdata.fun's own homepage via Git bot's radar. Partial overlap only (coin/dev checks, not headlines). Logged in missed-competitors.jsonl.

**Refined idea:** Tapeline Check should stop leading with a bare true/false verdict, because 90% of market-moving originals were true. Lead with two things free checkers don't do: a **"first happened" date stamp** ("real, but this happened 8 Oct; posted 14 days late") and the **poster's record**, which for coin posts includes a **dev-tie flag** (poster talked to or promoted the dev, via pumpdata.fun's free tier) and **exact-mint resolution** before judging. Any market cap or liquidity shown is read from the pool on-chain, not DexScreener. Ship the same check as an x402/MCP endpoint and a Grok Bot template alongside the extension. Evidence supports the direction (stale is the biggest failure class and is uncovered), but not yet the accuracy.

| Category | Old | New | Reason and source |
|---|---|---|---|
| Solo buildability | 7 | 7.5 | Stale-check retrieval ran free in one session with no LLM or paid API (idea bot prototype); dev-wallet data near free on pumpdata.fun's 300/day tier (verified on its site) |
| Differentiation | 4 | 4 | Date stamp + dev-tie are uncovered, but the prototype doesn't yet hit the accuracy pass line; no lift until it does |
| Distribution | 6 | 6 | Agent channels are real (pumpdata uses MCP/x402), but v1 doesn't include one and Larpcheck already has MCP/API; +0.5 once a version ships it |
| Money evidence | 6 | 6 | Nothing new on paying for accuracy |
| Token fit | 6 | 6 | Unchanged; Trench Bot's launch notes (one pinned mint, no boosts, no paid callers) are already in the plan |
| **New overall: 5.5/10** | 5.5 | **5.5** | Unchanged: build got cheaper, but differentiation and money evidence haven't moved |

**Rules gate: PASS** (tech-bro buyer; token fit 6 ≥ 5). Still 1st among rules-passing theses; 3rd of 9 overall behind Ledgerport 6.5 (outside rules) and Tapeline 6 (superseded by this).

**What would lift this score (updated):**
1. Same-event judge hits the pass line (8+ of 11 stale caught, 5 or fewer false flags on the 80 rows): Differentiation 4 → 5.5, overall about +0.5. Free, private.
2. v2 builds in the date stamp, dev-tie flag, exact-mint resolution, on-chain pool reads and an x402/MCP endpoint, with a licensed news source named and costed: Distribution +0.5, overall about +0.25.
3. Any evidence that traders pay for accuracy (for example a Whop or on-chain product selling verification rather than speed): Money evidence 6 → 7, overall about +0.5. The founding-pass test stays parked until Ethan picks this thesis.

## Re-score 24 Oct 2026 8:35am AWST (v2)
**Covers:** idea bot's Tapeline Check v2 (/workspace/idea-bot/theses/2026-10-23-0900-tapeline-check-v2.md, 23 Oct 9:00am AWST). Also:
- Trench Bot's blind same-event run (/workspace/trench-bot/blind-same-event/RESULT.md and METHOD.md; predictions frozen 23 Oct 8:52am AWST, sha256 recorded, scored afterwards).
- Trench Bot's poster-track-record.jsonl (79 handles).
- X bot's three thesis-refine notes (x-bot:signal:2026-10-23-0845-001/002/003).
- Fresh web checks of the new rivals, Newsflash and Brave pricing.
- Prep draft: /workspace/project-bot/drafts/draft-rescore-tapeline-check-v2.md (23 Oct 8:48am AWST).

**Blind same-event check (Trench Bot, never saw the labels): FAIL, kill line.**
- **Result:** caught **5 of 11** stale headlines (pass is 8 or more) with **7 false flags out of 69** (pass is 5 or fewer). That's under 6 caught, so it's past idea bot's kill line for the stamp as the lead feature.
- **False flags:** all 7 matched a real earlier article about the same event. Six were reposts 1 to 2.5 days after the first report, and the labels don't count a next-day repost as stale. The seventh was OpenAI "in talks" versus the actual raise 21 days later.
- **Misses:** 5 of the 6 were retrieval or paraphrase failures, where title-only search never found or matched the earlier story. One was the judge being too strict: Kraken/VARA scored a cosine of 0.65 against a 0.75 bar.
- **Post-hoc 48h cutoff:** 4 caught, 2 false flags. That's not official, and catches never reach 8 at any cutoff.
- **Caveat:** the rules were tuned about 4 times on Trench Bot's own reading of the same 100 posts, so the result is slightly optimistic. The run was free: Google News RSS (personal use only), MiniLM on CPU, no LLM.
- **Reading:** the judge separates "same event" from "same topic" much better than keywords did (7 false flags vs 23–38). The bottleneck is **retrieval from titles only**, plus where the stale line sits.

**Weak spots from the last review, checked against v2's "what changed":**
- **Differentiation (verdicts already free):** pivoted to a "first happened" stamp. Still not proven buildable at the pass line.
- **Nobody pays for accuracy:** still open. ArcaneNews and PVP ship old-news flags inside paid terminals, but nobody shows payment for the flag itself.
- **X policy (paid-promo label, public scorecard):** cut. Fixed.
- **Exact mint, dev-tie flag, on-chain pool reads:** fixed (in design).
- **Agent channel (MCP, x402, Grok Bot template):** fixed (in design).
- **Licensed news source:** named and costed, but there's a new problem. Brave's FAQ says storing results needs "a plan that includes storage rights", which clashes with the own-archive moat. Newsflash's free tier only reaches back 30 days, and at least 3 of v2's own stale examples (Warsh in April, the January wallet, the 2025 Trump quote) are older than that.
- **Retention:** design only (Telegram alerts). No usage evidence.

**Fact-check of new claims:**
- **Confirmed:**
  - ArcaneNews "Old news detection" and "Same news detection" ([arcane.news](https://arcane.news/)).
  - PVP's "Old News Threshold", which is delivery latency, not event age ([docs](https://docs.pvpterminal.com/desktop/desktop/settings/news)).
  - Tweet Fact Checker: "DEMO ONLY", no ratings.
  - Stale News Warning: 0 stars.
  - Custom Timestamps for X: 1 rating, post age only.
  - Newsflash: free key 1,000 a day with 30-day history; US$29/month for the 5-year archive; events carry `first_seen_at`, semantic match and an MCP server ([docs](https://newsflash.sh/docs)).
  - Brave Search: US$5 per 1,000 calls with US$5 of free credit a month, which needs attribution ([Brave](https://brave.com/search/api/), [Brave blog](https://brave.com/blog/most-powerful-search-api-for-ai/)).
- **Corrections:**
  - FactCheckRadar's store page shows "Updated October 22, 2026" (not 19 Oct). It also dates images ("when it first surfaced") ([store](https://chromewebstore.google.com/detail/factcheckradar/obepkghlneckiemaclcigahjnbkonhnf)).
  - The budget items add to A$710. It's ~A$694 only if the A$16 news line comes out of contingency.
  - The day-30 items add to A$110, not A$104. Both are still well inside A$1,000.
- **Not re-verified:** X API read price, the 17 complaints in 7 days, Larpcheck's user count.
- **Poster track record:** all 79 handles are rated low confidence and 65 appear on only one coin. It records who posts about coins, not who posts headlines, so it doesn't move the score.

**Token check (ASIC):**
- Holding sets the auto-stamp quota, and agents burn **their own** $TPLN for API credits.
- Card and USDC payments are never converted into token buys. Creator fees are bonus income only, never buybacks or burns. Holder Rewards and Tokenized Agent buybacks are off. pump.fun only, and launch only after 25 payers.
- **Pass.** Token fit stays 6, since it's still the Larpcheck hold-to-access pattern.

**Competitors the sweep missed:**
- [Kronical](https://kronical.ai): it "separate[s] the first report of a story from the repeat coverage that follows it" across news, filings and X, for finance teams and agents. Its co-founder pitches it under crypto posts. It's not an on-X stamp and has no public price, but it's the closest rival to the v2 core.
- [Mycroft Media Narrative Tracker](https://github.com/Humanitariansai/Mycroft/tree/main/n8n_Workflows/Media_Narrative_Tracker): an open-source n8n workflow that gives financial news an "information age" score with Groq, and has no labelled ground truth.
- Also: Newsflash's `first_seen_at` over MCP is now a substitute for our agent channel, not just a supplier.
- Both rows are logged in missed-competitors.jsonl.

**Refined idea:** Tapeline Check becomes a **"first reported" line on every market post, with a staleness flag the user sets**, rather than a stale/not-stale verdict.
- **Retrieval is the fix:** match on Newsflash first-seen events plus the **article ledes** and exact publish times (not titles), stored as our own derived records (post ID → event, first date, source URL) so we stay within Brave's terms. Brave News is used transiently for stories older than 30 days.
- **Two-stage judge:** first the cheap figure/name/action rules (they cut false flags from 23–38 to 7), then a small LLM on the top 3 candidates asking "same event, later development, or same topic?". That handles "in talks" turning into "raised" and paraphrases like Kraken.
- **Staleness flag:** user-set, for example "first reported 2+ days ago and nothing new", because next-day reposts aren't misleading to the labeller. Abstain rather than false-flag.
- **Coin card:** trimmed to exact mint plus the pumpdata dev check for the 4-week build.
- **Agent channel:** has to beat "Newsflash MCP + any LLM" on measured accuracy.
- **Re-test:** the same 80 rows on a fresh blind run before anything else.

| Category | v1 (23 Oct 8:50am) | v2 | Reason and source |
|---|---|---|---|
| Problem severity | 6 | 6 | No new harm evidence |
| Timing | 7 | 7 | Unchanged |
| Differentiation | 4 | 4 | The stamp is uncovered on X, but the blind run caught only 5 of 11 (RESULT.md). Kronical, ArcaneNews and Newsflash `first_seen_at` narrow the slot |
| Usability | 8 | 8 | Automatic stamp, no tagging |
| Ape appeal | 7 | **6.5** | Public "who called it first" scorecard cut for X policy. "This happened 14 days ago" is useful but less exciting |
| Solo buildability | 7.5 | **7** | The core judge failed on free retrieval. It needs licensed ledes and an LLM stage, and v2's 4-week scope grew (coin card, MCP, x402, Telegram) |
| Self-serve sales | 9 | 9 | Unchanged |
| Distribution | 6 | **6.5** | MCP, x402 and Grok Bot template now in the plan and costed (+0.5 pre-committed on 23 Oct). Newsflash MCP is a substitute, so no more than that |
| Retention | 5 | 5 | Telegram alerts are design only |
| Money evidence | 6 | 6 | Old-news flags exist inside paid terminals, but nobody pays for accuracy. Still capped |
| Token fit | 6 | 6 | ASIC check passes |
| **Overall** | **5.5** | **5.0** | **Kill line on the blind check.** The lead feature isn't proven, and the gains (agent channel, X-policy cut) are offset by lower ape appeal and buildability. **v1 at 5.5 stays the best version.** |

**Rules gate: PASS** (tech-bro buyer; token fit 6 ≥ 5). **Rank:** v1's 5.5 still counts, so Tapeline Check stays 1st among rules-passing theses. Overall it's level with Mint Seal and Breach Kit, behind Ledgerport 6.5 (outside the rules) and Tapeline 6 (superseded). v2 on its own would sit with Second Look, Revtrace and Askwatch at 5.

**What would lift this score (updated):**
1. A fresh blind run with lede-based retrieval (Newsflash events plus ledes) and the small-LLM second stage passes on the same 80 rows (8+ of 11 caught, 5 or fewer false flags), with the stale line set at 2+ days. That takes Differentiation 4 → 5 and overall to 6.0 (the no-payer cap). Use a fresh blind bot, or held-out rows, because this set has now been tuned on.
2. Evidence that traders pay for old-news or accuracy flags specifically: Money evidence 6 → 7, which lifts the cap.
3. Judge accuracy measured above a "Newsflash MCP + LLM" baseline on the same rows: Differentiation +0.5, Distribution +0.5.
4. Founding-pass test (parked until Ethan picks this thesis to launch).

## Re-score 24 Oct 2026 9:15am AWST (v3)
**Covers:** idea bot's Tapeline Check v3 (/workspace/idea-bot/theses/2026-10-24-0830-tapeline-check-v3.md, 24 Oct 8:30am AWST) and its window split (idea-bot/data/stale-check/window-split.md). Also:
- Trench Bot's official blind run on my fresh holdout (/workspace/trench-bot/blind-v3-holdout/: RESULT.md, METHOD.md, FROZEN.txt, score_output.txt).
- The holdout spec (/workspace/shared-data/project-bot/tapeline-holdout-v3/FREEZE.md; labels frozen 9:01am AWST).

**Blindness re-checked (9:13am AWST):** `labels.jsonl` sha256 still `dcca9fb2…3a71ad`, matching FREEZE.md. `predictions.frozen.jsonl` sha256 `11ae2333…ec123`, matching FROZEN.txt (frozen 9:09:51am AWST), and identical to `predictions.jsonl`. score.py asserts both hashes before it reads a label. Trench Bot disclosed one pre-freeze deviation: it read extra retrieved candidates for 11 rows and made 3 extra lookups. All of that was retrieval output, with no labels, so the run counts as blind.

**Blind holdout result (Trench Bot, never saw the labels): FAIL by one row, iterate zone.**
| | Result | Pass line (v3's own first move) | Kill line |
|---|---|---|---|
| Stale caught | **5 / 7 (71%)** | ≥ 6 / 7 (75%) | < 50% |
| In-window late reposts | 3 / 4 (75%) | report (in-window target 75%: met) | |
| Recycled claims (engine b) | 2 / 3 | report | |
| False flags on fresh | **0 / 16 (0%)** | ≤ 3% (0 / 16) | > 8% |
| FF among 10 same-day 1–9h reposts | 0 / 10 | report | |
| FF among 3 rows 24–48h old | 0 / 3 | report | |
| FF among 3 other fresh rows | 0 / 3 | report | |
| Correct type on catches | 5 / 5 | | |
| Stamp date within ±24h of label | 17 / 20 (85%) | ≥ 80% (thesis sub-target: met on a ±24h reading) | |
| Stamp date within ±6h | 5 / 20 (25%) | not set | |
| 24h side rule | 5 false flags | side result only | |
| Secondary check, old 80 rows | **not run** | ≥ 8 / 11, ≤ 5 FF (warning only) | |

- **Misses (both retrieval):** the Coinbase/The Block "Always-On Dollar" report (late repost, 80.5h). Its hype wording and the McKinsey $5T figure never matched the report's title, so there were 0 usable candidates. And Garlinghouse "record year" (recycled, about 64 days). The post moved a Ripple quote onto XRP, search found a different March quote, and the judge abstained, as the rules say.
- **What it fixed:** the v2 trap. Next-day and same-day reposts caused 6 of v2's 7 false flags. Here it's 0 of 10 same-day reposts and 0 of 3 rows 24–48h old, with the 48h line plus "earlier stage vs same event" judging. Topic traps (China 2030 target, BLOOM expansion, BlackRock transfers) all stayed silent.
- **Label sensitivity:** Trench Bot agreed with all 5 medium-confidence labels. If Riksbank or Securitize were relabelled fresh, it would read 4 of 6 caught (67%) with 0 FF, still in the iterate zone. No reading of the labels moves it to pass or kill.
- **Small n:** each stale row is worth 14 points and each fresh row 6. 5 of 7 and 6 of 7 can't be told apart statistically. The pre-agreed line still decides the score, so I'm not moving it after the fact.

**Weak spots from the v2 re-score, checked against v3's "what changed":**
- **Core judge failed blind:** partly fixed. False flags went from 7 of 69 to 0 of 16 on unseen data, and the catch rate is in the iterate zone, not at the kill line. It still hasn't passed.
- **Next-day repost false flags:** fixed on unseen data (0 of 13 rows that are 1–48h old).
- **Retrieval from titles only:** still the bottleneck. Both misses began there. v3 promised Newsflash events and ledes, but the free key needs a sign-up, so the run used Google News and Bing News RSS. The keyless Newsflash tier only looks back 24h. **Newsflash retrieval, v3's named fix, is still untested.**
- **"Small LLM" stage 2:** Trench Bot did the judging itself by reading the candidates, with a written reason for each row. It wasn't a cheap small model. So the result shows the method works, not that it works at v3's A$26/month LLM budget.
- **Recycled claims (engine b):** better than expected. Plain undated news search caught 2 of 3 with no claim library. The miss is the entity-swap case, which a claim library is for.
- **Exact publish time:** not fixed. 14 of 20 feed dates were early, by up to 31h. On fresh rows that's visible to the user: the China 2030 post (0.9h old) would have been stamped about 31h old, and the SEC post (5.4h) about 37h. That's wrong on a product whose whole job is the date, even though no LATE tag fired.
- **Budget:** fixed (see fact-check).
- **Benchmark vs "Newsflash MCP + LLM":** not run (needs a sign-up and Ethan's OK). Said plainly in v3.
- **Money for accuracy:** still open. No new evidence.

**Fact-check of v3's claims:**
- **Budget: confirmed.** 4-month items: 33 + 40 + 104 + 84 + 16 + 0 + 300 + 83 + 50 = **A$710**. Day 30: 33 + 10 + 26 + 21 + 20 = **A$110**. Headroom A$290. Monthly lines: 10 + 26 + 21 + 4 = A$61. Two small issues:
  - The executive summary says running cost is "about A$75 a month", but the table says A$61. The table is right.
  - Day 30 leaves out the A$4 news line. That's fair if Brave's US$5 free credit covers month 1, otherwise it's A$114.
  - Both are well inside A$1,000. The LLM line is untested, because stage 2 ran by hand.
- **Window split: confirmed** against the v2 blind run: 0 of 4 caught over 30 days, 5 of 7 inside 30 days.
- **Newsflash free key covers 30 days:** per its docs, yes, but it needs registration. The keyless tier is 50 requests a day with 24h lookback (Trench Bot, RESULT.md), so it can only confirm a story is fresh.
- **Pass line wording:** v3 says "≥75% of in-window late reposts". The holdout's official line counts all 7 stale rows, as set in FREEZE.md before the run. On v3's narrower in-window wording it would pass (3 of 4 = 75%, 0 FF). I score on the frozen line, since it was agreed first and covers the recycled rows the product would also stamp.
- **Not re-verified this run:** Kronical, FactCheckRadar's 22 Oct update (confirmed in the v2 re-score), X API read price, Tree News and 247 figures (unchanged since 22 Oct).

**Token check (pump.fun only):** $TPLN unchanged from v2. Hold it to set the auto-stamp quota. Users and agents burn **their own** tokens for deep checks and API credits. Card and USDC are never converted to token buys. Holder Rewards off, Tokenized Agent buybacks off, creator fees bonus only, launch after 25 paying users and the legal consult, ≤0.5 SOL labelled dev buy, one pinned CA. **Pass.** Token fit stays 6, since it's still the Larpcheck hold-to-access pattern.

**Competitors the sweep missed:** none new this run. Kronical and Mycroft (logged 24 Oct 8:35am) are now in v3's teardown.

**Refined idea:** keep v3's "stamp, don't accuse" design and the 48h LATE line. Both held on unseen data. Fix the two layers the misses point to:
- **Retrieval on the claim, not the headline.** Extract the actor, action, object/figure and any named report, strip hype words, and query on those. Search the named source itself (for example "Coinbase The Block report") as well as the post's wording.
- **Fetch the article page's own publish time** (`article:published_time` or JSON-LD `datePublished`) for the winning candidate before showing any stamp, and abstain from the date line when only a day-level feed date exists.
- **Engine (b) for entity swaps:** match the claim against both the stated entity and its close relations (Ripple ↔ XRP, Coinbase ↔ Base, issuer ↔ token), then check the claim library.

| Category | v1 (23 Oct 8:50am) | v2 (24 Oct 8:35am) | v3 | Change vs v2 / vs v1 | Reason and source |
|---|---|---|---|---|---|
| Problem severity | 6 | 6 | 6 | 0 / 0 | No new harm evidence. The holdout's 7 of 23 stale was a curated sample, not a prevalence count |
| Timing | 7 | 7 | 7 | 0 / 0 | Unchanged |
| Differentiation | 4 | 4 | **4.5** | +0.5 / +0.5 | First measured judge on unseen data: 0 of 16 false flags and 5 of 7 caught (RESULT.md). No free X tool stamps this. The pre-agreed +1 was for a pass, so only half. Kronical and Newsflash still narrow the slot |
| Usability | 8 | 8 | 8 | 0 / 0 | Neutral line that stays silent when unsure works. Wrong dates on 2 fresh stamps (up to 31h) need fixing, but there were no false accusations |
| Ape appeal | 7 | 6.5 | 6.5 | 0 / −0.5 | Still no public scorecard. "LATE 14 days" is useful, not exciting |
| Solo buildability | 7.5 | 7 | **7.5** | +0.5 / 0 | Scope trimmed back to a v1-sized 4 weeks (pool reads, staircase, dev-tie, Telegram after the money test), and the whole v3 pipeline ran free with no sign-up. Not higher: stage 2 was a capable bot reading by hand, not the costed small LLM, and production still needs licensed retrieval (Google News RSS is personal-use only) |
| Self-serve sales | 9 | 9 | 9 | 0 / 0 | Unchanged |
| Distribution | 6 | 6.5 | 6.5 | 0 / +0.5 | MCP, x402 and Grok Bot template kept. No lift until it beats "Newsflash MCP + LLM" (not run) |
| Retention | 5 | 5 | 5 | 0 / 0 | No usage evidence |
| Money evidence | 6 | 6 | 6 | 0 / 0 | Nobody shown paying for accuracy. Still the cap |
| Token fit | 6 | 6 | 6 | 0 / 0 | Pump.fun check passes. Same hold-to-access pattern as Larpcheck |
| **Overall** | **5.5** | **5.0** | **5.5** | **+0.5 / 0** | **Iterate zone on the blind holdout:** short of the pass line by one row, nowhere near the kill line. **v3 is the best version** (ties v1 on score, but it's the only one whose core judge has been measured on unseen data) |

**Why 5.5 and not 6.0 or 5.0:** the plan agreed before the run was 6.0 for a pass, 5.5 in the iterate zone and 5.0 at the kill line.
- **Not 6.0:** 5 of 7 is below the frozen 6 of 7 line. A one-row miss on a small sample is noise as much as signal, and that cuts both ways. Moving the line now would empty every future holdout of meaning. On top of that:
  - stage 2 was done by hand rather than by the costed small LLM;
  - Newsflash retrieval, v3's named fix, wasn't tested;
  - the 80-row secondary check wasn't run.
- **Not 5.0:** neither kill condition is close (71% caught vs a 50% floor; 0% FF vs an 8% ceiling). v2's actual failure, false flags on next-day reposts, went to zero on unseen rows. Both misses are retrieval problems that v4's two named fixes target directly.
- **Best version:** v3. It ties v1's 5.5, but v1's score came before any blind test and v2 failed one, so v3 is the version with evidence behind it. Same rule as Ledgerport v2.

**Rules gate: PASS** (tech-bro buyer; token fit 6 ≥ 5; pump.fun only, no payouts or fee-funded buybacks, launch after payers). **Rank:** 5.5 stays 1st among rules-passing theses. Overall it's level with Mint Seal and Breach Kit, behind Ledgerport 6.5 (outside the rules) and Tapeline 6 (superseded).

**What v4 must fix (in order):**
1. **Claim-plus-entity retrieval.** Build queries from the extracted actor, action, figure and named report, not the headline text. Also search the issuer's own site or newsroom for named reports. Target: the Coinbase/The Block report row is found.
2. **Publish time from the article page** for the winning candidate (and for every stamp shown), with a stamp only when an exact time exists. Target: ≥80% of shown stamps within ±6h (this run: 25%), with no fresh post stamped more than 24h old.
3. **Entity-swap matching in engine (b)** (Ripple ↔ XRP and similar), checked against a claim library or Google Fact Check data where the key's terms allow. Target: the Garlinghouse row is matched, with no new false matches.
4. **Run stage 2 on the actual small LLM** named in the budget, logging cost per check, so the A$26/month LLM line is measured, not assumed.
5. **A new fresh blind holdout**, since these 23 rows are now seen. Make it larger (aim for ≥12 stale and ≥30 fresh) so one row isn't 14 points. Keep the same lines: ≥75% caught, ≤3% FF, ≥80% of stamps correct. Run the 80-row secondary check as a warning.
6. **Newsflash retrieval and the "Newsflash MCP + LLM" baseline**, only with Ethan's OK for the free sign-up.
7. Fix the A$61 vs A$75 running-cost mismatch in the summary.

**What would lift this score (updated):**
1. v4 passes a fresh, larger blind holdout on the same lines: Differentiation 4.5 → 5, overall 6.0 (the no-payer cap).
2. It beats a "Newsflash MCP + LLM" baseline by ≥10 points at equal false flags: Distribution +0.5, Differentiation +0.5.
3. Evidence that traders pay for old-news or accuracy flags on their own: Money evidence 6 → 7, which lifts the cap.
4. Founding-pass test (parked until Ethan picks this thesis to launch).
