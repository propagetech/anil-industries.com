/* Anil Industries: progressive enhancement only. Every feature below has a JS-off fallback
   in the HTML (the nav lists itself, tables are plain, the quote form is a mailto form). */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var EMAIL = "info@anil-industries.com";

  /* ---- Navigation: mobile toggle + products submenu ------------------------------------ */
  var header = $(".site-header");
  var toggle = $(".nav-toggle");
  if (header && toggle) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  var subToggle = $(".nav__sub-toggle");
  if (subToggle) {
    subToggle.addEventListener("click", function () {
      var open = subToggle.getAttribute("aria-expanded") !== "true";
      subToggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".nav__item--sub")) subToggle.setAttribute("aria-expanded", "false");
    });
  }
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    if (subToggle && subToggle.getAttribute("aria-expanded") === "true") {
      subToggle.setAttribute("aria-expanded", "false");
      subToggle.focus();
    } else if (header && header.classList.contains("is-open")) {
      header.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.focus();
    }
  });

  /* ---- Grade finder: filter rows of both tables, toggle standard columns --------------- */
  var norm = function (s) { return (s || "").toLowerCase().replace(/[\s.\-\/]+/g, ""); };
  var q = $("#grade-q");
  var tables = $$("table[data-filterable]");
  var count = $("#grade-count");
  if (q && tables.length) {
    var run = function () {
      var term = norm(q.value);
      var shown = 0;
      tables.forEach(function (t) {
        $$("tbody tr", t).forEach(function (tr) {
          var cells = $$("th, td", tr);
          var hit = false;
          cells.forEach(function (c) {
            var m = term && !c.classList.contains("eq__act") && norm(c.textContent).indexOf(term) !== -1;
            c.classList.toggle("is-hit", !!m);
            if (m) hit = true;
          });
          tr.hidden = !!term && !hit;
          if (!tr.hidden && t.id === "eq-table") shown++;
        });
      });
      if (!count) return;
      if (!term) { count.textContent = ""; return; }
      var chemRows = $$("#chem-table tbody tr:not([hidden])").length;
      count.textContent = shown + " equivalence row" + (shown === 1 ? "" : "s") + " and " + chemRows +
        " chemistry row" + (chemRows === 1 ? "" : "s") + " match “" + q.value.trim() + "”.";
    };
    q.addEventListener("input", run);
    var start = new URLSearchParams(location.search).get("q");
    if (start) { q.value = start; run(); }
  }
  $$("[data-col-toggle]").forEach(function (box) {
    box.addEventListener("change", function () {
      var key = box.getAttribute("data-col-toggle");
      $$('#eq-table [data-col="' + key + '"]').forEach(function (c) { c.classList.toggle("is-hidden", !box.checked); });
    });
  });

  /* ---- Units: mm / inch ---------------------------------------------------------------- */
  var unitKey = "ai-units";
  var setUnits = function (u) {
    $$(".dim").forEach(function (el) {
      var mm = parseFloat(el.getAttribute("data-mm"));
      var prec = parseInt(el.getAttribute("data-prec"), 10) || 3;
      el.textContent = u === "in" ? (mm / 25.4).toFixed(prec) : el.getAttribute("data-mm");
    });
    $$("[data-unit-label]").forEach(function (el) { el.textContent = u === "in" ? "in" : "mm"; });
    $$(".units__btn").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-unit") === u ? "true" : "false"); });
  };
  if ($(".units__btn")) {
    $$(".units__btn").forEach(function (b) {
      b.addEventListener("click", function () {
        var u = b.getAttribute("data-unit");
        setUnits(u);
        try { localStorage.setItem(unitKey, u); } catch (e) { /* storage unavailable: fine */ }
      });
    });
    try { if (localStorage.getItem(unitKey) === "in") setUnits("in"); } catch (e) { /* ignore */ }
  }

  /* ---- Size check ---------------------------------------------------------------------- */
  var RANGES = [
    { name: "hardened and tempered strip", t: [0.10, 4.00], w: [5, 500] },
    { name: "cold rolled strip", t: [0.20, 4.50], w: [12.5, 450] }
  ];
  $$("[data-sizecheck]").forEach(function (form) {
    var out = $("[data-sizecheck-out]", form);
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var t = parseFloat(form.t.value), w = parseFloat(form.w.value);
      out.classList.remove("is-in", "is-out");
      if (!(t > 0) || !(w > 0)) {
        out.textContent = "Enter both a thickness and a width in millimetres.";
        return;
      }
      var fits = RANGES.filter(function (r) { return t >= r.t[0] && t <= r.t[1] && w >= r.w[0] && w <= r.w[1]; })
        .map(function (r) { return r.name; });
      var size = t + " × " + w + " mm";
      if (fits.length) {
        out.classList.add("is-in");
        out.textContent = size + " is inside our range for " + fits.join(" and ") + ".";
      } else {
        out.classList.add("is-out");
        out.textContent = size + " is outside our standard ranges. Ask us anyway: send the size with your enquiry.";
      }
      $$(".ruler__needle").forEach(function (n) {
        if (t >= 0 && t <= 4.5) { n.hidden = false; n.style.left = (t / 4.5 * 100) + "%"; } else { n.hidden = true; }
      });
    });
  });

  /* ---- RFQ: prefill from ?product= / ?grade=, then build a tidy mailto ------------------ */
  var rfq = $("[data-rfq]");
  if (rfq) {
    var params = new URLSearchParams(location.search);
    var prod = params.get("product");
    var grade = params.get("grade");
    if (prod) {
      var opt = $('option[data-key="' + prod.replace(/[^a-z]/g, "") + '"]', rfq);
      if (opt) opt.selected = true;
    }
    if (grade) { var g = $('[data-k="grade"]', rfq); if (g) g.value = grade.slice(0, 40); }

    rfq.addEventListener("submit", function (e) {
      e.preventDefault();
      var v = function (k) { var el = $('[data-k="' + k + '"]', rfq); return el ? el.value.trim() : ""; };
      var size = [v("thk"), v("wid")].filter(Boolean).join(" x ");
      var subject = "Quote request: " + [v("grade"), size ? size + " mm" : "", v("product")].filter(Boolean).join(", ");
      if (subject === "Quote request: ") subject = "Quote request";
      var rows = [
        ["Product", v("product")], ["Grade", v("grade")], ["Standard", v("standard")], ["Hardness", v("hardness")],
        ["Thickness (mm)", v("thk")], ["Thickness tolerance", v("thktol")], ["Width (mm)", v("wid")],
        ["Width tolerance", v("widtol")], ["Finish", v("finish")], ["Edge", v("edge")],
        ["Coil size or cut length", v("form")], ["Quantity", v("qty")], ["Delivery location", v("dest")],
        ["Part", v("part")], ["", ""], ["Name", v("name")], ["Company", v("company")], ["Phone", v("phone")]
      ];
      var body = "Hello Anil Industries,\n\nPlease quote for the following strip.\n\n" +
        rows.map(function (r) { return r[0] ? r[0] + ": " + (r[1] || "") : ""; }).join("\n") + "\n\nThank you.\n";
      location.href = "mailto:" + EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }

  /* ---- Print + copy -------------------------------------------------------------------- */
  $$("[data-print]").forEach(function (b) { b.addEventListener("click", function () { window.print(); }); });
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var src = $(b.getAttribute("data-copy"));
      if (!src || !navigator.clipboard) return;
      navigator.clipboard.writeText(src.textContent).then(function () {
        var t = b.textContent;
        b.textContent = "Copied";
        setTimeout(function () { b.textContent = t; }, 1600);
      });
    });
  });
})();
