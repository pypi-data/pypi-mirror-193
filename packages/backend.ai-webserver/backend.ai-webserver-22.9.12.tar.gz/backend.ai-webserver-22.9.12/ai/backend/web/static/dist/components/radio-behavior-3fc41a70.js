import{aa as e,ab as s,ac as t,ad as n,ae as a,af as o,j as r,_ as c,p as i,k as h,Q as d,ag as u}from"./backend-ai-webui-f03dfdc8.js";function l(o,r){const c=o.queryGroup(),i=c.indexOf(o),h=function(e,o,r){if(0==e.length)return null;switch(r){case a:case n:return o+1>e.length-1?0:o+1;case t:case s:return o-1<0?e.length-1:o-1}return null}(c,i,r.code);if(null!=h){const s=c[h];o.rowToElement(s),e(r)}}class p extends o{constructor(){super(...arguments),this.role="radio",this.formElementType="radio"}queryGroup(){return null!=this.name?d(this,`${this.nodeName.toLowerCase()}[name=${this.name}]:not([disabled])`):[]}rowToElement(e){e.click(),e.focus()}toggle(){this.checked=!0,this.dispatchChangeEvent()}updateTabindex(e){(e.has("disabled")||e.has("checked"))&&u(this,this.disabled||!this.checked&&this.isGroupedChecked()),e.has("checked")&&this.checked&&this.uncheckGroup()}isGroupedChecked(){return null!=this.queryGroup().find((e=>e.checked))}uncheckGroup(){const e=this.queryGroup();for(const s of e)s!==this&&(s.checked=!1,s.tabIndex=-1)}onKeyDown(e){super.onKeyDown(e),l(this,e)}}p.styles=[...o.styles,r("")],c([i({type:String,reflect:!0}),h("design:type",String)],p.prototype,"role",void 0);export{p as R};
