/* <optimal-film> · a looping brand film seen through fluted glass (v1.5)
 *
 *   <script src="assets/film/optimal-film.js" defer></script>
 *   <optimal-film src="assets/film/forest-satin.mp4" poster="assets/film/forest-satin.webp"></optimal-film>
 *
 * The film plays hidden; a fragment shader draws it through a sheet of reeded glass. The reeds
 * lean 17°, about seven across the frame; each shows a slice a little wider than itself, so the
 * folds repeat from reed to reed, with a bright lip on one edge, a dark seam on the other and a
 * hint of dispersion. The glass settles in when the element first shows, leans with the pointer
 * and thickens as the element scrolls away.
 *
 * Attributes: src, poster (required) · reeds (across the frame, default 7) · strength (0.7)
 *             · still (present: never play, draw the glass once)
 * Size it with CSS; it fills its box and covers like object-fit: cover.
 * No WebGL, or the film can't be read: the poster shows instead. Reduced motion: the film
 * doesn't play and the glass is drawn once over the poster. Decorative: aria-hidden.
 */
(() => {
  if (typeof customElements === 'undefined' || customElements.get('optimal-film')) return;
  const VS = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
  const FS = `precision highp float;uniform sampler2D V;uniform vec2 R,S;uniform float K,P,W;
  vec2 cover(vec2 uv){float ra=R.x/R.y,rm=S.x/S.y;vec2 s=ra>rm?vec2(1.,rm/ra):vec2(ra/rm,1.);return (uv-.5)*s+.5;}
  vec3 tap(vec2 q){return texture2D(V,clamp(cover(q/R),.001,.999)).rgb;}
  void main(){vec2 p=gl_FragCoord.xy,d=vec2(.956,.292);
    float s=dot(p,d)+P,f=fract(s/W),id=floor(s/W),k=K*(.78+.22*sin(id*1.7));
    vec2 q=p+d*(f-.5)*W*.9*k+vec2(0.,sin(id*2.31)*8.*k);
    vec3 c=vec3(tap(q+d*1.6*k).r,tap(q).g,tap(q-d*1.6*k).b);
    c=c*.5+(tap(q+d*4.*k)+tap(q-d*4.*k))*.25;
    float lip=1.-smoothstep(0.,.03,f),seam=smoothstep(.955,1.,f),bow=sin(f*3.14159);
    c=c*(1.-.24*k*seam)*(1.+.08*k*(bow-.5))+vec3(1.,.96,.93)*lip*.26*k;
    gl_FragColor=vec4(c,1.);}`;
  const reduced = () => matchMedia('(prefers-reduced-motion: reduce)').matches;

  class OptimalFilm extends HTMLElement {
    connectedCallback() {
      if (this._on) return; this._on = true;
      this.setAttribute('aria-hidden', 'true');
      /* only fill in what the page hasn't set: a page that positions the film absolutely keeps that */
      const cs = getComputedStyle(this), st = this.style; if (cs.display === 'inline') st.display = 'block'; if (cs.position === 'static') st.position = 'relative'; st.overflow = 'hidden';
      const fill = 'position:absolute;inset:0;width:100%;height:100%;display:block;';
      this._still = Object.assign(document.createElement('img'), { alt: '', src: this.getAttribute('poster') || '' });
      this._still.style.cssText = fill + 'object-fit:cover;';
      this._cv = document.createElement('canvas'); this._cv.style.cssText = fill + 'opacity:0;transition:opacity 1.4s ease;';
      this.append(this._still, this._cv);
      this._start();
    }
    disconnectedCallback() { this._on = false; cancelAnimationFrame(this._raf); this._io && this._io.disconnect(); this._vid && this._vid.pause(); removeEventListener('scroll', this._scroll); }
    _start() {
      const cv = this._cv, gl = cv.getContext('webgl', { antialias: false, alpha: false, premultipliedAlpha: false }); if (!gl) return;
      const sh = (t, s) => { const x = gl.createShader(t); gl.shaderSource(x, s); gl.compileShader(x); return x; };
      const pr = gl.createProgram(); gl.attachShader(pr, sh(gl.VERTEX_SHADER, VS)); gl.attachShader(pr, sh(gl.FRAGMENT_SHADER, FS)); gl.linkProgram(pr);
      if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) return;
      gl.useProgram(pr);
      gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer()); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
      const loc = gl.getAttribLocation(pr, 'p'); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
      gl.bindTexture(gl.TEXTURE_2D, gl.createTexture()); gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true);
      [[gl.TEXTURE_MIN_FILTER, gl.LINEAR], [gl.TEXTURE_MAG_FILTER, gl.LINEAR], [gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE], [gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE]].forEach(([a, b]) => gl.texParameteri(gl.TEXTURE_2D, a, b));
      const U = Object.fromEntries(['R', 'S', 'K', 'P', 'W'].map(n => [n, gl.getUniformLocation(pr, n)]));
      const still = this.hasAttribute('still') || reduced();
      const vid = this._vid = document.createElement('video');
      Object.assign(vid, { muted: true, loop: true, playsInline: true, preload: 'auto' }); vid.setAttribute('playsinline', ''); vid.setAttribute('muted', '');
      vid.style.cssText = 'position:absolute;width:2px;height:2px;opacity:0;pointer-events:none;';
      if (!still) { vid.src = this.getAttribute('src') || ''; this.append(vid); }
      let src = null, tainted = false;
      const upload = () => {
        if (!still && !tainted && vid.readyState >= 2 && vid.videoWidth) { try { gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, vid); src = vid; return; } catch (e) { tainted = true; } }
        const im = this._still; if (src !== im && im.complete && im.naturalWidth) { try { gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, im); src = im; } catch (e) { src = null; } }
      };
      const num = (a, d) => { const v = parseFloat(this.getAttribute(a)); return isFinite(v) ? v : d; };
      const dpr = Math.min(1.5, window.devicePixelRatio || 1), t0 = performance.now();
      let vis = true, P = 0, wantP = 0, scrollK = 0;
      this.addEventListener('pointermove', e => { if (e.pointerType !== 'mouse') return; const r = this.getBoundingClientRect(); wantP = ((e.clientX - r.left) / r.width - 0.5) * 70 * dpr; });
      this._scroll = () => { const r = this.getBoundingClientRect(); scrollK = Math.max(0, Math.min(1, -r.top / Math.max(1, r.height))); };
      addEventListener('scroll', this._scroll, { passive: true });
      const draw = now => {
        this._raf = 0; upload();
        if (src) {
          const w = Math.max(1, Math.round(this.clientWidth * dpr)), h = Math.max(1, Math.round(this.clientHeight * dpr));
          if (cv.width !== w || cv.height !== h) { cv.width = w; cv.height = h; gl.viewport(0, 0, w, h); }
          const t = (now - t0) / 1000, settle = still ? 0 : Math.max(0, 1 - t / 2.4);
          const k = num('strength', 0.7) + 0.6 * settle * settle + (still ? 0 : 0.05 * Math.sin(t * 0.5)) + 0.5 * scrollK;
          P += (wantP - P) * 0.05;
          gl.uniform2f(U.R, w, h); gl.uniform2f(U.S, src.videoWidth || src.naturalWidth, src.videoHeight || src.naturalHeight);
          gl.uniform1f(U.K, k); gl.uniform1f(U.P, P); gl.uniform1f(U.W, Math.max(128 * dpr, Math.min(300 * dpr, w / Math.max(2, num('reeds', 7)))));
          gl.drawArrays(gl.TRIANGLES, 0, 3); cv.style.opacity = '1';
        }
        if (this._on && vis && (!still || !src)) this._raf = requestAnimationFrame(draw);
      };
      this._io = new IntersectionObserver(es => { vis = es[0].isIntersecting;
        if (vis) { if (!still) vid.play().catch(() => {}); if (!this._raf) this._raf = requestAnimationFrame(draw); } else vid.pause(); }, { threshold: 0.01 });
      this._io.observe(this);
      this._raf = requestAnimationFrame(draw);
    }
  }
  customElements.define('optimal-film', OptimalFilm);
})();
