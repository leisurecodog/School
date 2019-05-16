function ck()
{
  const index=Math.floor(Math.random()*3);
  let str;
  if(index==0)
  {
    str="rock.png";
  }
  else if(index==1)
  {
    str="paper.png";
  }
  else
  {
    str="scissors.png";
  }
  box.src="images/"+str;
  if(p==0 && index==1)console.log("Compter Win!");
  else if(p==0 && index==2)console.log("Player Win!");
  else if(p==1 && index==0)console.log("Player Win!");
  else if(p==1 && index==2)console.log("Computer Win!");
  else if(p==2 && index==0)console.log("Computer Win!");
  else if(p==2 && index==1)console.log("Player Win!");
}
var p;
function f1()
{
  const e1 = document.querySelector('img');
  e1.src="images/rock.png";
  p=0;
  ck();
}
function f2()
{
  const e2 = document.querySelector('img');
  e2.src="images/paper.png";
  p=1;
  ck();

}
function f3()
{
  const e3 = document.querySelector('img');
  e3.src="images/scissors.png";
  p=2;
  ck();
}
const e1 = document.querySelector('#rock');
e1.addEventListener('click',f1);
const e2 = document.querySelector('#paper');
e2.addEventListener('click',f2);
const e3 = document.querySelector('#scissors');
e3.addEventListener('click',f3);
const boxes=document.querySelectorAll('img');
const box=boxes[1];
