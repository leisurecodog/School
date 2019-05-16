class Content{
  constructor()
  {
    const url1='https://www.ptt.cc/bbs/';
    const url2='/index.html';
    const url = location.href.split("?");
    var final=" ";
    var user=" ";
    if(url.length==3)
    {
      final=url[2];
      user=url[1];
    }
    else {
      final=url[1];
      user=" ";
    }
    this.back=this.back.bind(this);
    this.Btns=document.querySelectorAll('.barButton');
    var BtnName=BarButtons;
    for(var x=0;x<this.Btns.length;x++)//add name
    {
      this.Btns[x].textContent=BtnName[x];
      this.Btns[x].addEventListener('click',this.app);
    }
    if(location.href.split("?").length==3)//user's function
    {
      this.Btns[0].textContent="Add to Favorite";
      this.Btns[1].textContent="Remove from Favorite";
      this.Btns[2].textContent="My Favorite";
      this.Btns[3].textContent="Logout";
    }
    document.querySelector('.gif').addEventListener('click',this.back);//link to index.html
    document.querySelector('.ContentF').src=url1+final+url2;//show content
  }
  back()
  {
      const url=location.href.split("?");
      if(url.length==3)
        document.location.href="index.html?"+url[1];
      else {
        document.location.href='index.html';
      }
  }
  app()
  {
    const b=location.href.split("?")[2];
    const u=location.href.split("?")[1];
    if(this.textContent=='Add to Favorite')
    {
      var FF=localStorage.getItem(u);
      if(FF==null)//initialize
      {
        localStorage.setItem(u,b);
        alert("Add Success");
        return;
      }
      var arr=FF.split(",");
      for(var x in arr)
      {
        if(b==arr[x])
        {
          alert("INNNNNNNNNNN");
          return;
        }
      }
      arr.push(b);
      alert("Add Success");
      localStorage.setItem(u,arr);
    }
    else if(this.textContent=='Remove from Favorite')
    {
      var find=false;
      var FF=localStorage.getItem(u);
      if(FF==null)//initialize
      {
        alert("Empty Favorite List!");
        return;
      }
      var arr=FF.split(",");
      var Narr=[];
      for(var x in arr)
      {
        if(b==arr[x])
        {
          find=true;
          continue;
        }
        Narr.push(arr[x]);
      }
      if(!find)alert("Can't find such board name : "+b);
      else alert("Remove success.");
      localStorage.setItem(u,Narr);
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
const cnt= new Content;
