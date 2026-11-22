// Menú en celular
const btn = document.querySelector('.menu'), nav = document.getElementById('nav');
btn?.addEventListener('click', () => { nav.classList.toggle('abierto'); btn.setAttribute('aria-expanded', nav.classList.contains('abierto')); });
const toast = m => { const t = document.querySelector('.toast'); t.textContent = m; t.classList.add('ver'); setTimeout(() => t.classList.remove('ver'), 1500); };

// Botón "Copiar" en cada bloque de código
document.querySelectorAll('main pre').forEach(pre => {
  const b = document.createElement('button'); b.className = 'copiar'; b.type = 'button'; b.textContent = 'Copiar';
  b.addEventListener('click', async () => {
    const texto = pre.querySelector('code')?.innerText ?? pre.innerText;
    try { await navigator.clipboard.writeText(texto.replace(/\n$/, '')); b.textContent = '¡Copiado!'; b.classList.add('ok'); toast('Prompt copiado: pégalo en Claude Code'); }
    catch { b.textContent = 'Selecciona y copia'; }
    setTimeout(() => { b.textContent = 'Copiar'; b.classList.remove('ok'); }, 1800);
  });
  pre.appendChild(b);
});

// Casillas que se recuerdan (localStorage) y progreso por ruta
const casillas = document.querySelectorAll('input[data-clave]');
casillas.forEach(c => {
  c.checked = localStorage.getItem('taller:' + c.dataset.clave) === '1';
  c.addEventListener('change', () => { localStorage.setItem('taller:' + c.dataset.clave, c.checked ? '1' : '0'); progreso(); });
});
function progreso() {
  document.querySelectorAll('.nivel').forEach(n => n.classList.toggle('hecho-ok', !!n.querySelector('input:checked')));
  const p = document.querySelector('.progreso'); if (!p) return;
  const cs = document.querySelectorAll('.nivel input[data-clave]'), hechos = [...cs].filter(c => c.checked).length;
  p.querySelector('span').style.width = (100 * hechos / cs.length) + '%';
  p.querySelector('p').textContent = hechos === cs.length ? '🎉 ¡Ruta completa! Prepárate para la galería.' : `Llevas ${hechos} de ${cs.length} niveles.`;
}
progreso();

// Agenda y reloj de la sesión (sobrevive a recargar la página)
const agenda = document.getElementById('agenda'), DUR = 60 * 60 * 1000, K = 'taller:reloj';
const est = () => JSON.parse(localStorage.getItem(K) || '{"inicio":null,"pausa":null}');
const guarda = e => localStorage.setItem(K, JSON.stringify(e));
const mmss = ms => { const s = Math.max(0, Math.round(ms / 1000)); return String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'); };
function tick() {
  const e = est(); const trans = e.inicio ? ((e.pausa ?? Date.now()) - e.inicio) : 0; const min = trans / 60000;
  agenda?.querySelectorAll('li').forEach(li => {
    const a = +li.dataset.ini, b = +li.dataset.fin;
    li.classList.toggle('actual', !!e.inicio && min >= a && min < b); li.classList.toggle('pasada', !!e.inicio && min >= b);
  });
  if (!document.getElementById('reloj')) return;
  const li = [...agenda.querySelectorAll('li')].find(l => min >= +l.dataset.ini && min < +l.dataset.fin);
  document.getElementById('fase-nombre').textContent = !e.inicio ? 'Lista para empezar' : (li ? li.querySelector('b').textContent : 'Sesión terminada');
  document.getElementById('fase-desc').textContent = li && e.inicio ? li.querySelector('p').textContent : '';
  document.getElementById('fase-resta').textContent = li && e.inicio ? mmss(+li.dataset.fin * 60000 - trans) : '--:--';
  document.getElementById('total').textContent = mmss(Math.min(trans, DUR));
  document.getElementById('barra-total').style.width = Math.min(100, 100 * trans / DUR) + '%';
  document.getElementById('pausar').textContent = e.pausa ? '▶ Reanudar' : '⏸ Pausar';
}
document.getElementById('iniciar')?.addEventListener('click', () => { const e = est(); if (!e.inicio) guarda({ inicio: Date.now(), pausa: null }); tick(); });
document.getElementById('pausar')?.addEventListener('click', () => { const e = est(); if (!e.inicio) return;
  if (e.pausa) guarda({ inicio: e.inicio + (Date.now() - e.pausa), pausa: null }); else guarda({ inicio: e.inicio, pausa: Date.now() }); tick(); });
document.getElementById('reiniciar')?.addEventListener('click', () => { guarda({ inicio: null, pausa: null }); tick(); });
document.getElementById('pantalla')?.addEventListener('click', () => document.getElementById('reloj').requestFullscreen?.());
tick(); setInterval(tick, 1000);
