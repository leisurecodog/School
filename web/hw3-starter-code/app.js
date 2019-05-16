// TODO(you): Modify the class in whatever ways necessary to implement
// the flashcard app behavior.
//
// You may need to do things such as:
// - Changing the constructor parameters
// - Changing the code in the constructor
// - Adding methods
// - Adding additional fields

class App {
  constructor() {
    const menuElement = document.querySelector('#menu');
    this.menu = new MenuScreen(menuElement);
    this.plays=this.plays.bind(this);
    this.ShowResult=this.ShowResult.bind(this);
    this.option=this.option.bind(this);
    const mainElement = document.querySelector('#main');
    this.flashcards = new FlashcardScreen(mainElement);
    const resultElement = document.querySelector('#results');
    this.results = new ResultsScreen(resultElement);
    const buttonElement=document.querySelector('#choices');
    const desk=FLASHCARD_DECKS;
    document.addEventListener('clicked-title',this.plays);
    document.addEventListener('open-result',this.ShowResult);
    document.addEventListener('ed',this.option);
    for(var x in desk)
    {
      const t=document.createElement('div');
      t.textContent=desk[x]['title'];
      t.addEventListener('click',this.run);
      buttonElement.appendChild(t);
    }
    // Uncomment this pair of lines to see the "flashcard" screen:
    // this.menu.hide();
    // this.flashcards.show();

    // Uncomment this pair of lines to see the "results" screen:
    // this.menu.hide();
    // this.results.show();
  }
  option(event)
  {
    if(event.detail.Bname=='Continue')
    {
      this.results.hide();
      this.flashcards.C();
    }
    else if(event.detail.Bname=='Start Over?')
    {
      this.results.hide();
      this.flashcards.load(event);
    }
    else{
      this.results.hide();
      this.menu.show();
    }
  }
  plays(event)
  {
    this.menu.hide();
    this.flashcards.load(event);
  }
  ShowResult()
  {
    this.flashcards.hide();
    this.results.show();
  }
  run()
  {
    const Tname={TitleName:this.textContent};
    document.dispatchEvent(new CustomEvent('clicked-title',{detail:Tname}));
  }
}
