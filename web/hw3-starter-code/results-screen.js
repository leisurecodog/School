// TODO(you): Modify the class in whatever ways necessary to implement
// the flashcard app behavior.
//
// You may need to do things such as:
// - Changing the constructor parameters
// - Adding methods
// - Adding additional fields

class ResultsScreen {
  constructor(containerElement) {
    this.containerElement = containerElement;
    this.Final=this.Final.bind(this);
    document.addEventListener('send-result',this.Final);
  }
  Final(event)
  {
    const ConElement=document.querySelector('.continue');
    if(event.detail.cor==event.detail.total)
    ConElement.textContent='Start Over?';
    else
    ConElement.textContent='Continue';
    const acc=document.querySelector('.percent');
    acc.textContent=Math.round(event.detail.cor/event.detail.total*100);
    const cor=document.querySelectorAll('.correct');
    cor[1].textContent=event.detail.cor;
    const incor=document.querySelectorAll('.incorrect');
    incor[1].textContent=event.detail.incor;
    document.querySelector('.continue').addEventListener('click',this.Con);
    document.querySelector('.to-menu').addEventListener('click',this.Con);
  }
  show(numberCorrect, numberWrong) {
    this.containerElement.classList.remove('inactive');
  }
  Con()
  {
    const which={Bname:this.textContent};
    document.dispatchEvent(new CustomEvent('ed',{detail:which}));
  }
  hide() {
    this.containerElement.classList.add('inactive');
  }
}
