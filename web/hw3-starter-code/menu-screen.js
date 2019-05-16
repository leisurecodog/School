// TODO(you): Modify the class in whatever ways necessary to implement
// the flashcard app behavior.
//
// You may need to do things such as:
// - Changing the constructor parameters
// - Adding methods
// - Adding additional fields

class MenuScreen {
  constructor(containerElement) {
    this.containerElement = containerElement;

//    document.addEventListener('button-clicked', this.showButtonClicked);
  }
//  showButtonClicked(event) {
//    console.log(event.detail.buttonName);
//  }
  show() {
    this.containerElement.classList.remove('inactive');
  }

  hide() {
    this.containerElement.classList.add('inactive');
  }
}
  class Button {
  constructor(containerElement, text) {
    this.containerElement = containerElement;
    this.text=text;
    const button = document.createElement('button');
    button.textContent = text;

    this.onClick=this.onClick.bind(this);
    button.addEventListener('click', this.onClick);
    this.containerElement.append(button);
  }
  onClick() {
    const eventInfo = {
      buttonName: this.text
    };
    document.dispatchEvent(
        new CustomEvent('button-clicked', { detail: eventInfo }));
  }
}
