<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Palinsesto</title>
<meta name="theme-color" content="#FF6A5C">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Palinsesto">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@600;700&display=swap">
<style>
html{padding-top:env(safe-area-inset-top,0px)}
body{margin:0}
[hidden]{display:none!important}
.set{background:var(--surface);border-radius:20px;display:flex;flex-direction:column;box-shadow:var(--shadow)}
.set>*{display:flex;align-items:center;gap:12px;padding:14px 16px;font-weight:600;text-align:left;width:100%}
.set>*+*{border-top:1px solid var(--line)}
.set svg{width:20px;height:20px;color:var(--brand);flex:none}
.set small{display:block;color:var(--muted);font-weight:500;font-size:12.5px}
.set .g{flex:1;min-width:0}
/* Layout: app da telefono a colonna unica (max 460px), header + card "prossimo" a gradiente tramonto, striscia giorni scorrevole, timeline, tab bar in basso con + centrale. */
:root{
  --bg:#F3F1FA; --surface:#FFFFFF; --surface-2:#ECE9F6; --line:#E2DEF0;
  --fg:#1B1830; --muted:#6D6886; --faint:#A39FB8;
  --brand:#FF5C5C; --brand-2:#FF9A3D; --brand-fg:#FFFFFF;
  --hero-a:#FF5C7A; --hero-b:#FF8A3D; --hero-c:#FFC23D;
  --t-call:#3D7BFF; --t-app:#9A5CFF; --t-live:#FF3D71; --t-spon:#F5A100; --t-pers:#12B886; --t-dead:#6B7A99;
  --ok:#12B886;
  --f-display:"Outfit", "Segoe UI", system-ui, sans-serif;
  --f-body:"Plus Jakarta Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --f-mono:"JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;
  --shadow:0 2px 6px rgba(40,30,90,.06),0 12px 32px rgba(40,30,90,.08);
  --tint:14%;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0E0D1A; --surface:#1A1830; --surface-2:#242140; --line:#2E2A4D;
  --fg:#F4F2FF; --muted:#A7A2C6; --faint:#6E6993;
  --brand:#FF6B6B; --brand-2:#FFA14D; --brand-fg:#1A0E0E;
  --hero-a:#E8457A; --hero-b:#F2763A; --hero-c:#F5B434;
  --t-call:#6E9BFF; --t-app:#B98BFF; --t-live:#FF6B93; --t-spon:#FFC247; --t-pers:#3EDBA6; --t-dead:#96A3C0;
  --ok:#3EDBA6; --shadow:0 2px 6px rgba(0,0,0,.3),0 12px 32px rgba(0,0,0,.35); --tint:20%; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0E0D1A; --surface:#1A1830; --surface-2:#242140; --line:#2E2A4D;
  --fg:#F4F2FF; --muted:#A7A2C6; --faint:#6E6993;
  --brand:#FF6B6B; --brand-2:#FFA14D; --brand-fg:#1A0E0E;
  --hero-a:#E8457A; --hero-b:#F2763A; --hero-c:#F5B434;
  --t-call:#6E9BFF; --t-app:#B98BFF; --t-live:#FF6B93; --t-spon:#FFC247; --t-pers:#3EDBA6; --t-dead:#96A3C0;
  --ok:#3EDBA6; --shadow:0 2px 6px rgba(0,0,0,.3),0 12px 32px rgba(0,0,0,.35); --tint:20%; color-scheme:dark}

*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{background:var(--bg);color:var(--fg);font:15px/1.45 var(--f-body);-webkit-font-smoothing:antialiased}
button,input,select,textarea{font:inherit;color:inherit}
button{cursor:pointer;border:0;background:none;padding:0}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2.5px solid var(--brand);outline-offset:2px;border-radius:10px}
h1,h2,h3{font-family:var(--f-display);margin:0;letter-spacing:-.015em;text-wrap:balance}
.mono{font-family:var(--f-mono);font-variant-numeric:tabular-nums}

.app{max-width:460px;margin:0 auto;padding-inline:16px;padding-block:14px 120px;display:flex;flex-direction:column;gap:18px;min-height:100vh}
.screen{display:flex;flex-direction:column;gap:18px}

/* header */
.head{display:flex;align-items:center;gap:12px}
.head .hi{flex:1;min-width:0}
.head .hi small{display:block;color:var(--muted);font-size:13px;font-weight:600;text-transform:capitalize}
.head h1{font-size:27px;font-weight:800;line-height:1.15}
.avatar{width:44px;height:44px;border-radius:15px;background:linear-gradient(135deg,var(--hero-a),var(--hero-c));color:#fff;font-family:var(--f-display);font-weight:800;font-size:19px;display:grid;place-items:center;position:relative;flex:none}
.avatar i{position:absolute;right:-2px;bottom:-2px;width:13px;height:13px;border-radius:50%;border:2.5px solid var(--bg);background:var(--faint)}
.avatar i.ok{background:var(--ok)} .avatar i.warn{background:var(--t-spon)}

/* hero */
.hero{border-radius:26px;padding:20px;color:#fff;background:linear-gradient(135deg,var(--hero-a) 0%,var(--hero-b) 60%,var(--hero-c) 130%);position:relative;overflow:hidden;box-shadow:0 18px 40px -12px color-mix(in srgb,var(--hero-a) 60%,transparent)}
.hero::before{content:"";position:absolute;width:220px;height:220px;border-radius:50%;right:-70px;top:-90px;background:rgba(255,255,255,.14)}
.hero::after{content:"";position:absolute;width:140px;height:140px;border-radius:50%;right:40px;bottom:-80px;background:rgba(255,255,255,.1)}
.hero>*{position:relative;z-index:1}
.hero .kick{display:inline-flex;align-items:center;gap:7px;background:rgba(255,255,255,.2);padding:5px 10px 5px 8px;border-radius:999px;font-size:11.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.hero .kick i{width:8px;height:8px;border-radius:50%;background:#fff}
.hero.live .kick i{animation:pulse 1.2s ease-in-out infinite}
@keyframes pulse{50%{opacity:.3;transform:scale(.7)}}
.hero h2{font-size:26px;font-weight:800;line-height:1.12;margin-top:12px;overflow-wrap:anywhere}
.hero .when{font-size:14px;opacity:.9;margin-top:4px;font-weight:600}
.hero .count{display:flex;gap:8px;margin-top:16px}
.hero .unit{background:rgba(255,255,255,.2);border-radius:14px;padding:8px 0 6px;min-width:58px;text-align:center}
.hero .unit b{display:block;font-family:var(--f-mono);font-size:24px;line-height:1}
.hero .unit span{font-size:10px;font-weight:700;letter-spacing:.08em;opacity:.85;text-transform:uppercase}
.hero .acts{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}
.hbtn{background:#fff;color:#2A1420;font-weight:700;font-size:13.5px;padding:9px 14px;border-radius:12px;display:inline-flex;align-items:center;gap:6px}
.hbtn.alt{background:rgba(255,255,255,.2);color:#fff}
.hbtn svg{width:16px;height:16px}
.hero.empty h2{font-size:22px}
.hero.empty p{margin:6px 0 0;opacity:.9;font-size:14px}

/* day strip */
.strip-wrap{margin-inline:-16px}
.strip{display:flex;gap:8px;overflow-x:auto;padding:2px 16px 6px;scroll-snap-type:x mandatory;scrollbar-width:none}
.strip::-webkit-scrollbar{display:none}
.dayb{flex:none;width:54px;padding:10px 0 9px;border-radius:18px;background:var(--surface);display:flex;flex-direction:column;align-items:center;gap:2px;scroll-snap-align:start;box-shadow:0 1px 2px rgba(40,30,90,.05)}
.dayb small{font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
.dayb b{font-family:var(--f-display);font-size:20px;font-weight:700}
.dayb .dots{display:flex;gap:3px;height:6px;margin-top:2px}
.dayb .dots i{width:5px;height:5px;border-radius:50%;background:var(--c)}
.dayb.today b{color:var(--brand)}
.dayb[aria-pressed="true"]{background:var(--fg);color:var(--bg)}
.dayb[aria-pressed="true"] small{color:color-mix(in srgb,var(--bg) 70%,transparent)}
.dayb[aria-pressed="true"].today b{color:var(--brand-2)}

/* section head */
.sh{display:flex;align-items:baseline;justify-content:space-between;gap:10px}
.sh h3{font-size:19px;font-weight:700;text-transform:capitalize}
.sh span{font-size:13px;color:var(--muted);font-weight:600}
.link{color:var(--brand);font-weight:700;font-size:13.5px}

/* event cards */
.list{display:flex;flex-direction:column;gap:10px}
.card{display:grid;grid-template-columns:56px 1fr auto;gap:12px;align-items:center;background:var(--surface);border-radius:20px;padding:12px 12px 12px 12px;box-shadow:var(--shadow);text-align:left;width:100%;position:relative}
.card .tm{align-self:stretch;border-radius:14px;background:color-mix(in srgb,var(--c) var(--tint),transparent);color:var(--c);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:6px 0}
.card .tm b{font-family:var(--f-mono);font-size:15px;line-height:1.1}
.card .tm small{font-size:10.5px;font-weight:700;opacity:.85}
.card .tm svg{width:22px;height:22px}
.card .bd{min-width:0}
.card .ty{font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--c)}
.card .tt{font-weight:700;font-size:15.5px;line-height:1.25;overflow-wrap:anywhere;margin-top:1px}
.card .mt{font-size:12.5px;color:var(--muted);margin-top:3px;display:flex;gap:8px;flex-wrap:wrap}
.card .mt span{display:inline-flex;align-items:center;gap:4px;overflow-wrap:anywhere}
.card .mt svg{width:13px;height:13px;flex:none}
.tick{width:30px;height:30px;border-radius:10px;border:2px solid var(--line);display:grid;place-items:center;color:#fff;flex:none}
.tick svg{width:16px;height:16px}
.tick[aria-pressed="true"]{background:var(--ok);border-color:var(--ok)}
.card.done{opacity:.55}.card.done .tt{text-decoration:line-through}
.card.now{box-shadow:0 0 0 2px var(--c),var(--shadow)}
.card.now::after{content:"ORA";position:absolute;top:-8px;left:14px;background:var(--c);color:#fff;font-size:9.5px;font-weight:800;letter-spacing:.1em;padding:2px 7px;border-radius:6px}
.empty{background:var(--surface);border-radius:20px;padding:26px 20px;text-align:center;border:2px dashed var(--line)}
.empty .ill{font-size:34px;line-height:1}
.empty b{display:block;font-family:var(--f-display);font-size:18px;margin-top:8px}
.empty p{margin:4px 0 14px;color:var(--muted);font-size:14px}
.pill{background:var(--fg);color:var(--bg);font-weight:700;font-size:14px;padding:10px 16px;border-radius:14px;display:inline-flex;gap:6px;align-items:center}

/* month */
.mhead{display:flex;align-items:center;gap:8px}
.mhead h3{flex:1;font-size:22px;text-transform:capitalize}
.round{width:40px;height:40px;border-radius:14px;background:var(--surface);display:grid;place-items:center;box-shadow:0 1px 2px rgba(40,30,90,.06)}
.round svg{width:18px;height:18px}
.mgrid{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:4px;background:var(--surface);border-radius:22px;padding:12px 8px;box-shadow:var(--shadow)}
.mgrid .wd{font-size:11px;font-weight:700;color:var(--faint);text-align:center;padding-bottom:6px}
.mc{aspect-ratio:1/1.05;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-weight:600;font-size:15px;max-width:100%}
.mc.out{color:var(--faint)}
.mc.today{color:var(--brand);font-weight:800}
.mc[aria-pressed="true"]{background:var(--fg);color:var(--bg)}
.mc .dots{display:flex;gap:2px;height:5px}
.mc .dots i{width:5px;height:5px;border-radius:50%;background:var(--c)}

/* legend / filter */
.legend{display:flex;gap:6px;flex-wrap:wrap}
.lg{display:inline-flex;align-items:center;gap:6px;padding:6px 11px;border-radius:999px;font-size:12.5px;font-weight:700;background:color-mix(in srgb,var(--c) var(--tint),transparent);color:var(--c)}
.lg[aria-pressed="false"]{background:var(--surface);color:var(--faint)}
.lg i{width:7px;height:7px;border-radius:50%;background:currentColor}

/* search */
.search{display:flex;align-items:center;gap:10px;background:var(--surface);border-radius:16px;padding:0 14px;box-shadow:var(--shadow)}
.search svg{width:18px;height:18px;color:var(--muted);flex:none}
.search input{flex:1;min-width:0;border:0;background:transparent;padding:14px 0;font-size:16px;outline:none}

/* stats */
.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.st{background:var(--surface);border-radius:18px;padding:12px;box-shadow:0 1px 2px rgba(40,30,90,.05)}
.st b{display:block;font-family:var(--f-display);font-size:24px;font-weight:800;line-height:1.1;color:var(--c,var(--fg))}
.st span{font-size:12px;color:var(--muted);font-weight:600}

/* tab bar */
.tabbar{position:fixed;left:0;right:0;bottom:0;z-index:20;padding:0 12px calc(10px + env(safe-area-inset-bottom,0px));pointer-events:none}
.tabbar nav{pointer-events:auto;max-width:436px;margin:0 auto;background:color-mix(in srgb,var(--surface) 88%,transparent);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-radius:24px;box-shadow:0 10px 40px rgba(20,10,60,.18);display:grid;grid-template-columns:1fr 1fr 76px 1fr 1fr;align-items:center;height:68px;padding:0 6px}
.tab{display:flex;flex-direction:column;align-items:center;gap:3px;font-size:10.5px;font-weight:700;color:var(--faint);padding:6px 0}
.tab svg{width:23px;height:23px}
.tab[aria-selected="true"]{color:var(--fg)}
.tab[aria-selected="true"] svg{color:var(--brand)}
.plus{width:58px;height:58px;margin:-26px auto 0;border-radius:20px;background:linear-gradient(135deg,var(--hero-a),var(--hero-b));color:#fff;display:grid;place-items:center;box-shadow:0 10px 24px -6px color-mix(in srgb,var(--hero-a) 70%,transparent)}
.plus svg{width:28px;height:28px}

/* sheets */
.scrim{position:fixed;inset:0;z-index:40;background:rgba(14,10,30,.5);display:flex;align-items:flex-end;justify-content:center;animation:fade .18s ease}
.sheet{width:100%;max-width:460px;background:var(--bg);border-radius:28px 28px 0 0;padding:10px 16px calc(18px + env(safe-area-inset-bottom,0px));max-height:94vh;overflow-y:auto;display:flex;flex-direction:column;gap:16px;animation:up .26s cubic-bezier(.2,.9,.3,1)}
@keyframes up{from{transform:translateY(40px);opacity:.4}}
@keyframes fade{from{opacity:0}}
.grab{width:40px;height:5px;border-radius:3px;background:var(--line);margin:0 auto 2px}
.sheet h3{font-size:22px}
.sheet .row{display:flex;align-items:center;justify-content:space-between;gap:10px}
.x{width:36px;height:36px;border-radius:12px;background:var(--surface);display:grid;place-items:center}
.x svg{width:18px;height:18px}
.magic{background:var(--surface);border-radius:18px;padding:4px 4px 4px 14px;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow)}
.magic svg{width:18px;height:18px;color:var(--brand);flex:none}
.magic input{flex:1;min-width:0;border:0;background:transparent;padding:12px 0;font-size:16px;outline:none}
.magic-hint{font-size:12.5px;color:var(--muted);margin-top:-8px;padding-inline:4px}
.grp{display:flex;flex-direction:column;gap:8px}
.grp>label,.grp>.lb{font-size:12.5px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.inp{background:var(--surface);border:2px solid transparent;border-radius:14px;padding:12px 14px;font-size:16px;width:100%;min-width:0;outline:none}
.inp:focus{border-color:color-mix(in srgb,var(--brand) 50%,transparent)}
textarea.inp{min-height:76px;resize:vertical}
.big{font-family:var(--f-display);font-size:20px;font-weight:600}
.chips{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
.chips::-webkit-scrollbar{display:none}
.chips.wrap{flex-wrap:wrap}
.ch{flex:none;padding:9px 14px;border-radius:12px;background:var(--surface);font-weight:700;font-size:14px;display:inline-flex;align-items:center;gap:7px;border:2px solid transparent}
.ch[aria-pressed="true"]{border-color:var(--c,var(--fg));background:color-mix(in srgb,var(--c,var(--fg)) var(--tint),var(--surface));color:var(--c,var(--fg))}
.ch i{width:9px;height:9px;border-radius:50%;background:var(--c)}
.ch input{border:0;background:transparent;padding:0;width:auto;font-weight:700;outline:none}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.cta{background:linear-gradient(135deg,var(--hero-a),var(--hero-b));color:#fff;font-weight:800;font-size:16px;padding:16px;border-radius:18px;width:100%;box-shadow:0 10px 24px -8px color-mix(in srgb,var(--hero-a) 70%,transparent)}
.ghost{background:var(--surface);font-weight:700;padding:14px;border-radius:16px;width:100%}
.danger{color:var(--t-live)}
.confirm{background:color-mix(in srgb,var(--t-live) 12%,var(--surface));border-radius:16px;padding:12px 14px;display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-weight:600}
.confirm .sp{flex:1;min-width:140px}
.sbtn{padding:8px 12px;border-radius:10px;font-weight:700;font-size:13.5px;background:var(--surface)}
.sbtn.red{background:var(--t-live);color:#fff}

/* detail */
.dt-head{border-radius:22px;padding:18px;background:color-mix(in srgb,var(--c) var(--tint),var(--surface))}
.dt-head .ty{color:var(--c);font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
.dt-head h2{font-size:24px;margin-top:6px;overflow-wrap:anywhere}
.dt-head .when{margin-top:6px;font-weight:600;color:var(--muted);text-transform:capitalize}
.info{background:var(--surface);border-radius:18px;display:flex;flex-direction:column}
.info div{display:flex;gap:12px;padding:13px 14px;align-items:flex-start}
.info div+div{border-top:1px solid var(--line)}
.info svg{width:18px;height:18px;color:var(--muted);flex:none;margin-top:1px}
.info span{min-width:0;overflow-wrap:anywhere;white-space:pre-wrap}
.grid-acts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.act{background:var(--surface);border-radius:16px;padding:14px;font-weight:700;font-size:14px;display:flex;align-items:center;gap:8px;justify-content:center}
.act svg{width:18px;height:18px}
.act.main{background:var(--fg);color:var(--bg)}

/* alert + toast */
.alert{position:fixed;left:50%;transform:translateX(-50%);top:calc(10px + env(safe-area-inset-top,0px));z-index:60;width:min(440px,calc(100% - 24px));background:var(--surface);border-radius:22px;padding:14px;display:flex;gap:12px;align-items:center;box-shadow:0 20px 50px rgba(20,10,60,.3);animation:drop .3s cubic-bezier(.2,.9,.3,1)}
@keyframes drop{from{transform:translate(-50%,-30px);opacity:0}}
.alert .ic{width:44px;height:44px;border-radius:14px;background:linear-gradient(135deg,var(--hero-a),var(--hero-b));color:#fff;display:grid;place-items:center;flex:none}
.alert .ic svg{width:22px;height:22px}
.alert .g{flex:1;min-width:0}
.alert b{display:block;font-family:var(--f-display);font-size:16px;overflow-wrap:anywhere}
.alert small{color:var(--muted);font-size:13px}
.alert .bs{display:flex;flex-direction:column;gap:6px}
.toast{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(96px + env(safe-area-inset-bottom,0px));z-index:70;background:var(--fg);color:var(--bg);font-weight:700;font-size:14px;padding:11px 16px;border-radius:14px;max-width:calc(100% - 32px);box-shadow:var(--shadow)}
.tip{font-size:12.5px;color:var(--muted);text-align:center;padding:4px 10px}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>
</head>
<body>

<div class="app">
  <!-- AGENDA -->
  <section class="screen" id="s-agenda">
    <header class="head">
      <div class="hi"><small id="today"></small><h1 id="hello">Ciao Francesco</h1></div>
      <div class="avatar" title="Stato salvataggio">F<i id="syncDot"></i></div>
    </header>
    <div class="hero" id="hero"></div>
    <div class="strip-wrap"><div class="strip" id="strip"></div></div>
    <div class="sh"><h3 id="dayTitle">Oggi</h3><span id="dayCount"></span></div>
    <div class="list" id="dayList"></div>
  </section>

  <!-- MESE -->
  <section class="screen" id="s-mese" hidden>
    <div class="mhead">
      <button class="round" id="mPrev" aria-label="Mese precedente"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg></button>
      <h3 id="mTitle"></h3>
      <button class="round" id="mNext" aria-label="Mese successivo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg></button>
    </div>
    <div class="mgrid" id="mGrid"></div>
    <div class="legend" id="legend"></div>
    <div class="sh"><h3 id="mDayTitle"></h3><span id="mDayCount"></span></div>
    <div class="list" id="mDayList"></div>
  </section>

  <!-- PROSSIMI -->
  <section class="screen" id="s-pross" hidden>
    <header class="head"><div class="hi"><small>Prossimi 30 giorni</small><h1>In arrivo</h1></div></header>
    <div class="stats" id="stats"></div>
    <div id="upList" class="screen" style="gap:14px"></div>
  </section>

  <!-- CERCA -->
  <section class="screen" id="s-cerca" hidden>
    <header class="head"><div class="hi"><small>Tutti i tuoi eventi</small><h1>Cerca</h1></div></header>
    <label class="search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg><input id="q" placeholder="Nome, luogo, nota…" aria-label="Cerca"></label>
    <div class="list" id="qList"></div>
    <div class="sh" style="margin-top:8px"><h3>Impostazioni</h3></div>
    <div class="set">
      <button id="notifBtn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 0112 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 003.4 0"/></svg><span class="g">Notifiche<small id="notifTxt">Attiva gli avvisi del telefono</small></span></button>
      <button id="expBtn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg><span class="g">Salva backup<small>Scarica tutti gli eventi in un file</small></span></button>
      <label for="impFile" style="cursor:pointer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21V9M7 14l5-5 5 5M5 3h14"/></svg><span class="g">Carica backup<small>Ripristina o sposta gli eventi su un altro telefono</small></span><input type="file" id="impFile" accept=".json,application/json" hidden></label>
    </div>
  </section>

  <p class="tip" id="tip">Tocca un evento per aprirlo. Per la notifica sicura anche ad app chiusa usa il tasto Google Calendar.</p>
</div>

<div class="tabbar"><nav role="tablist">
  <button class="tab" role="tab" data-s="agenda" aria-selected="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 12h10M4 18h7"/></svg>Agenda</button>
  <button class="tab" role="tab" data-s="mese" aria-selected="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M8 3v4M16 3v4M3.5 10h17"/></svg>Mese</button>
  <button class="plus" id="plus" aria-label="Nuovo evento"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg></button>
  <button class="tab" role="tab" data-s="pross" aria-selected="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>Prossimi</button>
  <button class="tab" role="tab" data-s="cerca" aria-selected="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>Cerca</button>
</nav></div>

<!-- EDIT SHEET -->
<div class="scrim" id="editScrim" hidden>
  <form class="sheet" id="editForm" autocomplete="off">
    <div class="grab"></div>
    <div class="row"><h3 id="editTitle">Nuovo evento</h3><button type="button" class="x" id="editClose" aria-label="Chiudi"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>

    <div id="magicBox" class="grp">
      <label class="magic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 4.6L18.5 9l-4.7 1.5L12 15l-1.8-4.5L5.5 9l4.7-1.4z"/><path d="M19 15l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/></svg><input id="magic" placeholder="Scrivi: call con Marco domani alle 15"></label>
      <div class="magic-hint">Scrivi in una frase e compilo io i campi qui sotto.</div>
    </div>

    <div class="grp"><label for="f-title">Cosa</label><input class="inp big" id="f-title" required placeholder="Titolo dell'evento"></div>
    <div class="grp"><span class="lb">Tipo</span><div class="chips wrap" id="f-types"></div></div>
    <div class="grp"><span class="lb">Quando</span>
      <div class="chips" id="f-days"></div>
      <input class="inp" type="date" id="f-date" required aria-label="Data">
    </div>
    <div class="grp"><span class="lb">Ora</span>
      <div class="chips" id="f-times"></div>
      <div class="two"><input class="inp" type="time" id="f-time" aria-label="Ora di inizio">
        <select class="inp" id="f-dur" aria-label="Durata"><option value="15">Dura 15 min</option><option value="30">Dura 30 min</option><option value="45">Dura 45 min</option><option value="60">Dura 1 ora</option><option value="90">Dura 1 h 30</option><option value="120">Dura 2 ore</option><option value="180">Dura 3 ore</option><option value="240">Dura 4 ore</option></select></div>
    </div>
    <div class="grp"><span class="lb">Avvisami</span><div class="chips" id="f-rems"></div></div>
    <div class="grp"><span class="lb">Ripeti</span><div class="chips" id="f-reps"></div></div>
    <div class="grp"><label for="f-where">Dove o link</label><input class="inp" id="f-where" placeholder="Indirizzo, link Meet, Discord…"></div>
    <div class="grp"><label for="f-note">Note</label><textarea class="inp" id="f-note" placeholder="Cosa preparare, numeri, chi c'è…"></textarea></div>
    <button type="submit" class="cta" id="saveBtn">Salva evento</button>
  </form>
</div>

<!-- DETAIL SHEET -->
<div class="scrim" id="detScrim" hidden>
  <div class="sheet" id="det"></div>
</div>

<div class="alert" id="alert" hidden role="alert">
  <div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 0112 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 003.4 0"/></svg></div>
  <div class="g"><b id="alertTitle"></b><small id="alertMeta"></small></div>
  <div class="bs"><button class="sbtn" id="alertSnooze">+5 min</button><button class="sbtn red" id="alertOk">Ok</button></div>
</div>
<div class="toast" id="toast" hidden></div>

<script>
(() => {
const TYPES={
  call:{n:"Call",c:"--t-call",i:'<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2"/>'},
  app:{n:"Appuntamento",c:"--t-app",i:'<rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M8 3v4M16 3v4M3.5 10h17"/>'},
  live:{n:"Live",c:"--t-live",i:'<rect x="3" y="6" width="13" height="12" rx="3"/><path d="M16 10l5-3v10l-5-3"/>'},
  spon:{n:"Sponsor",c:"--t-spon",i:'<path d="M12 3l2.6 5.4 5.9.8-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.8z"/>'},
  pers:{n:"Personale",c:"--t-pers",i:'<path d="M6.5 6.5l11 11M4 9l5-5M15 20l5-5M3 11l2 2M11 3l2 2M19 11l2 2M11 19l2 2"/>'},
  dead:{n:"Scadenza",c:"--t-dead",i:'<path d="M12 3v2M5 21h14M7 21V9a5 5 0 0110 0v12"/><path d="M12 12v3"/>'}
};
const svgT=k=>`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${(TYPES[k]||TYPES.call).i}</svg>`;
const I={
  ok:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-10"/></svg>',
  pin:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6-7-11a7 7 0 0114 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
  link:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M10 14a5 5 0 007 0l3-3a5 5 0 00-7-7l-1 1"/><path d="M14 10a5 5 0 00-7 0l-3 3a5 5 0 007 7l1-1"/></svg>',
  bell:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 0112 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 003.4 0"/></svg>',
  rep:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 2l3 3-3 3"/><path d="M4 11V9a4 4 0 014-4h12M7 22l-3-3 3-3"/><path d="M20 13v2a4 4 0 01-4 4H4"/></svg>',
  clock:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>',
  note:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 5h14M5 10h14M5 15h9M5 20h6"/></svg>',
  cal:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M8 3v4M16 3v4M3.5 10h17M12 13v5M9.5 15.5h5"/></svg>',
  edit:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 013 3L7 19l-4 1 1-4z"/></svg>',
  trash:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/></svg>',
  x:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
  sun:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
};
const MESI=["gennaio","febbraio","marzo","aprile","maggio","giugno","luglio","agosto","settembre","ottobre","novembre","dicembre"];
const GIORNI=["domenica","lunedì","martedì","mercoledì","giovedì","venerdì","sabato"];
const $=s=>document.querySelector(s);
const pad=n=>String(n).padStart(2,"0");
const ymd=d=>`${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
const parseYmd=s=>{const [y,m,d]=s.split("-").map(Number);return new Date(y,m-1,d)};
const addDays=(d,n)=>{const x=new Date(d.getFullYear(),d.getMonth(),d.getDate());x.setDate(x.getDate()+n);return x};
const today0=()=>{const n=new Date();return new Date(n.getFullYear(),n.getMonth(),n.getDate())};
const startOfWeek=d=>addDays(d,-((d.getDay()+6)%7));
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const cv=k=>`var(${(TYPES[k]||TYPES.call).c})`;
const hm=d=>`${pad(d.getHours())}:${pad(d.getMinutes())}`;
const isUrl=s=>/^https?:\/\//i.test(s||"");

let events=[], col=null, mode="local";
let screen="agenda", sel=today0(), mSel=today0(), mCursor=today0(), filter=new Set(Object.keys(TYPES));
let editing=null, detailRef=null;
const fired=new Set(), snoozed={};

/* ---------- storage ---------- */
function loadLocal(){try{return JSON.parse(localStorage.getItem("palinsesto.events")||"[]")}catch(e){return []}}
function saveLocal(){try{localStorage.setItem("palinsesto.events",JSON.stringify(events))}catch(e){}}
const setSync=c=>{$("#syncDot").className=c||""};
async function initStore(){
  events=loadLocal(); render();
  setSync("ok");
}
async function persist(ev){
  if(mode==="db"){ const {id,...b}=ev; b.done=b.done||{};
    try{ await col.doc(id).set(JSON.parse(JSON.stringify(b))); }catch(e){ toast(e&&e.code==="quota_exceeded"?"Spazio pieno: elimina qualche evento vecchio":"Non salvato, controlla la connessione e riprova"); throw e; } }
  else { const i=events.findIndex(e=>e.id===ev.id); if(i>=0)events[i]=ev; else events.push(ev); saveLocal(); render(); }
}
async function removeEv(id){
  if(mode==="db"){ try{await col.doc(id).delete()}catch(e){toast("Non eliminato, riprova");throw e} }
  else { events=events.filter(e=>e.id!==id); saveLocal(); render(); }
}
const newId=()=>"e"+Date.now().toString(36)+Math.random().toString(36).slice(2,7);

/* ---------- occurrences ---------- */
function occursOn(ev,day){
  const st=parseYmd(ev.date); if(day<st) return false;
  switch(ev.rep||"none"){
    case "none":return ymd(day)===ev.date; case "daily":return true;
    case "weekdays":{const w=day.getDay();return w>0&&w<6}
    case "weekly":return day.getDay()===st.getDay(); case "monthly":return day.getDate()===st.getDate();
  } return false;
}
function occ(ev,day){ const [h,m]=(ev.time||"00:00").split(":").map(Number);
  const s=new Date(day.getFullYear(),day.getMonth(),day.getDate(),h,m); const e=new Date(s.getTime()+(Number(ev.dur)||60)*6e4); const key=ymd(day);
  return {ev,key,start:s,end:e,allDay:!ev.time,done:!!(ev.done&&ev.done[key])}; }
function dayItems(day,all){ return events.filter(ev=>(all||filter.has(ev.type||"call"))&&occursOn(ev,day)).map(ev=>occ(ev,day)).sort((a,b)=>(b.allDay-a.allDay)||a.start-b.start); }
function range(from,days,all){ const out=[]; for(let i=0;i<days;i++){const d=addDays(from,i); for(const ev of events){ if(!all&&!filter.has(ev.type||"call"))continue; if(occursOn(ev,d)) out.push(occ(ev,d)); }} return out.sort((a,b)=>a.start-b.start); }

/* ---------- text ---------- */
function relDay(d){const diff=Math.round((new Date(d.getFullYear(),d.getMonth(),d.getDate())-today0())/864e5);
  if(diff===0)return"oggi";if(diff===1)return"domani";if(diff===-1)return"ieri";if(diff>1&&diff<7)return GIORNI[d.getDay()];return `${GIORNI[d.getDay()]} ${d.getDate()} ${MESI[d.getMonth()]}`}
const durTxt=m=>{m=Number(m)||60;if(m<60)return m+" min";const h=Math.floor(m/60),r=m%60;return h+" h"+(r?" "+r:"")};
const remTxt=r=>{r=Number(r);if(!r)return"all'ora esatta";if(r>=1440)return"il giorno prima";if(r>=60)return(r/60)+(r===60?" ora":" ore")+" prima";return r+" min prima"};
const REPS={none:"Mai",daily:"Ogni giorno",weekdays:"Lun–Ven",weekly:"Ogni settimana",monthly:"Ogni mese"};

function gcalUrl(o){ const ev=o.ev;
  const f=d=>`${d.getFullYear()}${pad(d.getMonth()+1)}${pad(d.getDate())}`+(o.allDay?"":`T${pad(d.getHours())}${pad(d.getMinutes())}00`);
  const p=new URLSearchParams({action:"TEMPLATE",text:ev.title,dates:o.allDay?`${f(o.start)}/${f(addDays(o.start,1))}`:`${f(o.start)}/${f(o.end)}`,ctz:"Europe/Rome",
    details:[ev.note,`Promemoria: ${remTxt(ev.rem)}`].filter(Boolean).join("\n\n"),location:ev.where||""});
  const rr={daily:"RRULE:FREQ=DAILY",weekdays:"RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR",weekly:"RRULE:FREQ=WEEKLY",monthly:"RRULE:FREQ=MONTHLY"}[ev.rep]; if(rr)p.set("recur",rr);
  return "https://calendar.google.com/calendar/render?"+p.toString(); }

/* ---------- render pieces ---------- */
function card(o,showDay){
  const ev=o.ev, t=TYPES[ev.type]||TYPES.call, now=new Date(), isNow=!o.allDay&&o.start<=now&&now<o.end&&!o.done;
  const where=ev.where?`<span>${isUrl(ev.where)?I.link+" Link":I.pin+esc(ev.where)}</span>`:"";
  return `<div class="card ${o.done?"done":""} ${isNow?"now":""}" style="--c:${cv(ev.type)}" role="button" tabindex="0" data-open="${ev.id}" data-k="${o.key}">
    <div class="tm">${o.allDay?svgT(ev.type)+'<small>giorno</small>':`<b>${hm(o.start)}</b><small>${durTxt(ev.dur)}</small>`}</div>
    <div class="bd"><div class="ty">${t.n}${showDay?` · ${relDay(o.start)}`:""}</div><div class="tt">${esc(ev.title)}</div>
      ${(where||ev.rep&&ev.rep!=="none")?`<div class="mt">${where}${ev.rep&&ev.rep!=="none"?`<span>${I.rep}${REPS[ev.rep]}</span>`:""}</div>`:""}</div>
    <button class="tick" aria-pressed="${o.done}" aria-label="Segna come fatto" data-done="${ev.id}" data-k="${o.key}">${o.done?I.ok:""}</button></div>`;
}
function emptyBox(d){ return `<div class="empty"><div class="ill">🗓️</div><b>Giornata libera</b><p>Nessun impegno ${relDay(d)==="oggi"?"per oggi":relDay(d).startsWith(GIORNI[d.getDay()])?"per "+relDay(d):relDay(d)}.</p><button class="pill" data-new="${ymd(d)}">＋ Aggiungi qualcosa</button></div>`; }

function renderHero(){
  const now=new Date(); const list=range(addDays(now,-1),60,true).filter(o=>!o.done&&!o.allDay&&o.end>now);
  const cur=list.find(o=>o.start<=now), nx=cur||list[0], el=$("#hero");
  if(!nx){ el.className="hero empty"; el.innerHTML=`<span class="kick"><i></i>Tutto libero</span><h2>Nessun impegno in arrivo</h2><p>Tocca il + in basso per aggiungere call, live o appuntamenti.</p>`; return; }
  const t=TYPES[nx.ev.type]||TYPES.call, target=cur?nx.end:nx.start;
  el.className="hero"+(cur?" live":"");
  el.innerHTML=`<span class="kick"><i></i>${cur?"In corso":"Prossimo"} · ${t.n}</span>
    <h2>${esc(nx.ev.title)}</h2><div class="when">${relDay(nx.start).replace(/^./,c=>c.toUpperCase())} · ${hm(nx.start)} – ${hm(nx.end)}</div>
    <div class="count" id="count" data-t="${target.getTime()}" data-lbl="${cur?"fine":"inizio"}">${countHtml(target-now)}</div>
    <div class="acts">
      ${isUrl(nx.ev.where)?`<a class="hbtn" href="${esc(nx.ev.where)}" target="_blank" rel="noopener">${I.link}Entra</a>`:""}
      <button class="hbtn ${isUrl(nx.ev.where)?"alt":""}" data-open="${nx.ev.id}" data-k="${nx.key}">Dettagli</button>
      <a class="hbtn alt" href="${esc(gcalUrl(nx))}" target="_blank" rel="noopener">${I.cal}Calendar</a>
    </div>`;
}
function countHtml(ms){ ms=Math.max(0,ms); const s=Math.floor(ms/1000), d=Math.floor(s/86400), h=Math.floor(s%86400/3600), m=Math.floor(s%3600/60), x=s%60;
  const u=[]; if(d)u.push([d,"giorni"]); u.push([pad(h),"ore"],[pad(m),"min"]); if(!d)u.push([pad(x),"sec"]);
  return u.map(([v,l])=>`<div class="unit"><b>${v}</b><span>${l}</span></div>`).join(""); }

function renderStrip(){
  const t0=today0(), days=[...Array(21)].map((_,i)=>addDays(t0,i-2));
  if(!days.some(d=>ymd(d)===ymd(sel))) days.push(sel);
  $("#strip").innerHTML=days.map(d=>{ const it=dayItems(d,true); const k=ymd(d);
    return `<button class="dayb ${k===ymd(t0)?"today":""}" aria-pressed="${k===ymd(sel)}" data-sel="${k}"><small>${GIORNI[d.getDay()].slice(0,3)}</small><b>${d.getDate()}</b><span class="dots">${it.slice(0,3).map(o=>`<i style="--c:${cv(o.ev.type)}"></i>`).join("")}</span></button>`}).join("");
}
function renderDay(){
  const it=dayItems(sel,true); const r=relDay(sel);
  $("#dayTitle").textContent=r==="oggi"?"Oggi":r==="domani"?"Domani":r;
  $("#dayCount").textContent=it.length?`${it.length} ${it.length===1?"impegno":"impegni"}`:"";
  $("#dayList").innerHTML=it.length?it.map(o=>card(o)).join(""):emptyBox(sel);
}
function renderMonth(){
  const c=mCursor; $("#mTitle").textContent=`${MESI[c.getMonth()]} ${c.getFullYear()}`;
  const first=new Date(c.getFullYear(),c.getMonth(),1), s=startOfWeek(first), tk=ymd(today0());
  let h=["L","M","M","G","V","S","D"].map(g=>`<div class="wd">${g}</div>`).join("");
  for(let i=0;i<42;i++){ const d=addDays(s,i); if(i>=35&&d.getMonth()!==c.getMonth())break; const it=dayItems(d);
    h+=`<button class="mc ${d.getMonth()!==c.getMonth()?"out":""} ${ymd(d)===tk?"today":""}" aria-pressed="${ymd(d)===ymd(mSel)}" data-msel="${ymd(d)}" aria-label="${d.getDate()} ${MESI[d.getMonth()]}, ${it.length} eventi">${d.getDate()}<span class="dots">${it.slice(0,3).map(o=>`<i style="--c:${cv(o.ev.type)}"></i>`).join("")}</span></button>`; }
  $("#mGrid").innerHTML=h;
  $("#legend").innerHTML=Object.entries(TYPES).map(([k,t])=>`<button class="lg" style="--c:${cv(k)}" aria-pressed="${filter.has(k)}" data-f="${k}"><i></i>${t.n}</button>`).join("");
  const it=dayItems(mSel); const r=relDay(mSel);
  $("#mDayTitle").textContent=r.replace(/^./,x=>x.toUpperCase()); $("#mDayCount").textContent=it.length?`${it.length} ${it.length===1?"impegno":"impegni"}`:"";
  $("#mDayList").innerHTML=it.length?it.map(o=>card(o)).join(""):emptyBox(mSel);
}
function renderUp(){
  const now=new Date(), list=range(today0(),30,true).filter(o=>o.end>now||o.allDay&&o.key===ymd(now));
  const wk=range(startOfWeek(today0()),7,true);
  $("#stats").innerHTML=[["Questa settimana",wk.length,""],["Call",wk.filter(o=>o.ev.type==="call").length,cv("call")],["Live",wk.filter(o=>o.ev.type==="live").length,cv("live")]]
    .map(([l,n,c])=>`<div class="st" style="${c?"--c:"+c:""}"><b>${n}</b><span>${l}</span></div>`).join("");
  if(!list.length){ $("#upList").innerHTML=`<div class="empty"><div class="ill">✨</div><b>Niente nei prossimi 30 giorni</b><p>Aggiungi la prima call o la prossima live.</p><button class="pill" data-new="${ymd(today0())}">＋ Nuovo evento</button></div>`; return; }
  let out="", last=""; for(const o of list){ if(o.key!==last){ if(last) out+="</div></div>"; const r=relDay(o.start);
      out+=`<div class="screen" style="gap:10px"><div class="sh"><h3>${r}</h3><span>${o.start.getDate()} ${MESI[o.start.getMonth()].slice(0,3)}</span></div><div class="list">`; last=o.key; }
    out+=card(o); }
  $("#upList").innerHTML=out+"</div></div>";
}
function renderSearch(){
  const q=$("#q").value.trim().toLowerCase(), el=$("#qList");
  const list=[...events].filter(e=>!q||[e.title,e.where,e.note,(TYPES[e.type]||{}).n].join(" ").toLowerCase().includes(q)).sort((a,b)=>(b.date+(b.time||"")).localeCompare(a.date+(a.time||"")));
  if(!events.length){ el.innerHTML=`<div class="empty"><div class="ill">🔎</div><b>Ancora nessun evento</b><p>Quando ne aggiungi, li trovi tutti qui.</p></div>`; return; }
  if(!list.length){ el.innerHTML=`<div class="empty"><b>Nessun risultato</b><p>Prova con un'altra parola.</p></div>`; return; }
  el.innerHTML=list.slice(0,80).map(e=>{ const d=parseYmd(e.date); let nd=d; if(e.rep&&e.rep!=="none"){ for(let i=0;i<40;i++){ const x=addDays(today0(),i); if(occursOn(e,x)){nd=x;break} } } return card(occ(e,nd),true)}).join("");
}
function render(){
  const n=new Date(); $("#today").textContent=`${GIORNI[n.getDay()]} ${n.getDate()} ${MESI[n.getMonth()]}`;
  const h=n.getHours(); $("#hello").textContent=(h<5?"Buonanotte":h<13?"Buongiorno":h<18?"Buon pomeriggio":"Buonasera")+", Francesco";
  if(screen==="agenda"){renderHero();renderStrip();renderDay();}
  if(screen==="mese")renderMonth(); if(screen==="pross")renderUp(); if(screen==="cerca")renderSearch();
}
function go(s){ screen=s; ["agenda","mese","pross","cerca"].forEach(x=>$("#s-"+x).hidden=x!==s);
  document.querySelectorAll(".tab").forEach(b=>b.setAttribute("aria-selected",String(b.dataset.s===s)));
  try{localStorage.setItem("palinsesto.screen",s)}catch(e){} render(); window.scrollTo({top:0}); }

/* ---------- parser (italiano) ---------- */
function parseQuick(txt){
  let s=" "+txt.trim()+" "; const now=new Date(); let date=null,time=null,type=null,rep="none",m;
  const low=()=>s.toLowerCase(); const take=re=>{const r=low().match(re); if(r) s=s.slice(0,r.index)+" "+s.slice(r.index+r[0].length); return r;};
  const G="lunedì|martedì|mercoledì|giovedì|venerdì|sabato|domenica|lunedi|martedi|mercoledi|giovedi|venerdi";
  const gIdx=w=>GIORNI.findIndex(g=>g.replace("ì","i")===w.replace("ì","i"));
  if(take(/\s(ogni giorno|tutti i giorni)\s/)) rep="daily";
  else if(take(/\s(dal lunedì al venerdì|dal lunedi al venerdi|lun-ven)\s/)) rep="weekdays";
  else if(m=take(new RegExp("\\sogni ("+G+")\\s"))){rep="weekly"; date=addDays(now,((gIdx(m[1])-now.getDay())+7)%7);}
  else if(take(/\sogni settimana\s/)) rep="weekly"; else if(take(/\sogni mese\s/)) rep="monthly";
  if(take(/\s(stasera|stanotte)\s/)){date=date||now; time="21:00";}
  if(take(/\sdopodomani\s/)) date=addDays(now,2); else if(take(/\sdomani\s/)) date=addDays(now,1); else if(take(/\soggi\s/)) date=now;
  if(!date&&(m=take(/\s(?:tra|fra) (\d+) (giorni|giorno|settimane|settimana)\s/))) date=addDays(now,+m[1]*(m[2].startsWith("sett")?7:1));
  if(!date&&(m=take(new RegExp("\\s(?:il |(?:"+G+") )?(\\d{1,2})[\\/.-](\\d{1,2})(?:[\\/.-](\\d{2,4}))?\\s")))){ const y=m[3]?+(m[3].length===2?"20"+m[3]:m[3]):now.getFullYear(); date=new Date(y,m[2]-1,+m[1]); if(!m[3]&&date<addDays(now,-1)) date.setFullYear(y+1); }
  if(!date&&(m=take(new RegExp("\\s(?:il |(?:"+G+") )?(\\d{1,2}) ("+MESI.join("|")+")\\s")))){ date=new Date(now.getFullYear(),MESI.indexOf(m[2]),+m[1]); if(date<addDays(now,-1)) date.setFullYear(now.getFullYear()+1); }
  if(!date&&(m=take(new RegExp("\\s(?:(?:"+G+") prossimo|(?:"+G+"))\\s")))){ const w=gIdx(m[0].trim().split(" ")[0]); let d=((w-now.getDay())+7)%7; if(d===0)d=7; date=addDays(now,d); }
  if(m=take(/\s(?:alle|ore|h|dalle|verso le)\s?(\d{1,2})(?:[:.](\d{2}))?\s/)) time=`${pad(Math.min(23,+m[1]))}:${m[2]||"00"}`;
  else if(m=take(/\s(\d{1,2})[:.](\d{2})\s/)) time=`${pad(+m[1])}:${m[2]}`;
  if(take(/\s(?:mattina|stamattina|di mattina)\s/)) time=time||"10:00";
  if(take(/\s(?:pomeriggio|oggi pomeriggio|nel pomeriggio)\s/)) time=time||"15:00";
  if(take(/\s(?:sera|di sera)\s/)) time=time||"21:00";
  const l=low();
  if(/\b(call|chiamata|telefonata|meet|zoom|videochiamata|riunione|meeting)\b/.test(l)) type="call";
  else if(/\b(live|stream|diretta|twitch|podcast|registrazione|video|reel|tiktok|shooting)\b/.test(l)) type="live";
  else if(/\b(sponsor|pokerstars|brand|contratto|fattura|agenzia|collab)\b/.test(l)) type="spon";
  else if(/\b(scadenza|entro|pagare|pagamento|deadline|consegna|bolletta)\b/.test(l)) type="dead";
  else if(/\b(palestra|allenamento|pierluigi|cena|pranzo|aperitivo|partita|compleanno|calcetto|amici|stadio)\b/.test(l)) type="pers";
  else if(/\b(dentista|medico|visita|appuntamento|barbiere|parrucchiere|banca|commercialista|notaio|meccanico)\b/.test(l)) type="app";
  let title=s.replace(/\s+/g," ").trim().replace(/^(?:il|la|lo|alle)\s/i,"").replace(/\s(?:il|la|alle|di|a|per)$/i,"");
  title=title.charAt(0).toUpperCase()+title.slice(1);
  return {title:title||txt.trim(),date:date?ymd(date):null,time,type,rep};
}

/* ---------- edit sheet ---------- */
let F={};
function chipRow(el,opts,val,key,extra){ $(el).innerHTML=opts.map(([v,l,c])=>`<button type="button" class="ch" ${c?`style="--c:${c}"`:""} aria-pressed="${String(v)===String(val)}" data-${key}="${v}">${c?"<i></i>":""}${l}</button>`).join("")+(extra||""); }
function drawForm(){
  chipRow("#f-types",Object.entries(TYPES).map(([k,t])=>[k,t.n,cv(k)]),F.type,"ty");
  const t0=today0(); const dk=[[ymd(t0),"Oggi"],[ymd(addDays(t0,1)),"Domani"],[ymd(addDays(t0,2)),GIORNI[addDays(t0,2).getDay()].replace(/^./,c=>c.toUpperCase())],[ymd(addDays(t0,3)),GIORNI[addDays(t0,3).getDay()].replace(/^./,c=>c.toUpperCase())],[ymd(addDays(t0,7)),"Tra 1 settimana"]];
  chipRow("#f-days",dk,F.date,"dy");
  chipRow("#f-times",[["","Tutto il giorno"],["09:00","9:00"],["11:00","11:00"],["15:00","15:00"],["18:00","18:00"],["21:00","21:00"]],F.time||"","tm");
  chipRow("#f-rems",[[0,"All'ora"],[5,"5 min"],[15,"15 min"],[30,"30 min"],[60,"1 ora"],[1440,"Giorno prima"]],F.rem,"rm");
  chipRow("#f-reps",Object.entries(REPS),F.rep,"rp");
  $("#f-date").value=F.date; $("#f-time").value=F.time||""; $("#f-dur").value=String(F.dur||60);
}
function openEdit(ev,preset){
  editing=ev||null; F={title:"",type:"call",date:ymd(screen==="mese"?mSel:sel),time:"",dur:60,rem:15,rep:"none",where:"",note:"",...(ev||{}),...(preset||{})};
  $("#editTitle").textContent=ev?"Modifica evento":"Nuovo evento"; $("#saveBtn").textContent=ev?"Salva modifiche":"Salva evento";
  $("#magicBox").hidden=!!ev; $("#magic").value="";
  $("#f-title").value=F.title; $("#f-where").value=F.where||""; $("#f-note").value=F.note||"";
  drawForm(); closeDetail(); $("#editScrim").hidden=false;
  setTimeout(()=>(ev?$("#f-title"):$("#magic")).focus(),60);
}
const closeEdit=()=>{ $("#editScrim").hidden=true; editing=null; };
$("#magic").addEventListener("input",()=>{ const v=$("#magic").value.trim(); if(!v)return; const p=parseQuick(v);
  F.title=p.title; $("#f-title").value=p.title; if(p.date)F.date=p.date; if(p.time!==null)F.time=p.time; if(p.type)F.type=p.type; F.rep=p.rep; drawForm(); });
$("#magic").addEventListener("keydown",e=>{ if(e.key==="Enter"){ e.preventDefault(); $("#editForm").requestSubmit(); }});
$("#editForm").addEventListener("click",e=>{ const b=e.target.closest(".ch"); if(!b)return; const d=b.dataset;
  if(d.ty)F.type=d.ty; if(d.dy)F.date=d.dy; if(d.tm!==undefined)F.time=d.tm; if(d.rm!==undefined)F.rem=+d.rm; if(d.rp)F.rep=d.rp; drawForm(); });
$("#f-date").addEventListener("change",e=>{F.date=e.target.value;drawForm()});
$("#f-time").addEventListener("change",e=>{F.time=e.target.value;drawForm()});
$("#f-dur").addEventListener("change",e=>F.dur=+e.target.value);
$("#editClose").addEventListener("click",closeEdit);
$("#editScrim").addEventListener("click",e=>{ if(e.target.id==="editScrim") closeEdit(); });
$("#editForm").addEventListener("submit",async e=>{ e.preventDefault();
  const title=$("#f-title").value.trim(); if(!title){ $("#f-title").focus(); toast("Scrivi un titolo"); return; } if(!F.date){toast("Scegli il giorno");return}
  const ev={...(editing||{id:newId(),done:{},created:Date.now()}),title,type:F.type,date:F.date,time:F.time||"",dur:+F.dur||60,rem:+F.rem||0,rep:F.rep||"none",where:$("#f-where").value.trim(),note:$("#f-note").value.trim()};
  const wasEdit=!!editing;
  try{ await persist(ev); closeEdit(); sel=parseYmd(ev.date); mSel=sel; mCursor=sel; render();
    toast(wasEdit?"Modifiche salvate":`Aggiunto ${relDay(sel)}${ev.time?" alle "+ev.time:""}`); }catch(_){} });

/* ---------- detail sheet ---------- */
function openDetail(id,key){ detailRef={id,key}; refreshDetail(); $("#detScrim").hidden=false; }
function closeDetail(){ $("#detScrim").hidden=true; detailRef=null; }
function refreshDetail(){
  const ev=events.find(e=>e.id===detailRef.id); if(!ev){closeDetail();return}
  const o=occ(ev,parseYmd(detailRef.key)), t=TYPES[ev.type]||TYPES.call;
  $("#det").innerHTML=`<div class="grab"></div>
   <div class="row"><span></span><button class="x" data-close aria-label="Chiudi">${I.x}</button></div>
   <div class="dt-head" style="--c:${cv(ev.type)}"><div class="ty">${t.n}${o.done?" · fatto ✓":""}</div><h2>${esc(ev.title)}</h2>
     <div class="when">${relDay(o.start)} · ${o.allDay?"tutto il giorno":hm(o.start)+" – "+hm(o.end)}</div></div>
   <div class="info">
     ${o.allDay?"":`<div>${I.clock}<span>Dura ${durTxt(ev.dur)}</span></div>`}
     <div>${I.bell}<span>Avviso ${remTxt(ev.rem)}</span></div>
     ${ev.rep&&ev.rep!=="none"?`<div>${I.rep}<span>Si ripete: ${REPS[ev.rep].toLowerCase()}</span></div>`:""}
     ${ev.where?`<div>${isUrl(ev.where)?I.link:I.pin}<span>${isUrl(ev.where)?`<a href="${esc(ev.where)}" target="_blank" rel="noopener" style="color:var(--brand);font-weight:700">${esc(ev.where)}</a>`:esc(ev.where)}</span></div>`:""}
     ${ev.note?`<div>${I.note}<span>${esc(ev.note)}</span></div>`:""}
   </div>
   <div class="grid-acts">
     <button class="act main" data-done="${ev.id}" data-k="${o.key}">${I.ok}${o.done?"Non fatto":"Fatto"}</button>
     <a class="act" href="${esc(gcalUrl(o))}" target="_blank" rel="noopener">${I.cal}Google Calendar</a>
     <button class="act" data-edit="${ev.id}">${I.edit}Modifica</button>
     <button class="act danger" data-del="${ev.id}">${I.trash}Elimina</button>
   </div>
   <div id="delBox"></div>`;
}
$("#detScrim").addEventListener("click",async e=>{
  if(e.target.id==="detScrim"||e.target.closest("[data-close]")) return closeDetail();
  const ed=e.target.closest("[data-edit]"); if(ed){ openEdit(events.find(x=>x.id===ed.dataset.edit)); return; }
  const dl=e.target.closest("[data-del]"); if(dl){ const ev=events.find(x=>x.id===dl.dataset.del);
    $("#delBox").innerHTML=`<div class="confirm"><span class="sp">Eliminare${ev.rep&&ev.rep!=="none"?" tutte le ripetizioni di":""} “${esc(ev.title)}”?</span><button class="sbtn" data-cancel>Annulla</button><button class="sbtn red" data-yes="${ev.id}">Elimina</button></div>`; return; }
  if(e.target.closest("[data-cancel]")){ $("#delBox").innerHTML=""; return; }
  const y=e.target.closest("[data-yes]"); if(y){ try{ await removeEv(y.dataset.yes); closeDetail(); toast("Evento eliminato"); }catch(_){} }
});

/* ---------- global clicks ---------- */
async function toggleDone(id,k){ const ev=events.find(x=>x.id===id); if(!ev)return; const done={...(ev.done||{})};
  if(done[k]) delete done[k]; else { done[k]=true; if(navigator.vibrate) try{navigator.vibrate(15)}catch(e){} }
  try{ await persist({...ev,done}); if(done[k]) toast("Fatto ✓"); }catch(_){} }
document.addEventListener("click",e=>{
  const d=e.target.closest("[data-done]"); if(d){ e.stopPropagation(); toggleDone(d.dataset.done,d.dataset.k); return; }
  const n=e.target.closest("[data-new]"); if(n){ openEdit(null,{date:n.dataset.new}); return; }
  const o=e.target.closest("[data-open]"); if(o){ openDetail(o.dataset.open,o.dataset.k); return; }
  const s=e.target.closest("[data-sel]"); if(s){ sel=parseYmd(s.dataset.sel); renderStrip(); renderDay(); return; }
  const ms=e.target.closest("[data-msel]"); if(ms){ mSel=parseYmd(ms.dataset.msel); if(mSel.getMonth()!==mCursor.getMonth()) mCursor=mSel; renderMonth(); return; }
  const f=e.target.closest("[data-f]"); if(f){ const k=f.dataset.f; if(filter.has(k)&&filter.size===Object.keys(TYPES).length) filter=new Set([k]); else if(filter.has(k)){filter.delete(k); if(!filter.size) filter=new Set(Object.keys(TYPES));} else filter.add(k); renderMonth(); return; }
});
document.addEventListener("keydown",e=>{ if(e.key==="Enter"&&e.target.matches(".card")) e.target.click();
  if(e.key==="Escape"){ if(!$("#editScrim").hidden) closeEdit(); else if(!$("#detScrim").hidden) closeDetail(); } });
document.querySelectorAll(".tab").forEach(b=>b.addEventListener("click",()=>go(b.dataset.s)));
$("#plus").addEventListener("click",()=>openEdit());
$("#mPrev").addEventListener("click",()=>{ mCursor=new Date(mCursor.getFullYear(),mCursor.getMonth()-1,1); renderMonth(); });
$("#mNext").addEventListener("click",()=>{ mCursor=new Date(mCursor.getFullYear(),mCursor.getMonth()+1,1); renderMonth(); });
$("#q").addEventListener("input",renderSearch);

/* ---------- reminders ---------- */
let actx=null; document.addEventListener("pointerdown",()=>{ if(!actx){ try{actx=new (window.AudioContext||window.webkitAudioContext)()}catch(e){} } },{once:true});
function chime(){ if(!actx)return; try{ const t=actx.currentTime; [[0,784],[.16,988],[.32,1319]].forEach(([o,f])=>{const os=actx.createOscillator(),g=actx.createGain();os.type="sine";os.frequency.value=f;g.gain.setValueAtTime(.0001,t+o);g.gain.exponentialRampToValueAtTime(.22,t+o+.02);g.gain.exponentialRampToValueAtTime(.0001,t+o+.35);os.connect(g).connect(actx.destination);os.start(t+o);os.stop(t+o+.36)}) }catch(e){} }
let alertK=null;
function checkReminders(){
  const now=Date.now();
  for(const o of range(addDays(new Date(),-1),3,true)){ if(o.done||o.allDay) continue;
    const k=o.ev.id+"@"+o.key, at=snoozed[k]||(o.start.getTime()-(+o.ev.rem||0)*6e4);
    if(now>=at&&now<o.start.getTime()+10*6e4&&!fired.has(k+":"+at)){ fired.add(k+":"+at); alertK=k;
      const mins=Math.round((o.start-now)/6e4);
      $("#alertTitle").textContent=o.ev.title; $("#alertMeta").textContent=mins>0?`${(TYPES[o.ev.type]||TYPES.call).n} tra ${mins>=60?Math.round(mins/60)+" h":mins+" min"} · alle ${hm(o.start)}`:`È iniziato alle ${hm(o.start)}`;
      $("#alert").hidden=false; chime(); if(navigator.vibrate) try{navigator.vibrate([200,100,200])}catch(e){} document.title="🔔 "+o.ev.title; sysNotify(o,mins); break; } }
}
const resetTitle=()=>document.title="Palinsesto";
$("#alertOk").addEventListener("click",()=>{ $("#alert").hidden=true; resetTitle(); });
$("#alertSnooze").addEventListener("click",()=>{ if(alertK) snoozed[alertK]=Date.now()+5*6e4; $("#alert").hidden=true; resetTitle(); toast("Te lo ricordo tra 5 minuti"); });

let tt; function toast(m){ const t=$("#toast"); t.textContent=m; t.hidden=false; clearTimeout(tt); tt=setTimeout(()=>t.hidden=true,2400); }

/* ---------- tick ---------- */
let lastMin=-1;
function tick(){ const n=new Date(), c=$("#count");
  if(c&&screen==="agenda"){ const t=+c.dataset.t; if(t-n<=0) renderHero(); else c.innerHTML=countHtml(t-n); }
  if(n.getMinutes()!==lastMin){ lastMin=n.getMinutes(); render(); }
  checkReminders(); }

/* ---------- notifiche di sistema ---------- */
let swReg=null;
if("serviceWorker" in navigator){ navigator.serviceWorker.register("sw.js").then(r=>swReg=r).catch(()=>{}); }
function notifState(){ const t=$("#notifTxt"); if(!("Notification" in window)){t.textContent="Su questo browser: aggiungi l'app alla Home";return}
  t.textContent={granted:"Attive ✓ (con l'app aperta o in background)",denied:"Bloccate: riattivale dalle impostazioni del telefono",default:"Tocca per attivare gli avvisi"}[Notification.permission]; }
$("#notifBtn").addEventListener("click",async()=>{ if(!("Notification" in window)){toast("Aggiungi prima l'app alla schermata Home");return}
  const p=await Notification.requestPermission(); notifState(); if(p==="granted"){ sysNotify(null); } });
function sysNotify(o,mins){ if(!("Notification" in window)||Notification.permission!=="granted")return;
  const title=o?o.ev.title:"Notifiche attive"; const opts={body:o?(mins>0?`Tra ${mins} min · alle ${hm(o.start)}`:`Iniziato alle ${hm(o.start)}`):"Ti avviserò prima dei tuoi impegni.",icon:"icon-192.png",badge:"icon-192.png",tag:o?o.ev.id+o.key:"test",vibrate:[200,100,200]};
  try{ if(swReg&&swReg.showNotification) swReg.showNotification(title,opts); else new Notification(title,opts); }catch(e){} }
notifState();
/* ---------- backup ---------- */
$("#expBtn").addEventListener("click",()=>{ const blob=new Blob([JSON.stringify({app:"palinsesto",v:1,exported:new Date().toISOString(),events},null,2)],{type:"application/json"});
  const a=document.createElement("a"); a.href=URL.createObjectURL(blob); a.download=`palinsesto-backup-${ymd(new Date())}.json`; document.body.appendChild(a); a.click(); a.remove(); toast("Backup salvato"); });
$("#impFile").addEventListener("change",async e=>{ const f=e.target.files[0]; if(!f)return;
  try{ const d=JSON.parse(await f.text()); const list=Array.isArray(d)?d:d.events; if(!Array.isArray(list)) throw 0;
    const byId=new Map(events.map(x=>[x.id,x])); list.forEach(x=>{ if(x&&x.id&&x.title&&x.date) byId.set(x.id,x); });
    events=[...byId.values()]; saveLocal(); render(); toast(`Caricati ${list.length} eventi`); }catch(_){ toast("File non valido: usa un backup del Palinsesto"); }
  e.target.value=""; });
try{ const s=localStorage.getItem("palinsesto.screen"); if(["agenda","mese","pross","cerca"].includes(s)) screen=s; }catch(e){}
go(screen); initStore(); tick(); setInterval(tick,1000);
})();
</script>

</body>
</html>

{
  "name": "Palinsesto",
  "short_name": "Palinsesto",
  "description": "La tua agenda: call, live, appuntamenti e promemoria.",
  "lang": "it",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "orientation": "portrait",
  "background_color": "#F3F1FA",
  "theme_color": "#FF6A5C",
  "icons": [
    {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
    {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}
  ]
}

const CACHE="palinsesto-v1";
const SHELL=["./","index.html","manifest.webmanifest","icon-192.png","icon-512.png","apple-touch-icon.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(SHELL)));self.skipWaiting();});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==CACHE).map(x=>caches.delete(x)))));self.clients.claim();});
self.addEventListener("fetch",e=>{
  if(e.request.method!=="GET")return;
  e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(CACHE).then(c=>c.put(e.request,cp)).catch(()=>{});return r;}).catch(()=>caches.match(e.request).then(r=>r||caches.match("index.html"))));
});
self.addEventListener("notificationclick",e=>{e.notification.close();e.waitUntil(self.clients.matchAll({type:"window"}).then(cs=>{for(const c of cs){if("focus" in c)return c.focus();}return self.clients.openWindow("./");}));});
