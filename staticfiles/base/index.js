document.addEventListener('DOMContentLoaded', function() {
    load_developers();
  });

  function load_developers() {
   
    fetch(`/developers/`)
    .then(response => response.json())
    .then(developers => {
      //print developers
      console.log(developers);
      developers.forEach(developer => show_developers(developer));
    });
  }

  function show_developers(developer) {
    const divElement = document.createElement('div');
    divElement.className = "row";
  
    const username = document.createElement('div');
    username.className = "col-lg-2-md-3 col-sm-6 ml-4"
    username.innerHTML = developer.username;
    divElement.append(username);

    const bio = document.createElement('div');
    bio.className =  'col-lg-8'
    bio.innerHTML = developer.bio
    divElement.append(bio)

    const cardElement = document.createElement('div');
    cardElement.className = 'card'
    cardElement.style = 'border: 2px solid black;'
    cardElement.append(divElement);
    document.querySelector('#devs').append(cardElement);
  }

