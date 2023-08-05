import{S as C,i as z,s as B,A as H,B as u,f as b,D as g,E as p,p as v,F as h,G as M,O as d,H as E,N as V,q as j,aa as F,ab as G,b as I,ac as q,c as L,m as T,o as w,t as k,l as A,k as Y,n as Z,x as J}from"./index.3b5d9bed.js";/* empty css                                            */import{B as K}from"./Block.e25dc282.js";import{B as P}from"./BlockLabel.321a7bc3.js";import"./Button.cad7c48c.js";function Q(n){let e,t,a;return{c(){e=H("svg"),t=H("path"),a=H("path"),u(t,"fill","currentColor"),u(t,"d","M17.74 30L16 29l4-7h6a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h9v2H6a4 4 0 0 1-4-4V8a4 4 0 0 1 4-4h20a4 4 0 0 1 4 4v12a4 4 0 0 1-4 4h-4.84Z"),u(a,"fill","currentColor"),u(a,"d","M8 10h16v2H8zm0 6h10v2H8z"),u(e,"xmlns","http://www.w3.org/2000/svg"),u(e,"xmlns:xlink","http://www.w3.org/1999/xlink"),u(e,"aria-hidden","true"),u(e,"role","img"),u(e,"class","iconify iconify--carbon"),u(e,"width","100%"),u(e,"height","100%"),u(e,"preserveAspectRatio","xMidYMid meet"),u(e,"viewBox","0 0 32 32")},m(s,l){b(s,e,l),g(e,t),g(e,a)},p,i:p,o:p,d(s){s&&v(e)}}}class W extends C{constructor(e){super(),z(this,e,null,Q,B,{})}}function S(n,e,t){const a=n.slice();return a[12]=e[t],a[14]=t,a}function D(n){let e,t=n[12][0]+"",a,s,l,o=n[12][1]+"",r;return{c(){e=h("div"),s=M(),l=h("div"),u(e,"data-testid","user"),u(e,"class","message user svelte-134zwfa"),u(e,"style",a="background-color:"+n[2][0]),d(e,"latest",n[14]===n[3].length-1),d(e,"hide",n[12][0]===null),u(l,"data-testid","bot"),u(l,"class","message bot svelte-134zwfa"),u(l,"style",r="background-color:"+n[2][1]),d(l,"latest",n[14]===n[3].length-1),d(l,"hide",n[12][1]===null)},m(f,i){b(f,e,i),e.innerHTML=t,b(f,s,i),b(f,l,i),l.innerHTML=o},p(f,i){i&8&&t!==(t=f[12][0]+"")&&(e.innerHTML=t),i&4&&a!==(a="background-color:"+f[2][0])&&u(e,"style",a),i&8&&d(e,"latest",f[14]===f[3].length-1),i&8&&d(e,"hide",f[12][0]===null),i&8&&o!==(o=f[12][1]+"")&&(l.innerHTML=o),i&4&&r!==(r="background-color:"+f[2][1])&&u(l,"style",r),i&8&&d(l,"latest",f[14]===f[3].length-1),i&8&&d(l,"hide",f[12][1]===null)},d(f){f&&v(e),f&&v(s),f&&v(l)}}}function N(n){let e,t,a,s,l,o,r;return{c(){e=h("div"),t=h("div"),a=E(`
				\xA0
				`),s=h("div"),l=E(`
				\xA0
				`),o=h("div"),u(t,"class","dot-flashing svelte-134zwfa"),u(s,"class","dot-flashing svelte-134zwfa"),u(o,"class","dot-flashing svelte-134zwfa"),u(e,"data-testid","bot"),u(e,"class","message user pending svelte-134zwfa"),u(e,"style",r="background-color:"+n[2][0])},m(f,i){b(f,e,i),g(e,t),g(e,a),g(e,s),g(e,l),g(e,o)},p(f,i){i&4&&r!==(r="background-color:"+f[2][0])&&u(e,"style",r)},d(f){f&&v(e)}}}function X(n){let e,t,a,s=n[3],l=[];for(let r=0;r<s.length;r+=1)l[r]=D(S(n,s,r));let o=n[0]&&N(n);return{c(){e=h("div"),t=h("div");for(let r=0;r<l.length;r+=1)l[r].c();a=M(),o&&o.c(),u(t,"class","message-wrap svelte-134zwfa"),u(e,"class","wrap svelte-134zwfa")},m(r,f){b(r,e,f),g(e,t);for(let i=0;i<l.length;i+=1)l[i].m(t,null);g(t,a),o&&o.m(t,null),n[7](e)},p(r,[f]){if(f&12){s=r[3];let i;for(i=0;i<s.length;i+=1){const m=S(r,s,i);l[i]?l[i].p(m,f):(l[i]=D(m),l[i].c(),l[i].m(t,a))}for(;i<l.length;i+=1)l[i].d(1);l.length=s.length}r[0]?o?o.p(r,f):(o=N(r),o.c(),o.m(t,null)):o&&(o.d(1),o=null)},i:p,o:p,d(r){r&&v(e),V(l,r),o&&o.d(),n[7](null)}}}function x(n,e,t){let a,s,{value:l}=e,o,{style:r={}}=e,{pending_message:f=!1}=e,i,m;const y=j();F(()=>{m=i&&i.offsetHeight+i.scrollTop>i.scrollHeight-20}),G(()=>{m&&(i.scrollTo(0,i.scrollHeight),i.querySelectorAll("img").forEach(_=>{_.addEventListener("load",()=>{i.scrollTo(0,i.scrollHeight)})}))});function c(_){return _ in q?q[_].primary:_}function R(){return r.color_map?[c(r.color_map[0]),c(r.color_map[1])]:["#fb923c","#9ca3af"]}function U(_){I[_?"unshift":"push"](()=>{i=_,t(1,i)})}return n.$$set=_=>{"value"in _&&t(4,l=_.value),"style"in _&&t(5,r=_.style),"pending_message"in _&&t(0,f=_.pending_message)},n.$$.update=()=>{n.$$.dirty&16&&t(3,a=l||[]),n.$$.dirty&80&&l!==o&&(t(6,o=l),y("change"))},t(2,s=R()),[f,i,s,a,l,r,o,U]}class $ extends C{constructor(e){super(),z(this,e,x,X,B,{value:4,style:5,pending_message:0})}}function O(n){let e,t;return e=new P({props:{show_label:n[5],Icon:W,label:n[4]||"Chatbot",disable:typeof n[0].container=="boolean"&&!n[0].container}}),{c(){L(e.$$.fragment)},m(a,s){T(e,a,s),t=!0},p(a,s){const l={};s&32&&(l.show_label=a[5]),s&16&&(l.label=a[4]||"Chatbot"),s&1&&(l.disable=typeof a[0].container=="boolean"&&!a[0].container),e.$set(l)},i(a){t||(w(e.$$.fragment,a),t=!0)},o(a){k(e.$$.fragment,a),t=!1},d(a){A(e,a)}}}function ee(n){let e,t,a,s=n[5]&&O(n);return t=new $({props:{style:n[0],value:n[3],pending_message:n[6]?.status==="pending"}}),t.$on("change",n[8]),{c(){s&&s.c(),e=M(),L(t.$$.fragment)},m(l,o){s&&s.m(l,o),b(l,e,o),T(t,l,o),a=!0},p(l,o){l[5]?s?(s.p(l,o),o&32&&w(s,1)):(s=O(l),s.c(),w(s,1),s.m(e.parentNode,e)):s&&(Y(),k(s,1,1,()=>{s=null}),Z());const r={};o&1&&(r.style=l[0]),o&8&&(r.value=l[3]),o&64&&(r.pending_message=l[6]?.status==="pending"),t.$set(r)},i(l){a||(w(s),w(t.$$.fragment,l),a=!0)},o(l){k(s),k(t.$$.fragment,l),a=!1},d(l){s&&s.d(l),l&&v(e),A(t,l)}}}function le(n){let e,t;return e=new K({props:{elem_id:n[1],visible:n[2],$$slots:{default:[ee]},$$scope:{ctx:n}}}),{c(){L(e.$$.fragment)},m(a,s){T(e,a,s),t=!0},p(a,[s]){const l={};s&2&&(l.elem_id=a[1]),s&4&&(l.visible=a[2]),s&633&&(l.$$scope={dirty:s,ctx:a}),e.$set(l)},i(a){t||(w(e.$$.fragment,a),t=!0)},o(a){k(e.$$.fragment,a),t=!1},d(a){A(e,a)}}}function te(n,e,t){let{elem_id:a=""}=e,{visible:s=!0}=e,{value:l=[]}=e,{style:o={}}=e,{label:r}=e,{show_label:f=!0}=e,{color_map:i={}}=e,{loading_status:m}=e;function y(c){J.call(this,n,c)}return n.$$set=c=>{"elem_id"in c&&t(1,a=c.elem_id),"visible"in c&&t(2,s=c.visible),"value"in c&&t(3,l=c.value),"style"in c&&t(0,o=c.style),"label"in c&&t(4,r=c.label),"show_label"in c&&t(5,f=c.show_label),"color_map"in c&&t(7,i=c.color_map),"loading_status"in c&&t(6,m=c.loading_status)},n.$$.update=()=>{n.$$.dirty&129&&!o.color_map&&Object.keys(i).length&&t(0,o.color_map=i,o)},[o,a,s,l,r,f,m,i,y]}class ae extends C{constructor(e){super(),z(this,e,te,le,B,{elem_id:1,visible:2,value:3,style:0,label:4,show_label:5,color_map:7,loading_status:6})}}var fe=ae;const ue=["static"],ce=n=>({type:"Array<[string, string]>",description:"Represents list of message pairs of chat message.",example_data:n.value??[["Hi","Hello"],["1 + 1","2"]]});export{fe as Component,ce as document,ue as modes};
//# sourceMappingURL=index.44fe4285.js.map
