import{S as T,i as q,s as D,F as v,H as C,G as y,B as f,f as b,D as h,J as A,p as k,c as R,m as j,o as B,t as N,l as I,N as M,A as z,O as E,K as J,ab as ue,b as K,e as re,g as fe,h as _e,k as ce,n as oe,v as ge}from"./index.53206edc.js";/* empty css                                            */import{B as G}from"./BlockTitle.8ae2e6a4.js";const w=i=>{var e=null;return i<0?e=[52,152,219]:e=[231,76,60],me(he(Math.abs(i),[255,255,255],e))},he=(i,e,t)=>{i>1&&(i=1),i=Math.sqrt(i);var n=[0,0,0],o;for(o=0;o<3;o++)n[o]=Math.round(e[o]*(1-i)+t[o]*i);return n},me=i=>"rgb("+i[0]+", "+i[1]+", "+i[2]+")",U=(i,e,t,n,o)=>{var s=n/o,c=e/t,l=0,r=0,u=i?s>c:s<c;return u?(l=e,r=l/s):(r=t,l=r*s),{width:l,height:r,x:(e-l)/2,y:(t-r)/2}};function L(i,e,t){const n=i.slice();return n[2]=e[t],n}function de(i){let e;return{c(){e=C(i[1])},m(t,n){b(t,e,n)},p(t,n){n&2&&A(e,t[1])},d(t){t&&k(e)}}}function P(i){let e,t=i[2][0]+"",n,o,s;return{c(){e=v("div"),n=C(t),o=y(),f(e,"class","item svelte-12f6iga"),f(e,"style",s="background-color: "+w(i[2][1]))},m(c,l){b(c,e,l),h(e,n),h(e,o)},p(c,l){l&1&&t!==(t=c[2][0]+"")&&A(n,t),l&1&&s!==(s="background-color: "+w(c[2][1]))&&f(e,"style",s)},d(c){c&&k(e)}}}function ve(i){let e,t,n,o,s;t=new G({props:{$$slots:{default:[de]},$$scope:{ctx:i}}});let c=i[0],l=[];for(let r=0;r<c.length;r+=1)l[r]=P(L(i,c,r));return{c(){e=v("div"),R(t.$$.fragment),n=y(),o=v("div");for(let r=0;r<l.length;r+=1)l[r].c();f(o,"class","range svelte-12f6iga"),f(e,"class","input-number svelte-12f6iga")},m(r,u){b(r,e,u),j(t,e,null),h(e,n),h(e,o);for(let a=0;a<l.length;a+=1)l[a].m(o,null);s=!0},p(r,[u]){const a={};if(u&34&&(a.$$scope={dirty:u,ctx:r}),t.$set(a),u&1){c=r[0];let _;for(_=0;_<c.length;_+=1){const g=L(r,c,_);l[_]?l[_].p(g,u):(l[_]=P(g),l[_].c(),l[_].m(o,null))}for(;_<l.length;_+=1)l[_].d(1);l.length=c.length}},i(r){s||(B(t.$$.fragment,r),s=!0)},o(r){N(t.$$.fragment,r),s=!1},d(r){r&&k(e),I(t),M(l,r)}}}function be(i,e,t){let{interpretation:n}=e,{label:o=""}=e;return i.$$set=s=>{"interpretation"in s&&t(0,n=s.interpretation),"label"in s&&t(1,o=s.label)},[n,o]}class ke extends T{constructor(e){super(),q(this,e,be,ve,D,{interpretation:0,label:1})}}function Q(i,e,t){const n=i.slice();return n[3]=e[t],n[5]=t,n}function pe(i){let e;return{c(){e=C(i[2])},m(t,n){b(t,e,n)},p(t,n){n&4&&A(e,t[2])},d(t){t&&k(e)}}}function V(i){let e,t=i[3]+"",n,o,s;return{c(){e=v("li"),n=C(t),o=y(),f(e,"class","dropdown-item svelte-x98jkl"),f(e,"style",s="background-color: "+w(i[0][i[5]]))},m(c,l){b(c,e,l),h(e,n),h(e,o)},p(c,l){l&2&&t!==(t=c[3]+"")&&A(n,t),l&1&&s!==(s="background-color: "+w(c[0][c[5]]))&&f(e,"style",s)},d(c){c&&k(e)}}}function we(i){let e,t,n,o,s;t=new G({props:{$$slots:{default:[pe]},$$scope:{ctx:i}}});let c=i[1],l=[];for(let r=0;r<c.length;r+=1)l[r]=V(Q(i,c,r));return{c(){e=v("div"),R(t.$$.fragment),n=y(),o=v("ul");for(let r=0;r<l.length;r+=1)l[r].c();f(o,"class","dropdown-menu svelte-x98jkl")},m(r,u){b(r,e,u),j(t,e,null),h(e,n),h(e,o);for(let a=0;a<l.length;a+=1)l[a].m(o,null);s=!0},p(r,[u]){const a={};if(u&68&&(a.$$scope={dirty:u,ctx:r}),t.$set(a),u&3){c=r[1];let _;for(_=0;_<c.length;_+=1){const g=Q(r,c,_);l[_]?l[_].p(g,u):(l[_]=V(g),l[_].c(),l[_].m(o,null))}for(;_<l.length;_+=1)l[_].d(1);l.length=c.length}},i(r){s||(B(t.$$.fragment,r),s=!0)},o(r){N(t.$$.fragment,r),s=!1},d(r){r&&k(e),I(t),M(l,r)}}}function ye(i,e,t){let{interpretation:n}=e,{choices:o}=e,{label:s=""}=e;return i.$$set=c=>{"interpretation"in c&&t(0,n=c.interpretation),"choices"in c&&t(1,o=c.choices),"label"in c&&t(2,s=c.label)},[n,o,s]}class Se extends T{constructor(e){super(),q(this,e,ye,we,D,{interpretation:0,choices:1,label:2})}}function Ce(i){let e;return{c(){e=C(i[0])},m(t,n){b(t,e,n)},p(t,n){n&1&&A(e,t[0])},d(t){t&&k(e)}}}function Ae(i){let e,t,n,o,s,c,l,r,u,a,_,g,m;return t=new G({props:{$$slots:{default:[Ce]},$$scope:{ctx:i}}}),{c(){e=v("div"),R(t.$$.fragment),n=y(),o=v("button"),s=v("div"),l=y(),r=v("div"),u=z("svg"),a=z("line"),_=z("line"),f(s,"class","checkbox svelte-1yidkvc"),f(s,"style",c="background-color: "+w(i[2][0])),f(a,"x1","-7.5"),f(a,"y1","0"),f(a,"x2","-2.5"),f(a,"y2","5"),f(a,"stroke","black"),f(a,"stroke-width","4"),f(a,"stroke-linecap","round"),f(_,"x1","-2.5"),f(_,"y1","5"),f(_,"x2","7.5"),f(_,"y2","-7.5"),f(_,"stroke","black"),f(_,"stroke-width","4"),f(_,"stroke-linecap","round"),f(u,"viewBox","-10 -10 20 20"),f(u,"class","svelte-1yidkvc"),f(r,"class","checkbox svelte-1yidkvc"),f(r,"style",g="background-color: "+w(i[2][1])),f(o,"class","checkbox-item svelte-1yidkvc"),E(o,"selected",i[1]),f(e,"class","input-checkbox svelte-1yidkvc")},m(d,p){b(d,e,p),j(t,e,null),h(e,n),h(e,o),h(o,s),h(o,l),h(o,r),h(r,u),h(u,a),h(u,_),m=!0},p(d,[p]){const S={};p&9&&(S.$$scope={dirty:p,ctx:d}),t.$set(S),(!m||p&4&&c!==(c="background-color: "+w(d[2][0])))&&f(s,"style",c),(!m||p&4&&g!==(g="background-color: "+w(d[2][1])))&&f(r,"style",g),p&2&&E(o,"selected",d[1])},i(d){m||(B(t.$$.fragment,d),m=!0)},o(d){N(t.$$.fragment,d),m=!1},d(d){d&&k(e),I(t)}}}function Be(i,e,t){let{label:n=""}=e,{original:o}=e,{interpretation:s}=e;return i.$$set=c=>{"label"in c&&t(0,n=c.label),"original"in c&&t(1,o=c.original),"interpretation"in c&&t(2,s=c.interpretation)},[n,o,s]}class Ne extends T{constructor(e){super(),q(this,e,Be,Ae,D,{label:0,original:1,interpretation:2})}}function W(i,e,t){const n=i.slice();return n[4]=e[t],n[6]=t,n}function Re(i){let e;return{c(){e=C(i[3])},m(t,n){b(t,e,n)},p(t,n){n&8&&A(e,t[3])},d(t){t&&k(e)}}}function X(i){let e,t,n,o,s,c,l,r,u,a,_=i[4]+"",g,m;return{c(){e=v("button"),t=v("div"),o=y(),s=v("div"),c=z("svg"),l=z("line"),r=z("line"),a=y(),g=C(_),m=y(),f(t,"class","checkbox svelte-l6t04m"),f(t,"style",n="background-color: "+w(i[1][i[6]][0])),f(l,"x1","-7.5"),f(l,"y1","0"),f(l,"x2","-2.5"),f(l,"y2","5"),f(l,"stroke","black"),f(l,"stroke-width","4"),f(l,"stroke-linecap","round"),f(r,"x1","-2.5"),f(r,"y1","5"),f(r,"x2","7.5"),f(r,"y2","-7.5"),f(r,"stroke","black"),f(r,"stroke-width","4"),f(r,"stroke-linecap","round"),f(c,"viewBox","-10 -10 20 20"),f(c,"class","svelte-l6t04m"),f(s,"class","checkbox svelte-l6t04m"),f(s,"style",u="background-color: "+w(i[1][i[6]][1])),f(e,"class","checkbox-item  svelte-l6t04m"),E(e,"selected",i[0].includes(i[4]))},m(d,p){b(d,e,p),h(e,t),h(e,o),h(e,s),h(s,c),h(c,l),h(c,r),h(e,a),h(e,g),h(e,m)},p(d,p){p&2&&n!==(n="background-color: "+w(d[1][d[6]][0]))&&f(t,"style",n),p&2&&u!==(u="background-color: "+w(d[1][d[6]][1]))&&f(s,"style",u),p&4&&_!==(_=d[4]+"")&&A(g,_),p&5&&E(e,"selected",d[0].includes(d[4]))},d(d){d&&k(e)}}}function je(i){let e,t,n,o;t=new G({props:{$$slots:{default:[Re]},$$scope:{ctx:i}}});let s=i[2],c=[];for(let l=0;l<s.length;l+=1)c[l]=X(W(i,s,l));return{c(){e=v("div"),R(t.$$.fragment),n=y();for(let l=0;l<c.length;l+=1)c[l].c();f(e,"class","input-checkbox-group svelte-l6t04m")},m(l,r){b(l,e,r),j(t,e,null),h(e,n);for(let u=0;u<c.length;u+=1)c[u].m(e,null);o=!0},p(l,[r]){const u={};if(r&136&&(u.$$scope={dirty:r,ctx:l}),t.$set(u),r&7){s=l[2];let a;for(a=0;a<s.length;a+=1){const _=W(l,s,a);c[a]?c[a].p(_,r):(c[a]=X(_),c[a].c(),c[a].m(e,null))}for(;a<c.length;a+=1)c[a].d(1);c.length=s.length}},i(l){o||(B(t.$$.fragment,l),o=!0)},o(l){N(t.$$.fragment,l),o=!1},d(l){l&&k(e),I(t),M(c,l)}}}function Ie(i,e,t){let{original:n}=e,{interpretation:o}=e,{choices:s}=e,{label:c=""}=e;return i.$$set=l=>{"original"in l&&t(0,n=l.original),"interpretation"in l&&t(1,o=l.interpretation),"choices"in l&&t(2,s=l.choices),"label"in l&&t(3,c=l.label)},[n,o,s,c]}class Te extends T{constructor(e){super(),q(this,e,Ie,je,D,{original:0,interpretation:1,choices:2,label:3})}}function Y(i,e,t){const n=i.slice();return n[6]=e[t],n}function qe(i){let e;return{c(){e=C(i[5])},m(t,n){b(t,e,n)},p(t,n){n&32&&A(e,t[5])},d(t){t&&k(e)}}}function Z(i){let e,t;return{c(){e=v("div"),f(e,"style",t="background-color: "+w(i[6])),f(e,"class","svelte-9u5hcr")},m(n,o){b(n,e,o)},p(n,o){o&2&&t!==(t="background-color: "+w(n[6]))&&f(e,"style",t)},d(n){n&&k(e)}}}function De(i){let e,t,n,o,s,c,l,r,u,a;t=new G({props:{$$slots:{default:[qe]},$$scope:{ctx:i}}});let _=i[1],g=[];for(let m=0;m<_.length;m+=1)g[m]=Z(Y(i,_,m));return{c(){e=v("div"),R(t.$$.fragment),n=y(),o=v("input"),s=y(),c=v("div");for(let m=0;m<g.length;m+=1)g[m].c();l=y(),r=v("div"),u=C(i[0]),f(o,"type","range"),o.disabled=!0,f(o,"min",i[2]),f(o,"max",i[3]),f(o,"step",i[4]),f(o,"class","svelte-9u5hcr"),f(c,"class","range  svelte-9u5hcr"),f(r,"class","original svelte-9u5hcr"),f(e,"class","input-slider svelte-9u5hcr")},m(m,d){b(m,e,d),j(t,e,null),h(e,n),h(e,o),h(e,s),h(e,c);for(let p=0;p<g.length;p+=1)g[p].m(c,null);h(e,l),h(e,r),h(r,u),a=!0},p(m,[d]){const p={};if(d&544&&(p.$$scope={dirty:d,ctx:m}),t.$set(p),(!a||d&4)&&f(o,"min",m[2]),(!a||d&8)&&f(o,"max",m[3]),(!a||d&16)&&f(o,"step",m[4]),d&2){_=m[1];let S;for(S=0;S<_.length;S+=1){const F=Y(m,_,S);g[S]?g[S].p(F,d):(g[S]=Z(F),g[S].c(),g[S].m(c,null))}for(;S<g.length;S+=1)g[S].d(1);g.length=_.length}(!a||d&1)&&A(u,m[0])},i(m){a||(B(t.$$.fragment,m),a=!0)},o(m){N(t.$$.fragment,m),a=!1},d(m){m&&k(e),I(t),M(g,m)}}}function Ge(i,e,t){let{original:n}=e,{interpretation:o}=e,{minimum:s}=e,{maximum:c}=e,{step:l}=e,{label:r=""}=e;return i.$$set=u=>{"original"in u&&t(0,n=u.original),"interpretation"in u&&t(1,o=u.interpretation),"minimum"in u&&t(2,s=u.minimum),"maximum"in u&&t(3,c=u.maximum),"step"in u&&t(4,l=u.step),"label"in u&&t(5,r=u.label)},[n,o,s,c,l,r]}class Me extends T{constructor(e){super(),q(this,e,Ge,De,D,{original:0,interpretation:1,minimum:2,maximum:3,step:4,label:5})}}function x(i,e,t){const n=i.slice();return n[4]=e[t],n[6]=t,n}function ze(i){let e;return{c(){e=C(i[3])},m(t,n){b(t,e,n)},p(t,n){n&8&&A(e,t[3])},d(t){t&&k(e)}}}function $(i){let e,t,n,o,s=i[4]+"",c,l;return{c(){e=v("button"),t=v("div"),o=y(),c=C(s),l=y(),f(t,"class","radio-circle svelte-gdyna0"),f(t,"style",n="background-color: "+w(i[1][i[6]])),f(e,"class","radio-item svelte-gdyna0"),E(e,"selected",i[0]===i[4])},m(r,u){b(r,e,u),h(e,t),h(e,o),h(e,c),h(e,l)},p(r,u){u&2&&n!==(n="background-color: "+w(r[1][r[6]]))&&f(t,"style",n),u&4&&s!==(s=r[4]+"")&&A(c,s),u&5&&E(e,"selected",r[0]===r[4])},d(r){r&&k(e)}}}function Ee(i){let e,t,n,o;t=new G({props:{$$slots:{default:[ze]},$$scope:{ctx:i}}});let s=i[2],c=[];for(let l=0;l<s.length;l+=1)c[l]=$(x(i,s,l));return{c(){e=v("div"),R(t.$$.fragment),n=y();for(let l=0;l<c.length;l+=1)c[l].c();f(e,"class","input-radio svelte-gdyna0")},m(l,r){b(l,e,r),j(t,e,null),h(e,n);for(let u=0;u<c.length;u+=1)c[u].m(e,null);o=!0},p(l,[r]){const u={};if(r&136&&(u.$$scope={dirty:r,ctx:l}),t.$set(u),r&7){s=l[2];let a;for(a=0;a<s.length;a+=1){const _=x(l,s,a);c[a]?c[a].p(_,r):(c[a]=$(_),c[a].c(),c[a].m(e,null))}for(;a<c.length;a+=1)c[a].d(1);c.length=s.length}},i(l){o||(B(t.$$.fragment,l),o=!0)},o(l){N(t.$$.fragment,l),o=!1},d(l){l&&k(e),I(t),M(c,l)}}}function Fe(i,e,t){let{original:n}=e,{interpretation:o}=e,{choices:s}=e,{label:c=""}=e;return i.$$set=l=>{"original"in l&&t(0,n=l.original),"interpretation"in l&&t(1,o=l.interpretation),"choices"in l&&t(2,s=l.choices),"label"in l&&t(3,c=l.label)},[n,o,s,c]}class Oe extends T{constructor(e){super(),q(this,e,Fe,Ee,D,{original:0,interpretation:1,choices:2,label:3})}}function He(i){let e;return{c(){e=C(i[1])},m(t,n){b(t,e,n)},p(t,n){n&2&&A(e,t[1])},d(t){t&&k(e)}}}function Je(i){let e,t,n,o,s,c,l,r,u,a;return t=new G({props:{$$slots:{default:[He]},$$scope:{ctx:i}}}),{c(){e=v("div"),R(t.$$.fragment),n=y(),o=v("div"),s=v("div"),c=v("canvas"),l=y(),r=v("img"),f(s,"class","interpretation svelte-1dcng24"),J(r.src,u=i[0])||f(r,"src",u),f(r,"class","svelte-1dcng24"),f(o,"class","image-preview svelte-1dcng24"),f(e,"class","input-image")},m(_,g){b(_,e,g),j(t,e,null),h(e,n),h(e,o),h(o,s),h(s,c),i[6](c),h(o,l),h(o,r),i[7](r),a=!0},p(_,[g]){const m={};g&514&&(m.$$scope={dirty:g,ctx:_}),t.$set(m),(!a||g&1&&!J(r.src,u=_[0]))&&f(r,"src",u)},i(_){a||(B(t.$$.fragment,_),a=!0)},o(_){N(t.$$.fragment,_),a=!1},d(_){_&&k(e),I(t),i[6](null),i[7](null)}}}function Ke(i,e,t){let{original:n}=e,{interpretation:o}=e,{shape:s}=e,{label:c=""}=e,l,r;const u=(g,m,d,p)=>{var S=d/g[0].length,F=p/g.length,O=0;g.forEach(function(se){var H=0;se.forEach(function(ae){m.fillStyle=w(ae),m.fillRect(H*S,O*F,S,F),H++}),O++})};ue(()=>{let g=U(!0,r.width,r.height,r.naturalWidth,r.naturalHeight);s&&(g=U(!0,g.width,g.height,s[0],s[1]));let m=g.width,d=g.height;l.setAttribute("height",`${d}`),l.setAttribute("width",`${m}`),u(o,l.getContext("2d"),m,d)});function a(g){K[g?"unshift":"push"](()=>{l=g,t(2,l)})}function _(g){K[g?"unshift":"push"](()=>{r=g,t(3,r)})}return i.$$set=g=>{"original"in g&&t(0,n=g.original),"interpretation"in g&&t(4,o=g.interpretation),"shape"in g&&t(5,s=g.shape),"label"in g&&t(1,c=g.label)},[n,c,l,r,o,s,a,_]}class Ue extends T{constructor(e){super(),q(this,e,Ke,Je,D,{original:0,interpretation:4,shape:5,label:1})}}function ee(i,e,t){const n=i.slice();return n[2]=e[t],n}function Le(i){let e;return{c(){e=C(i[1])},m(t,n){b(t,e,n)},p(t,n){n&2&&A(e,t[1])},d(t){t&&k(e)}}}function te(i){let e,t;return{c(){e=v("div"),f(e,"class","item svelte-13lmfcp"),f(e,"style",t="background-color: "+w(i[2]))},m(n,o){b(n,e,o)},p(n,o){o&1&&t!==(t="background-color: "+w(n[2]))&&f(e,"style",t)},d(n){n&&k(e)}}}function Pe(i){let e,t,n,o,s;t=new G({props:{$$slots:{default:[Le]},$$scope:{ctx:i}}});let c=i[0],l=[];for(let r=0;r<c.length;r+=1)l[r]=te(ee(i,c,r));return{c(){e=v("div"),R(t.$$.fragment),n=y(),o=v("div");for(let r=0;r<l.length;r+=1)l[r].c();f(o,"class","range svelte-13lmfcp")},m(r,u){b(r,e,u),j(t,e,null),h(e,n),h(e,o);for(let a=0;a<l.length;a+=1)l[a].m(o,null);s=!0},p(r,[u]){const a={};if(u&34&&(a.$$scope={dirty:u,ctx:r}),t.$set(a),u&1){c=r[0];let _;for(_=0;_<c.length;_+=1){const g=ee(r,c,_);l[_]?l[_].p(g,u):(l[_]=te(g),l[_].c(),l[_].m(o,null))}for(;_<l.length;_+=1)l[_].d(1);l.length=c.length}},i(r){s||(B(t.$$.fragment,r),s=!0)},o(r){N(t.$$.fragment,r),s=!1},d(r){r&&k(e),I(t),M(l,r)}}}function Qe(i,e,t){let{interpretation:n}=e,{label:o=""}=e;return i.$$set=s=>{"interpretation"in s&&t(0,n=s.interpretation),"label"in s&&t(1,o=s.label)},[n,o]}class Ve extends T{constructor(e){super(),q(this,e,Qe,Pe,D,{interpretation:0,label:1})}}function le(i,e,t){const n=i.slice();return n[2]=e[t][0],n[3]=e[t][1],n}function We(i){let e;return{c(){e=C(i[0])},m(t,n){b(t,e,n)},p(t,n){n&1&&A(e,t[0])},d(t){t&&k(e)}}}function ne(i){let e,t=i[2]+"",n,o,s;return{c(){e=v("span"),n=C(t),o=y(),f(e,"class","text-span svelte-15c0u2m"),f(e,"style",s="background-color: "+w(i[3]))},m(c,l){b(c,e,l),h(e,n),h(e,o)},p(c,l){l&2&&t!==(t=c[2]+"")&&A(n,t),l&2&&s!==(s="background-color: "+w(c[3]))&&f(e,"style",s)},d(c){c&&k(e)}}}function Xe(i){let e,t,n,o;t=new G({props:{$$slots:{default:[We]},$$scope:{ctx:i}}});let s=i[1],c=[];for(let l=0;l<s.length;l+=1)c[l]=ne(le(i,s,l));return{c(){e=v("div"),R(t.$$.fragment),n=y();for(let l=0;l<c.length;l+=1)c[l].c();f(e,"class","input-text svelte-15c0u2m")},m(l,r){b(l,e,r),j(t,e,null),h(e,n);for(let u=0;u<c.length;u+=1)c[u].m(e,null);o=!0},p(l,[r]){const u={};if(r&65&&(u.$$scope={dirty:r,ctx:l}),t.$set(u),r&2){s=l[1];let a;for(a=0;a<s.length;a+=1){const _=le(l,s,a);c[a]?c[a].p(_,r):(c[a]=ne(_),c[a].c(),c[a].m(e,null))}for(;a<c.length;a+=1)c[a].d(1);c.length=s.length}},i(l){o||(B(t.$$.fragment,l),o=!0)},o(l){N(t.$$.fragment,l),o=!1},d(l){l&&k(e),I(t),M(c,l)}}}function Ye(i,e,t){let{label:n=""}=e,{interpretation:o}=e;return i.$$set=s=>{"label"in s&&t(0,n=s.label),"interpretation"in s&&t(1,o=s.interpretation)},[n,o]}class Ze extends T{constructor(e){super(),q(this,e,Ye,Xe,D,{label:0,interpretation:1})}}const xe={audio:Ve,dropdown:Se,checkbox:Ne,checkboxgroup:Te,number:ke,slider:Me,radio:Oe,image:Ue,textbox:Ze};function ie(i){let e,t,n;const o=[i[0],{original:i[1].original},{interpretation:i[1].interpretation}];var s=i[2];function c(l){let r={};for(let u=0;u<o.length;u+=1)r=ge(r,o[u]);return{props:r}}return s&&(e=new s(c())),{c(){e&&R(e.$$.fragment),t=re()},m(l,r){e&&j(e,l,r),b(l,t,r),n=!0},p(l,r){const u=r&3?fe(o,[r&1&&_e(l[0]),r&2&&{original:l[1].original},r&2&&{interpretation:l[1].interpretation}]):{};if(s!==(s=l[2])){if(e){ce();const a=e;N(a.$$.fragment,1,0,()=>{I(a,1)}),oe()}s?(e=new s(c()),R(e.$$.fragment),B(e.$$.fragment,1),j(e,t.parentNode,t)):e=null}else s&&e.$set(u)},i(l){n||(e&&B(e.$$.fragment,l),n=!0)},o(l){e&&N(e.$$.fragment,l),n=!1},d(l){l&&k(t),e&&I(e,l)}}}function $e(i){let e,t,n=i[1]&&ie(i);return{c(){n&&n.c(),e=re()},m(o,s){n&&n.m(o,s),b(o,e,s),t=!0},p(o,[s]){o[1]?n?(n.p(o,s),s&2&&B(n,1)):(n=ie(o),n.c(),B(n,1),n.m(e.parentNode,e)):n&&(ce(),N(n,1,1,()=>{n=null}),oe())},i(o){t||(B(n),t=!0)},o(o){N(n),t=!1},d(o){n&&n.d(o),o&&k(e)}}}function et(i,e,t){let n,{component:o}=e,{component_props:s}=e,{value:c}=e;return i.$$set=l=>{"component"in l&&t(3,o=l.component),"component_props"in l&&t(0,s=l.component_props),"value"in l&&t(1,c=l.value)},i.$$.update=()=>{i.$$.dirty&8&&t(2,n=xe[o])},[s,c,n,o]}class tt extends T{constructor(e){super(),q(this,e,et,$e,D,{component:3,component_props:0,value:1})}}var rt=tt;const ct=["dynamic"];export{rt as Component,ct as modes};
//# sourceMappingURL=index.1c94b1c0.js.map
