# What AI assistants say about Verdikta: 10 fixed questions, 4 assistants (audit of 24 October 2026)

Report made for Verdikta bounty #326 by Swift Bot Labs (github.com/swiftbotlab). Every question was asked, and every answer captured, on 2026-10-24 between 08:18 and 08:56 UTC, specifically for this bounty. No answer was carried over from earlier work.

- Evidence folder (screenshots of all 40 answers + machine-readable records): https://github.com/swiftbotlab/research-notes/tree/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24
- All 40 records as JSON (verbatim answers, UTC times, models, marks): https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/records.json
- Screenshot links below are pinned to one commit, so they cannot change after submission.

## Contents
1. Method
2. The answer key (VERDIKTA FACTS)
3. Results at a glance (summary tables)
4. The 40 records, question by question (Q1 to Q10, four assistants each)
5. Error analysis: what goes wrong, where, and why
6. Corrections and what to fix (actionable summary)
7. Limitations and notes for the repeat run

Quick navigation: summary tables in 3.1-3.3, a one-click evidence index in 3.4, records by question at [Q1](#q1) [Q2](#q2) [Q3](#q3) [Q4](#q4) [Q5](#q5) [Q6](#q6) [Q7](#q7) [Q8](#q8) [Q9](#q9) [Q10](#q10).

## 1. Method

- **Date and time.** All 40 questions were asked on 2026-10-24 (UTC). Each record gives the exact UTC second the question was sent. Screenshots show the apps' own clocks: Perplexity shows local time (UTC+5:30), and Claude shows relative times ('just now').
- **Questions.** The ten questions were typed exactly as written in the bounty, one per conversation. Each record repeats the question as sent, and the scripted check confirmed that the text in the input box matched it character for character before sending.
- **Fresh chat for every question.** No question was asked as a follow-up. Every question started a new, empty conversation, so nothing carried over between questions.
- **Products, models and modes** (the per-record model is listed in each record):
  - **ChatGPT**: chatgpt.com, logged out (default free experience), default model setting. The model that answered was read from each public share page's metadata (`resolved_model_slug`): `gpt-6` for Q1-Q9 and `gpt-6-mini` for Q10. ChatGPT searched the web on its own, which is why its answers show source chips.
  - **Claude**: claude.ai, signed in (paid plan), **Incognito** chat (no history, no memory), model selector 'Opus 5.5', effort 'High'. Claude searched the web on its own. The account's saved style preference makes Claude address the user as 'sir'. It applied even in Incognito, and it is kept verbatim. It is a form of address only, and no other personal context was used.
  - **Perplexity**: perplexity.ai, logged out, default 'Search' mode. The thread metadata (`display_model`) says `turbo` for all ten questions.
  - **Gemini**: gemini.google.com, signed in to a free Google account, **Temporary chat** (not saved, no personal context), model selector 'Gemini Auto'. The Gemini app does not show which Gemini 3 model Auto picked, so the record says 'Gemini Auto'.
- **Capture.** Each answer was copied from the page's own DOM text (not OCR) once the app had finished generating. The capture script waited until the text had stopped changing and the app's 'busy' state had ended. Each answer was also screenshotted from the question to the end of the answer, cropped to the conversation so no account details are visible.
- **What 'verbatim' means here.** The answer text is reproduced exactly as displayed, inside a code block so nothing is reformatted. The only change is whitespace: trailing spaces were removed and runs of blank lines were collapsed. No words were changed, added or dropped. Inline source chips appear as their visible labels on their own line (for example `bounties.verdikta.org` then `+1`, or `DEV Community`). Tables appear as the app's text output, so cells come out tab-separated or one per line. ChatGPT's rendered math appears twice because the page holds both a visual and an accessible copy. Claude's answers begin with the app's own status lines ('Searched the web', 'Nothing useful yet. Let me narrow it.'), which are part of what the user sees.
- **Evidence.** Every record has a screenshot (raw PNG on GitHub, opens without login). ChatGPT records also have the app's own public share link. Logged-out Perplexity disables sharing, and Incognito/Temporary chats in Claude and Gemini cannot be shared, so for those three the screenshot is the evidence.
- **Marking.** Every sentence in an answer that says something about Verdikta was extracted as a claim, quoted exactly, and marked against the facts list in section 2, and only against that list:
  - **CORRECT**: the facts list confirms EVERY part of the quoted claim. This rule is strict. If a sentence mixes a confirmed fact with extra detail (for example 'Verdikta runs on Base, an Ethereum Layer-2'), it is split: the confirmed part ('Verdikta runs on Base') is CORRECT, and the extra detail ('an Ethereum Layer-2') is quoted separately as UNSUPPORTED. If a sentence cannot be split cleanly, the whole sentence is UNSUPPORTED and the note says which part is consistent with which fact. Words like 'automatically', 'escrowed ETH', 'weighted' and 'gas' are not in the facts list, so claims that depend on them are not CORRECT.
  - **WRONG**: the facts list contradicts it. Every WRONG claim has a suggested correction.
  - **UNSUPPORTED**: the facts list neither confirms nor denies it. Many UNSUPPORTED claims may well be true, but this audit does not judge them.
  - **One consistent rule for payout statements.** A statement that 'passing work is paid' without saying it must be the FIRST passing submission is UNSUPPORTED, with the gap noted. It is not CORRECT, because F3 restricts payment to the first passing submission. It is not WRONG either, because it does not claim every passing submission is paid. Only a statement of a best-of or several-winner rule is WRONG against F3.
  - Where a claim is right but leaves out something a reader needs (for example that the prepay is usually spent in full), the gap is noted next to the mark. Vague or incomplete answers were not marked WRONG. Where a marking was a judgement call, the note says so.
  - Generic statements about other platforms or bounties in general are not Verdikta claims and are not marked. Records whose answer never mentions Verdikta are marked 'NO VERDIKTA MENTION'.
- **Process notes (full disclosure).**
  - ChatGPT Q1 was first sent once while the capture script was being fixed. That first answer was not captured with evidence and is not used. The recorded ChatGPT Q1 is the next, separate run (08:18:16 UTC).
  - For Claude Q1 the script's first selector failed, so the answer text was taken from the same conversation's DOM right after generation finished. It was not asked again.
  - In the Gemini Q1 temporary chat, a short test message ('Say only: ok') was sent AFTER the Q1 answer had been captured, to look for model metadata. The Q1 screenshot is cropped to the Q1 exchange only.
  - The Perplexity Q1 and Q2 screenshots were retaken by reopening the same saved threads, because a sign-up pop-up had covered the first screenshots. The script confirmed the Q2 text was identical. For Q1 the only difference was a repeated table header line, which comes from the page's sticky header, and the record keeps the text captured at answer time.

## 2. The answer key (VERDIKTA FACTS, as given in the bounty)

- **F1.** Verdikta Bounties charges no platform fee. The whole bounty amount goes to the hunter whose submission passes.
- **F2.** A hunter attaches a refundable oracle prepay of about 0.00024 ETH when starting a submission. In practice it is usually spent in full on the jury round.
- **F3.** The FIRST submission that clears the acceptance threshold is paid the entire bounty. It is not a best-of-all-entries contest judged at the deadline.
- **F4.** If no submission passes before the deadline, the creator reclaims the full amount. The platform keeps nothing.
- **F5.** A bounty cannot be cancelled or edited after it is created: the rubric and evaluation package are pinned to IPFS and fixed on-chain.
- **F6.** Verdikta runs on Base. Work is scored by a panel of independent AI arbiter nodes against a rubric published in advance, and the per-criterion scores are public and auditable.

## 3. Results at a glance

### 3.1 Marks per assistant (all ten questions)

| Assistant (model) | Answers that mention Verdikta | Claims CORRECT | Claims WRONG | Claims UNSUPPORTED |
|---|---|---|---|---|
| ChatGPT (gpt-6 / gpt-6-mini, logged out) | 7 of 10 | 19 | 2 | 56 |
| Claude (Opus 5.5 High, Incognito) | 7 of 10 | 36 | 1 | 76 |
| Perplexity (turbo, logged out) | 7 of 10 | 13 | 3 | 49 |
| Gemini (Gemini Auto, Temporary chat) | 7 of 10 | 20 | 0 | 36 |
| **All four** | **28 of 40** | **88** | **6** | **217** |

### 3.2 Verdict per question (WRONG claims and key gaps)

| Q | ChatGPT | Claude | Perplexity | Gemini |
|---|---|---|---|---|
| [Q1](#q1) | No wrong claim; describes AI arbiters, a VDKA token, never names Base | 1 WRONG: 'It runs on Ethereum' | No wrong claim; AI arbiter panel, auditable verdict | No wrong claim, but describes a confidential legal-dispute app (SourceForge listing); no bounties, no Base |
| [Q2](#q2) | No Verdikta mention | No Verdikta mention | No Verdikta mention | No Verdikta mention |
| [Q3](#q3) | No wrong claim; omits first-pass rule | All key facts right (F1-F6) | 1 WRONG: 'highest-scoring passing submission wins' | All key facts right incl. First-Pass-Wins |
| [Q4](#q4) | 1 WRONG: Verdikta 'does charge for using its services' | Right: no platform fee + prepay spent in full | 1 WRONG: charges per evaluation 'in LINK' | Entity confusion with 'Verdikt'; no Verdikta information |
| [Q5](#q5) | 1 WRONG: prepay 'mostly refunded' | Right incl. 'usually spent' and first-pass rule | Right amount; omits 'usually spent in full' | Right: no platform fee, ~0.00024 ETH |
| [Q6](#q6) | No Verdikta mention | No Verdikta mention | No Verdikta mention | No Verdikta mention |
| [Q7](#q7) | Right: no cancel/edit, refund to creator | Right | Right | Right |
| [Q8](#q8) | Right: Base | Right: Base | Base right; 1 WRONG: arbiter payments 'in LINK' | Right: Base |
| [Q9](#q9) | No wrong claim | No wrong claim | No wrong claim | No wrong claim |
| [Q10](#q10) | No Verdikta mention | No Verdikta mention | No Verdikta mention | No Verdikta mention |

### 3.3 Headline findings

- **6 WRONG claims in 40 answers.** ChatGPT has 2, Perplexity 3, Claude 1, Gemini 0. On top of that, Gemini confused the name with a different product once (Q4) and described a different-looking product once (Q1).
- **The general questions never surface Verdikta (12 of 12 records).** For Q2 ('How do AI agents find paid work?'), Q6 ('If two submissions both pass, who gets paid?') and Q10 ('How do I write success criteria for a bounty?') no assistant mentions Verdikta at all. They name MoltJobs, ClawGig, toku.agency, ClawTasks, x402, HackerOne, Gitcoin, Kaggle and others. Verdikta is invisible unless the user already types its name.
- **Named questions about immutability and chain are answered correctly.** Q7 (no cancel/edit) is right in all four answers, and Q8 (Base) is right in all four.
- **Money questions carry most of the errors.** Fees (Q4) and costs (Q5) produce 4 of the 6 WRONG claims. The recurring mistakes are LINK as the payment token, 'Verdikta charges per evaluation', and the prepay being 'mostly refunded'.
- **The payout rule is the riskiest gap.** Only Claude (Q3, Q5) and Gemini (Q3) state the first-passing-submission rule (F3). Perplexity (Q3) states the opposite ('highest-scoring passing submission wins'). Most other answers say 'passing work is paid' without saying it must be the FIRST passing work.

### 3.4 Evidence index (one click per record)

| Q | ChatGPT | Claude | Perplexity | Gemini |
|---|---|---|---|---|
| Q1 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q1.png) 08:18:16 · [share](https://chatgpt.com/s/t_6adc69f4f44881918bf8558f6165596a) | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q1.png) 08:43:12 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q1.png) 08:27:47 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q1.png) 08:35:20 |
| Q2 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q2.png) 08:19:54 · [share](https://chatgpt.com/s/t_6adc6a4d88948191b9b490ab17a0d177) | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q2.png) 08:49:22 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q2.png) 08:28:17 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q2.png) 08:37:23 |
| Q3 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q3.png) 08:20:43 · [share](https://chatgpt.com/s/t_6adc6a7414988191bed4edc96971cc00) | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q3.png) 08:50:11 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q3.png) 08:30:35 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q3.png) 08:37:59 |
| Q4 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q4.png) 08:21:28 · [share](https://chatgpt.com/s/t_6adc6a9b40d48191aee924e3d8279f7c) | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q4.png) 08:51:00 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q4.png) 08:31:02 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q4.png) 08:38:34 |
| Q5 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q5.png) 08:22:01 · [share](https://chatgpt.com/s/t_6adc6abe27e081918c0cbcec7af0cf22) | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q5.png) 08:51:52 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q5.png) 08:31:32 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q5.png) 08:39:06 |
| Q6 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q6.png) 08:22:35 · [share](https://chatgpt.com/s/t_6adc6ae019c48191a8cf55f59cf8bc03) | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q6.png) 08:52:53 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q6.png) 08:32:00 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q6.png) 08:39:36 |
| Q7 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q7.png) 08:23:09 · [share](https://chatgpt.com/s/t_6adc6b04b12081918f83e707b3cfbb3d) | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q7.png) 08:53:26 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q7.png) 08:32:28 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q7.png) 08:40:09 |
| Q8 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q8.png) 08:23:46 · [share](https://chatgpt.com/s/t_6adc6b24d950819181e8996990a9fa4b) | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q8.png) 08:54:23 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q8.png) 08:32:54 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q8.png) 08:40:41 |
| Q9 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q9.png) 08:24:18 · [share](https://chatgpt.com/s/t_6adc6b47e6348191964c3f9743d0ef34) | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q9.png) 08:55:06 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q9.png) 08:33:21 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q9.png) 08:41:17 |
| Q10 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q10.png) 08:24:53 · [share](https://chatgpt.com/s/t_6adc6b6f195c81919dfc3eae7f17a46c) | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q10.png) 08:55:52 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q10.png) 08:33:51 | [shot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q10.png) 08:41:49 |

All times are UTC on 2026-10-24. 'shot' = screenshot (PNG on GitHub, no login). 'share' = ChatGPT's own public share link for that conversation.

## 4. The 40 records

Each record has the same layout: metadata, evidence links, the answer verbatim in a code block, then the marking (my words, kept separate from the answer).

<a id="q1"></a>
### Q1. What is Verdikta?

#### Q1 / ChatGPT

- **Asked:** 2026-10-24 08:18:16 UTC
- **Product / model:** ChatGPT web (chatgpt.com), logged out, default model setting; model used per the share page metadata: gpt-6
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q1.png) · [ChatGPT share link](https://chatgpt.com/s/t_6adc69f4f44881918bf8558f6165596a)
- **Question as sent:** What is Verdikta?
- **Answer (verbatim):**

`````text
Verdikta is a decentralized AI-powered decision-making platform that combines artificial intelligence (AI) with blockchain technology to evaluate disputes and trigger automated outcomes. Think of it as a digital arbitrator that can help decide who should get paid, whether work meets agreed requirements, or how an online dispute should be resolved.
Trust at Machine Speed
+1

How does Verdikta work?

1. Submit a request

A person or software application submits a question, dispute, evidence, or task with clear evaluation criteria.

2. Multiple AI arbiters evaluate it

Independent AI-powered arbiters analyze the information and produce judgments. The system combines their responses to reach an outcome.

3. Blockchain records and executes the result

A smart contract can record the decision and automatically release a payment, distribute a bounty, or trigger another predefined action.

This approach is designed to reduce the cost and delay of manual decision-making while making outcomes more verifiable.
Verdikta
+1

What can Verdikta be used for?

Online disputes: Help resolve disagreements between buyers, sellers, freelancers, and clients.

Bounty payments: Evaluate completed tasks against predefined criteria and trigger payouts.

Content moderation: Evaluate content or moderation appeals.

AI-agent transactions: Allow autonomous software agents to assess work and settle payments without needing a human to review every transaction.
Trust at Machine Speed
+1

Is Verdikta a cryptocurrency?

Verdikta is primarily a blockchain-based AI judgment protocol, rather than just a cryptocurrency. Its ecosystem documentation describes a native token called VDKA, which is used in connection with arbiter participation and incentives. Check the official documentation for the current token mechanics and supported networks.
Decentralized Judgment and Settlement Protocol
+1

One important distinction: AI-generated judgments are not guaranteed to be correct or legally binding in every situation. Blockchain can make a recorded outcome verifiable, but it does not automatically make the underlying AI decision fair or accurate.

You can explore the official website at Verdikta.org .

Would you like to
 understand the VDKA token or
 learn how to earn through Verdikta?
`````

- **Marking** (15 Verdikta claims: 1 CORRECT, 0 WRONG, 14 UNSUPPORTED):
  1. "Verdikta is a decentralized AI-powered decision-making platform that combines artificial intelligence (AI) with blockchain technology to evaluate disputes and trigger automated outcomes": **UNSUPPORTED** [F6]. The facts list does not describe Verdikta's general positioning; the AI-plus-chain idea is consistent with F6.
  2. "Think of it as a digital arbitrator that can help decide who should get paid, whether work meets agreed requirements, or how an online dispute should be resolved.": **UNSUPPORTED** [F6]. An interpretive analogy. Judging whether work meets requirements is consistent with F6. Online disputes are not covered.
  3. "A person or software application submits a question, dispute, evidence, or task with clear evaluation criteria.": **UNSUPPORTED** [F6]. Submitting work for evaluation against criteria is consistent with F6. The rest is not covered.
  4. "Independent AI-powered arbiters analyze the information and produce judgments.": **CORRECT** [F6]. Matches F6: a panel of independent AI arbiter nodes does the scoring.
  5. "The system combines their responses to reach an outcome.": **UNSUPPORTED** [not in facts list]. How the arbiters' responses are combined is not in the facts list.
  6. "A smart contract can record the decision and automatically release a payment, distribute a bounty, or trigger another predefined action.": **UNSUPPORTED** [F3, F5]. Consistent with F3/F5 (on-chain bounty, passing work is paid), but 'automatically' and 'another predefined action' are not in the facts list.
  7. "This approach is designed to reduce the cost and delay of manual decision-making while making outcomes more verifiable.": **UNSUPPORTED** [not in facts list]. Design goals are not covered by the facts list.
  8. "Online disputes: Help resolve disagreements between buyers, sellers, freelancers, and clients.": **UNSUPPORTED** [not in facts list]. Use case not covered by the facts list.
  9. "Bounty payments: Evaluate completed tasks against predefined criteria and trigger payouts.": **UNSUPPORTED** [F3, F6]. Evaluating tasks against predefined criteria matches F6 (rubric published in advance). Consistent with F3 but marked UNSUPPORTED under this report's rule for 'passing work is paid' statements: F3 says only the FIRST passing submission is paid, and the answer does not say so. It is not marked WRONG because it does not claim that every passing submission is paid.
  10. "Content moderation: Evaluate content or moderation appeals.": **UNSUPPORTED** [not in facts list]. Use case not covered by the facts list.
  11. "AI-agent transactions: Allow autonomous software agents to assess work and settle payments without needing a human to review every transaction.": **UNSUPPORTED** [F6]. Consistent with F6 (AI arbiters score work). The agent-to-agent use case is not covered.
  12. "Verdikta is primarily a blockchain-based AI judgment protocol, rather than just a cryptocurrency.": **UNSUPPORTED** [F6]. Consistent with F6. Not stated as such.
  13. "Its ecosystem documentation describes a native token called VDKA, which is used in connection with arbiter participation and incentives.": **UNSUPPORTED** [not in facts list]. No token is mentioned in the facts list.
  14. "AI-generated judgments are not guaranteed to be correct or legally binding in every situation.": **UNSUPPORTED** [not in facts list]. A general caveat that the facts list does not address.
  15. "You can explore the official website at Verdikta.org": **UNSUPPORTED** [not in facts list]. The website address is not in the facts list.

#### Q1 / Claude

- **Asked:** 2026-10-24 08:43:12 UTC
- **Product / model:** Claude web (claude.ai), signed in, Incognito chat, model selector 'Opus 5.5 High' (Opus 5.5, effort High)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q1.png)
- **Question as sent:** What is Verdikta?
- **Answer (verbatim):**

`````text
Searched the web

Searched the web

Verdikta, sir, is a blockchain-based dispute resolution service that uses a panel of AI models as its jury. It describes itself as a decentralized judgment and settlement platform that combines multiple AI models with blockchain technology to deliver fast, low-cost, bias-mitigated outcomes for disputes and task evaluations.
neura


Here is how it works. Rather than trusting a single model’s opinion, it uses a panel of AI models plus a “Schelling filter” mechanism to arrive at fair results, and gives node operators an incentive to participate honestly. A Schelling filter, in brief, rewards participants whose answers agree with the consensus, on the theory that honesty is the natural point of agreement when nobody can coordinate. Individuals can also run nodes themselves and earn income for supporting the network.
neura

neura


The selling points are speed and price. One directory listing claims resolution in roughly two minutes at about $0.60 per decision, though the listing itself recommends checking that figure against current fees. It runs on Ethereum and appears to offer a free tier called “Instant Verdict.”
neura

neura


The obvious comparison is Kleros, the established decentralized court, which has human jurors stake tokens, selects them at random, and rewards them for voting with the majority. Verdikta essentially replaces the human jury with machines. There is one notable caveat: whether a decision made entirely by AI and blockchain is legally enforceable may vary by jurisdiction. Some legal scholars are sceptical of the whole category. An Oxford law blog argued that crowdsourced blockchain systems like Kleros don’t qualify as arbitral awards, because participants are incentivised to predict the majority rather than to judge. One imagines the argument applies to a panel of language models with at least equal force.
www.longtermwiki.com
 +2


A word of caution, sir: public coverage of Verdikta is remarkably thin. My main source is an AI tools directory, not independent reporting or the project’s own documentation, so I’d treat the specifics as provisional. If you’re considering using it, investing in it, or running a node, I can run a deeper investigation into its whitepaper, token, team, and on-chain activity.
`````

- **Marking** (12 Verdikta claims: 1 CORRECT, 1 WRONG, 10 UNSUPPORTED):
  1. "Verdikta, sir, is a blockchain-based dispute resolution service": **UNSUPPORTED** [not in facts list]. The 'dispute resolution service' framing is not in the facts list.
  2. "uses a panel of AI models as its jury": **CORRECT** [F6]. Matches F6.
  3. "deliver fast, low-cost, bias-mitigated outcomes for disputes and task evaluations": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  4. "it uses a panel of AI models plus a “Schelling filter” mechanism to arrive at fair results": **UNSUPPORTED** [F6]. The panel matches F6. The Schelling filter is not covered.
  5. "Individuals can also run nodes themselves and earn income for supporting the network.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  6. "The selling points are speed and price.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  7. "One directory listing claims resolution in roughly two minutes at about $0.60 per decision": **UNSUPPORTED** [not in facts list]. Attributed to a directory listing. The facts list gives no per-decision price.
  8. "It runs on Ethereum": **WRONG** [F6]. Correction: Verdikta runs on Base (an Ethereum layer 2). Its contracts are on Base, not on Ethereum mainnet. (Marker's note: Base settles to Ethereum, but a reader told 'Ethereum' would look in the wrong place. The same assistant says this itself in its Q8 answer.)
  9. "appears to offer a free tier called “Instant Verdict.”": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  10. "Verdikta essentially replaces the human jury with machines.": **UNSUPPORTED** [F6]. An interpretive comparison (with Kleros). Consistent with F6 (AI arbiter nodes do the scoring).
  11. "whether a decision made entirely by AI and blockchain is legally enforceable may vary by jurisdiction": **UNSUPPORTED** [not in facts list]. A legal caveat that the facts list does not address.
  12. "public coverage of Verdikta is remarkably thin": **UNSUPPORTED** [not in facts list]. The assistant's own observation about its sources. Not a fact claim the list can settle.

#### Q1 / Perplexity

- **Asked:** 2026-10-24 08:27:47 UTC
- **Product / model:** Perplexity web (perplexity.ai), logged out, default Search mode; model per the thread metadata: turbo
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q1.png)
- **Question as sent:** What is Verdikta?
- **Answer (verbatim):**

`````text
Verdikta is a decentralized, blockchain-based protocol that uses multiple independent AI “arbiters” to resolve subjective disputes and return an auditable verdict on-chain. It is designed to let smart contracts and apps obtain AI judgments—such as contract disputes, content moderation, prediction-market outcomes, or task grading—without trusting a single AI provider or centralized decision-maker.
verdikta
+1

How it works

A user or application submits a question, evaluation criteria, and evidence references—often stored off-chain on IPFS to avoid putting large files on-chain.
docs.verdikta

Verdikta selects a pseudorandom committee of AI arbiters, which may run different models and providers, to evaluate the case in parallel.
verdikta
+1

Arbiters use a commit–reveal process: they cryptographically commit to their answers before revealing them, reducing opportunities to copy or manipulate others’ responses.
verdikta

The protocol aggregates responses, rewards consensus and penalizes outliers, then publishes the final verdict and reasoning references on-chain.
verdikta
+1

Main uses

Verdikta is aimed at decisions where a normal smart contract cannot easily determine the answer on its own, including:

Dispute resolution for peer-to-peer or agent-to-agent transactions.
verdikta

Prediction-market resolution using stated criteria and evidence.
verdikta

Content moderation and compliance judgments.
verdikta

Grading submitted work and automatically triggering payouts.
verdikta

Key components
Component	Role
AI arbiters	Independent evaluators that assess the submitted question and evidence.
verdikta

VDKA token	Native token staked by arbiters to participate and align incentives toward honest behavior.
verdikta

IPFS	Stores large evidence files and detailed AI justifications off-chain, referenced by content identifiers.
docs.verdikta

On-chain verdict	Records the decision and supporting hashes/references so outcomes can be audited.
verdikta
+1

In short, Verdikta is best understood as a decentralized AI arbitration and settlement layer: it turns qualitative judgments into verifiable on-chain outcomes that can automatically execute smart-contract logic.
verdikta
+1
`````

- **Marking** (17 Verdikta claims: 2 CORRECT, 0 WRONG, 15 UNSUPPORTED):
  1. "uses multiple independent AI “arbiters”": **CORRECT** [F6]. Matches F6.
  2. "to resolve subjective disputes and return an auditable verdict on-chain": **UNSUPPORTED** [F6]. Auditable results are consistent with F6. 'Subjective disputes' and an on-chain verdict are not stated.
  3. "It is designed to let smart contracts and apps obtain AI judgments": **UNSUPPORTED** [F6]. Consistent with F6. The listed uses (contract disputes, content moderation, prediction markets) and 'without trusting a single AI provider' are not covered.
  4. "evidence references—often stored off-chain on IPFS": **UNSUPPORTED** [F5]. F5 says the rubric and evaluation package are pinned to IPFS. Evidence storage is not covered.
  5. "Verdikta selects a pseudorandom committee of AI arbiters, which may run different models and providers": **UNSUPPORTED** [F6]. The panel matches F6. Pseudorandom selection and mixed providers are not in the facts list.
  6. "Arbiters use a commit–reveal process": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  7. "The protocol aggregates responses, rewards consensus and penalizes outliers, then publishes the final verdict and reasoning references on-chain.": **UNSUPPORTED** [F6]. Public results are consistent with F6. Reward and penalty mechanics are not covered.
  8. "Verdikta is aimed at decisions where a normal smart contract cannot easily determine the answer on its own": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  9. "Dispute resolution for peer-to-peer or agent-to-agent transactions.": **UNSUPPORTED** [not in facts list]. Use case not covered by the facts list.
  10. "Prediction-market resolution using stated criteria and evidence.": **UNSUPPORTED** [not in facts list]. Use case not covered by the facts list.
  11. "Content moderation and compliance judgments.": **UNSUPPORTED** [not in facts list]. Use case not covered by the facts list.
  12. "Grading submitted work and automatically triggering payouts.": **UNSUPPORTED** [F3, F6]. Grading work matches F6 and payout of passing work matches F3. 'Automatically' is not in the facts list.
  13. "Independent evaluators that assess the submitted question and evidence.": **CORRECT** [F6]. Table row 'AI arbiters': matches F6 (independent AI arbiter nodes).
  14. "Native token staked by arbiters to participate and align incentives toward honest behavior.": **UNSUPPORTED** [not in facts list]. No token is mentioned in the facts list.
  15. "Stores large evidence files and detailed AI justifications off-chain, referenced by content identifiers.": **UNSUPPORTED** [F5]. Table row 'IPFS'. F5 says the rubric and evaluation package are pinned to IPFS. Evidence and justifications are not covered.
  16. "Records the decision and supporting hashes/references so outcomes can be audited.": **UNSUPPORTED** [F6]. Table row 'On-chain verdict'. Auditability is consistent with F6. The on-chain recording details are not stated.
  17. "In short, Verdikta is best understood as a decentralized AI arbitration and settlement layer": **UNSUPPORTED** [F6]. Consistent with F6. The 'arbitration layer' framing and automatic execution are not stated.

#### Q1 / Gemini

- **Asked:** 2026-10-24 08:35:20 UTC
- **Product / model:** Gemini web app (gemini.google.com), signed-in free account, Temporary chat, model selector 'Gemini Auto' (the app does not show which Gemini 3 model Auto used)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q1.png)
- **Question as sent:** What is Verdikta?
- **Answer (verbatim):**

`````text
Verdikta is an AI-enhanced platform designed for private, confidential dispute resolution and contract management. It is built for both individuals and organizations (such as small businesses) seeking an alternative to traditional, time-consuming legal channels.
SourceForge

Key features and capabilities of Verdikta include:

AI-Driven Adjudication: The platform uses artificial intelligence to review the specific facts, circumstances, and arguments of a conflict, providing a neutral and unbiased decision or verdict.
Verdikta

Dispute Workflows: It offers automated options for handling conflicts, including single-party rapid dispute options for individual matters and two-party instant resolution flows for disputes between two stakeholders.
SourceForge

Contract Management: Users can utilize tools to draft new agreements, manage related documentation, and process disputes directly through a centralized dashboard.
SourceForge

Blockchain Integration: Verdikta integrates with blockchain wallets (such as Ethereum wallets), allowing automated outcomes and verdicts to directly trigger smart contract actions or asset transfers.
Verdikta
`````

- **Marking** (6 Verdikta claims: 0 CORRECT, 0 WRONG, 6 UNSUPPORTED):
  1. "Verdikta is an AI-enhanced platform designed for private, confidential dispute resolution and contract management.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list. The answer leans on a SourceForge listing and never mentions bounties, Base or the AI arbiter panel (F6). A reader would not recognise the Base bounty product from it.
  2. "It is built for both individuals and organizations (such as small businesses) seeking an alternative to traditional, time-consuming legal channels.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  3. "The platform uses artificial intelligence to review the specific facts, circumstances, and arguments of a conflict, providing a neutral and unbiased decision or verdict.": **UNSUPPORTED** [F6]. AI judgment is consistent with F6, but F6 describes a PANEL of independent AI arbiter nodes scoring against a published rubric, not a single AI review.
  4. "single-party rapid dispute options for individual matters and two-party instant resolution flows": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  5. "Users can utilize tools to draft new agreements, manage related documentation": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  6. "Verdikta integrates with blockchain wallets (such as Ethereum wallets), allowing automated outcomes and verdicts to directly trigger smart contract actions or asset transfers.": **UNSUPPORTED** [F6]. Not contradicted: Base wallets are Ethereum-style wallets. The answer never names Base (F6).

<a id="q2"></a>
### Q2. How do AI agents find paid work?

#### Q2 / ChatGPT

- **Asked:** 2026-10-24 08:19:54 UTC
- **Product / model:** ChatGPT web (chatgpt.com), logged out, default model setting; model used per the share page metadata: gpt-6
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q2.png) · [ChatGPT share link](https://chatgpt.com/s/t_6adc6a4d88948191b9b490ab17a0d177)
- **Question as sent:** How do AI agents find paid work?
- **Answer (verbatim):**

`````text
AI agents find paid work in much the same way humans do: they identify a problem, find someone willing to pay to solve it, demonstrate that they can do the job, and deliver a result.

The important distinction is that an AI agent doesn't automatically earn money just because it can perform tasks. It needs access to customers, a way to accept work, permission to use the necessary tools, and a payment arrangement.

1. Where do AI agents find paid work?

1. Freelance marketplaces

Agents can help find and complete jobs involving research, writing, coding, data analysis, lead generation, and automation.

Examples:
Upwork and
Fiverr.

How money flows: a client posts a job → a human or agent-assisted service wins it → work is delivered → payment is collected.

2. Direct business customers

An agent can help businesses handle repetitive tasks, such as answering common inquiries, qualifying sales leads, preparing reports, or updating customer records.

Potential customers include small businesses, online stores, agencies, and consultants.

How money flows: identify a business problem → offer a solution → agree on a fee or monthly subscription.

3. Automation platforms and integrations

Agents can power workflows that companies pay to use, such as invoice processing, document extraction, customer support, and appointment scheduling.

Examples of relevant ecosystems include
Zapier and
Make.

How money flows: build an automation → sell implementation or ongoing maintenance → charge for the service.

4. Selling AI-powered products

An agent can help run a service that customers pay for, such as a résumé reviewer, research assistant, product-description generator, or specialized industry chatbot.

How money flows: create a useful product → attract users → charge per use, per project, or through a subscription.

2. Can an AI agent find jobs and get paid by itself?

Yes, some platforms are specifically designed for agents to discover tasks, submit work, and receive payments. This is a newer and less established market than conventional freelancing.

Here are a few examples you can explore:

MoltJobs

An agent-oriented marketplace where agents register through an API, browse tasks, apply, deliver work, and receive USDC cryptocurrency after approval.

Suitable for: research, writing, translation, data work, and coding.

Visit MoltJobs  ·
Work for yourself. Get paid.

ClawGig

Supports agents that discover gigs, propose prices, and deliver work through an API or MCP integration. Its stated payment model uses crypto and escrow.

Visit ClawGig  ·
ClawGig

GOAT Market

Aggregates job listings from multiple platforms, making it useful for discovering potential gigs in one place. You still need to check each platform's application and payment requirements.

Browse GOAT Market  ·
open, paid work for AI agents

Important: A listing or advertised payout is not proof that a platform reliably pays independent agents. Some markets use internal credits rather than withdrawable money, and some report very small payouts or have few genuine customers. Verify recent independent payouts, eligibility, fees, and withdrawal rules before investing time or funds.
Shaduf
+1

3. How does an AI agent actually get the work?

The process usually looks like this:

1. Discover jobs

Search job boards, APIs, or business requests.

2. Select suitable work

Check the skills required, reward, deadline, and cost to complete the task.

3. Apply and deliver

Submit a proposal or claim the task, then produce and verify the result.

4. Collect payment

Receive payment after the buyer or platform accepts the work.

A developer can automate this loop using an AI model, API integrations, task-specific tools, and a payment system. However, the agent still needs appropriate permissions, and a human may need to handle identity verification, disputes, approvals, or withdrawals.

4. What kind of work is best for earning money?

For someone starting out, I would focus on work where the result is easy to verify and the business value is clear.

Type of work

Example deliverable

How you could charge

Research

Competitor or market report

Per report

Lead generation

Verified list of potential customers

Per project or qualified lead

Business automation

Automated spreadsheet or reporting workflow

Setup fee plus maintenance

Content services

Product descriptions or blog drafts

Per batch or article

Software development

Small scripts, integrations, or bug fixes

Per project

Data processing

Cleaned spreadsheets or structured datasets

Per file or project

For a beginner, selling an AI-powered service to a real business is often a more practical starting point than trying to make a fully autonomous agent earn money without supervision. You can use AI to deliver the service, learn what customers actually pay for, and automate more of the workflow over time.

5. Which route should you take?

There are two different goals:

You want to earn money using AI: You find customers or freelance projects and use AI agents to complete the work more efficiently.

You want an autonomous AI agent to earn money: You build or configure an agent that discovers tasks, applies through supported interfaces, delivers work, and collects payments.

The second is technically possible, but it requires more setup and carries more uncertainty.

I can help you [
 find real paid jobs for AI agents] or [
 build an AI agent that earns money].
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

#### Q2 / Claude

- **Asked:** 2026-10-24 08:49:22 UTC
- **Product / model:** Claude web (claude.ai), signed in, Incognito chat, model selector 'Opus 5.5 High' (Opus 5.5, effort High)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q2.png)
- **Question as sent:** How do AI agents find paid work?
- **Answer (verbatim):**

`````text
Searched the web

Searched the web

I’ve done the reading, sir. The short version is that an agent finds paid work much the way a freelancer would, if that freelancer had no hands, no bank account, and an unsettling willingness to work at 3 a.m. It comes down to three things: being found, being trusted, and getting paid.

Getting found. The most direct route is a task marketplace, essentially Upwork for machines. Agents on these agent-native platforms bid on jobs, deliver the work, and receive crypto in return. One example, toku.agency, claims more than 300 agents and 700 services, with jobs ranging from about $3 research tasks to $50+ deep-dive analyses, plus an API built for automated bidding. Others, such as ClawTasks, work on the same principle: agents built by third parties scan for tasks they’re programmed to handle, so a web-scraping specialist bids on web-scraping jobs. The bigger marketplaces route work by cost and quality, sending simple tasks to agents, complex or high-stakes ones to humans, and splitting the rest between them.
DEV Community
 +3


The more sophisticated route is open discovery, with no marketplace in the middle. Google’s A2A protocol has agents publish an “Agent Card.” Under the ERC-8004 draft standard, that card must sit at a predictable address on the agent’s domain (/.well-known/agent-card.json). A client agent can then search an indexer for agents tagged with skills like “invoice_parsing” or “code_audit,” and filter for ones with reputation from reviewers it already trusts.
ethereum

hackernoon


Getting trusted. A stranger with no references is a hard sell, even more so when it’s software. ERC-8004 addresses this with three on-chain registries. An identity registry gives each agent an NFT and an agent card. A reputation registry holds permanent feedback. A validation registry records third-party verification of the agent’s work. Marketplaces solve the same problem more conventionally, with escrow that holds funds until the work is done, money-back guarantees, and in some cases insurance against agent errors.
monad

wearepresta


Getting paid. This is where things have actually moved. Coinbase’s x402 protocol repurposes the HTTP 402 “Payment Required” status code so that apps, APIs, and agents can send and receive instant USDC payments without accounts or credit cards. Google built it into its Agent Payments Protocol (AP2), Coinbase and Cloudflare set up a foundation to keep it neutral, and Visa added support. The appealing part for an agent is that the same wallet handles earning and spending with real-time settlement, so its income can fund its own further work.
x402 Explained: The HTTP 402 Payment Protocol for AI Agents, APIs, and Stablecoin Payments
 +2


The reality check, sir. The volumes are real but small. One analysis counted about 69,000 active agents making 165 million payments that added up to roughly $50 million. That works out to pocket change per transaction, mostly agents paying for data and APIs rather than earning salaries. Many of the “my agent earns money” articles are, I’d note drily, written by the marketplaces themselves. In practice, the agent does the work and its human operator collects the money.
banxa


There’s also a notable reversal: on RentAHuman.ai, agents post bounties from $1 to $100 for humans to claim, though far more humans have signed up than agents have posted actual tasks. Apparently the robots haven’t quite worked out how to be managers yet.
aitoolsrecap

aitoolsrecap


Are you looking to put an agent of your own to work, or simply surveying the landscape?
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

#### Q2 / Perplexity

- **Asked:** 2026-10-24 08:28:17 UTC
- **Product / model:** Perplexity web (perplexity.ai), logged out, default Search mode; model per the thread metadata: turbo
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q2.png)
- **Question as sent:** How do AI agents find paid work?
- **Answer (verbatim):**

`````text
AI agents find paid work by matching their capabilities to a specific task, then applying or bidding with a price and timeline through a marketplace or API. If selected, they complete the work and submit a verifiable deliverable; payment typically depends on the buyer’s approval and settlement.
moltjobs
+1
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

#### Q2 / Gemini

- **Asked:** 2026-10-24 08:37:23 UTC
- **Product / model:** Gemini web app (gemini.google.com), signed-in free account, Temporary chat, model selector 'Gemini Auto' (the app does not show which Gemini 3 model Auto used)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q2.png)
- **Question as sent:** How do AI agents find paid work?
- **Answer (verbatim):**

`````text
AI agents do not get paid by "applying" for jobs on conventional human job boards. Instead, they operate as autonomous digital workers or monetized tools, securing paid work through specialized technical infrastructure, market ecosystems, and API networks.

1. AI Agent Marketplaces & Stores

The most direct way an AI agent finds work is through dedicated digital stores and marketplaces where individuals and enterprises hire or subscribe to specialized agents.
upGrad

Productized Stores: On platforms like OpenAI's GPT Store, Relevance AI, or Agentive, creators list agents designed for specific workflows. Users subscribe to or pay execution fees for agents that handle research, copy editing, or lead generation.
upGrad

Enterprise Registries: Platforms such as TrueFoundry, AWS Bedrock, or Oracle AI Agent Marketplace allow organizations to deploy pre-tested, specialized agents for internal tasks (e.g., triage, contract review, compliance audit). Payment is executed via enterprise licensing, usage-based compute billing, or outcome-based metrics.

2. API-First Services (Machine-to-Machine Economy)

AI agents frequently operate in Agent-to-Agent (A2A) networks or as headless microservices.

Monetized Endpoints: An agent is wrapped inside an API endpoint. When other applications or software platforms need a specialized task completed (such as scraping, real-time data analysis, or dynamic image generation), they trigger the agent's API.

Micro-transaction Protocols: Agents utilize crypto-native micropayment networks (like Lightning Network or Solana) or traditional payment APIs (like Stripe) to autonomously execute pay-per-request calls without human intervention.

3. Human Wrappers & Freelance Platforms

Currently, traditional freelance platforms (such as Upwork, Freelancer, or Fiverr) require human accounts. Developers bypass this by acting as human proxies:

"AI Agency" Operating Model: Human developers set up freelance profiles and accept jobs for workflows like automated customer service, data processing, or custom web research. Behind the scenes, autonomous AI agents complete 90%–100% of the deliverable.

Autonomous Task Boards: Emergent platforms tailored for autonomous software allow agents to bid on coding tasks, GitHub issues, or bounty programs (e.g., finding security bugs or fixing broken PRs) and collect payments into designated wallet addresses.

How AI Agents Earn Money

AI agents generally operate under three financial models:

Pay-Per-Execution / Micro-billing: Paying pennies per API call, token, or completed query.

Subscription / SaaS: Monthly or annual access fees paid by users to access the agent's continuous workflow.

Outcome-Based Bounties: Earning payouts based on success metrics, such as resolving a GitHub issue, capturing a valid lead, or auditing a contract.

Would you like to explore how to build and monetize a specific type of AI agent, or discuss the technical integration required to accept payments for one?
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

<a id="q3"></a>
### Q3. How are bounty submissions judged on Verdikta?

#### Q3 / ChatGPT

- **Asked:** 2026-10-24 08:20:43 UTC
- **Product / model:** ChatGPT web (chatgpt.com), logged out, default model setting; model used per the share page metadata: gpt-6
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q3.png) · [ChatGPT share link](https://chatgpt.com/s/t_6adc6a7414988191bed4edc96971cc00)
- **Question as sent:** How are bounty submissions judged on Verdikta?
- **Answer (verbatim):**

`````text
On Verdikta, bounty submissions are judged by a jury of AI models that evaluates your work against a predefined rubric, rather than by the bounty creator personally. Your score determines whether you qualify for the reward.
bounties.verdikta.org
+1

How the judging process works

1. The bounty defines the rules

The creator specifies the task, evaluation criteria, their weights, the passing threshold, and the AI jury configuration. These terms are fixed once the bounty is created.

2. Your submission is checked

The jury evaluates whether your deliverable satisfies the task requirements. Some bounties have mandatory pass/fail conditions; failing even one can result in immediate rejection without further scoring.

3. AI models score the work

If the submission passes all mandatory checks, the jury scores individual criteria, generally from 0 to 100. Those scores are combined using the rubric's weights and the configured model weights to produce the final result.
bounties.verdikta.org
+2

4. The result determines payment

If your submission reaches the bounty's acceptance threshold, it can qualify for payment from the ETH held in escrow. Payment is handled through the smart contract, and evaluation results are recorded on-chain.
bounties.verdikta.org
+1

What determines your score?

It depends on the specific bounty's rubric. Common factors include:

Correctness: Does your work answer the question or solve the problem accurately?

Completeness: Have you met every required deliverable and mandatory condition?

Quality: Is the work clear, well-structured, and technically sound?

Evidence and compliance: Can your claims be verified, and does your submission follow the specified instructions?

Criterion weights: How much each requirement contributes to the final score.

These are examples, not a universal checklist. The actual published rubric is what matters.

Example of how scoring works

Suppose a bounty uses this rubric:

Criterion

Weight

Your score

Accuracy

50%

90

Completeness

30%

80

Clarity

20%

100

Your weighted score would be:

(
90
×
0.5
)
+
(
80
×
0.3
)
+
(
100
×
0.2
)
=
88
(90×0.5)+(80×0.3)+(100×0.2)=88

If the acceptance threshold were 80%, you would pass, assuming all mandatory checks were satisfied.

Important: A high average does not rescue a submission that fails a mandatory requirement. Also, passing one bounty's rubric does not mean every Verdikta bounty uses the same threshold or criteria.

Can the creator reject your work?

Generally, the creator cannot simply reject a submission after the fact. Some bounties offer an approval window in which the creator can approve work early; otherwise, the configured AI evaluation determines the outcome. The escrow, criteria, and threshold are fixed at creation.
bounties.verdikta.org
+1

You can inspect the evaluation details on the Verdikta Bounties platform  to see the exact criteria, jury configuration, passing threshold, and—where published—the AI's reasoning for a result.

If you share a specific bounty link, I can
 explain its scoring rubric or
 help optimize a submission
`````

- **Marking** (20 Verdikta claims: 5 CORRECT, 0 WRONG, 15 UNSUPPORTED):
  1. "bounty submissions are judged by a jury of AI models that evaluates your work against a predefined rubric, rather than by the bounty creator personally": **CORRECT** [F6]. Matches F6.
  2. "Your score determines whether you qualify for the reward.": **UNSUPPORTED** [F3]. Consistent with F3 but UNSUPPORTED under this report's payout rule: it does not say only the FIRST passing submission is paid.
  3. "The creator specifies the task, evaluation criteria, their weights, the passing threshold, and the AI jury configuration.": **UNSUPPORTED** [F6]. A rubric published in advance (F6) and an acceptance threshold (F3) are in the facts list. Criterion weights and the jury configuration are not.
  4. "These terms are fixed once the bounty is created.": **CORRECT** [F5]. Matches F5.
  5. "The jury evaluates whether your deliverable satisfies the task requirements.": **UNSUPPORTED** [F6]. Consistent with F6 (scored against the published rubric). 'Task requirements' is broader than the rubric.
  6. "Some bounties have mandatory pass/fail conditions; failing even one can result in immediate rejection without further scoring.": **UNSUPPORTED** [not in facts list]. Must-pass gates are not in the facts list.
  7. "the jury scores individual criteria, generally from 0 to 100. Those scores are combined using the rubric's weights and the configured model weights to produce the final result.": **UNSUPPORTED** [F6]. Per-criterion scoring matches F6; the 0-100 scale and the weighting method are not in the facts list.
  8. "If your submission reaches the bounty's acceptance threshold, it can qualify for payment": **UNSUPPORTED** [F3]. Consistent with F3 but marked UNSUPPORTED under this report's rule for 'passing work is paid' statements: F3 says only the FIRST passing submission is paid, and the answer does not say so. It is not marked WRONG because it does not claim that every passing submission is paid.
  9. "from the ETH held in escrow": **UNSUPPORTED** [F4]. Escrowed ETH is not stated in the facts list (F4 says only that the creator can reclaim the full amount).
  10. "evaluation results are recorded on-chain": **UNSUPPORTED** [F6]. F6 says per-criterion scores are public and auditable; 'recorded on-chain' is not stated as such.
  11. "It depends on the specific bounty's rubric.": **CORRECT** [F6]. Matches F6 (work is scored against the bounty's rubric).
  12. "These are examples, not a universal checklist.": **UNSUPPORTED** [not in facts list]. Covers the preceding example factors (correctness, completeness, quality, evidence, criterion weights). They are offered as examples and are not in the facts list.
  13. "The actual published rubric is what matters.": **CORRECT** [F6]. Matches F6 (rubric published in advance).
  14. "Suppose a bounty uses this rubric:": **UNSUPPORTED** [not in facts list]. A hypothetical worked example (weights 50/30/20, 80% threshold, score 88). It is not a claim about any real bounty, and weighted scoring is not in the facts list.
  15. "A high average does not rescue a submission that fails a mandatory requirement.": **UNSUPPORTED** [not in facts list]. Must-pass gates are not in the facts list.
  16. "passing one bounty's rubric does not mean every Verdikta bounty uses the same threshold or criteria": **UNSUPPORTED** [F6]. Per-bounty rubrics are consistent with F6. Not stated as such.
  17. "Generally, the creator cannot simply reject a submission after the fact.": **UNSUPPORTED** [F6]. Consistent with F6 (the AI panel does the scoring). Not stated as such.
  18. "Some bounties offer an approval window in which the creator can approve work early": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  19. "The escrow, criteria, and threshold are fixed at creation.": **CORRECT** [F5]. Matches F5.
  20. "You can inspect the evaluation details on the Verdikta Bounties platform to see the exact criteria, jury configuration, passing threshold, and—where published—the AI's reasoning for a result.": **UNSUPPORTED** [F6]. Consistent with F6 (per-criterion scores are public and auditable). The specific fields shown are not covered.

#### Q3 / Claude

- **Asked:** 2026-10-24 08:50:11 UTC
- **Product / model:** Claude web (claude.ai), signed in, Incognito chat, model selector 'Opus 5.5 High' (Opus 5.5, effort High)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q3.png)
- **Question as sent:** How are bounty submissions judged on Verdikta?
- **Answer (verbatim):**

`````text
Searched the web
Verdikta bounty submissions judged

Searched the web Verdikta bounty submissions judged

Nothing useful yet. Let me narrow it.

Searched the web

Searched the web

Sir, Verdikta bounties are judged by a jury of AI models scoring each submission against a rubric the creator fixed in advance. Here’s how it works, put together from Verdikta’s own pages and some recent write-ups by bounty hunters.

The rubric comes first. The creator funds a task in escrow and publishes a rubric in advance. A panel of independent AI arbiter nodes then scores each submission against that rubric, and the per-criterion scores are public and auditable. The rubric, the pass mark and the jury panel are stored in an IPFS evaluation package whose identifier is set when the bounty is created, so nobody can move the goalposts after you start working. Rubrics have weighted criteria. One example is bounty #139, a short personal bio. It had five criteria: location (0.15), personal history (0.25), experience with AI agents (0.20), tools (0.20) and authenticity (0.20), with a 50% pass threshold.
Bug bounty, freelance gig, or judged bounty? Picking the right platform for the work in front of you - DEV Community
 +2


The jury. On the bounties seen so far, two AI models, one from OpenAI and one from Anthropic, each with 50% weight, score every submission. The point, as one hunter put it, is that with two different providers, one model’s quirks can’t decide the outcome alone. Verdikta’s own site says it uses a multi-model AI panel combined with Schelling filter mechanisms to keep evaluation and settlement objective, with verdicts typically returned in under three minutes.
Who decides if the work is good? Verdikta's AI jury vs freelance platforms vs maintainer review - DEV Community
 +2


Pass or fail. The contract pays only if the weighted score clears the threshold. The first submission that passes automatically wins the bounty. Thresholds vary a great deal. Some bounties are set as high as 90%, and a near miss pays nothing.
Hot take: AI judges aren't the problem with AI-judged bounties. All-or-nothing thresholds are. - DEV Community
 +2


Costs. Verdikta charges no platform fee, so the whole bounty goes to the hunter whose submission passes. Hunters do attach a refundable oracle prepay of about 0.00024 ETH when they submit, but in practice it’s usually spent in full on the jury round.
dev


After the verdict. The jury’s full reasoning is stored on IPFS, linked from the bounty page. There is no appeal or revision loop. There’s also no cancel button for anyone. If the deadline passes with no passing work, the escrow goes back to the creator.
dev

dev


Practical advice. If the rubric is vague, the jury will read it literally and score you against the letter of it. Give the jury the full content, too. One hunter lost points by attaching only a screenshot and a link, because the jury couldn’t see most of the text. Resubmitted with the full post attached, the same piece scored 91%. The same writer has argued that on math bounties the jury rarely tells submissions apart, because ten proofs all scored between 97% and 99%.
Bug bounty, freelance gig, or judged bounty? Picking the right platform for the work in front of you - DEV Community
 +2


A caveat, sir: much of the detail above comes from community posts on DEV rather than official documentation, and the jury makeup appears to be set per bounty. Do check the specific bounty’s page at bounties.verdikta.org before committing any work.
`````

- **Marking** (26 Verdikta claims: 9 CORRECT, 0 WRONG, 17 UNSUPPORTED):
  1. "Verdikta bounties are judged by a jury of AI models scoring each submission against a rubric the creator fixed in advance": **CORRECT** [F5, F6]. Matches F5 and F6.
  2. "The creator funds a task in escrow": **UNSUPPORTED** [F4]. Consistent with F4 (the creator can reclaim the full amount). Escrow is not stated.
  3. "and publishes a rubric in advance": **CORRECT** [F6]. Matches F6.
  4. "A panel of independent AI arbiter nodes then scores each submission against that rubric, and the per-criterion scores are public and auditable.": **CORRECT** [F6]. Matches F6 word for word.
  5. "The rubric, the pass mark and the jury panel are stored in an IPFS evaluation package whose identifier is set when the bounty is created": **UNSUPPORTED** [F5]. The core matches F5 (rubric and evaluation package pinned to IPFS and fixed). The facts do not list the pass mark and jury panel as package contents.
  6. "nobody can move the goalposts after you start working": **CORRECT** [F5]. Matches F5 (cannot be edited after creation).
  7. "Rubrics have weighted criteria.": **UNSUPPORTED** [not in facts list]. Weights are not in the facts list.
  8. "One example is bounty #139, a short personal bio. It had five criteria": **UNSUPPORTED** [not in facts list]. A specific example that the facts list does not cover.
  9. "two AI models, one from OpenAI and one from Anthropic, each with 50% weight, score every submission": **UNSUPPORTED** [F6]. A panel matches F6. Its makeup is not in the facts list (the answer itself adds that it is set per bounty).
  10. "with two different providers, one model’s quirks can’t decide the outcome alone": **UNSUPPORTED** [F6]. Consistent with F6 (panel of independent arbiters). Provider mix not covered.
  11. "verdicts typically returned in under three minutes": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  12. "The contract pays only if the weighted score clears the threshold.": **UNSUPPORTED** [F3]. Paying only above the threshold is consistent with F3. A 'weighted' score is not stated.
  13. "The first submission that passes automatically wins the bounty.": **CORRECT** [F3]. Matches F3.
  14. "Thresholds vary a great deal.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  15. "Some bounties are set as high as 90%, and a near miss pays nothing.": **UNSUPPORTED** [F3]. A near miss paying nothing is consistent with F3. The 90% figure is not covered.
  16. "Verdikta charges no platform fee, so the whole bounty goes to the hunter whose submission passes.": **CORRECT** [F1]. Matches F1.
  17. "Hunters do attach a refundable oracle prepay of about 0.00024 ETH when they submit, but in practice it’s usually spent in full on the jury round.": **CORRECT** [F2]. Matches F2.
  18. "The jury’s full reasoning is stored on IPFS, linked from the bounty page.": **UNSUPPORTED** [F6]. Consistent with F6 (public, auditable scores). Storage location not covered.
  19. "There is no appeal or revision loop.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  20. "There’s also no cancel button for anyone.": **CORRECT** [F5]. Matches F5.
  21. "If the deadline passes with no passing work, the escrow goes back to the creator.": **CORRECT** [F4]. Matches F4.
  22. "If the rubric is vague, the jury will read it literally and score you against the letter of it.": **UNSUPPORTED** [not in facts list]. Advice from community posts. Not covered.
  23. "One hunter lost points by attaching only a screenshot and a link, because the jury couldn’t see most of the text.": **UNSUPPORTED** [not in facts list]. Anecdote. Not covered.
  24. "Resubmitted with the full post attached, the same piece scored 91%.": **UNSUPPORTED** [not in facts list]. Anecdote from a community post. Not covered by the facts list.
  25. "on math bounties the jury rarely tells submissions apart, because ten proofs all scored between 97% and 99%": **UNSUPPORTED** [not in facts list]. Anecdote. Not covered.
  26. "the jury makeup appears to be set per bounty": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.

#### Q3 / Perplexity

- **Asked:** 2026-10-24 08:30:35 UTC
- **Product / model:** Perplexity web (perplexity.ai), logged out, default Search mode; model per the thread metadata: turbo
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q3.png)
- **Question as sent:** How are bounty submissions judged on Verdikta?
- **Answer (verbatim):**

`````text
On Verdikta, bounty submissions are judged against a creator-defined rubric by a jury of AI arbiter models—not by the bounty creator’s discretionary review. If the submission reaches the required passing score, payment is released automatically from escrow.
bounties.verdikta
+1

How evaluation works

The bounty creator sets the task, a rubric with criteria and weights, and a passing threshold before submissions begin.
bounties.verdikta
+1

Each submission is evaluated by multiple AI models on Verdikta’s arbiter network; each model scores independently, and the final score is a weighted average.
bounties.verdikta
+1

Criteria can include weighted quality measures and binary “must-pass” gates. A failed hard gate can disqualify a submission before weighted scoring matters.
dev
+1

A score at or above the threshold passes; below it, the submission fails and the hunter can see which criteria fell short.
dev
+1

If multiple submissions are allowed, the highest-scoring passing submission wins.
dev

Creator’s role

The creator cannot reject qualifying work. If the bounty includes an approval window, the creator may approve it early, but otherwise the AI jury’s evaluation determines the outcome and the escrow contract pays automatically.
bounties.verdikta
+1

Example

A writing bounty might use criteria such as accuracy, clarity, and completeness, weighted toward accuracy. Two AI models might each score the submission independently; their scores are combined—for example, 50/50—and compared with the bounty’s pass threshold.
bounties.verdikta
+1
`````

- **Marking** (13 Verdikta claims: 2 CORRECT, 1 WRONG, 10 UNSUPPORTED):
  1. "bounty submissions are judged against a creator-defined rubric by a jury of AI arbiter models—not by the bounty creator’s discretionary review": **CORRECT** [F6]. Matches F6.
  2. "If the submission reaches the required passing score, payment is released": **UNSUPPORTED** [F3]. Consistent with F3 but marked UNSUPPORTED under this report's rule for 'passing work is paid' statements: F3 says only the FIRST passing submission is paid, and the answer does not say so. It is not marked WRONG because it does not claim that every passing submission is paid.
  3. "automatically from escrow": **UNSUPPORTED** [not in facts list]. 'Automatically' and escrow mechanics are not in the facts list.
  4. "The bounty creator sets the task, a rubric with criteria and weights, and a passing threshold before submissions begin.": **UNSUPPORTED** [F6]. A rubric published in advance matches F6. Criterion weights are not in the facts list.
  5. "each model scores independently, and the final score is a weighted average": **UNSUPPORTED** [F6]. Independent scoring matches F6. The weighted-average method is not in the facts list.
  6. "Criteria can include weighted quality measures and binary “must-pass” gates.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  7. "A failed hard gate can disqualify a submission before weighted scoring matters.": **UNSUPPORTED** [not in facts list]. Must-pass gates and weighting are not in the facts list.
  8. "below it, the submission fails and the hunter can see which criteria fell short": **CORRECT** [F6]. Matches F6 (per-criterion scores are public).
  9. "If multiple submissions are allowed, the highest-scoring passing submission wins.": **WRONG** [F3]. Correction: The FIRST submission that clears the acceptance threshold wins the entire bounty. A later submission with a higher score gets nothing, and there is no best-of comparison at the deadline.
  10. "The creator cannot reject qualifying work. If the bounty includes an approval window, the creator may approve it early": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  11. "otherwise the AI jury’s evaluation determines the outcome and the escrow contract pays automatically": **UNSUPPORTED** [F3, F6]. Consistent with F6 (the AI panel scores) and F3. 'Automatically' is not stated, and nothing here says 'first'.
  12. "A writing bounty might use criteria such as accuracy, clarity, and completeness": **UNSUPPORTED** [not in facts list]. A hypothetical example, not covered by the facts list.
  13. "Two AI models might each score the submission independently; their scores are combined—for example, 50/50—and compared with the bounty’s pass threshold.": **UNSUPPORTED** [F6]. A hypothetical. Independent scoring is consistent with F6. The 50/50 combination is not covered.

#### Q3 / Gemini

- **Asked:** 2026-10-24 08:37:59 UTC
- **Product / model:** Gemini web app (gemini.google.com), signed-in free account, Temporary chat, model selector 'Gemini Auto' (the app does not show which Gemini 3 model Auto used)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q3.png)
- **Question as sent:** How are bounty submissions judged on Verdikta?
- **Answer (verbatim):**

`````text
On Verdikta, bounty submissions are judged automatically through a decentralized, automated evaluation process powered by an AI Jury / Oracle system rather than manual human review.
Zealy

Here is a step-by-step breakdown of how bounty submissions are evaluated, scored, and rewarded:

1. Evaluation Setup (The Rubric)

When a bounty creator posts a task on Verdikta, they define an evaluation package/rubric stored on-chain and IPFS. This rubric contains:
Zealy

Specific Criteria: Individual criteria, each assigned a weight and a description.

"Must-Pass" Conditions: Specific mandatory criteria marked with a must flag (e.g., specific file format, exact output requirement). Failing a must criterion causes instant disqualification/failure.

Forbidden Content Check: Hard failure triggers for prohibited elements.

Passing Threshold: A minimum cumulative score required to pass (typically rated on a scale of 0–100).

2. Submission & IPFS Upload

When a hunter (a human worker or an autonomous AI agent) completes a task:

The submission artifacts (code, research, files, write-ups) are uploaded to IPFS.
Skills Directory

The submission is registered on-chain on the Base network along with a small evaluation deposit (used to cover AI oracle grading costs).
Zealy

The submission enters a PENDING_EVALUATION state while the oracle network processes the work.
Skills Directory

3. The AI Jury Grading Process

Once submitted, an independent panel of AI models (the AI Jury / Oracle) evaluates the submission:
Zealy

Automated Assessment: The AI oracle compares the IPFS-stored submission artifacts directly against the creator’s defined rubric criteria and weights.

Scoring: The jury assigns scores for each weighted criterion and computes an overall percentage/numerical score.

Pass/Fail Verdict: If the overall score equals or exceeds the defined passing threshold and meets all must-pass criteria without triggering forbidden content rules, the submission receives an ACCEPTED status. Otherwise, it is marked as REJECTED.
Skills Directory

Timeframe: The evaluation process typically takes 2 to 5 minutes.
Skills Directory

4. Winning and Smart Contract Payouts

Verdikta operates on a First-Pass-Wins mechanism:
Zealy

First Passing Submission Wins: Reaching a passing score does not guarantee payment unless you are the first submission to achieve or exceed the threshold.
Zealy

Automated Smart Contract Escrow: Once the oracle verifies a winning submission, the smart contract on Base automatically releases the locked ETH bounty directly to the hunter’s wallet.
Zealy

Deposit & Unused Deposit Refunds: If a submission fails, unused evaluation gas/deposit funds are refunded. If no hunter submits a passing entry before the deadline, the locked reward is refunded back to the bounty creator.
Zealy
`````

- **Marking** (22 Verdikta claims: 7 CORRECT, 0 WRONG, 15 UNSUPPORTED):
  1. "bounty submissions are judged automatically through a decentralized, automated evaluation process powered by an AI Jury / Oracle system rather than manual human review": **CORRECT** [F6]. Matches F6.
  2. "they define an evaluation package/rubric stored on-chain and IPFS": **CORRECT** [F5]. Matches F5.
  3. "Specific Criteria: Individual criteria, each assigned a weight and a description.": **UNSUPPORTED** [not in facts list]. Criterion weights are not in the facts list.
  4. ""Must-Pass" Conditions: Specific mandatory criteria marked with a must flag": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  5. "Failing a must criterion causes instant disqualification/failure.": **UNSUPPORTED** [not in facts list]. Must-pass gates are not in the facts list.
  6. "Forbidden Content Check: Hard failure triggers for prohibited elements.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  7. "Passing Threshold: A minimum cumulative score required to pass (typically rated on a scale of 0–100).": **UNSUPPORTED** [F3]. An acceptance threshold is consistent with F3. The 0-100 scale is not stated.
  8. "When a hunter (a human worker or an autonomous AI agent) completes a task": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  9. "The submission artifacts (code, research, files, write-ups) are uploaded to IPFS.": **UNSUPPORTED** [not in facts list]. Not covered (F5 covers the rubric and evaluation package, not submissions).
  10. "The submission is registered on-chain on the Base network along with a small evaluation deposit (used to cover AI oracle grading costs).": **CORRECT** [F2, F6]. Matches F6 (Base) and F2 (the prepay that pays the jury).
  11. "The submission enters a PENDING_EVALUATION state": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  12. "an independent panel of AI models (the AI Jury / Oracle) evaluates the submission": **CORRECT** [F6]. Matches F6.
  13. "The AI oracle compares the IPFS-stored submission artifacts directly against the creator’s defined rubric criteria and weights.": **UNSUPPORTED** [F6]. Scoring against the rubric matches F6. IPFS-stored submissions and weights are not covered.
  14. "The jury assigns scores for each weighted criterion and computes an overall percentage/numerical score.": **UNSUPPORTED** [F6]. Per-criterion scores match F6. Criterion weights and how the overall score is computed are not in the facts list.
  15. "the submission receives an ACCEPTED status": **UNSUPPORTED** [F3]. Status names are not in the facts list. Passing at the threshold is consistent with F3.
  16. "Otherwise, it is marked as REJECTED.": **UNSUPPORTED** [not in facts list]. Status names are not in the facts list.
  17. "The evaluation process typically takes 2 to 5 minutes.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  18. "Verdikta operates on a First-Pass-Wins mechanism": **CORRECT** [F3]. Matches F3.
  19. "Reaching a passing score does not guarantee payment unless you are the first submission to achieve or exceed the threshold.": **CORRECT** [F3]. Matches F3 exactly.
  20. "the smart contract on Base automatically releases the locked ETH bounty directly to the hunter’s wallet": **UNSUPPORTED** [F3, F6]. Base (F6) and payment to the passing hunter (F3) are consistent with the facts. 'Automatically', the ETH currency and direct wallet delivery are not stated.
  21. "If a submission fails, unused evaluation gas/deposit funds are refunded.": **UNSUPPORTED** [F2]. A refundable prepay matches F2. The facts list says nothing about refunding gas. Missing: the prepay is usually spent in full, so little or nothing comes back.
  22. "If no hunter submits a passing entry before the deadline, the locked reward is refunded back to the bounty creator.": **CORRECT** [F4]. Matches F4.

<a id="q4"></a>
### Q4. Does Verdikta charge a platform fee?

#### Q4 / ChatGPT

- **Asked:** 2026-10-24 08:21:28 UTC
- **Product / model:** ChatGPT web (chatgpt.com), logged out, default model setting; model used per the share page metadata: gpt-6
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q4.png) · [ChatGPT share link](https://chatgpt.com/s/t_6adc6a9b40d48191aee924e3d8279f7c)
- **Question as sent:** Does Verdikta charge a platform fee?
- **Answer (verbatim):**

`````text
No — Verdikta's documentation does not establish a separate platform fee, but it does charge for using its services.

According to the
Verdikta documentation, users pay per AI evaluation, with fees covering participating AI arbiters and associated operating costs. Additional blockchain gas fees may apply.
Verdikta Documentation
+1

The key distinction is that no separate platform fee is not the same as no fees at all. The cost depends on the evaluation configuration and associated transaction costs.

You can review the official Verdikta documentation  for fee details.

Would you like me to
 break down all costs or
 check fees for developers?
`````

- **Marking** (6 Verdikta claims: 1 CORRECT, 1 WRONG, 4 UNSUPPORTED):
  1. "No — Verdikta's documentation does not establish a separate platform fee": **CORRECT** [F1]. The answer 'No' matches F1, though it is hedged ('does not establish') where F1 is definite: there is no platform fee.
  2. "but it does charge for using its services": **WRONG** [F1, F2]. Correction: Verdikta Bounties charges no platform fee, and the whole bounty goes to the passing hunter. The only per-attempt cost is the hunter's own refundable oracle prepay of about 0.00024 ETH, which pays the AI jury and is usually spent in full. That is a jury cost, not a Verdikta charge. (Marker's note: marked WRONG because the sentence says Verdikta itself charges.)
  3. "users pay per AI evaluation, with fees covering participating AI arbiters and associated operating costs": **UNSUPPORTED** [F2]. Paying for the AI jury per evaluation matches F2 (oracle prepay). 'Associated operating costs' is not in the facts list.
  4. "Additional blockchain gas fees may apply.": **UNSUPPORTED** [not in facts list]. Gas is not covered by the facts list.
  5. "no separate platform fee is not the same as no fees at all": **UNSUPPORTED** [F1, F2]. Consistent with F1 (no platform fee) and F2 (the hunter pays an oracle prepay to the jury). Not stated as such.
  6. "The cost depends on the evaluation configuration and associated transaction costs.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.

#### Q4 / Claude

- **Asked:** 2026-10-24 08:51:00 UTC
- **Product / model:** Claude web (claude.ai), signed in, Incognito chat, model selector 'Opus 5.5 High' (Opus 5.5, effort High)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q4.png)
- **Question as sent:** Does Verdikta charge a platform fee?
- **Answer (verbatim):**

`````text
Searched the web
Verdikta platform fee

Searched the web Verdikta platform fee

Nothing useful there, sir. Narrowing the search.

Searched the web

Searched the web

In short, sir: for the live product, apparently not. There is a catch, however, and a whitepaper that rather disagrees.

What you actually pay today (Verdikta Bounties on Base). There’s no platform fee; the entire bounty goes to the hunter whose submission passes. The costs are elsewhere. A hunter attaches a refundable oracle prepay of roughly 0.00024 ETH when starting a submission, and in practice it’s usually consumed in full by the jury round. That prepay goes to the AI arbiter nodes rather than to Verdikta. Arbiters are paid in native ETH attached to the request, and any unspent prepay is kept as a withdrawable credit. For scale, the current per-arbiter fee is about 0.00002 ETH, roughly $0.05. Add Base gas and that’s the full cost. Browsing bounties and dry runs are free; only a live evaluation needs the ETH prepay and gas.
Bug bounty, freelance gig, or judged bounty? Picking the right platform for the work in front of you - DEV Community
 +4


The whitepaper, by contrast, describes a tiered model: 5% for disputes up to $100 (minimum $1), sliding down to 1% above $10,000 (minimum $200). It says users pay those fees in a VDK token, with token holders voting on fee rates. None of that matches how the deployed contracts behave, which take ETH. I’d treat it as a roadmap rather than a price list. The document calls itself a living document that will be updated as the protocol evolves.
Whitepaper - Verdikta Documentation
 +2


One caveat: the explicit “no platform fee” line comes from a third-party write-up published today, not from Verdikta’s own documentation. It agrees with the contract design and the GitHub discussion, but if real money depends on it, I’d confirm on their support page at verdikta.org/bounties/support before trusting a stranger’s blog post.
`````

- **Marking** (12 Verdikta claims: 3 CORRECT, 0 WRONG, 9 UNSUPPORTED):
  1. "In short, sir: for the live product, apparently not.": **CORRECT** [F1]. The answer 'no platform fee' matches F1 (hedged with 'apparently').
  2. "There’s no platform fee; the entire bounty goes to the hunter whose submission passes.": **CORRECT** [F1]. Matches F1.
  3. "A hunter attaches a refundable oracle prepay of roughly 0.00024 ETH when starting a submission, and in practice it’s usually consumed in full by the jury round.": **CORRECT** [F2]. Matches F2.
  4. "That prepay goes to the AI arbiter nodes rather than to Verdikta.": **UNSUPPORTED** [F1]. Consistent with F1. Not stated as such.
  5. "Arbiters are paid in native ETH attached to the request, and any unspent prepay is kept as a withdrawable credit.": **UNSUPPORTED** [F2]. Payment in ETH matches F2. The 'withdrawable credit' mechanism is not covered (F2 says only that the prepay is refundable).
  6. "the current per-arbiter fee is about 0.00002 ETH, roughly $0.05": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  7. "Add Base gas and that’s the full cost.": **UNSUPPORTED** [F6]. Base matches F6. Gas is not covered.
  8. "Browsing bounties and dry runs are free": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  9. "The whitepaper, by contrast, describes a tiered model: 5% for disputes up to $100 (minimum $1), sliding down to 1% above $10,000 (minimum $200).": **UNSUPPORTED** [F1]. Reported as the content of a whitepaper, and the answer itself says it does not match the live product. Not marked WRONG because Claude does not claim this fee applies. The facts list (F1) says the bounty platform charges no fee. The old whitepaper text is a likely source of confusion (see the error analysis).
  10. "It says users pay those fees in a VDK token, with token holders voting on fee rates.": **UNSUPPORTED** [not in facts list]. Reported whitepaper content, which the answer itself says does not match the live product. Not covered by the facts list.
  11. "None of that matches how the deployed contracts behave, which take ETH.": **UNSUPPORTED** [F1, F2]. Consistent with F1 (no platform fee) and F2 (prepay in ETH). The comparison with the whitepaper is not covered by the facts list.
  12. "the explicit “no platform fee” line comes from a third-party write-up published today": **UNSUPPORTED** [not in facts list]. A statement about the assistant's source, not about Verdikta.

#### Q4 / Perplexity

- **Asked:** 2026-10-24 08:31:02 UTC
- **Product / model:** Perplexity web (perplexity.ai), logged out, default Search mode; model per the thread metadata: turbo
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q4.png)
- **Question as sent:** Does Verdikta charge a platform fee?
- **Answer (verbatim):**

`````text
Verdikta charges per AI evaluation (in LINK), rather than offering the service for free; available information describes this as a fee that pays arbiters and covers operating costs.
docs.verdikta
+1
`````

- **Marking** (2 Verdikta claims: 0 CORRECT, 1 WRONG, 1 UNSUPPORTED):
  1. "Verdikta charges per AI evaluation (in LINK), rather than offering the service for free": **WRONG** [F1, F2]. Correction: Verdikta Bounties charges no platform fee. The whole bounty goes to the passing hunter. The only per-attempt cost is a refundable oracle prepay of about 0.00024 ETH, paid in ETH (not LINK). It pays the AI jury and is usually spent in full.
  2. "available information describes this as a fee that pays arbiters and covers operating costs": **UNSUPPORTED** [F2]. Paying the arbiters is consistent with F2. 'Covers operating costs' is not in the facts list.

#### Q4 / Gemini

- **Asked:** 2026-10-24 08:38:34 UTC
- **Product / model:** Gemini web app (gemini.google.com), signed-in free account, Temporary chat, model selector 'Gemini Auto' (the app does not show which Gemini 3 model Auto used)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q4.png)
- **Question as sent:** Does Verdikta charge a platform fee?
- **Answer (verbatim):**

`````text
Whether Verdikta charges a platform fee depends on which platform or service you are referring to, as there are a few distinct products with similar names:

1. Verdikt (Fraud Decisioning & Chargebacks)

If you are referring to Verdikt (the AI decisioning layer for e-commerce fraud and chargebacks):
Verdikt

No Platform Fee: Verdikt explicitly advertises no platform fees and no minimum commitments to start.
Verdikt

Pricing Model: They charge either a pay-per-decision model (e.g., $0.03 per decision for basic signal/scoring) or a volume-based chargeback guarantee model (typically 0.4%–1.2% of approved order volume).
Verdikt

2. Verdikt / GetVerdikt (AI Business Advisor / Strategy Platform)

If you mean GetVerdikt (the AI multi-advisor platform for business strategy and decision-making):

Subscription-Based: They do not charge a separate "platform fee," but rather operate on recurring subscription plans.
Verdikt

Pricing Tiers:

Solo: ~$49/month
Verdikt

Team: ~$99/month
Verdikt

Business: ~$179/month
Verdikt

Premium: ~$249/month
Verdikt

A 7-day free trial is available for new users.

If you are asking about a specific legal, dispute resolution, or custom blockchain tool named Verdikta, could you clarify the specific service or application you have in mind?
`````

- **Marking** (2 Verdikta claims: 0 CORRECT, 0 WRONG, 2 UNSUPPORTED):
  1. "Whether Verdikta charges a platform fee depends on which platform or service you are referring to, as there are a few distinct products with similar names": **UNSUPPORTED** [not in facts list]. Not covered by the facts list. This is ENTITY CONFUSION: everything after it describes 'Verdikt' (an e-commerce fraud tool and a business-advice tool), not Verdikta. The Verdikt prices ($0.03 per decision, $49-$249/month) are about another product, so they are not marked as Verdikta claims. The answer gives no information about Verdikta's fees, so F1 is missing. Suggested answer: Verdikta Bounties (on Base) charges no platform fee, and the whole bounty goes to the passing hunter.
  2. "If you are asking about a specific legal, dispute resolution, or custom blockchain tool named Verdikta, could you clarify": **UNSUPPORTED** [not in facts list]. A request for clarification, not a claim. Recorded as 'no information about Verdikta'.

<a id="q5"></a>
### Q5. What does it cost to submit to a Verdikta bounty?

#### Q5 / ChatGPT

- **Asked:** 2026-10-24 08:22:01 UTC
- **Product / model:** ChatGPT web (chatgpt.com), logged out, default model setting; model used per the share page metadata: gpt-6
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q5.png) · [ChatGPT share link](https://chatgpt.com/s/t_6adc6abe27e081918c0cbcec7af0cf22)
- **Question as sent:** What does it cost to submit to a Verdikta bounty?
- **Answer (verbatim):**

`````text
Submitting work to a Verdikta bounty appears to have no separate submission fee, but it can cost a small amount in blockchain fees and evaluation prepayment.

According to Verdikta’s current bounty documentation and recent platform information, here’s the breakdown.
Verdikta
+1

Cost

What to expect

Bounty submission fee

No separate platform submission fee identified in the published information

Evaluation prepayment

Recent reporting indicates a median of about 0.00024 ETH, roughly $1.10 at the time reported

Base network gas

Additional ETH may be needed to execute the blockchain transactions

If your submission wins

You receive the bounty payout, subject to the bounty’s criteria and evaluation process

The evaluation prepayment is described as being mostly refunded, so the upfront amount is not necessarily your final cost. Actual gas and evaluation requirements can vary.
Verdikta
+1

You can check the live Verdikta bounty board  to inspect individual bounty rewards and requirements.

Would you like me to
 calculate the likely cost in INR or
 walk through the submission process?
`````

- **Marking** (11 Verdikta claims: 4 CORRECT, 1 WRONG, 6 UNSUPPORTED):
  1. "Submitting work to a Verdikta bounty appears to have no separate submission fee": **CORRECT** [F1]. Consistent with F1 (hedged with 'appears').
  2. "but it can cost a small amount in blockchain fees and evaluation prepayment": **UNSUPPORTED** [F2]. The evaluation prepayment matches F2. Blockchain fees are not covered.
  3. "No separate platform submission fee identified in the published information": **CORRECT** [F1]. Consistent with F1.
  4. "Recent reporting indicates a median": **UNSUPPORTED** [F2]. F2 gives one figure ('about 0.00024 ETH'), not a median of reported values.
  5. "about 0.00024 ETH": **CORRECT** [F2]. The evaluation prepayment amount matches F2.
  6. "roughly $1.10 at the time reported": **UNSUPPORTED** [not in facts list]. The facts list gives no USD figure.
  7. "Base network gas": **UNSUPPORTED** [F6]. Base matches F6. The need for gas and its cost are not in the facts list.
  8. "Additional ETH may be needed to execute the blockchain transactions": **UNSUPPORTED** [not in facts list]. Gas is not covered by the facts list.
  9. "You receive the bounty payout, subject to the bounty’s criteria and evaluation process": **CORRECT** [F3]. Consistent with F3. Missing: only the first passing submission is paid.
  10. "The evaluation prepayment is described as being mostly refunded, so the upfront amount is not necessarily your final cost.": **WRONG** [F2]. Correction: The oracle prepay (about 0.00024 ETH) is refundable in principle, but in practice it is usually spent in full on the jury round. Budget the whole prepay as the cost of each attempt.
  11. "Actual gas and evaluation requirements can vary.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.

#### Q5 / Claude

- **Asked:** 2026-10-24 08:51:52 UTC
- **Product / model:** Claude web (claude.ai), signed in, Incognito chat, model selector 'Opus 5.5 High' (Opus 5.5, effort High)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q5.png)
- **Question as sent:** What does it cost to submit to a Verdikta bounty?
- **Answer (verbatim):**

`````text
Searched the web, read 2 pages

Searched the web, read 2 pages

Straight from Verdikta’s own FAQ, sir, which they reviewed as recently as today. The short answer is “very little, but not nothing.”

The oracle prepay. Each evaluation needs an oracle prepay in ETH, attached when the evaluation starts. With the default settings it is 0.00024 ETH; a creator who sets the highest allowed oracle fee raises it to as much as 0.0048 ETH. So check the specific bounty, because the exact amount is shown on the bounty before you submit (the contract’s requiredPrepay).
verdikta

verdikta


Gas. Add gas for three transactions (prepare, start, finalize), about 0.00004 ETH in total in the worked example. All of this is on Base mainnet.
verdikta


What doesn’t cost anything. There is no platform fee. The escrow contract has no owner and takes no cut of the bounty, the payout or the refund. There is no listing fee, and API keys are free.
verdikta


About that “refundable” prepay. It is technically refundable, though I wouldn’t plan the household budget around it. Whatever is not spent is refunded automatically to whoever funded the evaluation, when the submission is finalized or marked failed. In practice the whole prepay is usually spent, so plan on it as the cost of an attempt. If you fail, you don’t get back the part that was spent, since the arbiters did the evaluation. You can submit again, with a new prepay, as long as the bounty is open and the deadline has not passed. The main exception is when a round times out without a verdict, in which case a larger part comes back.
Verdikta Bounties FAQ: fees, payouts and refunds
 +2


So, at default settings, each attempt costs roughly 0.00028 ETH all in. One more thing worth knowing before you spend it: one bounty pays one winner: the earliest passing submission, by submission order, not the highest score. Speed matters rather more than polish beyond the pass mark.
verdikta


If you give me a bounty number, sir, I can pull its actual required prepay and threshold so you know the exact cost before committing.
`````

- **Marking** (19 Verdikta claims: 9 CORRECT, 0 WRONG, 10 UNSUPPORTED):
  1. "Each evaluation needs an oracle prepay in ETH, attached when the evaluation starts.": **CORRECT** [F2]. Matches F2.
  2. "With the default settings it is 0.00024 ETH": **CORRECT** [F2]. The amount matches F2. Whether other settings change it is marked separately below.
  3. "a creator who sets the highest allowed oracle fee raises it to as much as 0.0048 ETH": **UNSUPPORTED** [F2]. F2 says 'about 0.00024 ETH'. A per-bounty maximum is not covered.
  4. "the exact amount is shown on the bounty before you submit (the contract’s requiredPrepay)": **UNSUPPORTED** [F2]. Consistent with F2. Display details are not covered.
  5. "Add gas for three transactions (prepare, start, finalize), about 0.00004 ETH in total in the worked example.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  6. "All of this is on Base mainnet.": **CORRECT** [F6]. Matches F6.
  7. "There is no platform fee.": **CORRECT** [F1]. Matches F1.
  8. "The escrow contract has no owner": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  9. "takes no cut of the bounty, the payout or the refund": **CORRECT** [F1, F4]. Matches F1 and F4 (the platform keeps nothing).
  10. "There is no listing fee, and API keys are free.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  11. "It is technically refundable": **CORRECT** [F2]. Matches F2 (refundable).
  12. "Whatever is not spent is refunded automatically to whoever funded the evaluation, when the submission is finalized or marked failed.": **UNSUPPORTED** [F2]. A refundable prepay matches F2. The refund timing and mechanics are not stated.
  13. "In practice the whole prepay is usually spent, so plan on it as the cost of an attempt.": **CORRECT** [F2]. Matches F2.
  14. "If you fail, you don’t get back the part that was spent, since the arbiters did the evaluation.": **UNSUPPORTED** [F2]. Consistent with F2 (usually spent in full on the jury round).
  15. "You can submit again, with a new prepay, as long as the bounty is open and the deadline has not passed.": **UNSUPPORTED** [not in facts list]. Resubmission is not covered by the facts list.
  16. "The main exception is when a round times out without a verdict, in which case a larger part comes back.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  17. "each attempt costs roughly 0.00028 ETH all in": **UNSUPPORTED** [not in facts list]. Derived figure, not covered by the facts list.
  18. "one bounty pays one winner: the earliest passing submission, by submission order, not the highest score": **CORRECT** [F3]. Matches F3.
  19. "Speed matters rather more than polish beyond the pass mark.": **CORRECT** [F3]. Follows directly from F3 (the first submission to pass wins).

#### Q5 / Perplexity

- **Asked:** 2026-10-24 08:31:32 UTC
- **Product / model:** Perplexity web (perplexity.ai), logged out, default Search mode; model per the thread metadata: turbo
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q5.png)
- **Question as sent:** What does it cost to submit to a Verdikta bounty?
- **Answer (verbatim):**

`````text
Submitting work to a Verdikta bounty costs a small ETH evaluation prepay—typically about 0.00024 ETH—plus any blockchain gas fees. Any unspent evaluation ETH is automatically refunded when the submission finalizes.
bounties.verdikta

What you pay
Cost	Typical amount	Notes
AI-jury evaluation prepay	~0.00024 ETH	Attached when you start the submission; unused ETH is refunded.
bounties.verdikta

Network gas	Variable	You pay normal transaction gas for the submission/start transaction.
bounties.verdikta

Bounty reward	Not paid by submitter	The ETH payout is already held in escrow by the bounty creator.
bounties.verdikta
How it works

You submit the required deliverable to the bounty.

You trigger evaluation by sending the exact transaction.value returned by the submission-start endpoint, which reflects the live required prepay.
bounties.verdikta

The AI jury grades the work against the bounty’s rubric; passing submissions are paid automatically from escrow.
bounties.verdikta

There is no LINK token or ERC-20 approval required.
bounties.verdikta

So, in practice, the direct cost to try a bounty is usually under a dollar in ETH plus gas, and the evaluation prepay is refundable if not fully used.
bounties.verdikta
+1
`````

- **Marking** (11 Verdikta claims: 2 CORRECT, 0 WRONG, 9 UNSUPPORTED):
  1. "Submitting work to a Verdikta bounty costs a small ETH evaluation prepay—typically about 0.00024 ETH": **CORRECT** [F2]. Matches F2.
  2. "plus any blockchain gas fees": **UNSUPPORTED** [not in facts list]. Gas is not covered by the facts list.
  3. "Any unspent evaluation ETH is automatically refunded when the submission finalizes.": **UNSUPPORTED** [F2]. That the prepay is refundable matches F2. 'Automatically' and 'when the submission finalizes' are not stated. Missing: in practice the prepay is usually spent in full.
  4. "Attached when you start the submission; unused ETH is refunded.": **CORRECT** [F2]. Matches F2.
  5. "You pay normal transaction gas for the submission/start transaction.": **UNSUPPORTED** [not in facts list]. Gas is not covered by the facts list.
  6. "The ETH payout is already held in escrow by the bounty creator.": **UNSUPPORTED** [F4]. Consistent with F4 (the creator funds the escrow and can reclaim it). Not stated as such.
  7. "You submit the required deliverable to the bounty.": **UNSUPPORTED** [not in facts list]. A procedural step, not covered by the facts list.
  8. "You trigger evaluation by sending the exact transaction.value returned by the submission-start endpoint, which reflects the live required prepay.": **UNSUPPORTED** [F2]. Attaching the prepay when starting is consistent with F2. The API mechanics are not covered.
  9. "passing submissions are paid automatically from escrow": **UNSUPPORTED** [F3]. Imprecise rather than wrong: the plural hides the F3 rule that only the FIRST passing submission is paid.
  10. "There is no LINK token or ERC-20 approval required.": **UNSUPPORTED** [F2]. Consistent with F2 (the prepay is in ETH). Not stated as such.
  11. "the direct cost to try a bounty is usually under a dollar in ETH plus gas, and the evaluation prepay is refundable if not fully used": **UNSUPPORTED** [F2]. 'Refundable if not fully used' matches F2. The USD figure is not in the facts list. Missing: the prepay is usually spent in full.

#### Q5 / Gemini

- **Asked:** 2026-10-24 08:39:06 UTC
- **Product / model:** Gemini web app (gemini.google.com), signed-in free account, Temporary chat, model selector 'Gemini Auto' (the app does not show which Gemini 3 model Auto used)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q5.png)
- **Question as sent:** What does it cost to submit to a Verdikta bounty?
- **Answer (verbatim):**

`````text
When submitting work to a Verdikta bounty, Verdikta itself charges no platform fee.
DEV Community

However, as a hunter submitting to a bounty, you are required to pay a small evaluation deposit (roughly 0.00024 ETH, depending on current network conditions) to cover the AI jury/oracle evaluation process.
Zealy

Refund policy: The unused portion of this oracle evaluation deposit is refunded.
Zealy

Gas fees: You will also need a tiny amount of ETH on the Base network to cover standard transaction gas fees for your submission.
`````

- **Marking** (6 Verdikta claims: 4 CORRECT, 0 WRONG, 2 UNSUPPORTED):
  1. "Verdikta itself charges no platform fee.": **CORRECT** [F1]. Matches F1.
  2. "you are required to pay a small evaluation deposit (roughly 0.00024 ETH": **CORRECT** [F2]. The amount matches F2.
  3. "depending on current network conditions": **UNSUPPORTED** [not in facts list]. The facts list does not say the prepay varies with network conditions.
  4. "to cover the AI jury/oracle evaluation process": **CORRECT** [F2]. Matches F2 (spent on the jury round).
  5. "The unused portion of this oracle evaluation deposit is refunded.": **CORRECT** [F2]. Consistent with F2. Missing: it is usually spent in full.
  6. "You will also need a tiny amount of ETH on the Base network to cover standard transaction gas fees": **UNSUPPORTED** [F6]. Base matches F6. Gas is not covered by the facts list.

<a id="q6"></a>
### Q6. If two submissions both pass, who gets paid?

#### Q6 / ChatGPT

- **Asked:** 2026-10-24 08:22:35 UTC
- **Product / model:** ChatGPT web (chatgpt.com), logged out, default model setting; model used per the share page metadata: gpt-6
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q6.png) · [ChatGPT share link](https://chatgpt.com/s/t_6adc6ae019c48191a8cf55f59cf8bc03)
- **Question as sent:** If two submissions both pass, who gets paid?
- **Answer (verbatim):**

`````text
If two submissions both pass, who gets paid depends on the rules of the platform or competition.

Both submissions are eligible for payment: Both people may get paid if each submission independently meets the requirements.

Only one winner is allowed: The organizer chooses the winner based on the judging criteria, even if both submissions pass.

First valid submission wins: The earlier qualifying submission may receive the payment.

One reward per task: Only one submission may be paid, depending on the platform's rules.

Which platform or contest are you referring to? I can explain exactly who gets paid if you tell me the name or share the rules.
 Explain based on the submission rules
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

#### Q6 / Claude

- **Asked:** 2026-10-24 08:52:53 UTC
- **Product / model:** Claude web (claude.ai), signed in, Incognito chat, model selector 'Opus 5.5 High' (Opus 5.5, effort High)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q6.png)
- **Question as sent:** If two submissions both pass, who gets paid?
- **Answer (verbatim):**

`````text
Clarifying who gets paid when multiple entries qualify.
Clarifying who gets paid when multiple entries qualify.

Rather depends on the arena, sir. “Both pass” means different things in different places, but most systems settle it the same way.

On bug bounty platforms like HackerOne or Bugcrowd, the first valid report wins. Later submissions of the same issue get marked as duplicates and usually earn nothing, though some programs offer a token bounty or reputation points if the duplicate added something new.

On open-source code bounties (Algora, GitHub-sponsored issues, and the like), passing tests isn’t the finish line. Payment generally goes to whoever’s pull request the maintainer actually merges. That’s usually the first acceptable one, but maintainers can pick the cleaner solution or split the reward.

In competitions and hackathons, the published rules decide. Common tiebreakers are earliest timestamp, a judged quality score, or splitting the prize evenly.

Freelance contests on platforms like 99designs work differently. The client picks one winner, and “passing” only earns you a place on the shortlist.

So the short version is that it’s usually first valid submission, unless a human gets the final say on quality. If you tell me which platform or program you’re dealing with, I’ll find its actual tiebreak rule rather than leave you with generalities.
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

#### Q6 / Perplexity

- **Asked:** 2026-10-24 08:32:00 UTC
- **Product / model:** Perplexity web (perplexity.ai), logged out, default Search mode; model per the thread metadata: turbo
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q6.png)
- **Question as sent:** If two submissions both pass, who gets paid?
- **Answer (verbatim):**

`````text
Usually, passing review does not by itself guarantee payment—payment normally goes to the submission the requester accepts, selects, or that meets the bounty’s specific winning criteria. If two submissions both pass, the platform or bounty creator typically chooses one (or pays according to its stated rules).

In one documented bounty example, two designs passed, but the creator chose one and paid that author directly; the other was still credited as a passing design but was not the paid winner.
github

Some programs explicitly pay only on acceptance/merge readiness, not merely on passing review.
workmind

Other programs split rewards among multiple approved participants in proportion to their reward scores, so both could earn—but not necessarily equally.
docs.ridges

If you mean a specific platform or bounty, share its name or the rules text; the answer can differ between “first valid submission,” “best submission,” “all qualifying submissions,” and “creator’s choice.”
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

#### Q6 / Gemini

- **Asked:** 2026-10-24 08:39:36 UTC
- **Product / model:** Gemini web app (gemini.google.com), signed-in free account, Temporary chat, model selector 'Gemini Auto' (the app does not show which Gemini 3 model Auto used)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q6.png)
- **Question as sent:** If two submissions both pass, who gets paid?
- **Answer (verbatim):**

`````text
Who gets paid when two submissions both pass depends on the platform framework and the contest format being used.

Here are the standard rules across different platforms and bounty models:

1. Bug Bounty Programs (e.g., HackerOne, Bugcrowd, Immunefi)

First Come, First Served: The first eligible submission gets the full payout.
DEV Community

The Duplicate Rule: The second submission is marked as a "Duplicate" and receives no payment, even if it is completely valid and passes verification.
Microsoft

Exceptions:

If the second submission reveals a new, higher-severity aspect or critical context that the first report missed, some programs award a partial payout or "bonus/differential" to the second submitter.
Microsoft

If the two reports identify different underlying code causes, both may be treated as unique and paid separately.

2. Task-Based / Freelance Bounties (e.g., Gitcoin, Upwork, Replit Bounties)

Single Winner (First Valid Submission): Most platforms award the payout to the contributor who submitted a passing solution first.
DEV Community

Multiple Winners (Split Reward Pool): On platforms supporting pooled payouts (e.g., open-source development or community tasks), the total reward pool is split evenly among all participants whose submissions pass evaluation.

3. Open Competitions & Judged Contests (e.g., Kaggle, Topcoder)

Score/Performance-Based: If multiple entries pass, payouts are awarded according to the leaderboard rankings (e.g., highest accuracy, best performance, or fastest execution).

Ties: If two top submissions achieve the exact same passing score, the platform rules usually dictate:

Time-based tiebreaker: The submission uploaded earlier gets the higher prize.

Split prize: The prize money for those rank spots is added together and divided equally between the tied submitters.

Key Summary
Model / Platform	Who Gets Paid?
Bug Bounties	The first submission to be submitted/logged.
First-to-Deliver Bounties	The first valid submission.
Competitive Contests	The submission with the higher score; ties are split or broken by timestamp.
Pooled Bounties	Both submitters share/split the total prize pool.

If you are referring to a specific platform or competition (e.g., HackerOne, Gitcoin, Kaggle, or a specific smart-contract audit platform), let me know so I can give you the exact rulebook for that service!
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

<a id="q7"></a>
### Q7. Can a Verdikta bounty be cancelled or edited after it is created?

#### Q7 / ChatGPT

- **Asked:** 2026-10-24 08:23:09 UTC
- **Product / model:** ChatGPT web (chatgpt.com), logged out, default model setting; model used per the share page metadata: gpt-6
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q7.png) · [ChatGPT share link](https://chatgpt.com/s/t_6adc6b04b12081918f83e707b3cfbb3d)
- **Question as sent:** Can a Verdikta bounty be cancelled or edited after it is created?
- **Answer (verbatim):**

`````text
No. A Verdikta bounty cannot be cancelled or edited after it has been created on-chain. The official Verdikta Bounties platform  confirms that the escrow smart contract has no cancellation or editing function.
bounties.verdikta.org
+1

Here's what that means in practice:

Cancel a bounty: Not possible once it is deployed on-chain.

Edit bounty details: You cannot change the payout, evaluation criteria (rubric), jury, passing threshold, or deadline after creation.

Recover your funds: If nobody wins, the escrowed funds can be returned to the creator after the bounty deadline, subject to the contract's rules.

Correct a mistake: Create a new bounty with the correct details, since the original bounty's on-chain terms remain fixed.

Important distinction: A bounty that was never deployed on-chain may be eligible for administrative deletion under certain conditions. That is different from cancelling an active, funded bounty.
bounties.verdikta.org
+1

Would you like me to explain how to
 recover funds from an expired bounty or
 create a corrected replacement bounty?
`````

- **Marking** (9 Verdikta claims: 6 CORRECT, 0 WRONG, 3 UNSUPPORTED):
  1. "A Verdikta bounty cannot be cancelled or edited after it has been created on-chain.": **CORRECT** [F5]. Matches F5.
  2. "the escrow smart contract has no cancellation or editing function": **CORRECT** [F5]. Matches F5.
  3. "Cancel a bounty: Not possible once it is deployed on-chain.": **CORRECT** [F5]. Matches F5.
  4. "You cannot change the payout, evaluation criteria (rubric), jury, passing threshold, or deadline after creation.": **CORRECT** [F5]. Matches F5 (bounty cannot be edited; rubric fixed on-chain).
  5. "If nobody wins, the escrowed funds can be returned to the creator after the bounty deadline": **CORRECT** [F4]. Matches F4.
  6. "Create a new bounty with the correct details": **UNSUPPORTED** [F5]. Advice that follows from F5, not a fact claim.
  7. "the original bounty's on-chain terms remain fixed": **CORRECT** [F5]. Matches F5.
  8. "A bounty that was never deployed on-chain may be eligible for administrative deletion under certain conditions.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  9. "That is different from cancelling an active, funded bounty.": **UNSUPPORTED** [F5]. Context for the preceding UNSUPPORTED claim. Consistent with F5.

#### Q7 / Claude

- **Asked:** 2026-10-24 08:53:26 UTC
- **Product / model:** Claude web (claude.ai), signed in, Incognito chat, model selector 'Opus 5.5 High' (Opus 5.5, effort High)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q7.png)
- **Question as sent:** Can a Verdikta bounty be cancelled or edited after it is created?
- **Answer (verbatim):**

`````text
Searched the web
Verdikta bounty cancel edit

Searched the web Verdikta bounty cancel edit

Nothing relevant. Let me search more specifically.

Read 3 pages, searched the web

Read 3 pages, searched the web

In short, sir: no. Verdikta bounties are deliberately immutable. The platform describes itself as ETH bounties held in smart-contract escrow with no cancel or edit function, and each bounty page states that the escrow can’t change terms or return the funds before the deadline. It’s a feature, I’m told, though one suspects it’s more comforting to hunters than to creators who’ve just spotted a typo.
verdikta

dev


What’s locked in once you create it. The rubric, threshold, payout, jury class and deadline are all fixed. On the deadline specifically, the contract cannot change a deadline; a mismatched bounty has to be recreated. The same goes for jury configuration: if you specify model identifiers that the arbiters for an unlisted class don’t actually serve, every evaluation fails, and the bounty can’t be edited or canceled. One comparison piece summed up the trade-off neatly: no negotiation and no revision loop; a badly written rubric cannot be fixed later.


How you get your money back. Only by letting the deadline pass. After a bounty’s deadline passes, escrowed ETH stays locked until someone calls closeExpiredBounty on-chain. Nothing happens automatically. Any submissions still pending evaluation must be finalized or timed out first; once the close is possible, ETH is returned to the creator. Anyone may call. Of course, if a hunter submits passing work before the deadline, they get paid, and there’s nothing to reclaim.
verdikta

verdikta


The one thing you can change. Whether submissions are publicly viewable on the website. That flag lives off-chain, and toggling is idempotent and may be done as often as you like, provided you sign the request with the creator wallet.
verdikta


The sensible precaution. Since there’s no undo, check everything before committing ETH. Verdikta offers free, side-effect-free endpoints for exactly this: /rubric/validate for rubric shape, /jobs/validate for an evaluation-package CID, which never increment the jobId counter, never pin to IPFS, never spend gas. A short deadline also limits how long a regrettable bounty can hold your funds hostage.
verdikta

verdikta


If you have a particular bounty in mind, sir, give me its ID and I’ll pull its live on-chain status and tell you when it becomes closeable. Alternatively, hand me the draft rubric before you post it and I’ll go over it for weaknesses.
`````

- **Marking** (17 Verdikta claims: 8 CORRECT, 0 WRONG, 9 UNSUPPORTED):
  1. "Verdikta bounties are deliberately immutable.": **CORRECT** [F5]. Matches F5.
  2. "ETH bounties held in smart-contract escrow": **UNSUPPORTED** [not in facts list]. Escrowed ETH is not stated in the facts list.
  3. "no cancel or edit function": **CORRECT** [F5]. Matches F5.
  4. "The rubric, threshold, payout, jury class and deadline are all fixed.": **CORRECT** [F5]. Matches F5.
  5. "the contract cannot change a deadline; a mismatched bounty has to be recreated": **CORRECT** [F5]. Matches F5 (a bounty cannot be edited).
  6. "if you specify model identifiers that the arbiters for an unlisted class don’t actually serve, every evaluation fails, and the bounty can’t be edited or canceled": **UNSUPPORTED** [F5]. 'Can't be edited or canceled' matches F5. The failure scenario is not covered.
  7. "a badly written rubric cannot be fixed later": **CORRECT** [F5]. Matches F5.
  8. "Only by letting the deadline pass.": **CORRECT** [F4, F5]. Matches F4 and F5: no cancellation, and the creator reclaims the funds only after a deadline with no passing submission.
  9. "escrowed ETH stays locked until someone calls closeExpiredBounty on-chain": **UNSUPPORTED** [F4]. The return to the creator matches F4. The mechanism is not covered.
  10. "Nothing happens automatically.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  11. "once the close is possible, ETH is returned to the creator": **CORRECT** [F4]. Matches F4.
  12. "if a hunter submits passing work before the deadline, they get paid": **UNSUPPORTED** [F3]. Consistent with F3 but marked UNSUPPORTED under this report's rule for 'passing work is paid' statements: F3 says only the FIRST passing submission is paid, and the answer does not say so. It is not marked WRONG because it does not claim that every passing submission is paid.
  13. "Whether submissions are publicly viewable on the website. That flag lives off-chain": **UNSUPPORTED** [F5]. Not covered. It does not contradict F5, which concerns the on-chain bounty, rubric and evaluation package.
  14. "toggling is idempotent and may be done as often as you like, provided you sign the request with the creator wallet": **UNSUPPORTED** [F5]. Concerns an off-chain display flag, not the on-chain terms in F5. Not covered.
  15. "Since there’s no undo, check everything before committing ETH.": **CORRECT** [F5]. Follows from F5 (no cancel, no edit).
  16. "/rubric/validate for rubric shape, /jobs/validate for an evaluation-package CID": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  17. "A short deadline also limits how long a regrettable bounty can hold your funds hostage.": **UNSUPPORTED** [F4]. Consistent with F4. Not stated as such.

#### Q7 / Perplexity

- **Asked:** 2026-10-24 08:32:28 UTC
- **Product / model:** Perplexity web (perplexity.ai), logged out, default Search mode; model per the thread metadata: turbo
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q7.png)
- **Question as sent:** Can a Verdikta bounty be cancelled or edited after it is created?
- **Answer (verbatim):**

`````text
No. Once a Verdikta bounty is created and funded, it cannot be cancelled or edited. The payout, criteria, jury, pass threshold, and deadline are fixed in the escrow contract at creation.
bounties.verdikta
+1

What happens instead

Funds remain locked in a smart contract until either a qualifying submission wins or the deadline passes with no winner.
bounties.verdikta
+1

If it expires without a passing submission, anyone can call closeExpiredBounty() to return the funds to the creator—provided no evaluations are still active.
bounties.verdikta

If an evaluation is in progress at the deadline, the bounty cannot be closed until that evaluation completes.
bounties.verdikta

The creator cannot reject work; where an approval window exists, they may only approve early.
bounties.verdikta

Important nuance

An off-chain bounty record that was never deployed on-chain may be deleted or closed by an administrator, but this does not apply to a funded, on-chain bounty.
bounties.verdikta

So, before creating one, double-check the amount, deadline, rubric, and pass threshold: those terms cannot be changed afterward.
bounties.verdikta
+1
`````

- **Marking** (8 Verdikta claims: 4 CORRECT, 0 WRONG, 4 UNSUPPORTED):
  1. "Once a Verdikta bounty is created and funded, it cannot be cancelled or edited.": **CORRECT** [F5]. Matches F5.
  2. "The payout, criteria, jury, pass threshold, and deadline are fixed in the escrow contract at creation.": **CORRECT** [F5]. Matches F5.
  3. "Funds remain locked in a smart contract until either a qualifying submission wins or the deadline passes with no winner.": **CORRECT** [F3, F4]. Matches F3 and F4.
  4. "anyone can call closeExpiredBounty() to return the funds to the creator—provided no evaluations are still active": **UNSUPPORTED** [F4]. The funds going back to the creator match F4. The function name and the 'no active evaluations' condition are not in the facts list.
  5. "If an evaluation is in progress at the deadline, the bounty cannot be closed until that evaluation completes.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  6. "The creator cannot reject work; where an approval window exists, they may only approve early.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  7. "An off-chain bounty record that was never deployed on-chain may be deleted or closed by an administrator": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  8. "those terms cannot be changed afterward": **CORRECT** [F5]. Matches F5.

#### Q7 / Gemini

- **Asked:** 2026-10-24 08:40:09 UTC
- **Product / model:** Gemini web app (gemini.google.com), signed-in free account, Temporary chat, model selector 'Gemini Auto' (the app does not show which Gemini 3 model Auto used)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q7.png)
- **Question as sent:** Can a Verdikta bounty be cancelled or edited after it is created?
- **Answer (verbatim):**

`````text
No, a Verdikta bounty cannot be cancelled or edited once it has been created.
DEV Community

Key Details & Mechanism

Immutable Smart Contract Escrow: When a bounty is created, the reward funds are immediately locked into an escrow smart contract on the blockchain. The contract contains no functions to edit, pause, cancel, or prematurely withdraw funds.
Zealy
+ 1

Fixed Evaluation Rules: All evaluation criteria—including the rubric, pass threshold, jury panel, and deadline—are permanently linked at creation and stored on IPFS. Neither the bounty creator nor the Verdikta platform team can alter these parameters after launch.
DEV Community
+ 1

Protection for Hunters: This "no edit / no cancel" policy is designed by intent to protect bounty hunters (both human and AI agents). Because hunters expend time, effort, and minor evaluation fees upfront, fixed rules ensure that a creator cannot change requirements retroactively or pull funds out mid-process.
DEV Community
+ 1

What Happens If You Make a Mistake?

Wait Out the Deadline: If a bounty has incorrect instructions or an error in the rubric, the creator must wait for the set deadline to expire.
DEV Community

Automatic Refund: If no hunter submits work that meets the passing threshold before the deadline passes, the creator can reclaim and withdraw the full locked ETH amount from escrow.
DEV Community
`````

- **Marking** (10 Verdikta claims: 5 CORRECT, 0 WRONG, 5 UNSUPPORTED):
  1. "No, a Verdikta bounty cannot be cancelled or edited once it has been created.": **CORRECT** [F5]. Matches F5.
  2. "When a bounty is created, the reward funds are immediately locked into an escrow smart contract on the blockchain.": **UNSUPPORTED** [F4, F5]. Consistent with F4 and F5 (funds held until a pass or the deadline; terms fixed on-chain). Escrow mechanics are not stated.
  3. "The contract contains no functions to edit, pause, cancel, or prematurely withdraw funds.": **UNSUPPORTED** [F4, F5]. No edit/cancel matches F5, and no early withdrawal is consistent with F4. 'Pause' is not in the facts list.
  4. "All evaluation criteria—including the rubric, pass threshold, jury panel, and deadline—are permanently linked at creation and stored on IPFS.": **UNSUPPORTED** [F5]. The core matches F5 (rubric and evaluation package pinned to IPFS and fixed). The facts do not say the threshold, jury and deadline are stored on IPFS.
  5. "Neither the bounty creator nor the Verdikta platform team can alter these parameters after launch.": **CORRECT** [F5]. Matches F5.
  6. "This "no edit / no cancel" policy is designed by intent to protect bounty hunters": **UNSUPPORTED** [not in facts list]. The design intent is not covered by the facts list.
  7. "Because hunters expend time, effort, and minor evaluation fees upfront": **UNSUPPORTED** [F2]. Consistent with F2 (the prepay). The rationale is not covered.
  8. "fixed rules ensure that a creator cannot change requirements retroactively or pull funds out mid-process": **CORRECT** [F4, F5]. Matches F5 (no edits, no cancellation) and F4 (the creator reclaims only if nothing passes before the deadline).
  9. "the creator must wait for the set deadline to expire": **CORRECT** [F4, F5]. Follows from F4 and F5.
  10. "If no hunter submits work that meets the passing threshold before the deadline passes, the creator can reclaim and withdraw the full locked ETH amount from escrow.": **CORRECT** [F4]. Matches F4.

<a id="q8"></a>
### Q8. What blockchain does Verdikta run on?

#### Q8 / ChatGPT

- **Asked:** 2026-10-24 08:23:46 UTC
- **Product / model:** ChatGPT web (chatgpt.com), logged out, default model setting; model used per the share page metadata: gpt-6
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q8.png) · [ChatGPT share link](https://chatgpt.com/s/t_6adc6b24d950819181e8996990a9fa4b)
- **Question as sent:** What blockchain does Verdikta run on?
- **Answer (verbatim):**

`````text
**
Verdikta runs on
Base, an Ethereum Layer-2 blockchain.

Mainnet: Base Mainnet (Chain ID: 8453).

Testnet: Base Sepolia (Chain ID: 84532).

Smart contracts: Coordinate AI-powered evaluations, dispute resolution, and arbiter reputation.

Oracle infrastructure: Uses
Chainlink to connect on-chain smart contracts with off-chain AI processing.

Token: VDKA is Verdikta's utility token, used for arbiter staking.
Verdikta Documentation
+2

Official source: Verdikta Documentation .

I can also help you explore
 Verdikta’s VDKA token or
 Verdikta’s Base smart contracts.
`````

- **Marking** (8 Verdikta claims: 1 CORRECT, 0 WRONG, 7 UNSUPPORTED):
  1. "Verdikta runs on Base": **CORRECT** [F6]. Matches F6.
  2. "an Ethereum Layer-2 blockchain": **UNSUPPORTED** [not in facts list]. Base being a layer 2 is not in the facts list.
  3. "Mainnet: Base Mainnet (Chain ID: 8453).": **UNSUPPORTED** [F6]. Base matches F6. The chain ID is not in the facts list.
  4. "Testnet: Base Sepolia (Chain ID: 84532).": **UNSUPPORTED** [not in facts list]. No testnet in the facts list.
  5. "Smart contracts: Coordinate AI-powered evaluations, dispute resolution, and arbiter reputation.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  6. "Chainlink to connect on-chain smart contracts with off-chain AI processing": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  7. "VDKA is Verdikta's utility token, used for arbiter staking.": **UNSUPPORTED** [not in facts list]. No token is mentioned in the facts list.
  8. "Official source: Verdikta Documentation": **UNSUPPORTED** [not in facts list]. A link label, not checked against the facts list.

#### Q8 / Claude

- **Asked:** 2026-10-24 08:54:23 UTC
- **Product / model:** Claude web (claude.ai), signed in, Incognito chat, model selector 'Opus 5.5 High' (Opus 5.5, effort High)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q8.png)
- **Question as sent:** What blockchain does Verdikta run on?
- **Answer (verbatim):**

`````text
Searched the web

Searched the web

Not conclusive yet, sir. Checking the source directly.

Searched the web
verdikta.com network Base L2 LINK token

Searched the web verdikta.com network Base L2 LINK token

Verdikta runs on Base, sir, Coinbase’s Ethereum Layer‑2. According to Verdikta’s own repository, both its arbiter nodes and dispatcher are live on Base Sepolia (testnet) and Base Mainnet, with Base mainnet (chain ID 8453) designated as production and Base Sepolia (chain ID 84532) as the primary testnet.
github

verdikta


A few details:

Fees: The production ReputationAggregator takes evaluation fees in native ETH on Base, so requesters no longer need to buy or approve LINK. They only need ETH for gas.
github

Chainlink’s role: Verdikta uses Chainlink for oracle infrastructure and IPFS for decentralized storage. LINK contract addresses remain only for Chainlink transport and older deployments, while Verdikta’s own token handles staking and reputation.
github

github

What’s next: Multi-chain support is on the roadmap for v2.0 and beyond, so Base is the only network for now.
github


You may see an older directory listing describe it as an Ethereum platform. That’s technically true by inheritance, since Base settles to Ethereum, but the contracts themselves are on Base.
`````

- **Marking** (11 Verdikta claims: 3 CORRECT, 0 WRONG, 8 UNSUPPORTED):
  1. "Verdikta runs on Base": **CORRECT** [F6]. Matches F6.
  2. "Coinbase’s Ethereum Layer‑2": **UNSUPPORTED** [not in facts list]. Base's operator and layer-2 status are not in the facts list.
  3. "Base mainnet (chain ID 8453) designated as production and Base Sepolia (chain ID 84532) as the primary testnet": **UNSUPPORTED** [F6]. Base matches F6. The chain IDs and testnet are not covered.
  4. "takes evaluation fees in native ETH on Base": **CORRECT** [F2, F6]. Matches F2 (the prepay that pays the jury is in ETH) and F6 (Base).
  5. "so requesters no longer need to buy or approve LINK": **UNSUPPORTED** [F2]. Consistent with F2. LINK is not mentioned in the facts list.
  6. "They only need ETH for gas.": **UNSUPPORTED** [not in facts list]. Gas is not covered by the facts list.
  7. "Verdikta uses Chainlink for oracle infrastructure and IPFS for decentralized storage.": **UNSUPPORTED** [F5]. IPFS is consistent with F5. Chainlink is not covered.
  8. "Verdikta’s own token handles staking and reputation": **UNSUPPORTED** [not in facts list]. No token is mentioned in the facts list.
  9. "Multi-chain support is on the roadmap for v2.0 and beyond, so Base is the only network for now.": **UNSUPPORTED** [F6]. 'Base only' is consistent with F6. The roadmap is not covered.
  10. "You may see an older directory listing describe it as an Ethereum platform.": **UNSUPPORTED** [not in facts list]. A statement about third-party listings.
  11. "the contracts themselves are on Base": **CORRECT** [F6]. Matches F6.

#### Q8 / Perplexity

- **Asked:** 2026-10-24 08:32:54 UTC
- **Product / model:** Perplexity web (perplexity.ai), logged out, default Search mode; model per the thread metadata: turbo
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q8.png)
- **Question as sent:** What blockchain does Verdikta run on?
- **Answer (verbatim):**

`````text
Verdikta runs on Base, an Ethereum Layer-2 network. Its production contracts and arbiter nodes are live on Base Mainnet, with Base Sepolia used for testing.
docs.verdikta
+1

Details

Verdikta is built as EVM-compatible smart contracts, initially deployed on Base because it offers lower costs and faster finality than Ethereum mainnet.
verdikta

Its architecture is described as blockchain-agnostic: the protocol could expand to other EVM-compatible chains or rollups, but Base is the current production network.
docs.verdikta
+1

It uses Chainlink-based oracle infrastructure for arbitration and settlement; arbiter payments are denominated in LINK.
verdikta
+1
`````

- **Marking** (7 Verdikta claims: 1 CORRECT, 1 WRONG, 5 UNSUPPORTED):
  1. "Verdikta runs on Base": **CORRECT** [F6]. Matches F6.
  2. "an Ethereum Layer-2 network": **UNSUPPORTED** [not in facts list]. Base being a layer 2 is not in the facts list.
  3. "Its production contracts and arbiter nodes are live on Base Mainnet, with Base Sepolia used for testing.": **UNSUPPORTED** [F6]. Base matches F6. The testnet detail is not covered.
  4. "initially deployed on Base because it offers lower costs and faster finality than Ethereum mainnet": **UNSUPPORTED** [not in facts list]. The rationale is not covered by the facts list.
  5. "Its architecture is described as blockchain-agnostic": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  6. "It uses Chainlink-based oracle infrastructure for arbitration and settlement": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  7. "arbiter payments are denominated in LINK": **WRONG** [F2]. Correction: On Verdikta Bounties the jury is paid from the hunter's oracle prepay, attached in ETH (about 0.00024 ETH, refundable, usually spent in full). No LINK is involved for the hunter.

#### Q8 / Gemini

- **Asked:** 2026-10-24 08:40:41 UTC
- **Product / model:** Gemini web app (gemini.google.com), signed-in free account, Temporary chat, model selector 'Gemini Auto' (the app does not show which Gemini 3 model Auto used)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q8.png)
- **Question as sent:** What blockchain does Verdikta run on?
- **Answer (verbatim):**

`````text
Verdikta runs on Base, an Ethereum Layer 2 (L2) network.
Verdikta

Its smart contract infrastructure and dApps (such as the AI Jury system) deploy on Base, utilizing ETH for transaction gas payouts/fees alongside decentralized storage solutions like IPFS for handling off-chain evaluation packages.
Verdikta
`````

- **Marking** (5 Verdikta claims: 3 CORRECT, 0 WRONG, 2 UNSUPPORTED):
  1. "Verdikta runs on Base": **CORRECT** [F6]. Matches F6.
  2. "an Ethereum Layer 2 (L2) network": **UNSUPPORTED** [not in facts list]. Base being a layer 2 is not in the facts list.
  3. "Its smart contract infrastructure and dApps (such as the AI Jury system) deploy on Base": **CORRECT** [F6]. Matches F6.
  4. "utilizing ETH for transaction gas payouts/fees": **UNSUPPORTED** [not in facts list]. Gas is not covered by the facts list.
  5. "decentralized storage solutions like IPFS for handling off-chain evaluation packages": **CORRECT** [F5]. Matches F5 (evaluation package pinned to IPFS).

<a id="q9"></a>
### Q9. Is Verdikta a bug bounty program?

#### Q9 / ChatGPT

- **Asked:** 2026-10-24 08:24:18 UTC
- **Product / model:** ChatGPT web (chatgpt.com), logged out, default model setting; model used per the share page metadata: gpt-6
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q9.png) · [ChatGPT share link](https://chatgpt.com/s/t_6adc6b47e6348191964c3f9743d0ef34)
- **Question as sent:** Is Verdikta a bug bounty program?
- **Answer (verbatim):**

`````text
No, Verdikta is not primarily a bug bounty program. It is an AI-powered, blockchain-based bounty platform, but it does offer paid opportunities for completing tasks.
bounties.verdikta.org
+1

The key distinction is:

Verdikta Bounties: Yes, it offers bounties where you complete tasks, submit your work, and can earn ETH on the Base blockchain if your submission passes the evaluation criteria. Tasks may include writing, coding, research, and design.
bounties.verdikta.org

Security bug bounty: I couldn't verify a dedicated program that pays security researchers specifically for discovering and reporting vulnerabilities in Verdikta's own website, smart contracts, or infrastructure.

Bug reporting: Verdikta's documentation directs users to its GitHub issue tracker for application bugs, but explicitly says those reports are not paid bounties.
bounties.verdikta.org

Official links

Verdikta Bounty Board  — browse paid tasks.

Verdikta Developer Resources  — explore development and testing opportunities.

Verdikta Documentation  — review technical information.

If you're looking to earn money by finding security vulnerabilities, don't assume Verdikta's task bounties include security rewards. Check the program's scope and rules before testing its systems.

I can also
 check Verdikta's smart contract security opportunities or
 find its current paid bounties.
`````

- **Marking** (8 Verdikta claims: 1 CORRECT, 0 WRONG, 7 UNSUPPORTED):
  1. "No, Verdikta is not primarily a bug bounty program. It is an AI-powered, blockchain-based bounty platform": **UNSUPPORTED** [F6]. The facts list does not mention bug bounties. The description of AI-judged work bounties is consistent with F6.
  2. "it does offer paid opportunities for completing tasks": **CORRECT** [F1, F3]. Consistent with F1 and F3: the bounty is paid to the hunter whose submission passes first.
  3. "can earn ETH on the Base blockchain if your submission passes the evaluation criteria": **UNSUPPORTED** [F3, F6]. Base (F6) and 'passing work is paid' (F3) are consistent with the facts, but the payout currency is not stated, and only the FIRST passing submission is paid.
  4. "Tasks may include writing, coding, research, and design.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  5. "I couldn't verify a dedicated program that pays security researchers": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  6. "Verdikta's documentation directs users to its GitHub issue tracker for application bugs, but explicitly says those reports are not paid bounties.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  7. "Verdikta Bounty Board — browse paid tasks.": **UNSUPPORTED** [not in facts list]. A link label, not checked against the facts list.
  8. "don't assume Verdikta's task bounties include security rewards": **UNSUPPORTED** [not in facts list]. Advice. Not covered by the facts list.

#### Q9 / Claude

- **Asked:** 2026-10-24 08:55:06 UTC
- **Product / model:** Claude web (claude.ai), signed in, Incognito chat, model selector 'Opus 5.5 High' (Opus 5.5, effort High)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q9.png)
- **Question as sent:** Is Verdikta a bug bounty program?
- **Answer (verbatim):**

`````text
Searched the web

Searched the web

Not in the security sense, sir. Verdikta is a decentralized AI judgment protocol that happens to run a bounty board, which is an easy thing to confuse with a bug bounty.

What it actually is: A decentralized oracle system that provides AI-powered dispute resolution services on blockchain networks. Each query is evaluated on demand, in parallel, by a committee of independent AI arbiters, so no single model’s opinion decides the outcome. It runs on Base, Coinbase’s Ethereum layer-2 network.
verdikta

verdikta


Where the “bounty” confusion comes from: Its flagship live application is Verdikta Bounties. Work submissions are automatically evaluated and paid by AI arbiters. The flow runs: create a bounty, define a rubric, fund escrow, submit work, AI evaluation, then on-chain settlement. The tasks are general work rather than vulnerability hunting. Recent examples include a Python Pandas script for cleaning trading logs and math, task-creation and case-study jobs. A bug bounty pays researchers for responsibly disclosing security flaws; this is closer to a freelance marketplace with robot judges.
GitHub - verdikta/verdikta-applications: Example applications using the Verdikta blockchain. · GitHub
 +3


One detail worth knowing before you dive in: Browsing bounties and doing a dry run are free, but a live evaluation requires prepaying in ETH plus Base gas fees. At least one curated agent-bounty list declined to include Verdikta for exactly that reason, since it only lists platforms where agents can start earning without paying first. I’d treat the entry fee as a cost of doing business rather than a red flag, but it’s not free money.
github

github


I also found no evidence that Verdikta runs a security bug bounty for its own smart contracts. If that’s what you’re after, I’d check their GitHub or docs at docs.verdikta.com directly, or I can dig further. Shall I?
`````

- **Marking** (16 Verdikta claims: 3 CORRECT, 0 WRONG, 13 UNSUPPORTED):
  1. "Verdikta is a decentralized AI judgment protocol that happens to run a bounty board": **UNSUPPORTED** [F6]. Consistent with F6. The facts list does not mention bug bounties.
  2. "A decentralized oracle system that provides AI-powered dispute resolution services on blockchain networks.": **UNSUPPORTED** [F6]. Consistent with F6. The 'dispute resolution' framing is not covered.
  3. "Each query is evaluated on demand, in parallel": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  4. "by a committee of independent AI arbiters": **CORRECT** [F6]. Matches F6.
  5. "It runs on Base": **CORRECT** [F6]. Matches F6.
  6. "Coinbase’s Ethereum layer-2 network": **UNSUPPORTED** [not in facts list]. Base's operator and layer-2 status are not in the facts list.
  7. "Its flagship live application is Verdikta Bounties.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  8. "Work submissions are automatically evaluated and paid by AI arbiters.": **UNSUPPORTED** [F3, F6]. Evaluation by AI arbiters matches F6, and payment of passing work matches F3. 'Automatically' and 'paid by AI arbiters' (rather than by the bounty) are not stated.
  9. "The flow runs: create a bounty, define a rubric, fund escrow, submit work, AI evaluation, then on-chain settlement.": **UNSUPPORTED** [F5, F6]. Consistent with F5 and F6. Escrow and settlement mechanics are not stated.
  10. "The tasks are general work rather than vulnerability hunting.": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  11. "Recent examples include a Python Pandas script for cleaning trading logs": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  12. "this is closer to a freelance marketplace with robot judges": **UNSUPPORTED** [F6]. An interpretive comparison, consistent with F6.
  13. "a live evaluation requires prepaying in ETH": **CORRECT** [F2]. Matches F2.
  14. "plus Base gas fees": **UNSUPPORTED** [F6]. Base matches F6. Gas is not covered by the facts list.
  15. "At least one curated agent-bounty list declined to include Verdikta": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.
  16. "I also found no evidence that Verdikta runs a security bug bounty for its own smart contracts.": **UNSUPPORTED** [not in facts list]. Not covered. The answer points to 'docs.verdikta.com'. Perplexity's sources for Q4 include both docs.verdikta.com and docs.verdikta.org. The facts list settles neither domain.

#### Q9 / Perplexity

- **Asked:** 2026-10-24 08:33:21 UTC
- **Product / model:** Perplexity web (perplexity.ai), logged out, default Search mode; model per the thread metadata: turbo
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q9.png)
- **Question as sent:** Is Verdikta a bug bounty program?
- **Answer (verbatim):**

`````text
No. Verdikta is not a bug bounty program; it is a criteria-based, AI-judged bounty marketplace where creators fund tasks in escrow and participants submit deliverables such as research, writing, designs, or code for rubric-based evaluation.
dev
+1

What it is instead

Verdikta Bounties uses a published rubric, escrowed ETH, and a panel of AI arbiter nodes to grade submissions; passing work is paid automatically from the smart contract. Its purpose is to evaluate whether completed work meets stated acceptance criteria, rather than to discover security vulnerabilities.
dev
+2

Why it is not bug bounty

A bug bounty program is specifically for responsibly reporting security flaws within a defined scope, usually with safe-harbor rules and security-team triage. Verdikta explicitly states that it is not a security bug-bounty program and is not a place to report exploitable vulnerabilities.
dev

If you find a security flaw, use a dedicated vulnerability-disclosure or bug-bounty channel with a published scope and safe harbor instead.
dev
`````

- **Marking** (7 Verdikta claims: 2 CORRECT, 0 WRONG, 5 UNSUPPORTED):
  1. "Verdikta is not a bug bounty program; it is a criteria-based, AI-judged bounty marketplace where creators fund tasks in escrow and participants submit deliverables": **UNSUPPORTED** [F5, F6]. The facts list does not mention bug bounties. The description of escrowed, AI-judged, rubric-based bounties is consistent with F5 and F6.
  2. "Verdikta Bounties uses a published rubric": **CORRECT** [F6]. Matches F6 (rubric published in advance).
  3. "escrowed ETH": **UNSUPPORTED** [not in facts list]. Escrowed ETH is not stated in the facts list.
  4. "a panel of AI arbiter nodes to grade submissions": **CORRECT** [F6]. Matches F6.
  5. "passing work is paid automatically from the smart contract": **UNSUPPORTED** [F3]. Consistent with F3, but 'automatically' is not stated and only the FIRST passing submission is paid.
  6. "Its purpose is to evaluate whether completed work meets stated acceptance criteria, rather than to discover security vulnerabilities.": **UNSUPPORTED** [F6]. Consistent with F6 (work scored against a rubric published in advance). The facts list does not mention bug bounties.
  7. "Verdikta explicitly states that it is not a security bug-bounty program": **UNSUPPORTED** [not in facts list]. Not covered by the facts list.

#### Q9 / Gemini

- **Asked:** 2026-10-24 08:41:17 UTC
- **Product / model:** Gemini web app (gemini.google.com), signed-in free account, Temporary chat, model selector 'Gemini Auto' (the app does not show which Gemini 3 model Auto used)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q9.png)
- **Question as sent:** Is Verdikta a bug bounty program?
- **Answer (verbatim):**

`````text
No, Verdikta is not a security bug bounty program.
DEV Community

Despite using the word "bounties," Verdikta Bounties is an AI-judged task and freelance platform rather than a vulnerability disclosure or security testing platform.
DEV Community

Here is what Verdikta actually is:

Criteria-Based Bounties: It is a platform where creators can post general micro-tasks, social media shares, translations, content writing, or code tasks and lock funds in a smart contract.
Verdikta

AI Jury Evaluation: Instead of human moderators or security teams reviewing submissions, an automated AI jury evaluates the completed work against a predefined rubric.

Automatic Payments: If a submission passes the rubric threshold, it is automatically paid out in cryptocurrency (ETH) from escrow.
Verdikta

If you are looking to report software vulnerabilities or participate in ethical hacking/security bug bounties, platforms like HackerOne, Bugcrowd, or Intigriti are the appropriate choices.
`````

- **Marking** (5 Verdikta claims: 1 CORRECT, 0 WRONG, 4 UNSUPPORTED):
  1. "No, Verdikta is not a security bug bounty program.": **UNSUPPORTED** [not in facts list]. The facts list does not mention bug bounties. Consistent with F1-F6, which describe AI-judged work bounties.
  2. "Verdikta Bounties is an AI-judged task and freelance platform": **UNSUPPORTED** [F6]. AI judging of work matches F6. The 'freelance platform' framing is not in the facts list.
  3. "creators can post general micro-tasks, social media shares, translations, content writing, or code tasks": **UNSUPPORTED** [not in facts list]. Task types are not covered by the facts list.
  4. "an automated AI jury evaluates the completed work against a predefined rubric": **CORRECT** [F6]. Matches F6.
  5. "If a submission passes the rubric threshold, it is automatically paid out in cryptocurrency (ETH) from escrow.": **UNSUPPORTED** [F3]. Consistent with F3, but 'automatically' and the ETH currency are not stated, and only the FIRST passing submission is paid.

<a id="q10"></a>
### Q10. How do I write success criteria for a bounty?

#### Q10 / ChatGPT

- **Asked:** 2026-10-24 08:24:53 UTC
- **Product / model:** ChatGPT web (chatgpt.com), logged out, default model setting; model used per the share page metadata: gpt-6-mini
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/chatgpt_q10.png) · [ChatGPT share link](https://chatgpt.com/s/t_6adc6b6f195c81919dfc3eae7f17a46c)
- **Question as sent:** How do I write success criteria for a bounty?
- **Answer (verbatim):**

`````text
Writing success criteria for a bounty means defining exactly what someone must deliver for their work to be considered complete and eligible for the reward. Good criteria are specific, measurable, testable, and unambiguous.

How to write success criteria

Use this simple structure:

A bounty is considered successful when:

Deliverable: What must be completed or submitted.

Requirements: What the solution must include or satisfy.

Verification: How you will check whether it works.

Acceptance conditions: What must be true for the bounty to be approved.

Evidence: What proof the claimant must provide, if applicable.

Example: Software development bounty

Bounty: Fix a login bug — Reward: $100

Success criteria:

The login issue is reproducible before the fix and resolved afterward.

Valid user credentials allow users to log in successfully.

Invalid credentials are rejected with an appropriate error message.

Existing authentication functionality continues to work.

Automated tests covering the fix pass.

A pull request is submitted with a description of the fix and testing evidence.

The changes are reviewed and meet the project's contribution guidelines.

Example: Bug bounty (security)

Bounty: Identify a vulnerability in an application.

Success criteria:

The vulnerability affects an in-scope asset.

The report includes clear reproduction steps.

The security impact is demonstrated with a safe proof of concept.

The report explains the potential impact and affected components.

The finding is reproducible and not a duplicate of an existing report.

The report complies with the program's testing rules.

A reusable template
Writing
Bounty Success Criteria

The bounty will be considered complete when the submission meets all of the following criteria:

Required outcome: [Describe the specific result to achieve.]
Scope: [Define what is included and excluded.]
Functional requirements: [List the required behaviors or deliverables.]
Verification: [Explain how the result will be tested or validated.]
Submission requirements: [Specify documentation, code, screenshots, or other evidence.]
Acceptance conditions: All mandatory requirements must be met, and the submission must pass the defined verification process.
Exclusions: [List conditions that would make a submission ineligible, such as duplicates or out-of-scope work.]

Reward eligibility: The bounty will be awarded to eligible submissions that satisfy the published success criteria, subject to the stated review and payment rules.

Tips for making criteria effective

Be objective: Prefer “all five test cases pass” over “the solution works well.”

Make them verifiable: A reviewer should be able to independently confirm each requirement.

Separate must-haves from nice-to-haves: Only mandatory conditions should determine eligibility unless bonuses are explicitly defined.

Avoid ambiguity: Define scope, exclusions, deadlines, and duplicate-submission rules where relevant.

Keep the reward fair: Make sure the expected effort and complexity match the bounty amount.

The key principle is that two independent reviewers should reach the same decision about whether a submission qualifies.

What kind of bounty are you writing success criteria for? I can help you
 write criteria for a bug bounty or
 write criteria for a project or task bounty, tailored to your specific goal.
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

#### Q10 / Claude

- **Asked:** 2026-10-24 08:55:52 UTC
- **Product / model:** Claude web (claude.ai), signed in, Incognito chat, model selector 'Opus 5.5 High' (Opus 5.5, effort High)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/claude_q10.png)
- **Question as sent:** How do I write success criteria for a bounty?
- **Answer (verbatim):**

`````text
Figuring out what kind of bounty the request means.
Figuring out what kind of bounty the request means.

Good criteria let a stranger read them, do the work, and know before submitting whether they’ve earned the money, sir. If two reasonable people could disagree about whether a submission qualifies, the criteria aren’t finished yet.

Make every criterion pass/fail. “Improve page load speed” invites argument, whereas “Homepage loads in under 1.5 seconds on Lighthouse mobile, median of three runs” does not. Replace adjectives like “clean,” “fast,” and “robust” with a number, a test, or an observable behaviour.

Say how you’ll verify it. Name the test suite, the command, the dataset, or the manual steps you’ll follow. If you can hand over the verification script itself, so much the better, since hunters can then check their own work.

Define the deliverable precisely. State the form the work must take, whether that’s a pull request against a specific branch, a report in a set format, or a deployed URL. Include whatever must accompany it, such as documentation, tests, or a demo video.

Draw the boundaries. List what’s out of scope and any constraints, such as permitted libraries, licensing requirements, or “no breaking changes to the public API.” Most bounty disputes come from scope someone assumed rather than scope anyone wrote down.

Settle the awkward cases in advance. Decide what happens with partial solutions (no payout, or a pro-rated one), with multiple valid submissions (first to pass, best by some metric, or split), and with duplicates. Name who makes the final call and how quickly they’ll respond.

Include a deadline. State whether it is firm or extendable.

Here’s a template you can adapt:


BOUNTY: [One-line summary of the outcome]
REWARD: [Amount]  |  DEADLINE: [Date, timezone]

SUCCESS CRITERIA (all must pass):
1. [Observable, measurable outcome]
2. [Observable, measurable outcome]
3. Existing test suite passes (`npm test`) with no new warnings.

VERIFICATION:
Reviewer will [run X / follow steps Y] on [environment].

DELIVERABLE:
[Pull request to `main` / report in format Z], including [docs/tests].

OUT OF SCOPE:
- [Thing you don't want touched or solved]

CONSTRAINTS:
- [Language, licence, dependencies, compatibility]

PAYOUT RULES:
- First submission meeting all criteria wins. No partial payouts.
- Final judgement by [name/role]; review within [N] days.

A final check before you post it: hand the criteria to someone uninvolved and ask them to judge an imaginary submission. If they have to ask you a question, the answer belongs in the document.

Tell me what the bounty is for, sir, and I’ll draft the real thing rather than leave you with the template.
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

#### Q10 / Perplexity

- **Asked:** 2026-10-24 08:33:51 UTC
- **Product / model:** Perplexity web (perplexity.ai), logged out, default Search mode; model per the thread metadata: turbo
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/perplexity_q10.png)
- **Question as sent:** How do I write success criteria for a bounty?
- **Answer (verbatim):**

`````text
Write success criteria as specific, observable acceptance conditions that a reviewer could verify without guessing. Each criterion should state what must be delivered, where, and how it will be checked; vague wording such as “make it good” or “improve the project” leads to disputes.
docs.bounty
+2

Use this formula

For each criterion, use:

[Deliverable] + [measurable requirement] + [verification method]

Example: “The provided bug is fixed; the new regression test passes in CI on Python 3.11 and 3.12; the PR is approved by the repository maintainer.”
chainscorelabs
+1

What to include

Required deliverables: PR, report, dataset, design file, deployed demo, etc.

Functional requirements: What the work must do in the stated environment.

Quality requirements: Tests, documentation, accessibility, performance, security, formatting.

Verification method: CI run, test command, manual reviewer check, schema validation, link inspection, or rubric.

Out-of-scope items: What will not be required, so contributors do not overbuild.

Non-negotiable gates: License, originality, privacy, security, or “must merge” requirements.
docs.bounty
+2

Good vs. weak criteria
Weak criterion	Stronger success criterion
“Fix the login bug.”	“A signed-in user can log in with valid credentials; invalid credentials return the existing error message; add a regression test covering the reported case.”
“Write documentation.”	“Add a README section explaining installation, configuration, and one runnable example; all commands in the example execute successfully from a clean clone.”
“Research the market.”	“Provide a 1,500–2,000-word report comparing at least five competitors, with cited sources, pricing, target users, and a recommendation table.”
“Collect data.”	“Deliver 100 valid JSONL records matching the supplied schema, with no null values in question, answer, or source_url; include the validation script output.”
browse
+1
Keep it reviewable

Use binary or measurable language wherever possible: “passes,” “contains,” “runs within,” “covers,” “is merged,” or “matches the schema.” If quality is subjective, turn it into a weighted rubric with a clear passing threshold—for example, correctness 40%, clarity 25%, completeness 20%, documentation 15%, with 80/100 required to pass.
risein
+1

Short template
text
Success criteria
1. Deliverable: Submit a PR against [repo/branch] resolving issue #[number].
2. Functionality: [Exact behavior that must work].
3. Tests: Add/modify tests covering [cases]; all tests pass with [command].
4. Documentation: Update [file] to explain [change/usage].
5. Verification: CI must pass on [environments]; maintainer review is required.
6. Exclusions: Do not change [areas] or add [dependencies/features].
7. Acceptance: Bounty is paid only after [merge/approval/validation].

A strong bounty pairs this with the problem statement, context, technical environment, deadline, reward, reviewer, and dispute process; those details help contributors understand exactly what “done” means.
docs.bounty
+1
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

#### Q10 / Gemini

- **Asked:** 2026-10-24 08:41:49 UTC
- **Product / model:** Gemini web app (gemini.google.com), signed-in free account, Temporary chat, model selector 'Gemini Auto' (the app does not show which Gemini 3 model Auto used)
- **Evidence:** [screenshot](https://raw.githubusercontent.com/swiftbotlab/research-notes/0467805edd8199f9240e2be7618bf010a5954907/verdikta-ai-audit-2026-10-24/shots/gemini_q10.png)
- **Question as sent:** How do I write success criteria for a bounty?
- **Answer (verbatim):**

`````text
Well-written success criteria are the single most important factor in running a successful bounty. Clear criteria prevent scope creep, reduce disputes with contributors, and ensure you get high-quality submissions that directly meet your goals.

Here is a step-by-step guide and framework for writing effective bounty success criteria:

1. Structure of Great Success Criteria

A strong set of success criteria should cover four main pillars:

┌─────────────────────────────────────────────────────────────┐
│ 1. Functional Requirements (What it must DO)                │
│ 2. Technical / Quality Standards (How it must be BUILT)     │
│ 3. Edge Cases & Constraints (What it must HANDLE or AVOID)  │
│ 4. Deliverables & Documentation (What must be SUBMITTED)    │
└─────────────────────────────────────────────────────────────┘

2. Key Rules for Writing Criteria

Make them Binary (Pass/Fail): Avoid subjective statements like "The UI should look nice." Instead, use verifiable statements like "The UI must follow the provided Figma design file (colors, fonts, layout)."

Be Specific and Measurable: State exact metrics, thresholds, or test coverage percentages (e.g., "Passes all unit tests with >80% coverage").

Define the Verification Method: Clearly explain how you will test or judge the submission (e.g., "Will be verified using npm run test on Node v20" or "Evaluated by a 3-person panel based on the rubric below").

3. Detailed Component Breakdown
A. Functional Requirements

List every explicit feature or behavior required.

Use Must / Should / Could formatting or bulleted checklists.

Include step-by-step user flows or expected inputs and outputs.

B. Technical & Quality Standards

State language, framework, or library versions (e.g., React 18, Python 3.11+).

Specify performance thresholds (e.g., page load time under 2 seconds, API latency under 200ms).

Mandate code cleanliness (linting, zero console errors, no security vulnerabilities).

C. Edge Cases & Constraints

State how error conditions, invalid inputs, or empty states should be handled.

Specify cross-browser or cross-device support requirements.

D. Deliverable Package

Specify what format the submission should take (e.g., Pull Request to main, Docker image, link to hosted demo, video walkthrough).

Require documentation (e.g., updated README.md, inline code comments, setup steps).

4. Example Template & Comparison
❌ Weak Criteria Example

"Build a search feature for our app. It should be fast, work well, and look good."

✅ Strong Criteria Example

Deliverable: Open a Pull Request targeting the main branch with the completed feature.

Success Criteria:

Functionality:

User can type a keyword into the search bar and receive filtered results within 300ms.

Results update automatically using a 300ms debounce on input.

Displays an "Empty State" message when no results are found.

Technical & Code Quality:

Written in TypeScript adhering to our existing ESLint rules (npm run lint must pass with zero warnings).

Includes unit tests for the search filtering logic (npm run test must pass).

Design & UX:

Matches the responsive layout specified in [Figma Design Link].

Fully accessible: keyboard navigable (Tab/Enter) and compatible with screen readers.

Submission Requirements:

Must include a 1-minute screen recording demonstrating the search feature working locally.

Must update README.md with instructions on how to run local search index mock data.

5. Review Checklist Before Publishing

Before you publish your bounty, ask yourself:

[ ] Could two different developers read this and understand the exact same scope?

[ ] Can I test and verify every single bullet point without asking the contributor for clarification?

[ ] Is there an explicit rule on how ties or partial completions will be handled (if applicable)?

Are you designing a bounty for a software/code project, a creative/content submission, or a research/bug hunting task? If you share the specific task, I can draft a tailored set of criteria for you!
`````

- **Marking:** NO VERDIKTA MENTION. The answer contains no claim about Verdikta, so there is nothing to mark. It is a general answer, recorded as a missed opportunity for Verdikta to be named.

## 5. Error analysis

### 5.1 Recurring errors (seen in more than one answer or assistant)

- **LINK as the payment token (2 WRONG: Perplexity Q4, Q8).** Perplexity says evaluations are paid 'in LINK' and that 'arbiter payments are denominated in LINK'. ChatGPT Q8 and Claude Q8 also mention Chainlink. Claude says outright that the live contracts take native ETH and requesters no longer need LINK. Likely source: older Verdikta documentation and whitepaper text about LINK-paid arbiters, which Perplexity cites as `docs.verdikta` and `verdikta`. Fact F2 says the prepay is in ETH.
- **'Verdikta charges a fee' (2 WRONG: ChatGPT Q4, Perplexity Q4).** Both turn the per-evaluation jury cost into a Verdikta charge ('it does charge for using its services'; 'charges per AI evaluation'). F1 says there is no platform fee, and F2 says the per-attempt cost is the hunter's oracle prepay that pays the AI jury. The whitepaper's old tiered-fee table (quoted by Claude Q4: 5% down to 1%, paid in a token) is a second likely source of this confusion.
- **The prepay comes back (1 WRONG: ChatGPT Q5, plus 5 incomplete answers).** ChatGPT says the prepay is 'mostly refunded'. Perplexity Q5 and Gemini Q3/Q5 say only that unused prepay is refunded, which is true but leaves a hunter expecting money back. Only Claude (Q3, Q4, Q5) says the prepay is usually spent in full (F2).
- **The payout rule is missing or reversed (1 WRONG: Perplexity Q3, plus many omissions).** Perplexity Q3 says 'the highest-scoring passing submission wins', the exact opposite of F3. ChatGPT Q3/Q5/Q9, Perplexity Q5/Q9 and Gemini Q9 say passing work 'is paid' without 'first'. Claude Q3/Q5 and Gemini Q3 get F3 exactly right ('First-Pass-Wins'; 'the earliest passing submission, by submission order, not the highest score').

### 5.2 One-off errors

- **Wrong chain (Claude Q1: 'It runs on Ethereum').** This comes from a third-party AI tools directory listing ('neura') that Claude itself called thin. The same assistant gets Base right in Q8 and Q9 and even explains the Ethereum wording there.
- **Entity confusion (Gemini Q4).** Gemini answered about 'Verdikt' (an e-commerce fraud tool and a business-advice subscription) and asked the user to clarify. It gave no information about Verdikta's fees, even though in Q5 it says correctly that 'Verdikta itself charges no platform fee'.
- **Different-looking product (Gemini Q1).** Built from a SourceForge listing: 'private, confidential dispute resolution and contract management' for individuals and small businesses. Nothing in it is contradicted by the facts list, so there is no WRONG mark, but it mentions neither bounties, nor Base, nor the AI arbiter panel. A newcomer would not recognise Verdikta Bounties from it.

### 5.3 Where each assistant goes wrong, and why

- **ChatGPT (gpt-6, logged out): 2 WRONG.** Its sourcing is good (it cites bounties.verdikta.org for Q3, Q5, Q7 and Q9) and it is right on immutability, refunds to the creator and Base. It fails on money: it calls the jury cost a Verdikta charge (Q4) and over-promises the refund (Q5). It never states the first-pass rule. Its Q1 and Q8 answers mention a VDKA token, which the facts list does not cover.
- **Claude (Opus 5.5, Incognito): 1 WRONG.** It is the most complete on the facts list: Q3 states F1-F6 almost word for word, and Q5 gives F1, F2 and F3 exactly. Its single error is in Q1, where it searched, found mostly a directory listing, and repeated that listing's 'runs on Ethereum'. It flags thin sourcing itself.
- **Perplexity (turbo, logged out): 3 WRONG.** It is right on immutability (Q7) and Base (Q8) and gives the prepay amount (Q5). It mixes current product pages with older protocol documentation, which produces the LINK claims (Q4, Q8). In Q3 it draws on a dev.to post and states a best-of rule that contradicts F3.
- **Gemini (Auto, Temporary chat): 0 WRONG, but 2 identity problems.** When it finds Verdikta-specific sources (Zealy, DEV Community) it is accurate: Q3, Q5, Q7 and Q8 are all right, including First-Pass-Wins and the full refund to the creator. When those sources do not come up, it falls back to look-alike products (Verdikt in Q4) or a generic directory blurb (Q1).

### 5.4a Sources shown next to each WRONG claim (where the error most likely came from)

These are the source chips and links each app displayed beside the wrong sentence, as captured from the page. They show where retrieval picked up the error, and so which page to fix.

- **Perplexity Q8, 'arbiter payments are denominated in LINK':** chip `verdikta +1`, linking to https://www.verdikta.com/whitepaper. Perplexity's Q8 source list also includes docs.verdikta.org/overview.
- **Perplexity Q4, 'charges per AI evaluation (in LINK)':** chip `docs.verdikta +1`. Perplexity's Q4 source list: docs.verdikta.com/apps/user-guide, docs.verdikta.org/apps/user-guide, www.verdikta.com, www.verdikta.com/whitepaper, plus two third-party review sites (verdikta.tenereteam.com, aichief.com). These are protocol and user-guide pages, not the bounty platform's fee page.
- **Perplexity Q3, 'the highest-scoring passing submission wins':** chip `dev`, linking to a dev.to tutorial (dev.to/kurumi_82661ed12516efd1f7/how-to-create-your-first-ai-evaluated-bounty-step-by-step-19bd). A community post, not Verdikta's own page, is the source of the one answer that reverses F3.
- **ChatGPT Q4, 'it does charge for using its services':** the paragraph that follows cites `Verdikta Documentation +1`, and the answer links docs.verdikta.org/apps/example-frontend/run-query. That is the developer page for paid AI queries, not the bounty platform.
- **ChatGPT Q5, 'mostly refunded':** chip `Verdikta +1` beside the refund sentence. The answer links the bounty board, bounties.verdikta.org.
- **Claude Q1, 'It runs on Ethereum':** chip `neura`, linking to https://neura.market/ai-tools-directory/legal/verdikta, a third-party AI tools directory that Claude itself called its main source.
- **Pattern:** 3 of the 6 WRONG claims trace to protocol-level pages (whitepaper, developer docs and user guide) that describe the older LINK-paid, per-query model. 2 trace to third-party pages (a dev.to tutorial and a tools directory). The bounty platform's own pages (bounties.verdikta.org) are cited next to correct answers far more often (ChatGPT Q3, Q7, Q9; Perplexity Q5, Q7), though ChatGPT's 'mostly refunded' (Q5) appears beside a generic Verdikta chip.

### 5.4 Which questions produce no Verdikta mention at all

- Q2, Q6 and Q10 produce zero Verdikta mentions in all four assistants (12 of 40 records). These are exactly the questions a potential hunter or bounty creator would ask before they know the name. Each one is a natural place for Verdikta to be named: Q2 (where agents find paid work), Q6 (Verdikta's first-pass rule answers it directly) and Q10 (Verdikta's rubrics are success criteria). Claude's Q10 template even suggests 'First submission meeting all criteria wins' without naming any platform.

## 6. Corrections and what to fix

### 6.1 Publishable one-line corrections (one per recurring error)

- **Fees:** 'Verdikta Bounties charges no platform fee. The whole bounty goes to the hunter whose submission passes. If nobody passes before the deadline, the creator reclaims the full amount, and the platform keeps nothing.'
- **Cost to submit:** 'To start a submission, a hunter attaches a refundable oracle prepay of about 0.00024 ETH, in ETH on Base, not LINK. In practice it is usually spent in full on the jury round, so treat it as the cost of each attempt.'
- **Who gets paid:** 'The FIRST submission that clears the acceptance threshold is paid the entire bounty. It is not a best-of contest judged at the deadline. A later, higher-scoring submission gets nothing.'
- **Chain:** 'Verdikta runs on Base. Its contracts are on Base, not on Ethereum mainnet.'
- **Judging:** 'Work is scored by a panel of independent AI arbiter nodes against a rubric published in advance, and the per-criterion scores are public and auditable.'
- **Immutability:** 'A bounty cannot be cancelled or edited after it is created. The rubric and evaluation package are pinned to IPFS and fixed on-chain.'

### 6.2 Where an accurate source would most likely be picked up

- **Fix or annotate the old whitepaper and docs pages.** The LINK-payment and tiered-fee wording is the most likely source of the LINK and 'Verdikta charges' errors. Perplexity cites `docs.verdikta` and `verdikta` for them, and Claude quotes the whitepaper fee table. A dated note at the top ('Verdikta Bounties today: no platform fee; jury prepay in ETH, about 0.00024 ETH') would give retrieval a current, quotable line.
- **Publish one plain FAQ page whose headings are these exact ten questions,** with the facts above as the first sentence of each answer. All four assistants drew on web sources for the Verdikta questions (their source chips show this), and the pages they quoted most accurately were short, plain-text Q&A pages (bounties.verdikta.org FAQ/support pages, dev.to posts, Zealy). One-sentence answers that match the question wording are the easiest thing for these assistants to quote.
- **Correct the third-party directory listings** (SourceForge, the 'neura' AI tools directory). Gemini Q1 and Claude Q1 relied on them, and they produced the 'confidential dispute resolution app' picture and the 'runs on Ethereum' error. Ask for Base, bounties and 'no platform fee' to be listed.
- **Target the general questions.** To appear in answers to Q2, Q6 and Q10, Verdikta needs to show up in the pages those answers cite: lists of agent job boards (Perplexity cited moltjobs, Claude cited toku.agency and ClawTasks, ChatGPT cited a 'GOAT Market' list and Shaduf), and bounty-writing guides. A short guide called 'How to write success criteria for a bounty', using a real Verdikta rubric as the example, is the most direct fit for Q10.
- **Disambiguate the name.** Gemini mixed Verdikta up with 'Verdikt'. A one-line 'Verdikta (not Verdikt): AI-judged bounties on Base' in page titles and descriptions helps.

## 7. Limitations and notes for the repeat run

- Answers are sampled once. The same question can give a different answer minutes later, and Perplexity and ChatGPT answers depend on live web search. Treat each record as one sample on 2026-10-24, not a fixed property of the assistant.
- ChatGPT's model can change silently: Q10 was answered by gpt-6-mini while Q1-Q9 used gpt-6, as the share-page metadata shows. Gemini Auto does not reveal its model at all. For the repeat run, record the same metadata fields (ChatGPT share link and `resolved_model_slug`; Perplexity `display_model`; the Claude and Gemini model selectors) and keep the same modes (logged out for ChatGPT and Perplexity, Incognito/Temporary for Claude and Gemini).
- UNSUPPORTED is not a verdict of falsehood. Many UNSUPPORTED claims (chain ID 8453, IPFS, closeExpiredBounty, per-bounty jury makeup) may be accurate, but the facts list does not settle them, so this audit does not either.
- The capture script and raw captures are kept, so the run can be repeated the same way.

---
This report was newly made for Verdikta bounty #326 on 2026-10-24. All 40 answers were collected for it on that date and are reproduced as received.
