// TODO(you): Write the JavaScript necessary to complete the homework.

// You can access the RESULTS_MAP from "constants.js" in this file since
// "constants.js" has been included before "script.js" in index.html.
var i;
var pos;
const di=document.querySelectorAll('div');
const to=document.querySelectorAll('img');
function Onclick()
{
  let j;
  const cat=event.currentTarget;
  for(j=0;cat!=to[j];j++);
  to[j+1].src="images/checked.png";
  pos=(j+2)/2;
  di[pos].style.backgroundColor='#cfe3ff';
}
function semi()
{
  const d=event.currentTarget;
  const pic=document.querySelectorAll('img');
  if(pos%3==0)
  {
    di[pos-2].style.opacity="0.6";
    di[pos-2].style.backgroundColor='#f4f4f4';
    to[pos*2-3].src="images/unchecked.png";
    di[pos-1].style.opacity="0.6";
    di[pos-1].style.backgroundColor='#f4f4f4';
    to[pos*2-5].src="images/unchecked.png";
  }
  else if(pos%3==1)
  {
    di[pos+1].style.opacity="0.6";
    di[pos+1].style.backgroundColor='#f4f4f4';
    to[pos*2+1].src="images/unchecked.png";
    di[pos+2].style.opacity="0.6";
    di[pos+2].style.backgroundColor='#f4f4f4';
    to[pos*2+3].src="images/unchecked.png";
  }else {
    di[pos-1].style.opacity="0.6";
    di[pos-1].style.backgroundColor='#f4f4f4';
    to[pos*2-3].src="images/unchecked.png";
    di[pos+1].style.opacity="0.6";
    di[pos+1].style.backgroundColor='#f4f4f4';
    to[pos*2+1].src="images/unchecked.png";
  }
}
function reset()
{
  for(let k=1;k<di.length;k++)
  {
    di[k].style.backgroundColor='#f4f4f4';
    di[k].style.opacity="1.0";
  }
  const to=document.querySelectorAll('img');
  for(let k=0;k<to.length;k++)
  {
    if(k%2)
    {
      to[k].src="images/unchecked.png";
    }
  }
}
const ccc=document.querySelector('.choice-grid');
//ccc.addEventListener('click',Onclick);
const tt=document.querySelectorAll('img');
var len=tt.length;
for(i=0;i<len;i++)
{
  tt[i].addEventListener('click',Onclick);
}
const b=document.querySelectorAll('.be');
for(i=0;i<b.length;i++)
{
  b[i].addEventListener('click',semi);
}
const re=document.querySelector('button');
re.addEventListener('click',reset);
