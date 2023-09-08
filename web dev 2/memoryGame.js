const cardArray = [
    {
      name: "Rolls-Royce",
      img: "images/Rolls-Royce-Ghost.png",
    },
    {
      name: "Bugatti",
      img: "images/bugatti chiron.png",
    },
    {
      name: "Lamborghini",
      img: "images/lamborghini.png",
    },
    {
      name: "Mustang",
      img: "images/mustang.png",
    },
    {
      name: "Porsche",
      img: "images/porsche.png",
    },
    {
      name: "Supra",
      img: "images/supra.png",
    },
    {
        name: "Rolls-Royce",
        img: "images/Rolls-Royce-Ghost.png",
      },
      {
        name: "Bugatti",
        img: "images/bugatti chiron.png",
      },
      {
        name: "Lamborghini",
        img: "images/lamborghini.png",
      },
      {
        name: "Mustang",
        img: "images/mustang.png",
      },
      {
        name: "Porsche",
        img: "images/porsche.png",
      },
      {
        name: "Supra",
        img: "images/supra.png",
      },
  ];
  
  cardArray.sort(() => 0.5 - Math.random());
  
  let cardschosen = [];
  let cardschosenid = [];
  const cardwon = [];
  
  const griddisplay = document.querySelector("#grid");
  const resultdisplay = document.querySelector("#result");
  
  function createboard() {
    for (let i = 0; i < cardArray.length; i++) {
      const card = document.createElement("img");
      card.setAttribute("src", "images/blank1.png");
      card.setAttribute("data-id", i);
      card.addEventListener("click", flipcard);
      griddisplay.appendChild(card);
    }
  }
  
  function checkmatch() {
    const cards = document.querySelectorAll("img");
    const optiononeid = cardschosenid[0];
    const optiontwoid = cardschosenid[1];
    console.log("check the match");
    
    if (optiononeid === optiontwoid) {
      cards[optiononeid].setAttribute("src", "images/blank1.png");
      cards[optiontwoid].setAttribute("src", "images/blank1.png");
      alert("You have clicked the same image!");
    } else if (cardschosen[0] === cardschosen[1]) {
      alert("This is a match");
      cards[optiononeid].setAttribute("src", "images/white.png");
      cards[optiontwoid].setAttribute("src", "images/white.png");
      cards[optiononeid].removeEventListener("click", flipcard);
      cards[optiontwoid].removeEventListener("click", flipcard);
      cardwon.push(cardschosen[0]); // Push only one card's name, assuming it represents a pair.
    } else {
      cards[optiononeid].setAttribute("src", "images/blank1.png");
      cards[optiontwoid].setAttribute("src", "images/blank1.png");
      alert("Sorry, try again");
    }
    resultdisplay.textContent = cardwon.length;
    cardschosen = [];
    cardschosenid = [];
    if (cardwon.length === (cardArray.length / 2) ){
      resultdisplay.textContent = "Congrats!!";
    }
  }
  
  function flipcard() {
    const cardid = this.getAttribute("data-id");
    cardschosen.push(cardArray[cardid].name);
    cardschosenid.push(cardid);
    console.log(cardschosen);
    console.log(cardschosenid);
    this.setAttribute("src", cardArray[cardid].img);
    
    if (cardschosen.length === 2) {
      setTimeout(checkmatch, 500);
    }
  }
  
  createboard();
  