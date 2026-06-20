#!/usr/bin/env python3
"""54-sticker cube simulator. Faces: U R F D L B, each 9 stickers index 0..8 row-major.
Standard color scheme used: U=yellow(Y), D=white(W), F=green(G), B=blue(B), R=red(R), L=orange(O).
(Matt's grip: white on BOTTOM=D, yellow on TOP=U, green front, etc. Scheme is arbitrary for verification.)
"""

import copy

# facelet index: face letter -> list of 9 colors
FACES = ['U','R','F','D','L','B']

def solved():
    return {f: [c]*9 for f,c in zip(FACES, ['Y','R','G','W','O','B'])}

# A face turn: rotate that face's stickers clockwise + cycle adjacent edge strips.
# We define each basic move as sticker permutations. Index layout per face (row-major):
# 0 1 2
# 3 4 5
# 6 7 8

def rot_face_cw(face):
    f = face
    return [f[6],f[3],f[0], f[7],f[4],f[1], f[8],f[5],f[2]]

def move_U(c):
    c=copy.deepcopy(c)
    c['U']=rot_face_cw(c['U'])
    # top rows of F,R,B,L cycle: F<-R<-B<-L<-F (U turns top layer clockwise viewed from top)
    F,R,B,L=c['F'][:3],c['R'][:3],c['B'][:3],c['L'][:3]
    c['F'][:3]=R; c['R'][:3]=B; c['B'][:3]=L; c['L'][:3]=F
    return c

def move_D(c):
    c=copy.deepcopy(c)
    c['D']=rot_face_cw(c['D'])
    F,R,B,L=c['F'][6:],c['R'][6:],c['B'][6:],c['L'][6:]
    # D clockwise viewed from bottom: F<-L<-B<-R<-F
    c['F'][6:]=L; c['L'][6:]=B; c['B'][6:]=R; c['R'][6:]=F
    return c

def move_R(c):
    c=copy.deepcopy(c)
    c['R']=rot_face_cw(c['R'])
    # right columns of U,F,D and back. cols index 2,5,8. U col<-F col<-D col<-B(inverted)
    U=[c['U'][2],c['U'][5],c['U'][8]]
    F=[c['F'][2],c['F'][5],c['F'][8]]
    D=[c['D'][2],c['D'][5],c['D'][8]]
    B=[c['B'][0],c['B'][3],c['B'][6]]  # back is mirrored
    # R turn: U<-F, F<-D, D<-Binv, B<-Uinv
    c['U'][2],c['U'][5],c['U'][8]=F
    c['D'][2],c['D'][5],c['D'][8]=B[2],B[1],B[0]
    c['F'][2],c['F'][5],c['F'][8]=D
    c['B'][0],c['B'][3],c['B'][6]=U[2],U[1],U[0]
    return c

def move_L(c):
    c=copy.deepcopy(c)
    c['L']=rot_face_cw(c['L'])
    U=[c['U'][0],c['U'][3],c['U'][6]]
    F=[c['F'][0],c['F'][3],c['F'][6]]
    D=[c['D'][0],c['D'][3],c['D'][6]]
    B=[c['B'][2],c['B'][5],c['B'][8]]
    # L turn (clockwise from left): U<-B(inv), F<-U, D<-F, B<-D(inv)
    c['U'][0],c['U'][3],c['U'][6]=B[2],B[1],B[0]
    c['F'][0],c['F'][3],c['F'][6]=U
    c['D'][0],c['D'][3],c['D'][6]=F
    c['B'][2],c['B'][5],c['B'][8]=D[2],D[1],D[0]
    return c

def move_F(c):
    c=copy.deepcopy(c)
    c['F']=rot_face_cw(c['F'])
    U=[c['U'][6],c['U'][7],c['U'][8]]
    R=[c['R'][0],c['R'][3],c['R'][6]]
    D=[c['D'][0],c['D'][1],c['D'][2]]
    L=[c['L'][2],c['L'][5],c['L'][8]]
    # F clockwise: U bottom row -> R left col -> D top row -> L right col -> U
    c['R'][0],c['R'][3],c['R'][6]=U
    c['D'][0],c['D'][1],c['D'][2]=R[2],R[1],R[0]
    c['L'][2],c['L'][5],c['L'][8]=D
    c['U'][6],c['U'][7],c['U'][8]=L[2],L[1],L[0]
    return c

def move_B(c):
    c=copy.deepcopy(c)
    c['B']=rot_face_cw(c['B'])
    U=[c['U'][0],c['U'][1],c['U'][2]]
    R=[c['R'][2],c['R'][5],c['R'][8]]
    D=[c['D'][6],c['D'][7],c['D'][8]]
    L=[c['L'][0],c['L'][3],c['L'][6]]
    # B clockwise (from back): U top row -> L left col -> D bottom row -> R right col -> U
    c['L'][0],c['L'][3],c['L'][6]=U[2],U[1],U[0]
    c['D'][6],c['D'][7],c['D'][8]=L
    c['R'][2],c['R'][5],c['R'][8]=D[2],D[1],D[0]
    c['U'][0],c['U'][1],c['U'][2]=R
    return c

BASE={'U':move_U,'D':move_D,'R':move_R,'L':move_L,'F':move_F,'B':move_B}

def apply(c, alg):
    for tok in alg.split():
        f=tok[0]
        fn=BASE[f]
        n = 1
        if tok.endswith("'"): n=3
        elif tok.endswith("2"): n=2
        for _ in range(n): c=fn(c)
    return c

def eq(a,b): return a==b

if __name__=="__main__":
    s=solved()
    # sanity: R R R R = identity
    assert eq(apply(s,"R R R R"), s), "R4 fail"
    assert eq(apply(s,"U U U U"), s), "U4 fail"
    assert eq(apply(s,"F F F F"), s), "F4 fail"
    assert eq(apply(s,"L L L L"), s), "L4 fail"
    assert eq(apply(s,"B B B B"), s), "B4 fail"
    assert eq(apply(s,"D D D D"), s), "D4 fail"
    # sexy move x6 = identity
    assert eq(apply(s,"R U R' U' "*6), s), "sexy6 fail"
    # T-perm is its own inverse (T-perm twice = identity)
    tperm="R U R' U' R' F R2 U' R' U' R U R' F'"
    assert eq(apply(s,tperm+" "+tperm), s), "Tperm self-inverse fail"
    print("ALL SANITY CHECKS PASS")
