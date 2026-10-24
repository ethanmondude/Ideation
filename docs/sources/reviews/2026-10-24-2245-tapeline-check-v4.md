# Review: Tapeline Check v4 (an automatic "first reported" date stamp under X market headlines, and nothing else)

*Project Bot re-score · 24 Oct 2026, 10:45pm AWST (Perth time) · thesis: /workspace/idea-bot/theses/2026-10-24-2230-tapeline-check-v4.md (idea bot, 24 Oct 10:30pm AWST) · this is a version page: the full re-score, with the fact-check, weak-spot walk-through and token check, is the "Re-score 24 Oct 2026 10:45pm AWST (v4)" section of the canonical living review, 2026-10-22-2245-tapeline-check.md.*

## Verdict
- **Score: 5.5/10 (v4), unchanged from v3. Token fit 6/10. Passes Ethan's rules gate. v4 is the best version** (same score, more build-ready). Innovation 6, Usability 8.5, Uniqueness 5.5.
- **Up:** Usability 8 → 8.5 and buildability 7.5 → 8. Exact publish times are keyless and to the second (idea bot 11/11 and 8/8; my check 3/3), and earliest-across-outlets matters (OKX-ICE story: Cointelegraph 16.5h before CoinDesk).
- **Correction:** the figure line isn't ours. Larpcheck already replied "the buyer received 22.46 USDG, not the 23.64 posted" ([post](https://x.com/Larpcheckbot/status/2114000239371727246)), which is v4's own example. Cut it from v1.
- **Still capping it:** claim-based retrieval is unmeasured, and nobody is shown paying for accuracy.
- **Refined idea:** a date stamp and nothing else: `first reported <earliest exact time> · <outlet> · <age>`, LATE at 48h+.

**Claude Code build brief (v4, updated):** use the "Build brief for Claude Code" section of /workspace/idea-bot/theses/2026-10-24-2230-tapeline-check-v4.md (reproduced on the v4 version page) with these changes, which override it:
- **Remove** feature "figure mismatch line", the `source_figure` branch of the pseudocode, AT-T8, and the Hyperliquid/GeckoTerminal row from the data sources. Out of scope for v1.
- **Time resolver rule:** RSS `pubDate` (UTC) is primary. Page `datePublished`/`article:published_time` is a cross-check only: if the page time has no offset, accept it only if it equals the RSS time read as UTC (±60s); otherwise keep RSS. If neither gives a time to the second, abstain from the stamp. Treat HTTP 403 pages (The Block) as RSS-only.
- **Cluster rule:** stamp time = earliest source-backed time across every archive item the judge labels same_event; show the outlet of that earliest item. Fixture: Wells Fargo/OKX-ICE (Cointelegraph 23 Oct 21:32:16 UTC beats CoinDesk 24 Oct 14:06:24 UTC).
- **Acceptance tests:** AT-T1/AT-T2 run on the existing labelled sets (shared-data/project-bot/tapeline-holdout-v3/labels.jsonl and the 100-row set in shared-data/project-bot/tapeline-labels.jsonl), not a new holdout; AT-T1 must include the Coinbase/The Block "Always-On Dollar" row and AT-T5 the Garlinghouse row.
- Unverified in the brief: LLM cost per check (AT-T6), X API read price, Google Fact Check API commercial terms.


## Claude Code build brief (idea bot v4, with Project Bot overrides below taking priority)

#### Scope of the MVP (4 weeks)
A Chrome MV3 extension for x.com plus a small API that stamps market headlines with the earliest first-reported time of the event they describe, a LATE tag at 48h+, and a figure mismatch line when the source gives a different number. Out of scope for MVP: any true/false verdict, poster track records, account scores, perps trading, Telegram watchlists, coin dev checks.

#### Features in build order
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

#### Architecture and stack
- Extension: TypeScript, MV3, content script reads only the visible post text, post ID and created time; sends them to the API; renders one line. No remote code, permissions limited to x.com and the API host.
- API: Node + Hono on a A$10/month VPS; Postgres (or Supabase free) with `pg_trgm` and `pgvector`; a worker for feed polling.
- LLM: one small, cheap model for extraction and stage 2 (JSON mode); log tokens and cost per call.
- Payments: Lemon Squeezy webhooks; Solana RPC (free tier) for USDC receipts, token balances and burn memos.

#### Data sources, costs and terms
| Source | Use | Cost | Limits / terms |
|---|---|---|---|
| Outlet and exchange RSS | Event archive, times | Free | Store derived records (title, lede ≤300 chars, time, URL), link back; respect each feed's terms and robots |
| Article pages | Time cross-check | Free | One fetch per new article; some sites (The Block) block plain fetches, so RSS time is primary |
| X API reads | Pro auto-stamps of watchlist accounts | US$0.005/post (est. A$21/month) | X Developer Policy: event facts only, no per-account measurement or scores |
| Brave Search News | Lookups older than the archive | Free credit then paid | Transient use only, no storing result bodies |
| Google Fact Check Claim Search API | Recycled-claim seed | Free key | Check commercial-use terms before production |
| Hyperliquid info API, GeckoTerminal | Figure check for prices and pool moves | Free | Rate limits; cache 30s |
| Newsflash (optional) | Extra clustering | Free 1,000/day | Only with Ethan's OK for sign-up |

#### Core logic (rules and pseudocode)
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

#### UI and first-minute flow
Install → open x.com → click "stamp" on any market post (free) → one grey line appears in under 2 seconds, or a quiet "no match" tooltip. Pro: sign with a Solana wallet holding $TPLN or pay by card, pick up to 25 accounts, and stamps appear automatically. LATE is amber text, never red; nothing ever says "fake".

#### Token integration steps
1. Before launch: build with $TPLN mint as a config value; test on devnet with a dummy mint.
2. Launch on pump.fun only after 25 paying users and the legal consult; mint and freeze authority off; ≤0.5 SOL labelled dev buy from a published wallet; pin the CA in the extension About page, site and X bio.
3. Hold check: wallet signs a nonce; API reads the SPL balance (RPC); tiers at fixed token amounts set at launch, re-read every 24h.
4. Burn verifier: user burns their own $TPLN with an SPL memo `tpln:<credit_id>`; API confirms the burn tx and credits the account; public page lists every burn with Solscan links.
5. Creator fees to a published wallet, bonus only; no code path converts card or USDC revenue into token buys.

#### Acceptance tests (numeric pass lines)
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

