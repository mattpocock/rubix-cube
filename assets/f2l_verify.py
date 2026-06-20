import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cube import solved, apply, FACES

def inv(alg):
    out=[]
    for t in reversed(alg.split()):
        if t.endswith("'"): out.append(t[0])
        elif t.endswith("2"): out.append(t)
        else: out.append(t[0]+"'")
    return " ".join(out)

# FR slot pieces: corner D2/F8/R6, edge F5/R3. U layer (all U) + side TOP rows (0,1,2) are free.
# Everything else in bottom two layers must stay solved.
FR = {('D',2),('F',8),('R',6),('F',5),('R',3)}
def must_stay(c):
    s=solved()
    bad=[]
    for f in FACES:
        for i in range(9):
            if f=='U': continue
            if i in (0,1,2): continue           # side top rows = U layer area, free
            if (f,i) in FR: continue             # FR slot pieces, allowed to move
            if c[f][i]!=s[f][i]: bad.append((f,i,c[f][i]))
    return bad

def read_case(c):
    # locate the FR corner (colors of solved FR corner = D='W',F='G',R='R') and FR edge (F='G',R='R')
    # find where white-green-red corner sits & how white is oriented; find green-red edge
    corner=set(['W','G','R']); edge=set(['G','R'])
    cloc=eloc=None; wface=None
    # corner cubies: list of (face,idx) triples per corner - check all 8; we only care if it's in U layer or FR slot
    corners={
      'UFR':[('U',8),('F',2),('R',0)],'UFL':[('U',6),('F',0),('L',2)],
      'UBR':[('U',2),('R',2),('B',0)],'UBL':[('U',0),('L',0),('B',2)],
      'DFR':[('D',2),('F',8),('R',6)],'DFL':[('D',0),('F',6),('L',8)],
      'DBR':[('D',8),('R',8),('B',6)],'DBL':[('D',6),('L',6),('B',8)],
    }
    edges={
      'UF':[('U',7),('F',1)],'UR':[('U',5),('R',1)],'UB':[('U',1),('B',1)],'UL':[('U',3),('L',1)],
      'FR':[('F',5),('R',3)],'FL':[('F',3),('L',5)],'BR':[('B',3),('R',5)],'BL':[('B',5),('L',3)],
      'DF':[('D',1),('F',7)],'DR':[('D',5),('R',7)],'DB':[('D',7),('B',7)],'DL':[('D',3),('L',7)],
    }
    for name,st in corners.items():
        cols=set(c[f][i] for f,i in st)
        if cols==corner:
            cloc=name
            for f,i in st:
                if c[f][i]=='W': wface=f
    for name,st in edges.items():
        cols=set(c[f][i] for f,i in st)
        if cols==edge: eloc=name
    return cloc,wface,eloc

cands={
 "R U R'":"ready: white-right (L15)",
 "F' U' F":"ready: white-front (L15)",
 "U R U' R'":"join candidate A",
 "U' F' U F":"join candidate A-mirror",
 "R U2 R' U R U' R'":"white-up: R U2 R' then U R U' R' (Ruwix)",
 "F' U2 F U' F' U F":"white-up mirror",
 "R U' R'":"bring pair to top / split (Ruwix)",
 "U R U' R' U' F' U F":"separated reunion (Ruwix)",
}
s=solved()
for alg,label in cands.items():
    state=apply(s, inv(alg))      # inverse scrambles the case that 'alg' then solves
    bad=must_stay(state)
    cloc,wface,eloc=read_case(state)
    clean = "FR-ONLY ✓" if not bad else f"DISTURBS {len(bad)} other ✗"
    print(f"{alg:28s} | {clean:16s} | corner@{cloc} white→{wface}, edge@{eloc} | {label}")
    if bad: print("      disturbed:",bad[:6])

print("\n--- refinement pass ---")
more={
 # white-up cases, hunting for corner held at UFR
 "U' R U R' U R U' R'":"white-up A",
 "U R U2 R' U R U' R'":"white-up B",
 "R U2 R' U' R U R'":"white-up C",
 "U2 R U R' U R U' R'":"white-up D",
 "F' U' F U' F' U F":"white-up E (F-side)",
 "U2 R U' R' U' R U R'":"white-up F",
 # pop a wrongly-placed piece out of FR slot to the top
 "R U R'":"pop/insert",
 "R U' R'":"pop B",
}
for alg,label in more.items():
    state=apply(s, inv(alg))
    bad=must_stay(state)
    cloc,wface,eloc=read_case(state)
    clean = "FR-ONLY ✓" if not bad else f"DISTURBS {len(bad)} ✗"
    print(f"{alg:26s} | {clean:14s} | corner@{cloc} white→{wface}, edge@{eloc} | {label}")
