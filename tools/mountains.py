"""Meraki Ascent ridge artwork generator.

Draws four North Cascades-style ridge layers in the logo style (ink-plum
outlines, wavy gully lines, faceted pinks) and writes hero-range-0..3.svg.
Usage: python3 tools/mountains.py <output-folder>
Change a layer seed (5, 9, 13, 17) or its peak list for a new range in the same style.
"""
import random, math, sys
OUT=sys.argv[1]
class Noise:
    def __init__(s,seed): r=random.Random(seed); s.v=[r.uniform(-1,1) for _ in range(512)]
    def __call__(s,x):
        i=math.floor(x); f=x-i; f=f*f*(3-2*f)
        return s.v[i%512]*(1-f)+s.v[(i+1)%512]*f
    def fbm(s,x,o=3):
        return sum(s(x*2**k+k*17.3)/(2**k) for k in range(o))
def smooth(pts,close=False):
    d=f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    n=len(pts)
    for i in range(n-1):
        p0=pts[i-1] if i>0 else pts[i]; p1=pts[i]; p2=pts[i+1]; p3=pts[i+2] if i+2<n else pts[i+1]
        d+=f" C{p1[0]+(p2[0]-p0[0])/6:.1f} {p1[1]+(p2[1]-p0[1])/6:.1f} {p2[0]-(p3[0]-p1[0])/6:.1f} {p2[1]-(p3[1]-p1[1])/6:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d+(" Z" if close else "")
def ridge(peaks,W,base,rnd,nz):
    # control points: peaks + irregular saddles + shoulders
    ctl=[(-80,peaks[0][1]+120)]
    for i,(px,py,sharp) in enumerate(peaks):
        ctl.append((px-sharp*0.55,py+sharp*0.9+rnd.uniform(-8,8)))
        ctl.append((px,py))
        ctl.append((px+sharp*0.5,py+sharp*0.8+rnd.uniform(-8,8)))
        if i+1<len(peaks):
            nx,ny,_=peaks[i+1]
            sx=(px+nx)/2+rnd.uniform(-35,35); sy=max(py,ny)+rnd.uniform(70,140)
            sy=min(sy,base-60)
            ctl.append((sx,sy))
    ctl.append((W+80,peaks[-1][1]+120))
    ctl.sort()
    pts=[]
    for a,b in zip(ctl,ctl[1:]):
        steps=max(2,int(abs(b[0]-a[0])/7))
        for k in range(steps):
            t=k/steps; x=a[0]+(b[0]-a[0])*t; y=a[1]+(b[1]-a[1])*t
            jag=nz.fbm(x/38.0,3)*7 + nz(x/9.0+50)*2.2
            pts.append((x,y+jag))
    pts.append(ctl[-1])
    return pts
def ry(R,x):
    for a,b in zip(R,R[1:]):
        if a[0]<=x<=b[0]:
            t=(x-a[0])/(b[0]-a[0]+1e-9); return a[1]+t*(b[1]-a[1])
    return R[-1][1]
def organic(x0,y0,x1,y1,nz,amp,n,bow):
    off=random.random()*100
    pts=[]
    for i in range(n+1):
        t=i/n
        e=min(1,t*3.5)
        curve=bow*math.sin(t*math.pi*0.9)  # bows outward like a gully
        w=(nz.fbm(off+t*2.6,3)*amp*1.7 + nz(off*3+t*11)*amp*0.45)*e
        pts.append((x0+(x1-x0)*(t**1.15)+curve+w, y0+(y1-y0)*t))
    return pts
def rng_layer(W,base,peaks,seed,L,Rp,spacing,amp,out_fills,out_strokes,sw):
    rnd=random.Random(seed); random.seed(seed+1); nz=Noise(seed)
    R=ridge(peaks,W,base,rnd,nz)
    N=40
    starts=[]; x=-60
    while x<W+60: starts.append(x); x+=rnd.uniform(spacing*0.6,spacing*1.4)
    pk_x=[p[0] for p in peaks]
    starts=[s for s in starts if all(abs(s-p)>spacing*0.3 for p in pk_x)]+pk_x
    starts.sort()
    lines=[]; prev=-1e9
    for s in starts:
        pk=min(peaks,key=lambda p:abs(p[0]-s))
        side=1 if s>=pk[0] else -1
        xe=s+(s-pk[0])*rnd.uniform(0.5,1.0)+rnd.uniform(-14,14)
        xe=max(xe,prev+spacing*0.45); prev=xe
        bow=side*rnd.uniform(10,32)
        lines.append(organic(s,ry(R,s),xe,base,nz,amp,N,bow))
    last=None
    for i in range(len(lines)-1):
        a,b=lines[i],lines[i+1]
        mid=(a[0][0]+b[0][0])/2; pk=min(peaks,key=lambda p:abs(p[0]-mid)); left=mid<pk[0]
        pal=L if left else Rp
        top=[a[0]]+[p for p in R if a[0][0]<p[0]<b[0][0]]+[b[0]]
        bounds=[(0,0,top)]
        k=rnd.choice([1,2,2,3])
        for ia in sorted(rnd.sample(range(6,N-4),k)):
            off=rnd.randint(4,10)
            ib=ia-off if left else ia+off
            ib=max(3,min(N-3,ib))
            if ia<=bounds[-1][0]+3 or ib<=bounds[-1][1]+3: continue
            cut=organic(a[ia][0],a[ia][1],b[ib][0],b[ib][1],nz,amp*0.45,14,rnd.uniform(-6,6))
            bounds.append((ia,ib,cut)); out_strokes.append(smooth(cut))
        bounds.append((N,N,[a[N],b[N]]))
        for j in range(len(bounds)-1):
            ia0,ib0,c0=bounds[j]; ia1,ib1,c1=bounds[j+1]
            poly=c0+b[ib0:ib1+1]+c1[::-1]+a[ia0:ia1+1][::-1]
            f=rnd.choice([c for c in pal if c!=last]); last=f
            out_fills.append(f'<path d="{smooth(poly,True)}" fill="{f}" stroke="{f}" stroke-width="1.5"/>')
        # occasional dangling branch line (like logo's short strata)
        if rnd.random()<0.4:
            ia=rnd.randint(10,N-8)
            p=a[ia]; q=b[min(N-2,ia+rnd.randint(-3,6))]
            br=organic(p[0],p[1],p[0]+(q[0]-p[0])*rnd.uniform(0.35,0.6),p[1]+(q[1]-p[1])*0.5+rnd.uniform(8,22),nz,amp*0.35,8,0)
            out_strokes.append(smooth(br))
    for l in lines: out_strokes.append(smooth(l))
    out_strokes.append(f'{smooth(R)}|ridge')
def svg(W,H,layers,sw):
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMax slice">']
    for (peaks,seed,L,Rp,spacing,amp) in layers:
        fills=[];strokes=[]
        rng_layer(W,H+30,peaks,seed,L,Rp,spacing,amp,fills,strokes,sw)
        # ridge fill backing so no gaps
        parts+=fills
        parts.append(f'<g fill="none" stroke="#24091A" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round">')
        for s in strokes:
            if s.endswith('|ridge'): parts.append(f'<path d="{s[:-6]}" stroke-width="{sw+1.5}"/>')
            else: parts.append(f'<path d="{s}"/>')
        parts.append('</g>')
    parts.append('</svg>')
    return "\n".join(parts)
W=1600
P0=(["#F2A9CB","#EE97C0","#F5BBD6"],["#F9D3E5","#F7C6DD","#FADDEB"])
P1=(["#EC7DB3","#E86BA6","#F09BC4"],["#F6BBD7","#F3A6CC","#F8CDE1"])
P2=(["#E5469B","#E8579F","#EC6FA9"],["#F09BC4","#EF8FBE","#F3A6CC"])
P3=(["#E3288A","#DE1C7E","#E5469B"],["#EF8FBE","#EA7DB3","#F3A6CC"])
L0=([(120,150,70),(390,70,55),(560,120,40),(840,40,60),(1110,130,50),(1340,60,45),(1560,140,60)],5,*P0,100,9)
L1=([(40,270,60),(300,190,50),(640,230,55),(960,170,45),(1230,250,60),(1470,200,50)],9,*P1,96,10)
L2=([(180,140,45),(520,70,40),(760,180,55),(1080,110,45),(1400,150,50)],13,*P2,92,10)
L3=([(-20,260,60),(330,210,55),(640,300,50),(900,230,45),(1260,280,55),(1560,220,50)],17,*P3,88,11)
for k,(H,L,sw) in enumerate([(560,L0,5),(560,L1,5),(440,L2,6),(440,L3,6)]):
    open(OUT+f'/hero-range-{k}.svg','w').write(svg(W,H,[L],sw))
