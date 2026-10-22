# Ledgerport money test: will small SaaS teams pay now for a Sage 50 US API?

*Project Bot · written 22 Oct 2026, 10:05pm AWST · status: **draft, waiting for Ethan's OK** · sources: thesis `/workspace/idea-bot/theses/2026-10-22-1430-ledgerport.md`, review `/workspace/project-bot/reviews/2026-10-22-1445-ledgerport.md` (6.5/10, ranked 1st), `/workspace/shared-data/growth-bot/lessons.jsonl`. US$ → A$ at about 1.43 (mid-market, 22 Oct). Anything marked "est." is an estimate.*

## 1. Hypothesis (one)
Founders and CTOs of small SaaS teams (3 to 50 people) whose US customers run desktop Sage 50, mainly AI bookkeeping and AP-agent startups, plus vertical SaaS teams that maintain their own Sage 50 connector, **will pay a US$99 deposit now**. Each must also name a real Sage 50 US desktop customer ready to install within 30 days. Today there is no proof anyone pays for a Sage 50 US developer API. Conductor's US$44,163 MRR is for QuickBooks Desktop, and Daybook (UK) is pre-launch (review).

## 2. The test
- **What:** a paid pilot deposit taken through a **Stripe Payment Link** on a one-page site ("Sage 50 US API + MCP: join the sandbox"). No product gets built beyond a 3-day spike.
- **Offer:** **US$99 pilot deposit** (about A$141), credited to the first invoice. After the pilot it's US$49 per connected company file per month (Conductor's price), with 30% off for 12 months for the first 10 teams (thesis). My suggestion is to **refund the deposit in full if no sandbox ships by day 60 or the test is killed**, which lowers the barrier and keeps it clean under consumer law.
- **Every call asks:** how many Sage 50 US customers or prospects they have, whether any are on Sage-hosted "Sage 50 Cloud" (connectors can't run there), and whether they've looked at Apideck ($599/month floor) or Rutter (enterprise only).

## 3. Prospects: 40 teams, reached by email or DM from Ethan's accounts
| Channel (from the review) | Contacts (my split, est.) |
|---|---|
| AI bookkeeping and AP-agent startups that support QuickBooks Online and Xero but not desktop (YC and Product Hunt listings, their integrations pages) | 15 |
| Teams on Conductor's public logo wall (PalletWiz, CommerceAttain, Model Wiz, CloudRig and others) | 10 |
| Vertical SaaS advertising a self-built Sage 50 integration (ServiceBox, OrderEase, G2 "integrates with Sage 50", Sage US Marketplace) | 10 |
| Developers asking on Sage's SDK forum and on Reddit (public reply with a guide and sandbox link) | 5 |
US business hours are about 9pm to 7am AWST (US Eastern moves back an hour on 1 Nov), so emails get scheduled to land at 9am US Eastern and calls happen late at night in Perth.

## 4. Schedule (if approved by Sun 25 Oct, Day 1 = Mon 26 Oct)
- **Days 1 to 3 (26 to 28 Oct): spike and kit.** Windows VM plus Sage's sample company. The connector reads customers and invoices, then creates an invoice and reads it back through a local REST shim. **Day 1 first job: confirm the sample company works without the US$737 Sage 50 Pro licence.** Build the landing page and Stripe link in test mode, a private list of 40 prospects, and drafts of all outreach. Ethan reviews everything.
- **Days 4 to 7 (29 Oct to 1 Nov):** after Ethan's OK, send 10 contacts a day. Email sdk.50us@sage.com for an application ID. Check Apideck's Sage 50 US status page (a read only).
- **Days 8 to 14 (2 to 8 Nov):** one follow-up per contact, discovery calls, deposits. **Day 14 checkpoint (est.):** with 0 calls booked, stop early. With fewer than 3 booked, rewrite the pitch and move volume to the strongest channel.
- **Days 15 to 30 (9 to 24 Nov):** remaining calls, second follow-up, two guides published with Ethan's OK ("Sage 50 US API in 2026", "Sage 50 US MCP"), and an Apideck status check each week.
- **Day 30 (Tue 24 Nov): decision**, posted to the room and Ethan.

## 5. Cost (AUD)
| Item | A$ |
|---|---|
| Windows VM for the spike, 1 month (thesis: up to US$40/month, est.) | 57 |
| Domain plus landing page and docs (thesis: about US$50, est.) | 71 |
| Contingency: Stripe fees on refunds, extra VM time, FX (est.) | 50 |
| Stripe Payment Link, static hosting (GitHub Pages), outreach from Ethan's own accounts | 0 |
| **Total** | **about A$178 (est.)** |
**Deferred to the build, not in this test:** Sage 50 Pro licence US$737 (about **A$1,050**, more than the whole A$1,000 budget), code signing US$100 to 300 a year, terms and DPA template about A$500. That leaves about A$820 for the build, and the licence alone would use more than that.

## 6. Decision numbers (by Day 30, 24 Nov)
- **Pass, start the build:** 3 or more paid US$99 deposits, each naming a real Sage 50 US **desktop** customer ready to install within 30 days. Also needed: at least 10 discovery calls, at least 5 teams saying Sage 50 comes up at least monthly, and a spike that creates and reads back an invoice.
- **Iterate, one 14-day extension only (about A$60 more, est.):** exactly 2 deposits, or 3 or more where fewer than 3 named customers are desktop and ready. Add 20 contacts in the best channel. If bookkeepers rather than developers are pulling, test the review's pivot instead: an MCP connector at US$29 per company, sold straight to bookkeepers.
- **Kill (any one):** 1 or no deposits after 40 contacts. More than half the named customers on Sage-hosted Cloud. Fewer than 5 teams saying Sage 50 comes up monthly. Apideck ships Sage 50 US before Day 30 and prospects say $599 is fine. Sage refuses an application ID. Or the SDK can't be used without the paid licence.

## 7. Key risk and the early check
**Sage connector access and a shrinking base.** The SDK is 32-bit .NET only. A blank application ID works with sample companies only (Sage quick start). Apideck says access "can require a Sage ID tied to a Sage 50 licence". Sage-hosted Cloud can't run third-party software, and Sage says it's migrating customers there. **Checked early:** the Day 1 spike shows whether the sample company runs without buying the licence. The Day 4 application ID email tests Sage's willingness. Every call records how many of the prospect's customers are on Sage-hosted Cloud. Second risk: Apideck's connector, whose guide came out 17 Oct, gets a weekly status check.

## 8. Fit with Ethan's rules (flag)
The buyer is SaaS developers, not crypto tech bros, and token fit is weak (review; X bot's 4pm signal). **No token is part of this test.** A token would only come later, on pump.fun, only after paying users and only with a real token job, with Holder Rewards and Tokenized Agent buybacks off and no fee-funded buybacks or burns. Bots never launch or buy one.

## 9. Ethan approves (nothing public goes out before this)
- [ ] Run the test and spend up to about A$178 (VM, domain, contingency)
- [ ] Offer wording: US$99 deposit, credited and refundable, then US$49/file with 30% founding discount
- [ ] Working name: "Ledgerport" or another, with no "Sage" in it; descriptive "for Sage 50" only
- [ ] Landing page goes live (public) and Stripe Payment Link switches to live mode, on Ethan's own Stripe account
- [ ] The 40-contact list and the outreach email and DM text, sent from Ethan's accounts (needs Ethan's OK)
- [ ] Follow-ups 1 and 2 (needs Ethan's OK)
- [ ] Forum and Reddit replies (public, needs Ethan's OK)
- [ ] Email to sdk.50us@sage.com requesting an application ID (needs Ethan's OK)
- [ ] Publishing the 2 guides (public, needs Ethan's OK)
- [ ] Any Sage licence purchase (out of budget unless he decides otherwise)

## Amendment, 22 Oct 10:00pm AWST (from Git bot)
- **Day 0 check (before any spend):** confirm whether Rutter (and Codat) already sell a Sage 50 US desktop connector. Lead: [cyrieu/Sage50Connector](https://github.com/cyrieu/Sage50Connector), a C# tray app polling `production.rutterapi.com`, last pushed 14 Oct; owner's tie to Rutter unconfirmed. Check Rutter's and Codat's integration pages and docs.
- **Added kill/iterate trigger:** prospects who already get Sage 50 US through Rutter or Codat count toward the kill, the same as Apideck. If Rutter covers Sage 50 US, the edge narrows to the MCP sandbox and a lower price; re-price and re-pitch before Day 1, or drop the test.
