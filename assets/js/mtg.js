// Card previews and viewer, deck page tabs and filters, and the deck gallery filter.
(() => {
  if (window.mtgReady) return;
  window.mtgReady = true;
  // Turns off the CSS-only tab fallback in custom.css
  document.documentElement.classList.add('mtg-js');

  const store = {
    get: (k) => { try { return localStorage.getItem(k); } catch { return null; } },
    set: (k, v) => { try { localStorage.setItem(k, v); } catch {} },
  };

  // Full-size viewer: tap any card reference
  if (document.querySelector('.mtg-ref')) {
    const viewer = document.createElement('dialog');
    viewer.className = 'mtg-viewer not-prose';
    viewer.setAttribute('aria-label', 'Card viewer');
    viewer.innerHTML = `<img alt="">
      <div class="mtg-viewer-actions">
        <button type="button" data-action="flip" hidden>Flip</button>
        <a target="_blank" rel="noopener">Scryfall</a>
        <button type="button" data-action="close">Close</button>
      </div>`;
    document.body.append(viewer);
    const img = viewer.querySelector('img');
    const flip = viewer.querySelector('[data-action="flip"]');
    const link = viewer.querySelector('a');
    let faces = [];
    let face = 0;
    const show = () => { img.src = faces[face]; };

    document.addEventListener('click', (e) => {
      const ref = e.target.closest('.mtg-ref');
      if (!ref || e.metaKey || e.ctrlKey || e.shiftKey) return;
      e.preventDefault();
      faces = [ref.dataset.img, ref.dataset.back].filter(Boolean);
      face = 0;
      img.alt = ref.dataset.name;
      link.href = ref.href;
      flip.hidden = faces.length < 2;
      show();
      viewer.showModal();
    });
    flip.addEventListener('click', () => { face = (face + 1) % faces.length; show(); });
    viewer.querySelector('[data-action="close"]').addEventListener('click', () => viewer.close());
    // Clicking the backdrop or the image closes the dialog
    viewer.addEventListener('click', (e) => { if (e.target === viewer || e.target === img) viewer.close(); });
  }

  // Hover preview, only where a real pointer can hover
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    const tip = document.createElement('img');
    tip.className = 'mtg-tip';
    tip.alt = '';
    document.body.append(tip);
    const place = (e) => {
      const w = 244, h = 340, pad = 16;
      let x = e.clientX + pad, y = e.clientY - h / 2;
      if (x + w > window.innerWidth) x = e.clientX - w - pad;
      y = Math.max(pad, Math.min(y, window.innerHeight - h - pad));
      tip.style.transform = `translate(${x}px, ${y}px)`;
    };
    document.addEventListener('mouseover', (e) => {
      const ref = e.target.closest('.mtg-ref:not(.mtg-thumb)');
      if (!ref) return;
      tip.src = ref.dataset.img;
      tip.classList.add('is-visible');
      place(e);
    });
    document.addEventListener('mousemove', (e) => { if (tip.classList.contains('is-visible')) place(e); });
    document.addEventListener('mouseout', (e) => {
      if (e.target.closest('.mtg-ref')) tip.classList.remove('is-visible');
    });
  }

  // Shared helper for List/Images and bracket toggles
  const bindToggle = (root, attr, key) => {
    const buttons = root.querySelectorAll(`.mtg-toggle [data-${attr}]`);
    const select = (value) => {
      if (![...buttons].some((b) => b.dataset[attr] === value)) return;
      root.dataset[attr] = value;
      buttons.forEach((b) => b.setAttribute('aria-pressed', b.dataset[attr] === value));
    };
    buttons.forEach((b) => b.addEventListener('click', () => { select(b.dataset[attr]); store.set(key, b.dataset[attr]); }));
    select(store.get(key));
  };

  // Decklist / Primer tabs, kept in the URL hash so links can target either
  document.querySelectorAll('.mtg-tabs').forEach((tabs) => {
    const links = [...tabs.querySelectorAll('[role="tab"]')];
    const panels = links.map((a) => document.getElementById(a.hash.slice(1)));
    const select = (id) => {
      links.forEach((a, i) => {
        const on = a.hash === `#${id}`;
        a.setAttribute('aria-selected', on);
        panels[i].hidden = !on;
      });
    };
    const fromHash = () => {
      // A hash may also point inside a panel, such as a primer heading
      const target = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
      const panel = target && target.closest('.mtg-panel');
      select(panel ? panel.id : tabs.dataset.default);
    };
    links.forEach((a) => a.addEventListener('click', (e) => {
      e.preventDefault();
      history.replaceState(null, '', a.hash);
      select(a.hash.slice(1));
      // When scrolled into the content, jump back to the top of the new panel
      const top = tabs.getBoundingClientRect().top + window.scrollY - parseFloat(getComputedStyle(tabs).top || 0);
      if (window.scrollY > top) window.scrollTo({ top });
    }));
    window.addEventListener('hashchange', fromHash);
    fromHash();
  });

  document.querySelectorAll('.mtg-deck').forEach((deck) => {
    bindToggle(deck, 'view', 'mtg-view');

    const copy = deck.querySelector('.mtg-copy');
    copy.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(copy.dataset.export);
        copy.textContent = 'Copied!';
      } catch {
        copy.textContent = 'Copy failed';
      }
      setTimeout(() => { copy.textContent = 'Copy list'; }, 1500);
    });

    // Filters: AND across groups, OR within a group. The panel and the pinned quick bar
    // both have color and mana value buttons; they share state by data-filter/data-value.
    const active = { role: new Set(), color: new Set(), mv: new Set() };
    let query = '';
    const search = deck.querySelector('.mtg-search');
    const chips = deck.querySelectorAll('[data-filter]');
    const shown = deck.querySelector('.mtg-shown');
    const shownShort = deck.querySelector('.mtg-shown-short');
    const clears = deck.querySelectorAll('.mtg-clear');
    const empty = deck.querySelector('.mtg-empty');
    const sections = deck.querySelectorAll('.mtg-section');

    const matches = ({ dataset: d }) =>
      (!active.role.size || d.roles.split(' ').some((r) => active.role.has(r))) &&
      (!active.mv.size || active.mv.has(d.mv)) &&
      (!active.color.size || [...active.color].some((c) => (c === 'C' ? d.ci === '' : d.ci.includes(c)))) &&
      (!query || d.search.includes(query));

    const apply = () => {
      const filtering = Boolean(query) || Object.values(active).some((s) => s.size);
      let visible = 0;
      let total = 0;
      sections.forEach((section) => {
        let count = 0;
        section.querySelectorAll('li').forEach((li) => {
          const ok = matches(li);
          const qty = Number(li.dataset.qty);
          li.hidden = !ok;
          if (ok) count += qty;
          if (!section.classList.contains('mtg-section-extra')) {
            total += qty;
            if (ok) visible += qty;
          }
        });
        section.hidden = count === 0;
        section.querySelector('.mtg-count').textContent = count;
      });
      shown.textContent = filtering ? `Showing ${visible} of ${total} cards` : `${total} cards`;
      shownShort.textContent = filtering ? `${visible} of ${total}` : '';
      clears.forEach((c) => { c.hidden = !filtering; });
      empty.hidden = [...sections].some((s) => !s.hidden);
    };

    const tabs = document.querySelector('.mtg-tabs');
    const quick = deck.querySelector('.mtg-quick');
    const stickyHeight = () => (tabs ? tabs.offsetHeight : 0) + quick.offsetHeight;
    const scrollToSection = (section) => window.scrollTo({
      top: section.getBoundingClientRect().top + window.scrollY - stickyHeight(),
    });

    chips.forEach((chip) => chip.addEventListener('click', () => {
      // From the pinned bar, keep the reader on the section they were looking at
      // (or the next one with matches) instead of wherever the shorter list lands
      const list = [...sections];
      const anchor = deck.classList.contains('is-compact') &&
        list.find((s) => !s.hidden && s.getBoundingClientRect().bottom > stickyHeight());
      const { filter, value } = chip.dataset;
      const set = active[filter];
      const on = !set.has(value);
      if (on) set.add(value); else set.delete(value);
      chips.forEach((c) => {
        if (c.dataset.filter === filter && c.dataset.value === value) c.setAttribute('aria-pressed', on);
      });
      apply();
      if (anchor) {
        const target = list.slice(list.indexOf(anchor)).find((s) => !s.hidden) || list.find((s) => !s.hidden);
        if (target) scrollToSection(target);
      }
    }));
    search.addEventListener('input', () => { query = search.value.trim().toLowerCase(); apply(); });
    clears.forEach((c) => c.addEventListener('click', () => {
      Object.values(active).forEach((s) => s.clear());
      chips.forEach((chip) => chip.setAttribute('aria-pressed', false));
      search.value = '';
      query = '';
      apply();
    }));

    // Pinned quick bar: shown once the panel's last filter row (the curve) has scrolled up
    // under the tabs. Watching the whole panel let the bar vanish when a filtered list was
    // short enough to bring the panel's bottom edge back into view. This checks position on
    // scroll rather than using an IntersectionObserver, which never fires if a fast fling or
    // jump carries the curve from below the screen to above it within one frame.
    const curve = deck.querySelector('.mtg-filters .mtg-curve');
    let pending = false;
    const update = () => {
      pending = false;
      const compact = curve.getBoundingClientRect().bottom < (tabs ? tabs.offsetHeight : 0);
      if (compact !== deck.classList.contains('is-compact')) {
        deck.classList.toggle('is-compact', compact);
        quick.inert = !compact;
      }
    };
    const schedule = () => {
      if (!pending) { pending = true; requestAnimationFrame(update); }
    };
    const measure = () => { deck.style.setProperty('--mtg-quick-h', `${quick.offsetHeight}px`); schedule(); };
    measure();
    window.addEventListener('scroll', schedule, { passive: true });
    window.addEventListener('resize', measure);

    apply();
  });

  // Deck gallery: bracket (remembered) AND archetype (from the URL hash, e.g. #combo)
  document.querySelectorAll('.mtg-gallery').forEach((gallery) => {
    const brackets = gallery.querySelectorAll('[data-bracket]:is(button)');
    const archetypes = gallery.querySelectorAll('[data-archetype]');
    const decks = gallery.querySelectorAll('li');
    const status = gallery.querySelector('.mtg-gallery-status');
    let bracket = store.get('mtg-bracket') || 'all';
    let archetype = '';

    const render = () => {
      if (![...brackets].some((b) => b.dataset.bracket === bracket)) bracket = 'all';
      brackets.forEach((b) => b.setAttribute('aria-pressed', b.dataset.bracket === bracket));
      archetypes.forEach((b) => b.setAttribute('aria-pressed', b.dataset.archetype === archetype));
      let shown = 0;
      decks.forEach((li) => {
        const ok = (bracket === 'all' || li.dataset.bracket === bracket) &&
          (!archetype || li.dataset.archetypes.split(' ').includes(archetype));
        li.hidden = !ok;
        if (ok) shown += 1;
      });
      status.textContent = shown === decks.length ? `${shown} decks` : `Showing ${shown} of ${decks.length} decks`;
    };

    brackets.forEach((b) => b.addEventListener('click', () => {
      bracket = b.dataset.bracket;
      store.set('mtg-bracket', bracket);
      render();
    }));
    // Tapping the selected archetype again clears it
    archetypes.forEach((b) => b.addEventListener('click', () => {
      archetype = archetype === b.dataset.archetype ? '' : b.dataset.archetype;
      history.replaceState(null, '', archetype ? `#${archetype}` : location.pathname);
      render();
    }));
    const fromHash = () => {
      const wanted = decodeURIComponent(location.hash.slice(1));
      archetype = [...archetypes].some((b) => b.dataset.archetype === wanted) ? wanted : '';
      render();
    };
    window.addEventListener('hashchange', fromHash);
    fromHash();
  });
})();
