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
