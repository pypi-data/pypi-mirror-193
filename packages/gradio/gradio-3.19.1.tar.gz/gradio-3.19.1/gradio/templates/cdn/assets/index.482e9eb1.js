import{S as f,i as _,s as c,c as b,m as v,o as d,t as g,l as h,T as y,H as B,f as k,J as C,p as S,x as q}from"./index.53206edc.js";import{B as w}from"./Button.1ff5d34e.js";import{X as H}from"./Blocks.25a8e7e9.js";function J(n){let t=n[5](n[3])+"",i;return{c(){i=B(t)},m(e,a){k(e,i,a)},p(e,a){a&40&&t!==(t=e[5](e[3])+"")&&C(i,t)},d(e){e&&S(i)}}}function R(n){let t,i;return t=new w({props:{variant:n[4],elem_id:n[1],style:n[0],visible:n[2],$$slots:{default:[J]},$$scope:{ctx:n}}}),t.$on("click",n[6]),{c(){b(t.$$.fragment)},m(e,a){v(t,e,a),i=!0},p(e,[a]){const l={};a&16&&(l.variant=e[4]),a&2&&(l.elem_id=e[1]),a&1&&(l.style=e[0]),a&4&&(l.visible=e[2]),a&168&&(l.$$scope={dirty:a,ctx:e}),t.$set(l)},i(e){i||(d(t.$$.fragment,e),i=!0)},o(e){g(t.$$.fragment,e),i=!1},d(e){h(t,e)}}}function T(n,t,i){let e;y(n,H,s=>i(5,e=s));let{style:a={}}=t,{elem_id:l=""}=t,{visible:o=!0}=t,{value:u}=t,{variant:m="primary"}=t;function r(s){q.call(this,n,s)}return n.$$set=s=>{"style"in s&&i(0,a=s.style),"elem_id"in s&&i(1,l=s.elem_id),"visible"in s&&i(2,o=s.visible),"value"in s&&i(3,u=s.value),"variant"in s&&i(4,m=s.variant)},[a,l,o,u,m,e,r]}class X extends f{constructor(t){super(),_(this,t,T,R,c,{style:0,elem_id:1,visible:2,value:3,variant:4})}}var D=X;const E=["static"],F=n=>({type:"string",description:"button label",example_data:n.value||"Run"});export{D as Component,F as document,E as modes};
//# sourceMappingURL=index.482e9eb1.js.map
