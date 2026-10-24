# Review: Tapeline Check v3 (a "first reported" stamp under X market headlines that stays quiet unless it's sure)

*Project Bot re-score · 24 Oct 2026, 9:15am AWST (Perth time) · thesis: /workspace/idea-bot/theses/2026-10-24-0830-tapeline-check-v3.md (idea bot, 24 Oct 8:30am AWST) · this is a version page: the full re-score, with the blind-test table, weak-spot walk-through, fact-check and token check, is the "Re-score 24 Oct 2026 9:15am AWST (v3)" section of 2026-10-22-2245-tapeline-check.md*

## Verdict
- **Score: 5.5/10 (v3). Token fit 6/10. Passes Ethan's rules gate.** **v3 is now the best version.** It ties v1's 5.5, but it's the only version whose core judge has been measured on unseen data. v2 scored 5.0.
- **Blind holdout (Trench Bot, predictions frozen 9:09am AWST before any label was seen): iterate zone.** It caught **5 of 7** stale posts, one short of the 6 of 7 pass line, with **0 of 16** false flags.
  - Late reposts 3 of 4, recycled claims 2 of 3. All 5 catches got the right type.
  - **0 false flags on the 10 same-day reposts.** That was the trap that sank v2, which had 7 false flags in 69.
  - Both misses were retrieval failures. One was a hype-worded post about a Coinbase/The Block report that never matched the report's title. The other was a recycled Garlinghouse quote that the post moved from Ripple onto XRP.
  - Feed dates ran up to 31h early. Stamp dates were within 24h on 17 of 20 but within 6h on only 5 of 20, so a 24h rule would have made 5 false flags.
- **Why 5.5:** the plan agreed before the run was 6.0 for a pass, 5.5 in the iterate zone and 5.0 at the kill line. It missed the pass line, but nowhere near the kill line (71% caught vs a 50% floor, 0% FF vs 8%). Three things are also still untested: stage 2 was judged by hand rather than by the costed small LLM, Newsflash retrieval wasn't used, and the 80-row secondary check wasn't run.
- **Budget checked:** A$110 to day 30 and A$710 over 4 months both add up, with A$290 of headroom. The summary's "about A$75 a month" should read A$61.

## Score breakdown
| Category | v1 | v2 | v3 | Reason |
|---|---|---|---|---|
| Problem severity | 6 | 6 | 6 | No new harm evidence |
| Timing | 7 | 7 | 7 | Unchanged |
| Differentiation | 4 | 4 | 4.5 | 0 of 16 false flags and 5 of 7 caught on unseen data. Half the pass lift |
| Usability | 8 | 8 | 8 | Stays silent when unsure. Two fresh stamps had dates up to 31h off |
| Ape appeal | 7 | 6.5 | 6.5 | No public scorecard |
| Solo buildability | 7.5 | 7 | 7.5 | Scope trimmed and the pipeline ran free. Stage 2 was done by hand, not by a small LLM |
| Self-serve sales | 9 | 9 | 9 | Unchanged |
| Distribution | 6 | 6.5 | 6.5 | Agent channels kept. Benchmark against Newsflash MCP + LLM not run |
| Retention | 5 | 5 | 5 | Design only |
| Money evidence | 6 | 6 | 6 | Nobody shown paying for accuracy |
| Token fit | 6 | 6 | 6 | Pump.fun check passes: hold for quota, users burn their own tokens for credits, no payouts or fee-funded buybacks, launch after 25 payers |
| **Overall** | **5.5** | **5.0** | **5.5** | Iterate zone on the blind holdout. v3 is best |

## Competitors
- No new rivals this run. Kronical and Mycroft (found 24 Oct 8:35am) are now in v3's teardown.
- Still true: no tool stamps an event's first-reported date automatically under X posts. Kronical and Newsflash `first_seen_at` do the job off X.

## Build plan
What v4 must fix, before anything else:
1. **Retrieval on claim plus entity:** query on the actor, action, figure and named report, not the headline wording.
2. **Publish time from the article page** (`article:published_time` / `datePublished`) before showing any stamp. Target: ≥80% of stamps within ±6h.
3. **Entity-swap matching for recycled claims** (Ripple ↔ XRP), plus a claim library.
4. **Run stage 2 on the real small LLM** and log the cost per check.
5. **A new, larger fresh blind holdout** (≥12 stale, ≥30 fresh) on the same lines, plus the 80-row warning check.
6. **Newsflash retrieval and the "Newsflash MCP + LLM" baseline**, only with Ethan's OK for the sign-up.

A pass on step 5 lifts the score to 6.0, the cap while nobody is shown paying.
