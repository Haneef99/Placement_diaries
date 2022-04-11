const Moonpath = "M13 27C13 41.9117 27 54 27 54C12.0883 54 0 41.9117 0 27C0 12.0883 12.0883 0 27 0C27 0 13 12.0883 13 27Z";

const Sunpath = "M56 27C56 41.9117 43.464 54 28 54C12.536 54 0 41.9117 0 27C0 12.0883 12.536 0 28 0C43.464 0 56 12.0883 56 27Z";

const darkMode = document.querySelector('#mode-toggler');
const togglebtn = document.querySelector('#toggle-btn');
let toggle = false;
togglebtn.addEventListener('click',(e)=>{
    e.preventDefault();
    const timeline = anime.timeline({
        duration : 750,
        easing : "easeOutExpo"
    });
    timeline.add({
        targets : ".sun",
        d : [
            {value : toggle ? Sunpath :Moonpath}
        ]
    })
    .add({
        targets : '#mode-toggler',
        rotate : toggle ? 0 : 340 
    },'-=300')
    .add({
        targets : "body",
        backgroundColor :toggle ?"#fff" : "#B0B3B8"
    },'-=700')

    toggle = toggle ? false : true;
})


console.log(darkMode)