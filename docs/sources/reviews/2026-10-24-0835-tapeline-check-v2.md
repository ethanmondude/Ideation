# Review: Tapeline Check v2 (when did this headline actually happen, and what does the fine print get wrong?)

*Project Bot re-score · 24 Oct 2026, 8:35am AWST (Perth time) · thesis: /workspace/idea-bot/theses/2026-10-23-0900-tapeline-check-v2.md (idea bot, 23 Oct 9:00am AWST) · this is a version page: the full re-score, with the weak-spot walk-through, fact-check and token check, is the "Re-score 24 Oct 2026 8:35am AWST (v2)" section of 2026-10-22-2245-tapeline-check.md*

## Verdict
- **Score: 5.0/10 (v2). Token fit 6/10. Passes Ethan's rules gate.** **v1 stays the best version at 5.5**, so it's still 1st among rules-passing theses.
- **Why it dropped:** Trench Bot's blind same-event judge (it never saw the labels) failed at the kill line. It caught **5 of 11** stale headlines (pass is 8 or more) with **7 of 69** false flags (pass is 5 or fewer).
  - 5 of the 6 misses were retrieval failures: searching on titles alone never found the earlier story.
  - 6 of the 7 false flags were real reposts 1 to 2.5 days after the first report, which the labels don't count as stale.
  - The judge itself cut false flags from 23–38 down to 7.
- **Kept:** the X-policy cut (no public scorecard or paid-promo labels), the agent channels (MCP, x402, Grok Bot template), exact-mint resolution and the dev-tie flag.
- **Refined idea:** a "first reported" line on every market post with a **user-set staleness flag**. Retrieval uses Newsflash first-seen events plus **article ledes** and exact publish times, and we store only our own derived records (Brave's storage terms). The judge has two stages: figure/name rules, then a small LLM. It abstains rather than false-flag. Re-test on a fresh blind run.

## Score breakdown
| Category | v1 | v2 | Reason |
|---|---|---|---|
| Problem severity | 6 | 6 | No new harm evidence |
| Timing | 7 | 7 | Unchanged |
| Differentiation | 4 | 4 | The stamp failed the blind test (5 of 11). Kronical, ArcaneNews and Newsflash `first_seen_at` narrow the slot |
| Usability | 8 | 8 | Automatic, no tagging |
| Ape appeal | 7 | 6.5 | Public scorecard cut |
| Solo buildability | 7.5 | 7 | Needs licensed ledes plus an LLM stage, and the scope grew |
| Self-serve sales | 9 | 9 | Unchanged |
| Distribution | 6 | 6.5 | MCP, x402 and Grok Bot template costed. Newsflash MCP is a substitute |
| Retention | 5 | 5 | Design only |
| Money evidence | 6 | 6 | Nobody shown paying for accuracy |
| Token fit | 6 | 6 | ASIC check passes: hold for quota, burn own tokens for credits, no payouts or fee-funded buybacks |
| **Overall** | **5.5** | **5.0** | Kill line on the blind check. v1 stays best |

## Competitors
- New this run:
  - [Kronical](https://kronical.ai) separates first reports from repeat coverage, for finance teams and agents.
  - [Mycroft Media Narrative Tracker](https://github.com/Humanitariansai/Mycroft/tree/main/n8n_Workflows/Media_Narrative_Tracker) is an open-source information-age scorer.
- Confirmed:
  - [ArcaneNews](https://arcane.news/) has old-news and same-news detection inside its paid terminal.
  - [PVP Terminal](https://docs.pvpterminal.com/desktop/desktop/settings/news)'s Old News Threshold measures delivery lag.
  - [FactCheckRadar](https://chromewebstore.google.com/detail/factcheckradar/obepkghlneckiemaclcigahjnbkonhnf) is click-only and was updated 22 Oct 2026.
  - Tweet Fact Checker (demo only), Stale News Warning (0 stars) and Custom Timestamps for X (post age only).
- None stamps the event's first date automatically under X posts.

## Build plan
Next free private step:
1. Re-run the blind same-event check on the 80 rows with lede-based retrieval: Newsflash events (the free key covers 30 days) plus transient Brave News for older stories.
2. Add a small-LLM "same event / later development / same topic" stage on the top 3 candidates.
3. Set the stale line at 2 or more days.

Use a fresh blind bot or held-out rows, because this set has now been tuned on. Everything else in v2's 4-week plan stays, with the coin card trimmed to exact mint plus the pumpdata dev check. A pass lifts the score to 6.0, the cap while nobody is shown paying.
