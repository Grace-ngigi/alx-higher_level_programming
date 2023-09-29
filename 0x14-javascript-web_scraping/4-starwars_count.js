#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200){
	  const filmsData = JSON.parse(body).results;
	  let i = 0;
	  for (const index in filmsData){
		  const chars = filmsData[index].characters;
		  for (const charIdx in chars){
			  if(chars[charIdx].includes('18')){
				  i++;
			  }
		  }
	 }
	  console.log(i);
  } else {
	  console.log("An error occurred" + response.statusCode);
  }
});
		 
