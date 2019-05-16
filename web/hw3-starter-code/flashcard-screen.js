// TODO(you): Modify the class in whatever ways necessary to implement
// the flashcard app behavior.
//
// You may need to do things such as:
// - Changing the constructor parameters
// - Rewriting some of the existing methods, such as changing code in `show()`
// - Adding methods
// - Adding additional fields

class FlashcardScreen {
  constructor(containerElement) {
    var word;
    var arr=[];
    var record=[];
    let index=0;
    let total=0;
    let savecor=0;
    let saveincor=0;
    let Orix=null;
    let Oriy=null;
    let Offsetx=0;
    let Offsety=0;
    let M=false;
    let M2=false;
    let cor=0;
    let incor=0;
    let judgeFlag=false;
    this.containerElement = containerElement;
    this.Start=this.Start.bind(this);
    this.End=this.End.bind(this);
    this.Move=this.Move.bind(this);
    this.show=this.show.bind(this);
    this.load=this.load.bind(this);
    this.judge=this.judge.bind(this);
    this.reverse=this.reverse.bind(this);
    this.Result=this.Result.bind(this);
    this.C=this.C.bind(this);
    const desk=document.querySelector('#flashcard-container');
    desk.addEventListener('pointerdown',this.Start);
    desk.addEventListener('pointerup',this.End);
    desk.addEventListener('pointermove',this.Move);
  }
  load(event)
  {
    const a=document.querySelector('.correct');
    a.textContent=0;
    const b=document.querySelector('.incorrect');
    b.textContent=0;
    var d=FLASHCARD_DECKS;
    var tmp=event.detail.TitleName;
    for(var x in d)
    {
      if(d[x]['title']==tmp){this.word=d[x]['words'];break;}
    }
    this.cor=0;
    this.incor=0;
    this.index=0;
    this.savecor=0;
    this.saveincor=0;
      this.arr=[];
      this.record=[];
      const data=this.word;
      for (var x in data)
      {
        this.arr.push(x);
        this.record.push(false);
      }
    this.total=this.arr.length;
    this.show();
  }
  C()
  {
    this.cor=0;
    this.incor=0;
    this.index=0;
    const a=document.querySelector('.correct');
    a.textContent=0;
    const b=document.querySelector('.incorrect');
    b.textContent=0;
    for (var x=0;x<this.arr.length;x++)
    {
      if(this.record[x]==true)
      {
        this.record.splice(x,1);
        this.arr.splice(x,1);
        x--;
      }
    }
    this.show();
  }
  judge(dataX)
  {
    if(!this.judgeFlag)
    {
      this.judgeFlag=true;
      if(dataX>0)
      {
        const a=document.querySelector('.correct');
        this.cor++;
        a.textContent=this.cor;
        this.record[this.index-1]=true;
      }
      else if(dataX<0)
      {
        const a=document.querySelector('.incorrect');
        this.incor++;
        a.textContent=this.incor;
      }
    }
  }
  reverse(dataX)
  {
    if(this.judgeFlag)
    {
      this.judgeFlag=false;
      if(dataX>0)
      {
        const a=document.querySelector('.correct');
        this.cor--;
        this.record[this.index-1]=false;
        a.textContent=this.cor;
      }
      else if(dataX<0)
      {
        const a=document.querySelector('.incorrect');
        this.incor--;
        a.textContent=this.incor;
      }
    }
  }
  Start(event)
  {
    this.Orix=event.clientX;
    this.Oriy=event.clientY;
    this.M=true;
    event.currentTarget.setPointerCapture(event.pointerId);
  }
  End(event)
  {
    if(!(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) && this.M2)this.card._flipCard();
    this.Offsetx=0;
    this.Offsety=0;
    this.M=false;
    event.currentTarget.style.transform = 'translate(' +
    0 + 'px, ' + 0 + 'px)';
    this.M2=false;
    const back=document.querySelector('body');
    back.style.backgroundColor='#d0e6df';
    var jud=event.clientX-this.Orix;
    if(Math.abs(jud)>=150)
    {
      this.card.del();
      this.show();
      this.judgeFlag=false;
    }
  }
  Move(event)
  {
    if(!this.Offsetx)
    {
      this.Offsetx=0;
      this.Offsety=0;
    }
    if(!this.M)return ;
    event.preventDefault();
    const deltaX = event.clientX - this.Orix;
    const deltaY = event.clientY - this.Oriy;
    const translateX = this.Offsetx + deltaX;
    const translateY = this.Offsety + deltaY;
    event.currentTarget.style.transform = 'translate(' + translateX+'px , '+ translateY +'px) rotate(' +translateX*0.2+'deg)';
    this.M2=true;
    const back=document.querySelector('body');
    if(Math.abs(translateX)>150)
    {back.style.backgroundColor='#97b7b7';this.judge(translateX);}
    else
    {back.style.backgroundColor='#d0e6df';this.reverse(translateX);}

  }
  Result()
  {
    const Ind={idx:this.index};
    document.dispatchEvent(new CustomEvent('open-result',{detail:Ind}));
    const Re={cor:this.cor+this.savecor,incor:this.incor+this.saveincor,total:this.total};
    this.savecor+=this.cor;
    this.saveincot+=this.incor;
    document.dispatchEvent(new CustomEvent('send-result',{detail:Re}));
  }
  show() {
    var desk=this.word;
    this.containerElement.classList.remove('inactive');
    const flashcardContainer = document.querySelector('#flashcard-container');
    if(this.index<this.arr.length)
    {this.card = new Flashcard(flashcardContainer, this.arr[this.index],desk[this.arr[this.index]] );this.index++;}
    else {
      this.Result();
    }
  }

  hide() {
    this.containerElement.classList.add('inactive');
  }
}
