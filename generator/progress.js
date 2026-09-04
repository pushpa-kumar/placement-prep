import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const SUPABASE_URL = "https://sfvyqwwrmojcaapvoidh.supabase.co";
const SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNmdnlxd3dybW9qY2FhcHZvaWRoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODc4OTU5MDcsImV4cCI6MjEwMzQ3MTkwN30.SUZCiwyh7R949efP9vyDphxQfdB9U6pid9M3I64AZv8";

const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

const state = { user: null, done: new Map() };

function isDone(id) {
  return state.done.has(id);
}

function doneCount(type) {
  if (!type) return state.done.size;
  let n = 0;
  state.done.forEach((t) => { if (t === type) n++; });
  return n;
}

function getUser() {
  return state.user;
}

async function loadProgress() {
  const { data, error } = await supabase.from("progress").select("item_id, item_type");
  if (!error) state.done = new Map((data || []).map((r) => [r.item_id, r.item_type]));
  renderAll();
}

async function toggle(id, type) {
  if (!state.user) {
    await signIn();
    return;
  }
  if (state.done.has(id)) {
    state.done.delete(id);
    renderAll();
    await supabase.from("progress").delete().eq("item_id", id);
  } else {
    state.done.set(id, type);
    renderAll();
    await supabase.from("progress").upsert({ user_id: state.user.id, item_id: id, item_type: type });
  }
}

async function signIn() {
  await supabase.auth.signInWithOAuth({ provider: "github", options: { redirectTo: window.location.href } });
}

async function signOut() {
  await supabase.auth.signOut();
}

function renderAuthSlot() {
  const slot = document.getElementById("authSlot");
  if (!slot) return;
  if (state.user) {
    const label = state.user.user_metadata?.user_name || state.user.email || "Signed in";
    slot.innerHTML = `<span class="auth-user">${label}</span><button type="button" class="auth-btn" id="authSignOut">Sign out</button>`;
    document.getElementById("authSignOut")?.addEventListener("click", signOut);
  } else {
    slot.innerHTML = `<button type="button" class="auth-btn" id="authSignIn">Sign in with GitHub</button>`;
    document.getElementById("authSignIn")?.addEventListener("click", signIn);
  }
}

function renderCheckboxes() {
  document.querySelectorAll(".done-checkbox[data-item-id]").forEach((el) => {
    const done = isDone(el.dataset.itemId);
    el.classList.toggle("done", done);
    el.setAttribute("aria-pressed", done ? "true" : "false");
    el.textContent = done ? "✓ Done" : "Mark done";
  });
}

function renderSummaries() {
  document.querySelectorAll("[data-progress-summary]").forEach((el) => {
    const type = el.dataset.progressSummary;
    const total = el.dataset.progressTotal ? parseInt(el.dataset.progressTotal, 10) : null;
    const n = doneCount(type);
    el.textContent = total !== null ? `${n} / ${total}` : String(n);
  });
  document.querySelectorAll("[data-progress-signin-hint]").forEach((el) => {
    el.style.display = state.user ? "none" : "";
  });
  document.querySelectorAll("[data-progress-signed-in]").forEach((el) => {
    el.style.display = state.user ? "" : "none";
  });
}

// Per-page completion bar. Scope comes from the DOM rather than a build-time
// count, so pages that render their cards client-side stay correct as long as
// they call refresh() afterwards.
function renderPageStatus() {
  const bars = document.querySelectorAll(".page-status");
  if (!bars.length) return;
  const boxes = document.querySelectorAll(".done-checkbox[data-item-id]");
  const total = boxes.length;
  let n = 0;
  boxes.forEach((el) => { if (isDone(el.dataset.itemId)) n++; });
  const pct = total ? Math.round((n / total) * 100) : 0;
  bars.forEach((bar) => {
    bar.style.display = total ? "" : "none";
    bar.setAttribute("aria-valuenow", String(pct));
    bar.querySelectorAll('[data-page-progress="count"]').forEach((e) => { e.textContent = `${n} / ${total}`; });
    bar.querySelectorAll('[data-page-progress="pct"]').forEach((e) => { e.textContent = `${pct}%`; });
    bar.querySelectorAll('[data-page-progress="fill"]').forEach((e) => { e.style.width = `${pct}%`; });
  });
}

function renderAll() {
  renderAuthSlot();
  renderCheckboxes();
  renderSummaries();
  renderPageStatus();
}

document.addEventListener("click", (ev) => {
  const cb = ev.target.closest(".done-checkbox[data-item-id]");
  if (cb) toggle(cb.dataset.itemId, cb.dataset.itemType || "item");
});

async function init() {
  const { data: { session } } = await supabase.auth.getSession();
  state.user = session ? session.user : null;
  renderAll();
  if (state.user) await loadProgress();

  supabase.auth.onAuthStateChange(async (_event, session) => {
    state.user = session ? session.user : null;
    if (state.user) {
      await loadProgress();
    } else {
      state.done.clear();
      renderAll();
    }
  });
}

window.PlacementProgress = { isDone, doneCount, getUser, toggle, signIn, signOut, refresh: renderAll };

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
