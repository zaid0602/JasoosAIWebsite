"""JasoosAI promotional website, built with Gradio.

Run:  pip install gradio  &&  python app.py
"""
import gradio as gr

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=IBM+Plex+Mono:wght@400;500&family=Instrument+Sans:wght@400;500;600&display=swap');
:root{--bg:#eceff3;--sf:#fff;--ink:#16213a;--mute:#566079;--line:#d3d9e3;--tag:#f4b400;--tagink:#3a2a00;--bad:#d23b3b;--ok:#13826c}
.dark{--bg:#0f1524;--sf:#18213a;--ink:#e8ecf6;--mute:#9aa6c3;--line:#2a3555;--tagink:#241a00;--ok:#3ecfb0}
*,*::before,*::after{box-sizing:border-box}
gradio-app,.gradio-container,body{background:var(--bg)!important;font-family:'Instrument Sans',system-ui,sans-serif!important}
.gradio-container{max-width:1120px!important;width:100%!important;margin:0 auto!important;padding:0 16px 40px!important;color:var(--ink)}
footer{display:none!important}
.j h1,.j h2,.j h3{font-family:'Bricolage Grotesque',system-ui,sans-serif;color:var(--ink);letter-spacing:-.02em;line-height:1.08;margin:0}
.j h1{font-size:clamp(28px,5.5vw,60px);font-weight:800}
.j h2{font-size:clamp(24px,4vw,42px);font-weight:800;max-width:24ch;margin-top:52px}
.j p,.j li,.j td,.j th{color:var(--mute);font-size:16px;line-height:1.6}
.j .lede{max-width:56ch;margin:16px 0 0;font-size:clamp(16px,2vw,18px)}
.j .hero-wrap{padding-top:28px}
.j .bar{display:flex;align-items:center;justify-content:space-between;padding:14px 0;border-bottom:1px solid var(--line);flex-wrap:wrap;gap:8px 16px}
.j .bar-sub{font-size:14px;color:var(--mute)}
.j .logo{font:800 22px 'Bricolage Grotesque'}.j .logo span{background:var(--tag);color:var(--tagink);padding:0 6px;border-radius:3px;margin-left:2px}
.j .stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:16px 24px;margin:28px 0 0;padding:0;list-style:none}
.j .stats li{font-size:15px;line-height:1.4}
.j .stats b{display:block;font:800 clamp(22px,3vw,26px) 'Bricolage Grotesque';color:var(--ink);line-height:1.15;margin-bottom:2px}
.j .tbl{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--line);border-radius:8px;background:var(--sf);margin-top:28px;max-width:100%}
.j table{border-collapse:collapse;width:100%;min-width:560px}
.j th,.j td{text-align:left;padding:13px 16px;border-bottom:1px solid var(--line);vertical-align:top}
.j th{color:var(--mute);font-weight:600;font-size:14px}.j td:nth-child(3){color:var(--ok);font-weight:600}
.j tr:last-child td{border-bottom:0}
.j .bento{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-top:32px}
.j .bento>div{padding:24px;border:1px solid var(--line);border-radius:8px;background:var(--sf)}
.j .bento h3{font-size:20px;margin-bottom:8px}.j .bento p{margin:0;font-size:15px}
.j .s4{grid-column:span 4}.j .s2{grid-column:span 2}.j .s3{grid-column:span 3}
.j .dk{background:var(--ink)!important;border-color:var(--ink)!important}.j .dk h3{color:var(--bg)}.j .dk p{color:var(--bg);opacity:.8}
.j .big{font:800 clamp(38px,6vw,52px)/1 'Bricolage Grotesque';color:var(--ok);margin-bottom:8px}
.j .chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.j .chips span{font:500 12.5px 'IBM Plex Mono';border:1px solid var(--line);padding:3px 8px;border-radius:4px;color:var(--mute)}
.j .arch{margin-top:28px;border-left:3px solid var(--ink)}
.j .arch div{display:grid;grid-template-columns:48px 220px 1fr;gap:10px;padding:14px 0;border-bottom:1px solid var(--line);align-items:baseline}
.j .arch i{font:500 14px 'IBM Plex Mono';font-style:normal;color:var(--mute);padding-left:12px}
.j .arch b{font:700 18px 'Bricolage Grotesque';color:var(--ink)}
.j .arch .gate{background:var(--tag);margin-left:-3px;padding-left:3px}.j .arch .gate *{color:var(--tagink)}
.j .roi{display:grid;grid-template-columns:repeat(3,1fr);margin-top:28px;border-top:2px solid var(--ink)}
.j .roi div{padding:20px 20px 20px 0;border-bottom:1px solid var(--line)}
.j .roi b{display:block;font:800 clamp(26px,3.5vw,34px) 'Bricolage Grotesque';color:var(--ok);line-height:1.1;margin-bottom:4px}
.j .roi small{color:var(--mute);font-size:14px;display:block;line-height:1.4}
.j .two{display:grid;grid-template-columns:1fr 1fr;gap:48px;margin-top:28px}
.j .two h3{font-size:22px;margin-bottom:10px}.j .two ul{list-style:none;margin:0;padding:0}
.j .two li{padding:11px 0;border-bottom:1px solid var(--line);font-size:15px}.j .two li b{color:var(--ink)}
.j .cta{background:var(--ink);border-radius:8px;padding:48px 36px;margin-top:64px}
.j .cta h2{color:var(--bg);margin-top:0}.j .cta p{color:var(--bg);opacity:.8}
.j .btn-group{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}
.j .btn{display:inline-block;padding:12px 20px;border-radius:6px;font-weight:600;text-decoration:none;background:var(--tag);color:var(--tagink);text-align:center;transition:opacity .15s ease}
.j .btn:hover{opacity:.92}
.j .btn.o{background:transparent;color:var(--bg);border:2px solid var(--bg)}
.case{border:2px solid var(--ink);border-radius:8px;overflow:hidden;background:var(--sf);box-shadow:0 4px 14px rgba(0,0,0,0.06)}
.case .hd{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px;padding:10px 14px;background:var(--tag);color:var(--tagink);font:600 12.5px 'IBM Plex Mono'}
.case .term{background:#0a0f1c;color:#dfe6f5;padding:18px;min-height:220px;font:400 13px/1.7 'IBM Plex Mono',monospace;white-space:pre-wrap;word-break:break-word;overflow-x:auto;-webkit-overflow-scrolling:touch}
.case h3{font:700 16px 'Bricolage Grotesque';color:#fff;margin:0 0 8px}
.case .k{color:#8fa0c8}.case .bad{color:#ff7b7b}.case .good{color:#4fe0c0}.case .hl{color:#ffcf45}
.step-btn-row{display:flex!important;flex-wrap:wrap!important;gap:6px!important;margin-bottom:10px!important}
.step-btn-row>*{flex:1 1 calc(20% - 6px)!important;min-width:0!important}
.step-btn-row button{font-weight:600!important;padding:7px 4px!important;font-size:12.5px!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important}
@media(max-width:850px){
  .j .bento>div{grid-column:span 6!important}
  .j .two{grid-template-columns:1fr;gap:32px}
  .j .arch div{grid-template-columns:36px 1fr;gap:4px 10px;padding:12px 8px 12px 0;align-items:start}
  .j .arch div i{grid-row:1/3;padding-left:8px;font-size:15px;font-weight:700}
  .j .arch div b{grid-column:2;font-size:16px}
  .j .arch div span{grid-column:2;font-size:14px;line-height:1.5}
  .j .roi{grid-template-columns:1fr 1fr}
  .j h2{max-width:100%;margin-top:40px}
}
@media(max-width:640px){
  .gradio-container{padding:0 12px 32px!important}
  .j .bar{flex-direction:column;align-items:flex-start;gap:6px;padding:12px 0}
  .j .hero-wrap{padding-top:20px!important}
  .j .bento>div{padding:18px 14px}
  .j .bento h3{font-size:18px}
  .j .tbl table{min-width:500px}
  .j th,.j td{padding:10px 12px;font-size:13.5px}
  .j .cta{padding:30px 18px;margin-top:40px}
  .j .btn-group{flex-direction:column;gap:10px}
  .j .btn{display:block;width:100%;margin:0}
  .case .term{padding:14px 12px;font-size:12px;min-height:200px}
}
@media(max-width:520px){
  .step-btn-row>*{flex:1 1 calc(33.333% - 6px)!important}
}
@media(max-width:420px){
  .j .roi{grid-template-columns:1fr}
  .j .roi div{padding:14px 0}
  .j .stats{grid-template-columns:1fr 1fr;gap:14px 16px}
}
"""

STEPS = [
    ("Detect", "00:00", "Alert firing",
     '<span class="k">source</span>   prometheus\n<span class="k">service</span>  checkout-api\n<span class="bad">5xx rate 38%</span> (baseline 0.1%)\n<span class="k">severity</span> P1'),
    ("Correlate", "00:00", "Gathering evidence",
     '<span class="k">fingerprint</span>  sha256:9c1e…a47\n<span class="k">cache</span>        miss, new incident\n<span class="k">playbooks</span>    3 matched (CrashLoopBackOff)\n<span class="k">blast radius</span> web-frontend, order-svc'),
    ("Diagnose", "00:42", "Root cause",
     '<span class="bad">Missing env PAYMENT_VAULT_SECRET</span>\n<span class="k">commit</span>   <span class="hl">f89a2b1</span>, deployed 4 min ago\n<span class="k">proposed</span> k8s rollback to v2.4.0\n<span class="k">verify</span>   rate(http_5xx[1m]) &lt; 0.001'),
    ("Authorize", "01:10", "Approval required",
     'Action is paused at the human gate.\n<span class="k">namespace</span> prod (allowed)\n<span class="k">action</span>    rollout undo checkout-api\n<span class="k">operator</span>  on-call: alex'),
    ("Verify", "02:05", "Resolved",
     '<span class="good">Rolled back to v2.4.0</span>\n<span class="good">error rate 0.04% (&lt; 0.1%)</span>\n<span class="k">annotation</span>  posted to Grafana\n<span class="k">post-mortem</span> INC-2041/final_report.md'),
]


def case_html(i):
    name, t, head, body = STEPS[i]
    return (f'<div class="case"><div class="hd"><span>CASE INC-2041 · checkout-api · {name}</span>'
            f'<span>{t}</span></div><div class="term"><h3>{head}</h3>{body}</div></div>')


def show(i):
    # panel html, approve button visibility, state, next-button label
    return case_html(i), gr.update(visible=(i == 3)), i, gr.update(value="Replay" if i == 4 else "Next step")


NAV = '<div class="j"><div class="bar"><div class="logo">Jasoos<span>AI</span></div><div class="bar-sub">Autonomous SRE Command Center</div></div></div>'

HERO = """<div class="j hero-wrap">
<h1>Stop alert fatigue. Resolve outages in seconds, not hours.</h1>
<p class="lede">JasoosAI is the model-agnostic autonomous SRE co-pilot. It turns telemetry storms into a pinpointed root cause, a verified PromQL query, and a one-click safe fix that only runs when a human approves it.</p>
<ul class="stats"><li><b>60%+</b>lower MTTR</li><li><b>&lt;45ms</b>detect and correlate</li><li><b>70%+</b>fewer LLM tokens</li><li><b>370+</b>built-in runbooks</li></ul>
<p style="margin-top:24px;font-size:14px">Try the interactive case file: step through the incident or press Authorize.</p></div>"""

BODY = """<div class="j">
<h2>The 2 AM page, before and after</h2>
<p class="lede">On-call engineers lose most of an incident to gathering context. JasoosAI does that work first, then asks for your approval.</p>
<div class="tbl"><table><thead><tr><th>Challenge</th><th>Manual incident response</th><th>With JasoosAI</th></tr></thead><tbody>
<tr><td>Alert fatigue</td><td>Hundreds of fragmented alerts a day</td><td>Signals correlated into one incident thread</td></tr>
<tr><td>Time to triage</td><td>8–15 minutes across dashboards</td><td>Under 45 seconds, blast radius mapped</td></tr>
<tr><td>Time to resolution</td><td>45–60+ minutes per P1</td><td>Under 15 minutes, culprit commit named</td></tr>
<tr><td>Runbooks</td><td>Stale wikis, ~30% search hit rate</td><td>85%+ accurate semantic retrieval</td></tr>
<tr><td>Fix risk</td><td>Copy-pasted commands under pressure</td><td>Parameterized actions behind human approval</td></tr>
<tr><td>LLM spend</td><td>A paid call for every duplicate alert</td><td>Cached diagnosis, 0 tokens</td></tr>
<tr><td>Post-mortems</td><td>2–4 hours of timeline work</td><td>Generated in under 2 minutes</td></tr>
</tbody></table></div>

<h2>Built for the people holding the pager</h2>
<div class="bento">
<div class="s4"><h3>Catch it before the alert fires</h3><p>Isolation Forest anomaly detection watches request rate, CPU, memory and p99 latency. Prophet forecasting projects 12 hours of history to warn about disk or connection-pool exhaustion hours ahead.</p><div class="chips"><span>Prometheus</span><span>Grafana</span><span>SigNoz</span><span>Datadog</span><span>Coralogix</span><span>CloudWatch</span></div></div>
<div class="s2"><div class="big">0</div><h3>Tokens on repeat alerts</h3><p>Token Shield™ fingerprints alerts with SHA-256 and serves the cached diagnosis in under 45ms.</p></div>
<div class="s2"><h3>Any model, no lock-in</h3><p>OpenAI, Claude, Gemini or local Ollama, with provider failover in about a second.</p></div>
<div class="s4 dk"><h3>Nothing destructive runs without a human</h3><p>Rollbacks, restarts, scaling and patches stop at a hardcoded approval gate. kube-system, vault and security namespaces are permanently blocklisted, and every decision is logged.</p></div>
<div class="s3"><h3>370+ runbooks on day one</h3><p>Kubernetes, AWS, Sentry, Spinnaker and Coralogix playbooks, searched semantically with keyword fallback.</p></div>
<div class="s3"><h3>Works where you already are</h3><p>Approve from Slack with /jasoos triage, get WhatsApp digests, call the REST API from PagerDuty or CI, or use the terminal CLI.</p></div>
</div>

<h2>Five tiers, one approval gate</h2>
<div class="arch">
<div><i>1</i><b>Telemetry ingestion</b><span>Prometheus, Grafana, SigNoz OTLP, Datadog, Coralogix</span></div>
<div><i>2</i><b>Reasoning core</b><span>Anomaly models, Token Shield cache, runbook RAG, multi-agent loop</span></div>
<div class="gate"><i>3</i><b>Human-in-the-loop gate</b><span>Hard interrupt before self-heal, durable checkpoints, PII sanitizer</span></div>
<div><i>4</i><b>Self-healing registry</b><span>Kubernetes rollout undo, Ansible, Terraform, AWS and GCP SDKs</span></div>
<div><i>5</i><b>Experience and audit</b><span>Command Center UI, Slack, WhatsApp, CLI, post-mortems in MinIO or S3</span></div>
</div>

<h2>Measured against the manual way</h2>
<div class="roi">
<div><b>95%</b><small>faster to acknowledge</small></div><div><b>60%+</b><small>lower MTTR</small></div><div><b>98%</b><small>faster runbook discovery</small></div>
<div><b>70%+</b><small>LLM cost savings</small></div><div><b>99%</b><small>faster post-mortems</small></div><div><b>0</b><small>unauthorized actions</small></div>
</div>

<h2>Safe for the team that signs off</h2>
<div class="two">
<div><h3>Security and compliance</h3><ul>
<li><b>Air-gapped option.</b> Run Ollama, Qdrant and MinIO inside your firewall.</li>
<li><b>Sanitized input.</b> Passwords, JWTs, AWS keys and card numbers are scrubbed before the model sees them.</li>
<li><b>Durable audit trail.</b> Timestamped operators, payloads and outputs.</li>
<li><b>Least-privilege RBAC.</b> Honors ServiceAccount and IAM boundaries.</li></ul></div>
<div><h3>Who it helps</h3><ul>
<li><b>On-call engineers.</b> Context at 2 AM and verified one-click fixes.</li>
<li><b>Lead SREs.</b> Less toil and lower LLM spend.</li>
<li><b>Engineering leaders.</b> SLA protection and standard post-mortems.</li>
<li><b>Security officers.</b> No public-LLM leakage, full tool-use record.</li></ul></div>
</div>
<h2>Questions leaders ask first</h2></div>"""

FAQ = [
    ("How do you stop the AI from running dangerous commands?",
     "Destructive operations never run autonomously. The workflow has a hardcoded interrupt before self-healing, so rollback, restart, scale and patch need explicit human confirmation. Critical namespaces like kube-system and vault are permanently blocklisted."),
    ("Can we run it without sending data outside our network?",
     "Yes. JasoosAI supports local Ollama models (Llama 3.2 / 3.3), so the whole system can run in a private cluster or an air-gapped environment."),
    ("How does Token Shield™ save money?",
     "Outages produce storms of near-identical alerts. Each is hashed into a SHA-256 fingerprint; repeats inside the cache window get the verified diagnosis in under 45ms with no tokens used, saving 70%+ on LLM spend."),
    ("Does it replace our monitoring tools?",
     "No. It connects to Prometheus, Grafana, SigNoz, Datadog, Coralogix and CloudWatch through their standard APIs."),
]

CTA = """<div class="j"><div class="cta"><h2>Let JasoosAI take the next page.</h2>
<p class="lede">See a checkout-api incident go from alert to verified fix in a live demo, or explore the offline simulation sandbox on your own.</p>
<div class="btn-group"><a class="btn" href="#">Book an enterprise demo</a><a class="btn o" href="#">Launch simulation sandbox</a><a class="btn o" href="#">Explore 370+ runbooks on GitHub</a></div></div></div>"""

with gr.Blocks(title="JasoosAI — Autonomous SRE Command Center") as demo:
    gr.HTML(f"<style>{CSS}</style>")
    gr.HTML(NAV)
    state = gr.State(0)

    with gr.Row(equal_height=False):
        with gr.Column(scale=11, min_width=280):
            gr.HTML(HERO)
        with gr.Column(scale=10, min_width=280):
            panel = gr.HTML(case_html(0))
            with gr.Row(elem_classes=["step-btn-row"]):
                step_btns = [gr.Button(s[0], size="sm") for s in STEPS]
            approve = gr.Button("🚀 Authorize & execute fix", variant="primary", visible=False)
            nxt = gr.Button("Next step", variant="secondary")

    outs = [panel, approve, state, nxt]
    for n, b in enumerate(step_btns):
        b.click(lambda n=n: show(n), None, outs)
    approve.click(lambda: show(4), None, outs)
    nxt.click(lambda i: show((i + 1) % 5), state, outs)

    gr.HTML(BODY)
    for q, a in FAQ:
        with gr.Accordion(q, open=False):
            gr.Markdown(a)
    gr.HTML(CTA)

if __name__ == "__main__":
    demo.launch()

