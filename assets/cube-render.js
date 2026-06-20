/* Shared isometric cube renderer for the Rubik's-cube lessons.
 * Grip-accurate: yellow top (U), green front (F = left drawn face), red right (R).
 * Lifted out of lesson 0016 so every later lesson draws identical cubes.
 *
 * Usage:
 *   <span data-cube="white:F;edge:UR;slot:1"></span>   (auto-rendered on load)
 *   window.__cube(spec)  -> SVG string (used by trainers)
 *
 * Spec keys (all optional):
 *   white : 'F' | 'R' | 'U'      where the corner's white sticker points (corner sits at UFR)
 *   edge  : 'UF' | 'UR' | null   the partner edge, sitting in the TOP layer
 *   slot  : 0 | 1                draw the empty front-right slot (dashed)
 *   trap  : 'edge'               draw the partner edge TRAPPED in the front-right slot
 *   corner: 0 | 1                set 0 to hide the corner (e.g. only an edge is shown)
 *   fr    : 'solved'|'flip'|'twist'|'wrong'
 *                                fill the front-right slot column with REAL face colours
 *                                (green front, red right, white) to show a filled-but-wrong
 *                                slot. Use with corner:0; edge:null.
 *   centers: 0 | 1              paint the three visible CENTRE stickers their real colours
 *                                (U yellow, F green, R red) — anchors which faces a slot
 *                                sits between. (lesson 19, the first-principles foundation)
 *   real  : 0 | 1              draw the loose corner + edge in their REAL colours
 *                                (white + green + red) instead of abstract grey/blue, so a
 *                                learner connects the picture to the actual piece in hand.
 */
(function () {
  var s = 26, cos30 = Math.cos(Math.PI/6), sin30 = 0.5, Ax = 85, Ay = 88;
  var FV = [-cos30*s, -sin30*s], RV = [cos30*s, -sin30*s], DV = [0, s];
  function vT(cf,cr){ return [Ax+cf*FV[0]+cr*RV[0], Ay+cf*FV[1]+cr*RV[1]]; }
  function vF(c,r){ return [Ax+c*FV[0]+r*DV[0], Ay+c*FV[1]+r*DV[1]]; }
  function vR(c,r){ return [Ax+c*RV[0]+r*DV[0], Ay+c*RV[1]+r*DV[1]]; }
  var DARK='#403d37', WHITE='#f4f2ec', CORNER='#9c968c', EDGE='#3b7dd8', SLOT='#d9d3c8';
  var GREEN='#3a9d52', RED='#c0392b', YELLOW='#f4cf28';   // real face colours for slot-inspection diagrams

  function poly(v, fill, dashed) {
    var pts = v.map(function(p){ return p[0].toFixed(1)+','+p[1].toFixed(1); }).join(' ');
    var st = dashed ? 'stroke="#c8401a" stroke-width="1.6" stroke-dasharray="3 2"' : 'stroke="#13110f" stroke-width="1.3"';
    return '<polygon points="'+pts+'" fill="'+fill+'" '+st+' stroke-linejoin="round"/>';
  }
  function label(p, t, col){ return '<text x="'+p[0].toFixed(1)+'" y="'+p[1].toFixed(1)+'" font-family="-apple-system,sans-serif" font-size="11" font-weight="700" fill="'+col+'" text-anchor="middle" dominant-baseline="central">'+t+'</text>'; }

  function build(spec) {
    var ov = {};
    function set(k,f,d){ ov[k]={fill:f,dash:!!d}; }
    // empty front-right slot (corner spot row 2, edge spot row 1)
    if (spec.slot){ set('F,0,1',SLOT,1); set('F,0,2',SLOT,1); set('R,0,1',SLOT,1); set('R,0,2',SLOT,1); }
    // edge trapped down in the slot's middle row (corner spot left empty/dashed above)
    if (spec.trap === 'edge'){
      set('F,0,2',SLOT,1); set('R,0,2',SLOT,1);     // corner spot still empty
      set('F,0,1',EDGE);   set('R,0,1',EDGE);        // edge wedged in the middle row
    }
    // corner at UFR (top cell 0,0 / front cell 0,0 / right cell 0,0)
    // real:1 paints the two non-white stickers green/red (the actual white-green-red corner)
    var cBody = spec.real ? null : CORNER;
    if (spec.corner !== 0){
      if (spec.white==='F'){ set('F,0,0',WHITE); set('T,0,0',cBody||GREEN); set('R,0,0',cBody||RED); }
      else if (spec.white==='R'){ set('R,0,0',WHITE); set('T,0,0',cBody||GREEN); set('F,0,0',cBody||RED); }
      else if (spec.white==='U'){ set('T,0,0',WHITE); set('F,0,0',cBody||GREEN); set('R,0,0',cBody||RED); }
    }
    // partner edge sitting up in the top layer (real:1 → its true green/red colours)
    var e1 = spec.real ? GREEN : EDGE, e2 = spec.real ? RED : EDGE;
    if (spec.edge==='UF'){ set('T,1,0',e1); set('F,1,0',e2); }
    else if (spec.edge==='UR'){ set('T,0,1',e1); set('R,1,0',e2); }

    // real centre stickers — anchors which faces a slot lies between
    if (spec.centers){ set('T,1,1',YELLOW); set('F,1,1',GREEN); set('R,1,1',RED); }

    // front-right slot filled with REAL face colours (corner row 2, edge row 1)
    if (spec.fr){
      // default = solved: front column green, right column red
      var cF=GREEN, cR=RED, eF=GREEN, eR=RED;
      if (spec.fr==='flip'){ eF=RED; eR=GREEN; }                 // edge twisted: colours swapped
      else if (spec.fr==='twist'){ cF=WHITE; cR=GREEN; }         // corner twisted: white peeks on front
      else if (spec.fr==='wrong'){ cF=RED; cR=GREEN; eF=RED; eR=GREEN; } // a different piece sits here
      set('F,0,2',cF); set('R,0,2',cR);   // corner
      set('F,0,1',eF); set('R,0,1',eR);   // edge
    }

    var out = [];
    var cf, cr, c, r, k;
    for (cf=0; cf<3; cf++) for (cr=0; cr<3; cr++){
      k='T,'+cf+','+cr; var o=ov[k]||{fill:DARK};
      out.push(poly([vT(cf,cr),vT(cf+1,cr),vT(cf+1,cr+1),vT(cf,cr+1)], o.fill, o.dash));
    }
    for (c=0; c<3; c++) for (r=0; r<3; r++){
      k='F,'+c+','+r; var of=ov[k]||{fill:DARK};
      out.push(poly([vF(c,r),vF(c+1,r),vF(c+1,r+1),vF(c,r+1)], of.fill, of.dash));
    }
    for (c=0; c<3; c++) for (r=0; r<3; r++){
      k='R,'+c+','+r; var orr=ov[k]||{fill:DARK};
      out.push(poly([vR(c,r),vR(c+1,r),vR(c+1,r+1),vR(c,r+1)], orr.fill, orr.dash));
    }
    out.push(label(vT(1.5,1.5), 'U', '#bdb7ab'));
    out.push(label(vF(1.5,1.5), 'F', '#7ea98a'));
    out.push(label(vR(1.5,1.5), 'R', '#cf8d86'));
    return '<svg viewBox="0 0 170 176" role="img" aria-label="cube state">'+out.join('')+'</svg>';
  }
  function parse(str){
    var spec={white:'F',edge:null,slot:false,trap:null,corner:1,fr:null,centers:0,real:0};
    str.split(';').forEach(function(kv){ var p=kv.split(':');
      if(p[0]==='white')spec.white=p[1];
      else if(p[0]==='edge')spec.edge=(p[1]==='null'?null:p[1]);
      else if(p[0]==='slot')spec.slot=(p[1]==='1');
      else if(p[0]==='trap')spec.trap=(p[1]==='null'?null:p[1]);
      else if(p[0]==='corner')spec.corner=(p[1]==='0'?0:1);
      else if(p[0]==='fr')spec.fr=(p[1]==='null'?null:p[1]);
      else if(p[0]==='centers')spec.centers=(p[1]==='1'?1:0);
      else if(p[0]==='real')spec.real=(p[1]==='1'?1:0);
    });
    return spec;
  }
  var nodes = document.querySelectorAll('[data-cube]');
  Array.prototype.forEach.call(nodes, function(n){ n.innerHTML = build(parse(n.getAttribute('data-cube'))); });
  window.__cube = build;
})();
