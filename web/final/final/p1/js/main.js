presents=['cake.gif','pocky.gif','tv.gif']
used=[0,0,0];
function check()
{
  var count=0;
  for(var x=0;x<3;x++)
  {
    if(used[x])count++;
  }
  if(count==3)
  {
    const title=document.querySelector('h1');
    title.textContent="Enjoy your presents!";
  }
}
function show()
{
  for(var i=0;i<3;i++)
  {
    if(used[i])continue;
    else
    {
      this.src='images/'+presents[i];
      used[i]=1;
      check()
      break;
    }
  }
}

const photo=document.querySelectorAll('img');
for(var i =0;i<3;i++)
{
  photo[i].addEventListener('click',show);
}
