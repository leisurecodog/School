const s9=document.querySelectorAll('.s1990');
const s20=document.querySelectorAll('.s2000');
const sall=document.querySelectorAll('img');

const all=document.querySelectorAll('button');
const button1=document.querySelector('#all');
const button2=document.querySelector('#nineties');
const button3=document.querySelector('#noughties');
function show()
{
  if(this.textContent=="All cars")
  {
    for(var x=0;x<sall.length;x++)
    {
      sall[x].classList.remove('inactive');
    }
  }
  else if(this.textContent=="1990s")
  {
    for(var x=0;x<s9.length;x++)
    {
      s9[x].classList.remove('inactive');
    }
    for(var x=0;x<s20.length;x++)
    {
      s20[x].classList.add('inactive');
    }
  }
  else if(this.textContent=="2000s")
  {
    for(var x=0;x<s9.length;x++)
    {
      s9[x].classList.add('inactive');
    }
    for(var x=0;x<s20.length;x++)
    {
      s20[x].classList.remove('inactive');
    }
  }
}
for(var x=0;x<3;x++)
{
  all[x].addEventListener('click',show);
}
