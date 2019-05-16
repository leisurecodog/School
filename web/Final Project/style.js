class Bar{//area of Bar class
  constructor()
  {
    this.Element=document.querySelector('.bar');
    this.Btns=document.querySelectorAll('.barButton');
    var BtnName=BarButtons;
    for(var x=0;x<this.Btns.length;x++)//add event to each button in bar and add name
    {
      this.Btns[x].addEventListener('click',this.Links);
      this.Btns[x].textContent=BtnName[x];
    }
    if(location.href.split("?").length==2)
    {
      this.Btns[2].textContent="My Favorite";
      this.Btns[3].textContent="Logout";
    }
    else {
      this.Btns[2].textContent="about author";
      this.Btns[3].textContent="Login";
    }
  }
  Links()//load bar's function
  {
    const frame=document.querySelector('.frame');
    //console.log(this.textContent);
    if(this.textContent=='about PTT')
    {
      frame.src="https://zh.wikipedia.org/zh-tw/%E6%89%B9%E8%B8%A2%E8%B8%A2";
      frame.classList.toggle('frminactive');
    }
    else if(this.textContent=='PTT wikipedia')
    {
      frame.src="http://zh.pttpedia.wikia.com/wiki/PTT%E9%84%89%E6%B0%91%E7%99%BE%E7%A7%91";
      frame.classList.toggle('frminactive');
    }
    else if(this.textContent=='Login')
    {
      document.location.href='Login.html';
    }
    else if(this.textContent=='Logout')
    {
      alert("Logout success.");
      document.location.href='index.html';
    }
  }
}
class FB{
  constructor()
  {
    this.update=this.update.bind(this);
    this.Btns=document.querySelectorAll('.barButton');
    this.update=this.update.bind(this);
    if(this.Btns[2].textContent=='My Favorite')
    {
      this.Btns[2].addEventListener('click',this.update)
    }

  }
  Fclick()
  {
    var ck=location.href.split("?");
    check=0;
    if(ck.length==2)
    {
      document.location.href='Content.html?'+ck[1]+'?'+this.textContent;
    }
    else
    {
      document.location.href='Content.html?'+this.textContent;
    }
  }
  update()
  {
    const Container=document.querySelector('.body');
    const user=location.href.split("?")[1];
    var having=false;
    var FF=[];
    if(localStorage.getItem(user)!=null)
    {
      FF=localStorage.getItem(user).split(",");
    }
    for(var x in FF){if(FF[x]==""){delete FF[x];continue;}having=true;break;}
    if(!having)
    {
      alert("Don't be silly");
      return ;
    }
    //start update
    if(check==0)
    {
      const de=document.querySelectorAll('.Fbtn');
      for(var x=0;x<de.length;x++)
      {
        de[x].classList.remove('Fbtn');
        de[x].classList.add('inactive');
      }
      for(var x in FF)
      {
        const btn=new Button(Container,FF[x],'Fbtn')
      }
      const Test=document.querySelectorAll('.Fbtn');
      for(var x=0;x<Test.length;x++)
      {
        Test[x].addEventListener('click',this.Fclick);
      }
      check=1;
    }
    const a=document.querySelectorAll(".btn");
    const b=document.querySelectorAll(".Fbtn");
    for(var x=0;x<a.length;x++)a[x].classList.toggle('inactive');
    for(var x=0;x<b.length;x++)b[x].classList.toggle('inactive');
  }
}
class BtnsTop{//top level of button
  constructor()
  {
    var InitBoard=DESK;
    const BtnContainer=document.querySelector('.body');
    for(var x in InitBoard)//load each top board
    {
      //console.log(InitBoard[x]['title']);
        const btn=new Button(BtnContainer,InitBoard[x]['title'],'button1')
    }
    const tmp=document.querySelectorAll('.button1');
    for(var x=0;x<tmp.length;x++)//add event
    {
      tmp[x].addEventListener('click',this.OnClick);
    }
  }
  OnClick()//create sub board of which is clicked and vanish all top board
  {
    const NextBtn=new BtnSec(this.textContent);
    const btn1=document.querySelectorAll('.button1');
    for (var x=0;x<btn1.length;x++)
    {
      btn1[x].classList.add('inactive1');
    }
  }
}
class BtnSec//subboard class
{
  constructor(ancient)
  {
    const BtnContainer=document.querySelector('.body');
    this.text=ancient;
    for(var x in DESK)
    {
      if(DESK[x]['title']==ancient)
      {
        this.SUB=DESK[x]['words'];
        break;
      }
    }
    for(var x in this.SUB)
    {
      const SubBtn=new Button(BtnContainer,x,'button2');
    }
    const tmp=document.querySelectorAll('.button2');
    for(var x=0;x<tmp.length;x++)//add event
    {
      tmp[x].addEventListener('click',this.OnClick);
    }
  }
  OnClick()
  {
    var ck=location.href.split("?");
    check=0;
    if(ck.length==2)
    {
      document.location.href='Content.html?'+ck[1]+'?'+this.textContent;
    }
    else
    {
      document.location.href='Content.html?'+this.textContent;
    }
  }
}

class Button {
  constructor(containerElement, text,CLS) {
    this.containerElement = containerElement;
    this.text=text;
    const button = document.createElement('button');
    button.classList.add(CLS);//add class
    if(CLS!='Fbtn')
    {
      button.classList.add('btn');
    }
    else {
      button.classList.add('inactive');
    }
    button.textContent = text;
    this.containerElement.append(button);
  }
}
var check=0;
